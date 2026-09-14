#!/usr/bin/env python3
"""Scoped, bounded lifecycle guard. No network, transcript reads, or LINE sends."""

from datetime import datetime, timedelta
import fcntl
import hashlib
import json
import os
from pathlib import Path
import sys
import uuid
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
PRIVATE = Path.home() / ".codex/automations/ai"
SESSION = "01a02beb-5305-7900-a265-7e06ad01ccbd"
TZ = ZoneInfo("Asia/Taipei")
MAX_CONTINUATIONS = 3
MAX_MINUTES = 90
MAX_UNCHANGED = 2


def now():
    return datetime.now(TZ)


def read_json(path):
    try:
        data = json.loads(path.read_text())
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def write_json(path, data):
    from line_watchdog_source import write_atomic
    write_atomic(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def folder(day):
    return ROOT / f"wiki/daily/{day[:4]}/{day[5:7]}/{day}"


def complete(state):
    """Require publication receipts AND unchanged validated local artifacts."""
    from line_watchdog_source import sent_date, validate_deck
    from render_daily_slides import parse_report
    day = now().date().isoformat()
    try:
        if state.get("date") != day or state.get("stage") != "complete":
            return False
        if sent_date(PRIVATE / "line-sent-key") != day:
            return False
        relative = f"wiki/daily/{day[:4]}/{day[5:7]}/{day}/slides-{day}.html"
        expected = f"https://lucaskk.github.io/daily-news/{relative}?v={state['version']}"
        if state.get("public_url") != expected or not state.get("line_result"):
            return False
        report = folder(day) / f"daily-news-{day}.md"
        notes = folder(day) / f"source-notes-{day}.md"
        data = parse_report(report.read_text())
        stamp = datetime.fromisoformat(state["cutoff"]).astimezone(TZ).strftime("%Y-%m-%d %H:%M:%S")
        if data["date"] != day or stamp not in data["cutoff"] or stamp not in notes.read_text():
            return False
        validate_deck((ROOT / relative).read_text(), day)
        hashes = state.get("verified_hashes", {})
        # A legacy completed run has no byte receipts; never resend it automatically.
        if not hashes:
            return True
        for name in (relative, "wiki/daily/latest-slides.html", "index.html"):
            if hashes.get(name) != hashlib.sha256((ROOT / name).read_bytes()).hexdigest():
                return False
        return True
    except (OSError, ValueError, KeyError, TypeError):
        return False


def heartbeat(prompt):
    # Only recognize the outer scheduler envelope, never quoted text inside a chat.
    if not prompt.strip().startswith("<heartbeat>"):
        return False
    try:
        root = ET.fromstring(prompt.strip())
        return root.tag == "heartbeat" and root.findtext("automation_id") == "ai"
    except ET.ParseError:
        return False


def context(guard, state):
    from news_workflow import instructions
    day = guard["date"]
    cutoff = state.get("cutoff", "尚未建立；先執行 begin 凍結截點")
    stage = state.get("stage", "research_pending")
    step = (f"python3 scripts/daily_news_pipeline.py finish --date {day}"
            if stage != "research_pending" else
            "接續來源筆記與日報；完成後執行 daily_news_pipeline.py finish")
    return (instructions() + f"當前仍是 {day} 每日新聞產製，不是歷史對話的介面／告警問題。"
            f"凍結截點：{cutoff}；階段：{stage}；下一步：{step}。"
            "先讀 wiki/daily/README.md 及當日來源筆記，不讀完整歷史表；"
            "新來源與去重結果分批落檔。發布驗證與唯一 LINE watchdog 成功後，"
            f"執行 python3 scripts/daily_news_pipeline.py check --date {day}。"
            "不得為通過檢查捏造新聞、改寫成功狀態、重送或修改防護。"
            "若使用者要求停止、暫停或改做別的工作，尊重最新要求；"
            "若有無法修復的障礙，說明實際原因，不宣稱完成。")


def progress(state):
    day = now().date().isoformat()
    paths = [folder(day) / f"{prefix}-{day}.{ext}" for prefix, ext in
             [("daily-news", "md"), ("source-notes", "md"), ("slides", "html")]]
    result = [state.get("stage"), state.get("commit")]
    for path in paths:
        result.append(hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None)
    return result


def handle(event):
    if event.get("session_id") != SESSION or Path(event.get("cwd", "/")).resolve() != ROOT.resolve():
        return {}
    day = now().date().isoformat()
    PRIVATE.mkdir(parents=True, exist_ok=True)
    path = PRIVATE / f"guard-{day}.json"
    with (PRIVATE / "guard.lock").open("a+") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        guard = read_json(path)
        state = read_json(PRIVATE / f"production-{day}.json")
        kind = event.get("hook_event_name")
        if kind not in {"UserPromptSubmit", "SessionStart", "Stop", "Interrupt", "PipelineBegin"}:
            return {}
        turn = event.get("turn_id", "")
        # Retain bounded, non-content evidence even if a hook safely declines action.
        audit_path = PRIVATE / f"guard-events-{day}.json"
        audit = read_json(audit_path).get("events", [])
        if not isinstance(audit, list):
            audit = []
        audit.append({
            "date": day, "event": kind, "at": now().isoformat(),
            "has_turn_id": bool(turn), "status_before": guard.get("status"),
            "stop_hook_active": bool(event.get("stop_hook_active")),
        })
        write_json(audit_path, {"events": audit[-64:]})
        if kind in {"UserPromptSubmit", "PipelineBegin"}:
            prompt = event.get("prompt", "")
            continuation = guard.get("status") == "active" and bool(guard.get("last_reason")) and prompt == guard["last_reason"]
            resume = prompt.strip() == "繼續今日新聞產製"
            if not (kind == "PipelineBegin" or heartbeat(prompt) or continuation or resume):
                if guard.get("status") == "active":
                    guard.update(status="paused", cause="new_user_input")
                    write_json(path, guard)
                return {}
            if complete(state):
                return {}
            if guard.get("date") != day:
                guard = {"date": day, "started_at": now().isoformat(), "count": 0,
                         "unchanged": 0, "nonce": uuid.uuid4().hex}
            # Neither duplicate begin nor a generated continuation resets the budget.
            if guard.get("status") == "exhausted":
                return {"systemMessage": "今日新聞自動接續已達上限；需人工檢查，不再自動重跑。"}
            guard.update(status="active", turn_id=turn, cause="production")
            write_json(path, guard)
            return {"hookSpecificOutput": {"hookEventName": "UserPromptSubmit",
                                            "additionalContext": context(guard, state)}} if kind == "UserPromptSubmit" else {}
        if guard.get("date") != day or guard.get("status") != "active":
            return {}
        if kind == "Interrupt":
            guard.update(status="paused", cause="user_interrupt")
            write_json(path, guard)
            return {}
        if complete(state):
            guard.update(status="complete", cause="verified_delivery")
            write_json(path, guard)
            return {}
        if kind == "SessionStart":
            if event.get("source") not in {"compact", "resume", "startup"}:
                return {}
            return {"hookSpecificOutput": {"hookEventName": "SessionStart",
                                            "additionalContext": context(guard, state)}}
        if turn and guard.get("turn_id") and turn != guard["turn_id"]:
            return {}
        # Some hosts omit the extension turn_id. Scope + active guard still apply;
        # new user input/Interrupt above always pauses before this fallback.
        turn = turn or guard.get("turn_id") or f"active-{guard['nonce']}"
        if event.get("turn_id") and guard.get("last_stop_turn") == turn and not event.get("stop_hook_active"):
            return {"decision": "block", "reason": guard["last_reason"]}
        fingerprint = progress(state)
        guard["unchanged"] = guard.get("unchanged", 0) + 1 if fingerprint == guard.get("progress") else 0
        elapsed = now() - datetime.fromisoformat(guard["started_at"])
        if guard.get("count", 0) >= MAX_CONTINUATIONS or elapsed >= timedelta(minutes=MAX_MINUTES) or guard["unchanged"] >= MAX_UNCHANGED:
            guard.update(status="exhausted", cause="continuation_limit", checked_at=now().isoformat())
            write_json(path, guard)
            return {"systemMessage": "新聞尚未完成，自動接續已達次數／時間／無進展上限；已保留進度，LINE 由既有配送檢查告警。"}
        reason = f"[daily-news-resume:{day}:{guard['nonce']}] " + context(guard, state)
        guard.update(count=guard.get("count", 0) + 1, last_stop_turn=turn,
                     last_reason=reason, progress=fingerprint, checked_at=now().isoformat())
        write_json(path, guard)
        return {"decision": "block", "reason": reason}


def arm_from_pipeline():
    handle({"session_id": os.environ.get("CODEX_THREAD_ID"), "cwd": str(ROOT),
            "hook_event_name": "PipelineBegin"})


def main():
    try:
        event = json.load(sys.stdin)
        output = handle(event) if isinstance(event, dict) else {}
    except Exception:
        # Never leak raw input/errors, or lock the user's conversation on a bad hook.
        output = {"systemMessage": "每日新聞防護檢查失敗，未要求自動接續；請檢查防護程式。"}
    print(json.dumps(output, ensure_ascii=False))


if __name__ == "__main__":
    main()
