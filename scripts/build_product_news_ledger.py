#!/usr/bin/env python3
"""Build a searchable product-news ledger from all historical daily reports."""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DAILY_ROOT = ROOT / "wiki" / "daily"
OUTPUT = DAILY_ROOT / "product-news-ledger.md"

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
    capture_date: str
    company: str
    title: str
    published_at: str
    status: str
    prior_date: str
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


def prior_capture(block: str, capture_date: str, continuation: bool) -> str:
    if not continuation:
        return capture_date
    candidates = [d for d in DATE_RE.findall(block) if d < capture_date]
    return min(candidates) if candidates else "續報；前次日期未能由區塊自動解析"


def comparison_key(company: str, title: str) -> str:
    normalized = re.sub(r"[^0-9a-z\u4e00-\u9fff]+", "", f"{company}|{title}".lower())
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:12]


def from_heading_section(section: str, capture_date: str) -> list[Item]:
    matches = list(ITEM_HEADING.finditer(section))
    items: list[Item] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(section)
        block = section[match.start() : end]
        title = match.group(2).strip()
        continuation = title.startswith("續報｜")
        company = company_for(title)
        urls = tuple(dict.fromkeys(clean_url(url) for url in URL_RE.findall(block)))
        items.append(
            Item(
                capture_date=capture_date,
                company=company,
                title=title,
                published_at=publication_time(block, capture_date),
                status="續報" if continuation else "首次收錄",
                prior_date=prior_capture(block, capture_date, continuation),
                urls=urls,
                key=comparison_key(company, title),
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
        urls = tuple(dict.fromkeys(clean_url(url) for url in URL_RE.findall(line)))
        items.append(
            Item(
                capture_date=capture_date,
                company=company,
                title=title,
                published_at=f"{capture_date}（當日報告未單列時間）",
                status="續報" if continuation else "首次收錄",
                prior_date="續報；請查來源筆記" if continuation else capture_date,
                urls=urls,
                key=comparison_key(company, title),
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


def render(items: list[Item], report_count: int) -> str:
    rows = []
    for item in sorted(items, key=lambda x: (x.capture_date, x.title), reverse=True):
        source_links = "<br>".join(item.urls) if item.urls else "當日報告未保留可解析網址"
        rows.append(
            "| "
            + " | ".join(
                table_escape(value)
                for value in (
                    item.capture_date,
                    item.company,
                    item.title,
                    item.published_at,
                    item.status,
                    item.prior_date,
                    source_links,
                    item.key,
                )
            )
            + " |"
        )
    return f"""---
title: "科技產品新聞歷史比對表"
type: product-news-ledger
updated: {max((item.capture_date for item in items), default='unknown')}
status: generated
tags: [daily-news, tech-products, deduplication, provenance]
---

# 科技產品新聞歷史比對表

此表由 `scripts/build_product_news_ledger.py` 掃描所有歷史日報的科技／AI 區段自動產生，用於每日選題前快速去重。它是輔助索引，不取代對 `daily-news-*.md`、`source-notes-*.md` 與原始來源的全文搜尋及人工事件判讀。

- 掃描日報：{report_count} 份。
- 擷取科技／AI 項目：{len(items)} 則。
- 更新方式：`python3 scripts/build_product_news_ledger.py`
- 時間限制：全球新聞仍採 24 小時；科技產品候選可採 7 天，但已收錄的同一產品變更不得重複。

| 收錄日期 | 公司／組織 | 產品／更新內容 | 事件／發佈時間 | 狀態 | 首次或前次相關日期 | 參考網址 | 比對鍵 |
|---|---|---|---|---|---|---|---|
{chr(10).join(rows)}
"""


def main() -> None:
    reports = sorted(DAILY_ROOT.glob("**/daily-news-*.md"))
    items: list[Item] = []
    for report in reports:
        items.extend(extract_items(report))
    OUTPUT.write_text(render(items, len(reports)), encoding="utf-8")
    print(f"Wrote {len(items)} product records from {len(reports)} reports to {OUTPUT}")


if __name__ == "__main__":
    main()
