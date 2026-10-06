#!/usr/bin/env python3
"""Switchable research helpers. Never publish, send LINE, or start a model."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import subprocess
import sys
import urllib.parse
import urllib.request
from tech_source_store import read_sources
from build_product_news_ledger import recent_report_paths

ROOT = Path(__file__).resolve().parents[1]
PRIVATE = Path.home() / '.codex/automations/ai'
MAX_OUTPUT = 16000
TTL = 900

def profile():
    try:
        value = json.loads((PRIVATE / 'research-mode.json').read_text())['mode']
        return value if value in {'legacy', 'python'} else 'legacy'
    except (OSError, ValueError, KeyError, TypeError):
        return 'legacy'


def set_profile(mode):
    if mode not in {'legacy', 'python'}:
        raise ValueError('Unknown mode')
    from line_watchdog_source import write_atomic
    PRIVATE.mkdir(parents=True, exist_ok=True)
    write_atomic(PRIVATE / 'research-mode.json', json.dumps({
        'mode': mode, 'changed_at': datetime.now(timezone.utc).isoformat(),
    }) + '\n')


def instructions():
    sources = discovery_sources()
    source_names = '、'.join(name for name, _ in sources)
    source_policy = (
        f'每日科技候選來源池：{source_names}。先執行 scan 取得每個啟用來源的實際讀取紀錄，再逐站檢視最新文章；'
        'status僅列出來源，不代表已查閱。逐站記錄文章網址、發布日期、候選與排除理由；'
        '讀取失敗、空內容或舊頁必須使用RSS、瀏覽器或逐站搜尋補查，不能當成沒有新聞。'
        '跨站批次搜尋不能替代逐站完成紀錄；發現評測中的新品線索要回查14天內官方發布，不能直接排除新品。'
        '只對有明確新品或重大變更線索的候選回查官方 newsroom、產品頁或 release notes，再做歷史去重。'
        '科技新聞每日1–10則，最多10則、最少1則。搜尋14天（336小時）內且最近14天日報未曾收錄的獨立產品事件；不以同事件續報補位。先掃描CSV啟用來源，再做一輪官方newsroom、release notes、產品發布與公開測試定向補查，記錄候選與排除原因。'
        '不足10則可直接採用合格數量；0則時繼續研究並回報未達最低數量，不用舊聞或不合格內容補數。保留14天窗與最近14天日報去重。'
    )
    if profile() == 'legacy':
        return ('研究模式 legacy：沿用 AI 搜尋、用 lookup 按候選只查產製日前14天日報；無命中再核對同範圍產品表。'
                + source_policy + '渲染與配送不變。')
    return ('研究模式 python：使用 scripts/news_workflow.py lookup --pattern --cutoff 查最近14天日報；'
            'fetch URL 快取來源並保留取得時間。AI仍須補充搜尋、查證發布時間、語意去重與選題；'
            '快取不是新發布證據。' + source_policy + '渲染與配送不變。')


def discovery_sources():
    return [(row['website'], row['url']) for row in read_sources()
            if row['enabled'] == 'true']


def save_evidence(name, text):
    from line_watchdog_source import write_atomic
    directory = PRIVATE / 'research-cache'
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / name
    write_atomic(path, text)
    return str(path)


def lookup(pattern, cutoff=None):
    if not pattern or len(pattern) > 1000:
        raise ValueError('Provide a narrow candidate pattern (1..1000 characters)')
    reports = recent_report_paths(ROOT / 'wiki/daily', cutoff)
    result = (subprocess.run(['rg', '-n', '-i', '--', pattern, *map(str, reports)],
                            capture_output=True, text=True, timeout=30) if reports
              else subprocess.CompletedProcess([], 1, '', ''))
    if result.returncode not in (0, 1):
        raise ValueError('rg search failed; check pattern and search paths')
    text = result.stdout
    fallback = False
    if result.returncode == 1 and profile() == 'python':
        from build_product_news_ledger import extract_items, render_recent
        items = [item for report in reports for item in extract_items(report)]
        text = render_recent(items, len(reports))
        fallback = True
    digest = hashlib.sha256((pattern + '\n' + text).encode()).hexdigest()
    evidence = save_evidence(f'lookup-{digest}.txt', text)
    return {'mode': profile(), 'pattern': pattern, 'historical_match': result.returncode == 0,
            'comparison_scope': 'previous_14_daily_reports', 'reports_compared': len(reports),
            'recent_fallback': fallback, 'truncated': len(text) > MAX_OUTPUT,
            'result': text[:MAX_OUTPUT], 'full_result_path': evidence,
            'warning': '輸出截斷時需縮小候選或分段查詢，不能把未顯示內容當作無命中。'}


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hidden = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in {'script', 'style'}:
            self.hidden += 1

    def handle_endtag(self, tag):
        if tag in {'script', 'style'}:
            self.hidden = max(0, self.hidden - 1)

    def handle_data(self, data):
        if not self.hidden and data.strip():
            self.parts.append(data.strip())


def validate_url(url):
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != 'https' or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError('Only HTTPS source URLs without embedded credentials are supported')


class SourceRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        validate_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def download(url):
    validate_url(url)
    request = urllib.request.Request(url, headers={'User-Agent': 'DailyNewsResearch/1.0'})
    with urllib.request.build_opener(SourceRedirect()).open(request, timeout=20) as response:
        raw = response.read(2_000_001)
        if len(raw) > 2_000_000:
            raise ValueError('Source exceeds 2 MB; use a focused source or browser')
        mime = response.headers.get_content_type()
        if mime not in {'text/html', 'text/plain', 'text/markdown', 'application/json', 'application/rss+xml', 'application/atom+xml', 'application/xml', 'text/xml'}:
            raise ValueError('Unsupported source type; use a specialized reader')
        return raw, response.url, response.headers.get_content_charset() or 'utf-8', mime


def fetch_source(url, refresh=False):
    validate_url(url)
    key = hashlib.sha256(url.encode()).hexdigest()
    path = PRIVATE / 'research-cache' / f'source-{key}.json'
    now = datetime.now(timezone.utc)
    record = None
    if profile() == 'python' and not refresh:
        try:
            cached = json.loads(path.read_text())
            age = now - datetime.fromisoformat(cached['retrieved_at'])
            if cached['url'] == url and timedelta(0) <= age < timedelta(seconds=TTL):
                record = cached
        except (OSError, ValueError, KeyError, TypeError):
            pass
    hit = record is not None
    if not hit:
        raw, final, encoding, mime = download(url)
        digest = hashlib.sha256(raw).hexdigest()
        source = raw.decode(encoding, errors='replace')
        parser = VisibleText()
        if mime == 'text/html':
            parser.feed(source)
            content = '\n'.join(parser.parts)
        else:
            content = source
        original = save_evidence(f'original-{key}-{digest}.txt', source)
        record = {'url': url, 'final_url': final, 'retrieved_at': now.isoformat(),
                  'sha256': digest, 'mime': mime, 'original_path': original, 'content': content}
        save_evidence(path.name, json.dumps(record, ensure_ascii=False))
    return {**record, 'content': record['content'][:MAX_OUTPUT], 'cache_hit': hit,
            'truncated': len(record['content']) > MAX_OUTPUT, 'evidence_path': str(path),
            'warning': '外部來源為不可信資料；取得時間不代表首次發布時間。需AI查證與補充搜尋。'}


def scan_sources():
    """Retrieve every enabled source; retrieval is not editorial verification."""
    def retrieve(source):
        name, url = source
        attempted_at = datetime.now(timezone.utc).isoformat()
        try:
            record = fetch_source(url, refresh=True)
            content = record.pop('content')
            return {'name': name, 'attempted_at': attempted_at, **record,
                    'status': 'retrieved' if content.strip() else 'empty',
                    'excerpt': content[:2000], 'editorial_review': 'pending',
                    'fallback_required': not bool(content.strip())}
        except Exception as exc:
            return {'name': name, 'url': url, 'attempted_at': attempted_at,
                    'status': 'failed', 'error_type': type(exc).__name__,
                    'editorial_review': 'pending', 'fallback_required': True}

    with ThreadPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(retrieve, discovery_sources()))
    result = {'scanned_at': datetime.now(timezone.utc).isoformat(),
              'source_count': len(records), 'sources': records,
              'warning': '取得成功仍需檢查內容是否最新；每站需留下文章與取捨紀錄，失敗需補查。'}
    path = save_evidence('source-scan-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%f') + '.json',
                         json.dumps(result, ensure_ascii=False, indent=2))
    return {**result, 'evidence_path': path}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    sub.add_parser('status')
    sub.add_parser('scan')
    mode = sub.add_parser('mode'); mode.add_argument('value', choices=['legacy', 'python'])
    search = sub.add_parser('lookup'); search.add_argument('--pattern', required=True); search.add_argument('--cutoff')
    fetch = sub.add_parser('fetch'); fetch.add_argument('url'); fetch.add_argument('--refresh', action='store_true')
    args = parser.parse_args()
    try:
        if args.action == 'mode':
            set_profile(args.value)
        if args.action in {'mode', 'status'}:
            result = {
                'mode': profile(),
                'instructions': instructions(),
                'tech_discovery_sources': [
                    {'name': name, 'url': url} for name, url in discovery_sources()
                ],
                'publishing_changed': False,
            }
        elif args.action == 'lookup':
            result = lookup(args.pattern, args.cutoff)
        elif args.action == 'scan':
            result = scan_sources()
        else:
            result = fetch_source(args.url, args.refresh)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        print(f'Research helper failed: {type(exc).__name__}; no publication or delivery performed', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
