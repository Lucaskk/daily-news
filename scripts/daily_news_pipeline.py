#!/usr/bin/env python3
"""Durable daily checkpoint and bounded render -> publish -> LINE completion."""

import argparse
from datetime import date, datetime
import fcntl
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time

import line_watchdog_source as watchdog
import render_daily_slides as reader

ROOT = Path(__file__).resolve().parents[1]
PRIVATE = Path.home() / ".codex/automations/ai"
BASE = "https://lucaskk.github.io/daily-news"
REPO = "https://github.com/Lucaskk/daily-news.git"


def now():
    return datetime.now(watchdog.TAIPEI)


def state_path(day):
    date.fromisoformat(day)
    return PRIVATE / f"production-{day}.json"


def save(state, stage, **extra):
    if "last_error" not in extra:
        state.pop("last_error", None)
    state.update(stage=stage, checked_at=now().isoformat(timespec="seconds"), **extra)
    watchdog.write_atomic(state_path(state["date"]), json.dumps(state, ensure_ascii=False, indent=2) + "\n")


def begin(day, cutoff=None):
    path = state_path(day)
    if path.exists():
        state = json.loads(path.read_text())
        if cutoff and datetime.fromisoformat(cutoff) != datetime.fromisoformat(state["cutoff"]):
            raise ValueError("A resumed run must retain its frozen cutoff")
        return state
    stamp = datetime.fromisoformat(cutoff) if cutoff else now()
    if stamp.tzinfo is None or stamp.astimezone(watchdog.TAIPEI).date().isoformat() != day:
        raise ValueError("Cutoff needs an explicit timezone and must match the run date")
    state = {"date": day, "cutoff": stamp.isoformat(timespec="seconds")}
    save(state, "research_pending")
    return state


def command(args, cwd=ROOT):
    try:
        result = subprocess.run(args, cwd=cwd, text=True, capture_output=True, timeout=180)
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"{Path(args[0]).name} command timed out") from None
    if result.returncode:
        # Keep command output out of persisted state: tools may print credentials.
        raise RuntimeError(f"{Path(args[0]).name} {args[1] if len(args) > 1 else ''} exited {result.returncode}")
    return result.stdout


