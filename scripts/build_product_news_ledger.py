#!/usr/bin/env python3
"""Build a product comparison ledger from the previous fourteen daily reports."""

from __future__ import annotations

import hashlib
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo
import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DAILY_ROOT = ROOT / "wiki" / "daily"
RECENT_OUTPUT = DAILY_ROOT / "product-news-recent-14d.md"


def recent_report_paths(root=DAILY_ROOT, cutoff=None):
    stamp = datetime.fromisoformat(cutoff.replace('Z', '+00:00')) if cutoff else datetime.now(ZoneInfo('Asia/Taipei'))
    if stamp.tzinfo is None:
        raise ValueError('Cutoff requires an explicit timezone')
    day = stamp.astimezone(ZoneInfo('Asia/Taipei')).date()
    paths = []
    for offset in range(14, 0, -1):
        report_day = day - timedelta(days=offset)
        name = report_day.isoformat()
        path = root / name[:4] / name[5:7] / name / f'daily-news-{name}.md'
        if path.is_file():
            paths.append(path)
    return paths

TECH_HEADING = re.compile(
    r"^##\s+.*(?:科技.*(?:AI|人工智慧)|(?:Technology|Tech).*AI|AI.*(?:Product|產品))",
    re.IGNORECASE | re.MULTILINE,
)
ITEM_HEADING = re.compile(r"^###\s+(T?\d+)\.\s+(.+?)\s*$", re.MULTILINE)
URL_RE = re.compile(r"https?://[^\s)>\]]+")
DATE_RE = re.compile(r"\b(20\d{2}-\d{2}-\d{2})\b")

COMPANY_PATTERNS = [
    (r"OpenAI|ChatGPT|\bCodex\b|\bAstra\b", "OpenAI"),
    (r"Anthropic|Claude", "Anthropic"),
    (r"Google|Gemini|NotebookLM|YouTube|Android|Chrome", "Google"),
    (r"Microsoft|Azure|Windows|Xbox", "Microsoft"),
    (r"GitHub|Copilot", "GitHub"),
    (r"Apple|Siri|iPhone|iPad|MacBook", "Apple"),
    (r"Meta|WhatsApp|Instagram|Facebook", "Meta"),
    (r"Amazon|AWS|Alexa", "Amazon / AWS"),
    (r"NVIDIA|Nvidia|\bRTX\b", "NVIDIA"),
    (r"Qualcomm|高通|Dragonwing|Snapdragon", "Qualcomm"),
    (r"CrowdStrike|Falcon|SafeMind", "CrowdStrike"),
    (r"Waymo", "Waymo"),
    (r"Tesla", "Tesla"),
    (r"Samsung", "Samsung"),
    (r"IBM", "IBM"),
    (r"Cloudflare", "Cloudflare"),
    (r"Broadcom|VMware|Tanzu", "Broadcom / VMware"),
    (r"Adobe", "Adobe"),
    (r"Reducto", "Reducto"),
    (r"LogicGate", "LogicGate"),
    (r"SpaceX|\bxAI\b", "SpaceX / xAI"),
    (r"DeepSeek", "DeepSeek"),
    (r"Alibaba|Qwen", "Alibaba"),
    (r"Moonshot|Kimi", "Moonshot AI"),
    (r"ByteDance|Doubao|TikTok", "ByteDance"),
    (r"Oracle", "Oracle"),
    (r"Mistral", "Mistral AI"),
    (r"Perplexity", "Perplexity"),
    (r"Hugging Face", "Hugging Face"),
    (r"Sony", "Sony"),
    (r"Dyson", "Dyson"),
    (r"NAVEE|Fold P10", "NAVEE"),
    (r"Tuya|Doova", "Tuya Smart"),
    (r"Netflix", "Netflix"),
    (r"Spotify", "Spotify"),
    (r"Uber", "Uber"),
    (r"Airbnb", "Airbnb"),
    (r"Samsung", "Samsung"),
    (r"Huawei", "Huawei"),
    (r"Xiaomi", "Xiaomi"),
    (r"ByteDance", "ByteDance"),
]


