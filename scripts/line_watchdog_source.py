#!/usr/bin/env python3
"""Installed only at ~/.codex/automations/ai/line_watchdog.py for live delivery.

Repository reference: scripts/line_watchdog_source.py. Private configuration and
state stay beside the installed file and must never be copied into the repo.
"""

from __future__ import annotations

import json
import fcntl
import hashlib
import os
import re
import sys
import tempfile
import time
import uuid
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta
from html.parser import HTMLParser
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parent
ENV_PATH = ROOT / "line.env"
STATE_PATH = ROOT / "line-sent-key"
ALERT_STATE_PATH = ROOT / "line-missing-alert-key"
LINE_PUSH_URL = "https://api.line.me/v2/bot/message/push"
TAIPEI = ZoneInfo("Asia/Taipei")


def write_atomic(path: Path, text: str) -> None:
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as stream:
        temporary = Path(stream.name)
        try:
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
        except BaseException:
            temporary.unlink(missing_ok=True)
            raise
    try:
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def record_status(state: str, now: datetime, **extra) -> None:
    write_atomic(ROOT / "line-watchdog-status.json", json.dumps({
        "checked_at": now.isoformat(timespec="seconds"),
        "date": now.date().isoformat(), "status": state, **extra,
    }, ensure_ascii=False, indent=2) + "\n")


def sent_date(path: Path) -> str:
    return path.read_text().strip().split(":", 1)[0] if path.exists() else ""


def log(message: str, *, error: bool = False) -> None:
    timestamp = datetime.now(TAIPEI).isoformat(timespec="seconds")
    print(f"{timestamp} {message}", file=sys.stderr if error else sys.stdout)


def load_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        raise FileNotFoundError("Missing private LINE configuration")

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        values[key.strip()] = value
    return values


def require(values: dict[str, str], key: str) -> str:
    value = values.get(key, "").strip()
    if not value:
        raise ValueError(f"Missing required setting: {key}")
    return value


def fetch(url: str, *, method: str = "GET", data: bytes | None = None, headers: dict[str, str] | None = None) -> bytes:
    request = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def push_text(token: str, to_id: str, text: str, retry_key: str) -> bool:
    payload = {"to": to_id, "messages": [{"type": "text", "text": text}]}
    for attempt in range(3):
        try:
            fetch(LINE_PUSH_URL, method="POST", data=json.dumps(payload).encode("utf-8"), headers={
                "Authorization": f"Bearer {token}", "Content-Type": "application/json",
                "X-Line-Retry-Key": retry_key,
            })
            return True
        except urllib.error.HTTPError as exc:
            if exc.code == 409 and (exc.headers or {}).get("x-line-accepted-request-id"):
                return True
            log(f"LINE push failed: HTTP {exc.code}", error=True)
            if exc.code < 500:
                return False
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            log(f"LINE push failed: {type(exc).__name__}", error=True)
        if attempt < 2:
            time.sleep(2 ** (attempt + 1))
    return False


def send_once(token: str, to_id: str, text: str, kind: str, now: datetime, state_path: Path) -> bool:
    day = now.date().isoformat()
    if sent_date(state_path) == day:
        return True
    request_path = ROOT / f"line-request-{kind}-{day}.json"
    recipient_hash = hashlib.sha256(to_id.encode()).hexdigest()
    if request_path.exists():
        request = json.loads(request_path.read_text())
        age = now - datetime.fromisoformat(request["created_at"])
        if age < timedelta(0) or age >= timedelta(hours=23, minutes=55):
            raise ValueError("Uncertain LINE request is outside its safe retry window; manual reconciliation required")
        if request["recipient_hash"] != recipient_hash:
            raise ValueError("Recipient changed during a pending LINE request")
    else:
        request = {"retry_key": str(uuid.uuid4()), "created_at": now.isoformat(),
                   "recipient_hash": recipient_hash, "text": text}
        # Persist the first payload/key before POST, so timeouts and process crashes
        # retry exactly the same request rather than sending a second message.
        write_atomic(request_path, json.dumps(request, ensure_ascii=False) + "\n")
    if not push_text(token, to_id, request["text"], request["retry_key"]):
        return False
    write_atomic(state_path, day + "\n")
    return True


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refresh = ""
        self.in_report = False
        self.report = []
        self.article_ranks = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "refresh":
            self.refresh = attrs.get("content", "")
        if tag == "script":
            self.in_report = attrs.get("id") == "report-data"
        if tag == "article":
            self.article_ranks.append(attrs.get("data-rank"))

    def handle_endtag(self, tag):
        if tag == "script":
            self.in_report = False

    def handle_data(self, data):
        if self.in_report:
            self.report.append(data)


def public_deck(base_url: str, latest_url: str, today: str) -> tuple[str, str]:
    page = Page()
    page.feed(fetch(latest_url, headers={"Cache-Control": "no-cache"}).decode("utf-8"))
    match = re.search(r"url\s*=\s*(.+)$", page.refresh, re.I)
    if not match:
        raise ValueError("Latest entry has no dated deck redirect")
    slide_url = urllib.parse.urljoin(latest_url, match[1].strip().strip("\"'"))
    parts = urllib.parse.urlsplit(slide_url)
    expected = f"{base_url}/wiki/daily/{today[:4]}/{today[5:7]}/{today}/slides-{today}.html"
    target = urllib.parse.urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))
    if target != expected:
        raise ValueError("Latest entry does not point to today's trusted dated deck")
    validate_deck(fetch(slide_url).decode("utf-8"), today)
    return slide_url, today


