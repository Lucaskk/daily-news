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
