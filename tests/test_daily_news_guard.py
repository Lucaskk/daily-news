"""Lifecycle regression tests: no model calls, network, or live LINE delivery."""
from datetime import datetime, timedelta
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import daily_news_guard as g

DAY = "2026-09-12"
NOW = datetime.fromisoformat(DAY + "T08:01:29+08:00")
PROMPT = '<heartbeat><automation_id>ai</automation_id><instructions>Produce news</instructions></heartbeat>'


class GuardTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        for key, value in [("ROOT", self.root), ("PRIVATE", self.root / "private"), ("now", lambda: NOW)]:
            p = patch.object(g, key, value)
            p.start(); self.addCleanup(p.stop)
        g.PRIVATE.mkdir()
        self.production = {"date": DAY, "cutoff": NOW.isoformat(), "stage": "research_pending"}
        g.write_json(g.PRIVATE / f"production-{DAY}.json", self.production)

    def event(self, kind, **kwargs):
        return {"session_id": g.SESSION, "cwd": str(g.ROOT), "turn_id": "turn1",
                "hook_event_name": kind, **kwargs}

    def arm(self):
        return g.handle(self.event("UserPromptSubmit", prompt=PROMPT))

    def state(self):
        return g.read_json(g.PRIVATE / f"guard-{DAY}.json")

    def stop(self, **kwargs):
        return g.handle(self.event("Stop", **kwargs))

    def advance(self, turn):
        return g.handle(self.event("UserPromptSubmit", turn_id=turn, prompt=self.state()["last_reason"]))

    def test_today_regression_wrong_final_cannot_finish(self):
        self.arm()
        result = self.stop(last_assistant_message="LINE 錯誤通知已加入，32項測試通過")
        self.assertEqual(result["decision"], "block")
        self.assertIn("research_pending", result["reason"])
        self.assertIn(NOW.isoformat(), result["reason"])

    def test_september14_cli_answer_is_blocked_without_turn_extension(self):
        self.arm()
        event = self.event('Stop', last_assistant_message='Codex 的兩種操作介面')
        event.pop('turn_id')
        self.assertEqual(g.handle(event)['decision'], 'block')
        g.handle(event)
        self.assertNotIn('decision', g.handle(event))
        self.assertEqual(self.state()['status'], 'exhausted')

    def test_same_turn_stop_hook_continuations_are_bounded(self):
        self.arm()
        self.stop()
        self.stop(stop_hook_active=True)
        self.assertNotIn('decision', self.stop(stop_hook_active=True))
        self.assertEqual(self.state()['status'], 'exhausted')

    def test_pause_still_wins_when_stop_has_no_turn_id(self):
        self.arm()
        g.handle(self.event('UserPromptSubmit', prompt='先停下'))
        self.assertEqual(self.stop(turn_id=''), {})

    def test_audit_does_not_store_message_content(self):
        self.arm(); self.stop(last_assistant_message='PRIVATE TEXT')
        text = (g.PRIVATE / f'guard-events-{DAY}.json').read_text()
        self.assertNotIn('PRIVATE TEXT', text)
        self.assertIn('Stop', text)

    def test_compaction_restores_active_task(self):
        self.arm()
        result = g.handle(self.event("SessionStart", source="compact"))
        self.assertIn("當前仍是", result["hookSpecificOutput"]["additionalContext"])
        self.assertEqual(self.state()["count"], 0)

    def test_other_thread_never_arms(self):
        self.assertEqual(g.handle(self.event("UserPromptSubmit", prompt=PROMPT, session_id="other")), {})
        self.assertEqual(self.state(), {})

    def test_other_project_never_arms(self):
        self.assertEqual(g.handle(self.event("UserPromptSubmit", prompt=PROMPT, cwd="/tmp")), {})

    def test_ordinary_chat_does_not_arm_even_with_pending_checkpoint(self):
        self.assertEqual(g.handle(self.event("UserPromptSubmit", prompt="為何今天沒收到？")), {})
        self.assertEqual(self.stop(), {})

    def test_quoted_or_other_heartbeat_not_accepted(self):
        for text in ["Explain " + PROMPT, PROMPT.replace("ai<", "other<"), "<heartbeat>bad"]:
            self.assertFalse(g.heartbeat(text))

    def test_new_user_instruction_disarms_even_unknown_language(self):
        self.arm()
        g.handle(self.event("UserPromptSubmit", prompt="先停下，改分析別的事", turn_id="new"))
        self.assertEqual(self.state()["status"], "paused")
        self.assertEqual(self.stop(turn_id="new"), {})

    def test_interrupt_does_not_restart(self):
        self.arm()
        g.handle(self.event("Interrupt"))
        self.assertEqual(self.state()["cause"], "user_interrupt")
        self.assertEqual(self.stop(), {})

    def test_explicit_resume_keeps_budget(self):
        self.arm(); self.stop()
        g.handle(self.event("Interrupt"))
        g.handle(self.event("UserPromptSubmit", prompt="繼續今日新聞產製", turn_id="new"))
        self.assertEqual(self.state()["status"], "active")
        self.assertEqual(self.state()["count"], 1)

    def test_duplicate_stop_is_idempotent(self):
        self.arm()
        first = self.stop()
        for _ in range(5):
            self.assertEqual(self.stop(), first)
        self.assertEqual(self.state()["count"], 1)
        self.assertEqual(self.state()["unchanged"], 0)

    def test_generated_continuation_binds_new_turn(self):
        self.arm(); self.stop(); self.advance("turn2")
        self.assertEqual(self.state()["turn_id"], "turn2")
        self.assertEqual(self.state()["count"], 1)
        self.assertEqual(self.stop(turn_id="turn2")["decision"], "block")

    def test_stale_turn_does_not_block_new_chat(self):
        self.arm()
        self.assertEqual(self.stop(turn_id="other"), {})

    def test_unchanged_repeated_work_exhausts(self):
        self.arm(); self.stop(); self.advance("turn2"); self.stop(turn_id="turn2")
        self.advance("turn3")
        self.assertNotIn("decision", self.stop(turn_id="turn3"))
        self.assertEqual(self.state()["status"], "exhausted")

    def test_count_limit_even_when_notes_change(self):
        self.arm()
        g.folder(DAY).mkdir(parents=True)
        for n in range(4):
            if n:
                self.advance(str(n))
            (g.folder(DAY) / f"source-notes-{DAY}.md").write_text(str(n))
            result = self.stop(turn_id=str(n) if n else "turn1")
        self.assertNotIn("decision", result)
        self.assertEqual(self.state()["count"], 3)

    def test_timeout_and_begin_cannot_reset_budget(self):
        self.arm()
        with patch.object(g, "now", return_value=NOW + timedelta(minutes=91)):
            self.assertNotIn("decision", self.stop())
            g.handle(self.event("PipelineBegin"))
        self.assertEqual(self.state()["status"], "exhausted")

    def test_cross_day_has_no_automatic_old_resume(self):
        self.arm()
        with patch.object(g, "now", return_value=NOW + timedelta(days=1)):
            self.assertEqual(self.stop(), {})

    def test_complete_receipt_allows_stop(self):
        self.arm()
        with patch.object(g, "complete", return_value=True):
            self.assertEqual(self.stop(), {})
        self.assertEqual(self.state()["status"], "complete")

    def test_complete_day_heartbeat_does_not_rearm(self):
        with patch.object(g, "complete", return_value=True):
            self.arm()
        self.assertEqual(self.state(), {})

    def test_missing_or_false_complete_is_not_success(self):
        self.assertFalse(g.complete({}))
        self.assertFalse(g.complete(dict(self.production, stage="complete")))

    def test_pipeline_fallback_requires_exact_session(self):
        with patch.dict("os.environ", {"CODEX_THREAD_ID": "other"}):
            g.arm_from_pipeline()
        self.assertEqual(self.state(), {})
        with patch.dict("os.environ", {"CODEX_THREAD_ID": g.SESSION}):
            g.arm_from_pipeline()
        self.assertEqual(self.stop()["decision"], "block")

    def test_no_prompt_or_last_answer_saved(self):
        self.arm(); self.stop(last_assistant_message="PRIVATE CHAT CONTENT")
        text = (g.PRIVATE / f"guard-{DAY}.json").read_text()
        self.assertNotIn("PRIVATE CHAT CONTENT", text)
        self.assertNotIn("Produce news", text)

    def test_delayed_continuation_does_not_override_interrupt(self):
        self.arm(); self.stop()
        reason = self.state()["last_reason"]
        g.handle(self.event("Interrupt"))
        g.handle(self.event("UserPromptSubmit", prompt=reason, turn_id="late"))
        self.assertEqual(self.state()["status"], "paused")

    def test_receipt_hashes_detect_changed_local_entry(self):
        relative = f"wiki/daily/2026/09/{DAY}/slides-{DAY}.html"
        files = [relative, "wiki/daily/latest-slides.html", "index.html"]
        for name in files:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("validated fixture")
        stamp = NOW.strftime("%Y-%m-%d %H:%M:%S")
        for prefix in ["daily-news", "source-notes"]:
            (g.folder(DAY) / f"{prefix}-{DAY}.md").write_text(stamp)
        state = dict(self.production, stage="complete", version="test", line_result="Sent LINE message",
                     public_url=f"https://lucaskk.github.io/daily-news/{relative}?v=test",
                     verified_hashes={name: hashlib.sha256((self.root / name).read_bytes()).hexdigest() for name in files})
        with patch("line_watchdog_source.sent_date", return_value=DAY), \
             patch("line_watchdog_source.validate_deck"), \
             patch("render_daily_slides.parse_report", return_value={"date": DAY, "cutoff": stamp}):
            self.assertTrue(g.complete(state))
            (self.root / "index.html").write_text("changed after verification")
            self.assertFalse(g.complete(state))


if __name__ == "__main__":
    unittest.main()
