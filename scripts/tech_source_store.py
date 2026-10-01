#!/usr/bin/env python3
"""Local CSV store for daily technology discovery sources."""

import argparse
import csv
from datetime import datetime
import os
from pathlib import Path
import tempfile
from urllib.parse import urlsplit, urlunsplit
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / 'wiki/daily/config/tech-sources.csv'
FIELDS = ('url', 'added_at', 'website', 'category', 'enabled', 'origin', 'note')


def normalized_url(value):
    parsed = urlsplit(value.strip())
    if parsed.scheme != 'https' or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError('網址必須是沒有帳密的 HTTPS 網址')
    if parsed.port and parsed.port != 443:
        raise ValueError('網址不可使用非標準連接埠')
    return urlunsplit(('https', parsed.netloc.lower(), parsed.path or '/', parsed.query, ''))


def read_sources(path=CSV_PATH):
    path = path.resolve()
    with path.open('r', encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        if tuple(reader.fieldnames or ()) != FIELDS:
            raise ValueError('來源 CSV 欄位不符：' + ','.join(FIELDS))
        rows = []
        seen = set()
        for number, row in enumerate(reader, 2):
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f'第 {number} 列欄位數不符')
            url = normalized_url(row['url'])
            if url in seen:
                raise ValueError(f'第 {number} 列網址重複：{url}')
            seen.add(url)
            if row['enabled'].strip().lower() not in {'true', 'false'}:
                raise ValueError(f'第 {number} 列 enabled 必須是 true 或 false')
            row['url'] = url
            row['enabled'] = row['enabled'].strip().lower()
            rows.append(row)
    return rows


def write_sources(rows, path=CSV_PATH):
    path = path.resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix='.tech-sources-', suffix='.csv', dir=path.parent)
    try:
        with os.fdopen(descriptor, 'w', encoding='utf-8-sig', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def add_source(url, website='', category='其他', origin='local', note='', path=CSV_PATH):
    url = normalized_url(url)
    rows = read_sources(path)
    if any(row['url'] == url for row in rows):
        return False
    rows.append({'url': url,
                 'added_at': datetime.now(ZoneInfo('Asia/Taipei')).isoformat(timespec='seconds'),
                 'website': website.strip() or urlsplit(url).hostname,
                 'category': category.strip() or '其他', 'enabled': 'true',
                 'origin': origin.strip() or 'local', 'note': note.strip()})
    write_sources(rows, path)
    return True


def source_list_messages(rows, checked_at):
    """Include every CSV field and split text below LINE's 5000 UTF-16 unit limit."""
    labels = {'url': '網址', 'added_at': '加入時間', 'website': '網站名稱',
              'category': '類別', 'enabled': '啟用狀態', 'origin': '加入來源', 'note': '備註'}
    text = f'目前網址清單：共 {len(rows)} 筆（含停用）\n查詢時間：{checked_at}\n'
    for index, row in enumerate(rows, 1):
        text += f'\n[{index}]\n'
        for field in FIELDS:
            value = row[field] or ('未記錄' if field == 'added_at' else '未填寫')
            if field == 'enabled':
                value = '啟用' if value == 'true' else '停用'
            text += f'{labels[field]}：{value}\n'
    parts, current, units = [], [], 0
    for char in text:
        size = len(char.encode('utf-16-le')) // 2
        if units + size > 4500:
            parts.append(''.join(current)); current, units = [], 0
        current.append(char); units += size
    if current:
        parts.append(''.join(current))
    return [f'網址清單 {index}/{len(parts)}\n{part}' for index, part in enumerate(parts, 1)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    sub.add_parser('list')
    add = sub.add_parser('add')
    add.add_argument('url')
    add.add_argument('--website', default='')
    add.add_argument('--category', default='其他')
    add.add_argument('--origin', default='local')
    add.add_argument('--note', default='')
    args = parser.parse_args()
    if args.action == 'add':
        print('已新增' if add_source(args.url, args.website, args.category, args.origin, args.note)
              else '網址已存在')
    else:
        for row in read_sources():
            print(f"{row['enabled']}\t{row['website']}\t{row['url']}")


if __name__ == '__main__':
    main()
