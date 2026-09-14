#!/usr/bin/env python3
"""Switchable research helpers. Never publish, send LINE, or start a model."""

import argparse
from datetime import datetime, timedelta, timezone
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import subprocess
import sys
import urllib.parse
import urllib.request

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
    if profile() == 'legacy':
        return '研究模式 legacy：沿用 AI 搜尋、按候選 rg 查歷史；無命中才讀近7天表。渲染與配送不變。'
    return ('研究模式 python：使用 scripts/news_workflow.py lookup --pattern 查歷史；'
            'fetch URL 快取來源並保留取得時間。AI仍須補充搜尋、查證發布時間、語意去重與選題；'
            '快取不是新發布證據。渲染與配送不變。')


def save_evidence(name, text):
    from line_watchdog_source import write_atomic
    directory = PRIVATE / 'research-cache'
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / name
    write_atomic(path, text)
    return str(path)


def lookup(pattern):
    if not pattern or len(pattern) > 1000:
        raise ValueError('Provide a narrow candidate pattern (1..1000 characters)')
    result = subprocess.run(['rg', '-n', '-i', '--glob', 'daily-news-*.md',
                             '--glob', 'source-notes-*.md', '--glob', 'product-news-ledger.md',
                             '--', pattern, str(ROOT / 'wiki/daily')],
                            capture_output=True, text=True, timeout=30)
    if result.returncode not in (0, 1):
        raise ValueError('rg search failed; check pattern and search paths')
    text = result.stdout
    fallback = False
    if result.returncode == 1 and profile() == 'python':
        recent = ROOT / 'wiki/daily/product-news-recent-7d.md'
        if not recent.is_file():
            raise ValueError('No recent table; first run build_product_news_ledger.py')
        text = recent.read_text()
        fallback = True
    digest = hashlib.sha256((pattern + '\n' + text).encode()).hexdigest()
    evidence = save_evidence(f'lookup-{digest}.txt', text)
    return {'mode': profile(), 'pattern': pattern, 'historical_match': result.returncode == 0,
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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    sub.add_parser('status')
    mode = sub.add_parser('mode'); mode.add_argument('value', choices=['legacy', 'python'])
    search = sub.add_parser('lookup'); search.add_argument('--pattern', required=True)
    fetch = sub.add_parser('fetch'); fetch.add_argument('url'); fetch.add_argument('--refresh', action='store_true')
    args = parser.parse_args()
    try:
        if args.action == 'mode':
            set_profile(args.value)
        if args.action in {'mode', 'status'}:
            result = {'mode': profile(), 'instructions': instructions(), 'publishing_changed': False}
        elif args.action == 'lookup':
            result = lookup(args.pattern)
        else:
            result = fetch_source(args.url, args.refresh)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        print(f'Research helper failed: {type(exc).__name__}; no publication or delivery performed', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