@dataclass(frozen=True)
class Item:
    company: str
    product: str
    update: str
    published_at: str
    capture_date: str
    status: str
    urls: tuple[str, ...]
    key: str


def tech_section(text: str) -> str | None:
    match = TECH_HEADING.search(text)
    if not match:
        return None
    next_section = re.search(r"^##\s+", text[match.end() :], re.MULTILINE)
    end = match.end() + next_section.start() if next_section else len(text)
    return text[match.end() : end]


def report_date(path: Path) -> str:
    match = DATE_RE.search(path.name)
    return match.group(1) if match else "unknown"


def clean_url(url: str) -> str:
    return url.rstrip(".,;:，。；：")


def company_for(title: str) -> str:
    matches: list[tuple[int, str]] = []
    for pattern, company in COMPANY_PATTERNS:
        match = re.search(pattern, title, re.IGNORECASE)
        if match:
            matches.append((match.start(), company))
    if matches:
        return min(matches, key=lambda item: item[0])[1]
    candidate = re.sub(r"^續報[｜|]\s*", "", title).strip()
    candidate = re.split(
        r"(?:推出|發表|發布|宣布|預告|新增|開放|導入|更新|擴大|完成|收購|launch(?:es|ed)?|announc(?:es|ed)|unveil(?:s|ed)|release(?:s|d)|introduc(?:es|ed)|add(?:s|ed)|expand(?:s|ed))",
        candidate,
        maxsplit=1,
        flags=re.IGNORECASE,
    )[0].strip(" -—:：")
    words = candidate.split()
    return " ".join(words[:4])[:80] or "待人工判定"


def publication_time(block: str, capture_date: str) -> str:
    match = re.search(r"(?:發佈|發布)時間[｜:]\s*([^\n]+)", block)
    if match:
        return match.group(1).strip()
    return f"{capture_date}（當日報告未單列時間）"


def update_content(title: str) -> str:
    return re.sub(r"^續報[｜|]\s*", "", title).strip()


def product_for(company: str, title: str) -> str:
    candidate = update_content(title)
    company_aliases = {company}
    company_aliases.update(part.strip() for part in re.split(r"[/／]", company))
    for alias in sorted(company_aliases, key=len, reverse=True):
        candidate = re.sub(
            rf"^{re.escape(alias)}(?:\s*[｜|:：-]\s*|\s+)",
            "",
            candidate,
            count=1,
            flags=re.IGNORECASE,
        )

    candidate = re.sub(
        r"^(?:正式)?(?:預告|推出|發表|發布|宣布|上線|開放|新增|更新|擴大|導入|完成|收購)\s*",
        "",
        candidate,
    )
    product = re.split(
        r"[，。；;]|\s+(?:將|主打|結合|提供|支援|加入|帶來|進入|擴至|開放|成為)\s*",
        candidate,
        maxsplit=1,
    )[0].strip(" -—:：")
    if product.startswith(("在 ", "於 ")) or len(product) > 80:
        return company
    return product or company


def comparison_key(company: str, product: str, update: str) -> str:
    normalized = re.sub(
        r"[^0-9a-z\u4e00-\u9fff]+", "", f"{company}|{product}|{update}".lower()
    )
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:12]


def from_heading_section(section: str, capture_date: str) -> list[Item]:
    matches = list(ITEM_HEADING.finditer(section))
    items: list[Item] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(section)
        block = section[match.start() : end]
        title = match.group(2).strip()
        continuation = title.startswith("續報｜")
        metadata = re.search(r"公司／產品[｜:]\s*([^｜\n]+)｜([^\n]+)", block)
        if metadata:
            company = metadata.group(1).strip()
            product = metadata.group(2).strip()
        else:
            company = company_for(title)
            product = product_for(company, title)
        update = update_content(title)
        urls = tuple(dict.fromkeys(clean_url(url) for url in URL_RE.findall(block)))
        items.append(
            Item(
                company=company,
                product=product,
                update=update,
                published_at=publication_time(block, capture_date),
                capture_date=capture_date,
                status="續報" if continuation else "首次收錄",
                urls=urls,
                key=comparison_key(company, product, update),
            )
        )
    return items