def validate_deck(html: str, today: str) -> None:
    """Use the same structural gate before publishing and before delivery."""
    deck = Page()
    deck.feed(html)
    report = json.loads("".join(deck.report))
    if not isinstance(report, dict) or report.get("date") != today:
        raise ValueError("Public HTML report date does not match today")
    stories = report.get("stories", [])
    if not isinstance(stories, list) or not all(isinstance(s, dict) for s in stories):
        raise ValueError("Public report stories are malformed")
    for story in stories:
        sources = story.get("sources")
        if story.get("category") not in {"tech", "world"} or not isinstance(sources, list) or not sources:
            raise ValueError("Public report contains an invalid category or missing sources")
        for source in sources:
            if not isinstance(source, dict) or not isinstance(source.get("label"), str) or not source["label"].strip():
                raise ValueError("Public report source label is missing")
            url = source.get("url")
            if not isinstance(url, str) or urllib.parse.urlsplit(url).scheme not in {"http", "https"} or not urllib.parse.urlsplit(url).netloc:
                raise ValueError("Public report source URL is invalid")
    world = [s.get("rank") for s in stories if s.get("category") == "world"]
    if world != [str(i) for i in range(1, 11)] or not all(s.get("sources") for s in stories):
        raise ValueError("Public HTML is missing ten ordered world stories or sources")
    if deck.article_ranks != [s.get("rank") for s in stories]:
        raise ValueError("Public HTML articles do not match embedded report data")
    tech = [s for s in stories if s["category"] == "tech"]
    if [s.get("rank") for s in tech] != [f"T{i}" for i in range(1, len(tech) + 1)] or stories != tech + [s for s in stories if s["category"] == "world"]:
        raise ValueError("Public report product order is invalid")


def run_once(now: datetime) -> int:
    today = now.date().isoformat()
    if os.environ.get("FORCE_LINE_PUSH") == "1":
        raise ValueError("Forced delivery is disabled; reconcile delivery state explicitly instead")
    if sent_date(STATE_PATH) == today:
        record_status("already_sent", now, delivered_date=today)
        if os.environ.get("LINE_WATCHDOG_QUIET") != "1":
            log(f"LINE daily slides already sent for {today}")
        return 0
    env = load_env(ENV_PATH)
    base_url = require(env, "PUBLIC_SLIDES_BASE_URL").rstrip("/")
    token = require(env, "LINE_CHANNEL_ACCESS_TOKEN")
    to_id = require(env, "LINE_TO_ID")

    latest_path = env.get("DAILY_SLIDES_PATH", "/wiki/daily/latest-slides.html")
    latest_url = f"{base_url}/{latest_path.lstrip('/')}"
    alert_hour = int(env.get("LINE_MISSING_ALERT_HOUR", "10"))
    if not 0 <= alert_hour <= 23:
        raise ValueError("Invalid missing-publish alert hour")
    try:
        slide_url, slide_date = public_deck(base_url, latest_url, today)
    except (urllib.error.URLError, OSError, ValueError) as exc:
        reason = f"{type(exc).__name__}: {exc}"
        if now.hour >= alert_hour:
            alert_text = (
                "Daily News 發布異常\n"
                f"日期：{today}\n"
                f"截至：{now:%H:%M}（Asia/Taipei）\n"
                "今日公開新聞尚未通過日期、完整性或連線檢查。\n"
                "請檢查 Codex 產製與 GitHub Pages。系統會持續檢查，恢復後補送。"
            )
            already_alerted = sent_date(ALERT_STATE_PATH) == today
            alerted = send_once(token, to_id, alert_text, "alert", now, ALERT_STATE_PATH)
            if alerted and not already_alerted:
                log(f"Sent LINE missing-publish alert: {today}")
            record_status("publish_unavailable", now, error=reason, alert_accepted=alerted)
            return 1  # An accepted alert does not mean the news was delivered.
        record_status("waiting_for_publish", now, error=reason)
        return 0

    message = (
        "Daily News 投影片已完成\n"
        f"日期：{slide_date}\n"
        "主旨：每日全球與科技 AI 新聞\n"
        f"連結：{slide_url}"
    )
    if not send_once(token, to_id, message, "news", now, STATE_PATH):
        record_status("delivery_failed", now, slide_url=slide_url)
        return 1
    record_status("sent", now, delivered_date=today, slide_url=slide_url)
    log(f"Sent LINE message: {slide_date} | {slide_url}")
    return 0


def main() -> int:
    now = datetime.now(TAIPEI)
    with (ROOT / "line-watchdog.lock").open("a+") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            log("Another LINE watchdog is running; no duplicate execution")
            return 0
        try:
            return run_once(now)
        except Exception as exc:
            log(f"LINE watchdog failed: {type(exc).__name__}: {exc}", error=True)
            record_status("error", now, error=f"{type(exc).__name__}: {exc}")
            return 1


if __name__ == "__main__":
    raise SystemExit(main())