def prepare(state):
    day = state["date"]
    folder = ROOT / f"wiki/daily/{day[:4]}/{day[5:7]}/{day}"
    report = folder / f"daily-news-{day}.md"
    notes = folder / f"source-notes-{day}.md"
    if not report.is_file() or not notes.is_file() or len(notes.read_text().strip()) < 100:
        raise ValueError("Research incomplete: report and source notes are required")
    data = reader.parse_report(report.read_text())
    frozen = datetime.fromisoformat(state["cutoff"]).astimezone(watchdog.TAIPEI).strftime("%Y-%m-%d %H:%M:%S")
    if data["date"] != day or frozen not in data["cutoff"] or frozen not in notes.read_text():
        raise ValueError("Report/source notes do not retain the frozen date and cutoff")
    output, version = reader.render(report)
    watchdog.validate_deck(output.read_text(), day)
    reader.update_entries(output, version)
    command([sys.executable, "scripts/build_product_news_ledger.py"])
    allowed_names = {f"{prefix}-{day}.{extension}" for prefix, extension in [
        ("daily-news", "md"), ("source-notes", "md"), ("slides", "html"),
        ("presentation", "json"), ("source-evidence", "json")]}
    files = [p.relative_to(ROOT) for p in folder.rglob("*") if p.is_file() and
             not p.is_symlink() and (p.parent == folder and p.name in allowed_names or
             p.parent == folder / "assets" and p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"})]
    files += [Path(p) for p in ("index.html", ".nojekyll", "wiki/daily/latest-slides.html",
                               "wiki/daily/product-news-ledger.md", "wiki/daily/product-news-recent-7d.md")]
    save(state, "ready_to_publish", version=version)
    return files


def publish(state, files):
    # A clean clone and explicit allowlist cannot accidentally commit .env or stocks.
    clone = Path(tempfile.mkdtemp(prefix=f"daily-news-pipeline-{state['date']}-"))
    save(state, "publishing", clone=str(clone))
    command(["git", "clone", "--depth", "1", "--branch", "main", REPO, str(clone)])
    for relative in files:
        target = clone / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / relative, target)
    command(["git", "add", "--", *map(str, files)], clone)
    if command(["git", "diff", "--cached", "--name-only"], clone).strip():
        command(["git", "-c", "user.name=Daily News", "-c", "user.email=daily-news@users.noreply.github.com",
                 "commit", "-m", f"Publish daily news {state['date']}"], clone)
        for attempt in range(3):
            try:
                command(["git", "push", "origin", "HEAD:main"], clone)
                break
            except RuntimeError:
                if attempt == 2:
                    raise
                time.sleep(5)
                command(["git", "fetch", "origin", "main"], clone)
                command(["git", "rebase", "origin/main"], clone)
    save(state, "verifying_pages", commit=command(["git", "rev-parse", "HEAD"], clone).strip())


def verify_public(state, attempts=20):
    day = state["date"]
    latest = f"{BASE}/wiki/daily/latest-slides.html"
    dated = f"wiki/daily/{day[:4]}/{day[5:7]}/{day}/slides-{day}.html"
    for attempt in range(attempts):
        try:
            url, _ = watchdog.public_deck(BASE, latest, day)
            for relative, remote in [(dated, url), ("wiki/daily/latest-slides.html", latest), ("index.html", BASE + "/")]:
                public = watchdog.fetch(remote, headers={"Cache-Control": "no-cache"})
                if hashlib.sha256(public).digest() != hashlib.sha256((ROOT / relative).read_bytes()).digest():
                    raise ValueError("Pages has not deployed the current bytes yet")
            save(state, "pages_verified", public_url=url)
            return
        except (OSError, ValueError):
            if attempt == attempts - 1:
                raise
            time.sleep(15)


def deliver(state):
    if state["stage"] != "pages_verified":
        raise ValueError("LINE requires verified GitHub Pages")
    for attempt in range(3):
        # The installed watchdog alone owns credentials, locks and retry keys.
        try:
            output = command([sys.executable, str(PRIVATE / "line_watchdog.py")])
            if "Sent LINE message" not in output and "already sent" not in output:
                raise RuntimeError("Watchdog did not confirm delivery")
            if watchdog.sent_date(PRIVATE / "line-sent-key") != state["date"]:
                raise RuntimeError("Watchdog success belongs to another date")
            save(state, "complete", line_result=output.strip())
            print(output.strip())
            return
        except RuntimeError:
            if attempt == 2:
                raise
            time.sleep(15)


def finish(state):
    if state["date"] != now().date().isoformat():
        raise ValueError("Refusing to publish an old run as today's news")
    if state["stage"] == "complete":
        if watchdog.sent_date(PRIVATE / "line-sent-key") != state["date"]:
            raise ValueError("Completion checkpoint conflicts with LINE delivery state")
        return
    # Resume the last committed content before considering another render/push.
    if state["stage"] not in {"verifying_pages", "pages_verified"}:
        publish(state, prepare(state))
    verify_public(state)
    deliver(state)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["begin", "status", "finish", "verify-deliver", "check"])
    parser.add_argument("--date", default=now().date().isoformat())
    parser.add_argument("--cutoff")
    args = parser.parse_args()
    PRIVATE.mkdir(parents=True, exist_ok=True)
    with (PRIVATE / "production.lock").open("a+") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("Another publication command is running", file=sys.stderr)
            return 2
        state = None
        try:
            state = begin(args.date, args.cutoff)
            if args.action == "finish":
                finish(state)
            elif args.action == "verify-deliver":
                if state["date"] != now().date().isoformat():
                    raise ValueError("Cannot deliver an old date")
                verify_public(state)
                deliver(state)
            print(json.dumps(state, ensure_ascii=False, indent=2))
            if args.action == "check":
                return 0 if state["stage"] == "complete" and watchdog.sent_date(PRIVATE / "line-sent-key") == args.date else 2
            return 0
        except Exception as exc:
            if state is not None:
                save(state, state["stage"], last_error=f"{type(exc).__name__}: {exc}")
            print(f"Daily publication incomplete: {exc}", file=sys.stderr)
            return 1


if __name__ == "__main__":
    raise SystemExit(main())