def split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def from_table_section(section: str, capture_date: str) -> list[Item]:
    items: list[Item] = []
    for line in section.splitlines():
        if not re.match(r"^\|\s*\d+\s*\|", line):
            continue
        cells = split_table_row(line)
        if len(cells) < 3 or not cells[0].isdigit():
            continue
        title = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", cells[1]).strip()
        if not title:
            continue
        continuation = title.startswith("續報｜")
        company = company_for(title)
        product = product_for(company, title)
        update = update_content(title)
        urls = tuple(dict.fromkeys(clean_url(url) for url in URL_RE.findall(line)))
        items.append(
            Item(
                company=company,
                product=product,
                update=update,
                published_at=f"{capture_date}（當日報告未單列時間）",
                capture_date=capture_date,
                status="續報" if continuation else "首次收錄",
                urls=urls,
                key=comparison_key(company, product, update),
            )
        )
    return items


def extract_items(path: Path) -> list[Item]:
    text = path.read_text(encoding="utf-8")
    section = tech_section(text)
    if not section:
        return []
    capture_date = report_date(path)
    heading_items = from_heading_section(section, capture_date)
    return heading_items if heading_items else from_table_section(section, capture_date)


def table_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def render_rows(items: list[Item]) -> str:
    rows = []
    for item in sorted(items, key=lambda x: (x.capture_date, x.update), reverse=True):
        source_links = "<br>".join(item.urls) if item.urls else "當日報告未保留可解析網址"
        rows.append(
            "| "
            + " | ".join(
                table_escape(value)
                for value in (
                    item.company,
                    item.product,
                    item.update,
                    item.published_at,
                    item.capture_date,
                    item.status,
                    source_links,
                    item.key,
                )
            )
            + " |"
        )
    return "\n".join(rows)


def render_recent(items: list[Item], report_count: int) -> str:
    known_dates = [date.fromisoformat(item.capture_date) for item in items if item.capture_date != "unknown"]
    latest = max(known_dates, default=date.today())
    start = latest - timedelta(days=13)
    recent = [
        item
        for item in items
        if item.capture_date != "unknown" and date.fromisoformat(item.capture_date) >= start
    ]
    return f"""---
title: "科技產品新聞最近 14 天比對表"
type: product-news-ledger-recent
updated: {latest.isoformat()}
status: generated
tags: [daily-news, tech-products, deduplication, recent]
---

# 科技產品新聞最近 14 天比對表

本檔只整理產製日前 14 天的日報，可完整讀取做去重確認；不搜尋更早日報、完整歷史表或來源筆記。實際發布窗仍以當日研究截點與來源筆記判定。

- 掃描日報：{report_count} 份。
- 最近 14 天項目：{len(recent)} 則。
- 日報日期範圍：{min(known_dates).isoformat() if known_dates else '無日報'} 至 {max(known_dates).isoformat() if known_dates else '無日報'}。

| 公司 | 產品 | 更新內容 | 發佈時間 | 收錄日期 | 狀態 | 來源網址 | 比對鍵 |
|---|---|---|---|---|---|---|---|
{render_rows(recent)}
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--key', nargs=3)
    parser.add_argument('--cutoff')
    args = parser.parse_args()
    if args.key:
        print(comparison_key(*args.key))
        return
    reports = recent_report_paths(DAILY_ROOT, args.cutoff)
    items: list[Item] = []
    for report in reports:
        items.extend(extract_items(report))
    RECENT_OUTPUT.write_text(render_recent(items, len(reports)), encoding="utf-8")
    print(
        f"Wrote {len(items)} product records from {len(reports)} reports to "
        f"{RECENT_OUTPUT}"
    )


if __name__ == "__main__":
    main()
