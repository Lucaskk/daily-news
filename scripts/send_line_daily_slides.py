#!/usr/bin/env python3
"""Push the latest daily slides URL to LINE Messaging API.

Required environment variables:
- LINE_CHANNEL_ACCESS_TOKEN
- LINE_TO_ID
- PUBLIC_SLIDES_BASE_URL

Optional:
- DAILY_SLIDES_PATH, defaults to /wiki/daily/latest-slides.html
- DAILY_REPORT_PATH, used to derive date and subject for the LINE message
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


LINE_PUSH_URL = "https://api.line.me/v2/bot/message/push"
DEFAULT_RETRIES = 4
DEFAULT_RETRY_DELAY_SECONDS = 5


def require_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value


def join_url(base: str, path: str) -> str:
    return base.rstrip("/") + "/" + path.lstrip("/")


def read_text(path: str | Path) -> str:
    return Path(path).read_text(encoding="utf-8")


def int_env(name: str, default: int) -> int:
    value = os.environ.get(name, "").strip()
    if not value:
        return default
    try:
        return max(1, int(value))
    except ValueError:
        raise SystemExit(f"Invalid integer environment variable: {name}")


def infer_report_path(slides_path: str) -> Path | None:
    explicit = os.environ.get("DAILY_REPORT_PATH", "").strip()
    if explicit:
        return Path(explicit)

    if "latest-slides.html" in slides_path:
        latest = Path("wiki/daily/latest-slides.html")
        if not latest.exists():
            return None
        latest_html = read_text(latest)
        match = re.search(r"url=([^\"'>]+slides-(\d{4}-\d{2}-\d{2})\.html)", latest_html)
        if not match:
            return None
        relative_slide = match.group(1)
        date = match.group(2)
        return latest.parent / Path(relative_slide).parent / f"daily-news-{date}.md"

    match = re.search(r"slides-(\d{4}-\d{2}-\d{2})\.html", slides_path)
    if not match:
        return None
    date = match.group(1)
    return Path(slides_path.lstrip("/")).parent / f"daily-news-{date}.md"


def extract_subject(report_path: Path | None) -> tuple[str, str]:
    if not report_path or not report_path.exists():
        return "今日 Daily News", "每日全球與科技 AI 新聞投影片"

    text = read_text(report_path)
    date_match = re.search(r"date:\s*(\d{4}-\d{2}-\d{2})", text)
    heading_match = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    brief_match = re.search(
        r"## Executive Brief\s+(.+?)(?:\n## |\Z)",
        text,
        flags=re.DOTALL,
    )

    date = date_match.group(1) if date_match else report_path.stem.replace("daily-news-", "")
    title = heading_match.group(1).strip() if heading_match else f"Daily News {date}"

    subject = title
    if brief_match:
        first_paragraph = re.sub(r"\s+", " ", brief_match.group(1).strip().split("\n\n")[0])
        if first_paragraph:
            subject = first_paragraph[:92].rstrip("，。；、 ") + ("..." if len(first_paragraph) > 92 else "")

    return date, subject


def main() -> int:
    token = require_env("LINE_CHANNEL_ACCESS_TOKEN")
    to_id = require_env("LINE_TO_ID")
    base_url = require_env("PUBLIC_SLIDES_BASE_URL")
    slides_path = os.environ.get("DAILY_SLIDES_PATH", "/wiki/daily/latest-slides.html")
    retries = int_env("LINE_PUSH_RETRIES", DEFAULT_RETRIES)
    retry_delay = int_env("LINE_PUSH_RETRY_DELAY_SECONDS", DEFAULT_RETRY_DELAY_SECONDS)
    slides_url = join_url(base_url, slides_path)
    report_path = infer_report_path(slides_path)
    date, subject = extract_subject(report_path)

    payload = {
        "to": to_id,
        "messages": [
            {
                "type": "text",
                "text": (
                    f"Daily News 投影片已完成\n"
                    f"日期：{date}\n"
                    f"主旨：{subject}\n"
                    f"連結：{slides_url}"
                ),
            }
        ],
    }

    for attempt in range(1, retries + 1):
        request = urllib.request.Request(
            LINE_PUSH_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
            method="POST",
        )

        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                response.read()
            break
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            retryable = exc.code == 429 or 500 <= exc.code < 600
            if not retryable or attempt == retries:
                print(f"LINE push failed: HTTP {exc.code}\n{body}", file=sys.stderr)
                return 1
            print(
                f"LINE push attempt {attempt}/{retries} failed: HTTP {exc.code}; retrying...",
                file=sys.stderr,
            )
        except urllib.error.URLError as exc:
            if attempt == retries:
                print(f"LINE push failed: {exc}", file=sys.stderr)
                return 1
            print(f"LINE push attempt {attempt}/{retries} failed: {exc}; retrying...", file=sys.stderr)

        time.sleep(retry_delay * attempt)

    print(f"Sent LINE message: {date} | {subject} | {slides_url}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
