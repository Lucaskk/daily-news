"""No live GitHub writes or LINE calls in these recovery tests."""
from datetime import datetime
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import daily_news_pipeline as p

DAY = "2026-09-11"
CUTOFF = "2026-09-11T08:00:53+08:00"


class PipelineTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        for name, value in [("ROOT", self.root), ("PRIVATE", self.root),
                            ("now", lambda: datetime.fromisoformat(CUTOFF))]:
            mock = patch.object(p, name, value)
            mock.start()
            self.addCleanup(mock.stop)
        mock = patch.object(p.time, "sleep")
        mock.start()
        self.addCleanup(mock.stop)
        self.state = p.begin(DAY, CUTOFF)

    def test_begin_freezes_cutoff_and_resume_keeps_stage(self):
        p.save(self.state, "verifying_pages")
        self.assertEqual(p.begin(DAY)["stage"], "verifying_pages")
        self.assertEqual(p.begin(DAY)["cutoff"], CUTOFF)
        with self.assertRaises(ValueError):
            p.begin(DAY, "2026-09-11T09:00:00+08:00")

    def test_timezone_and_date_required(self):
        with self.assertRaises(ValueError):
            p.begin("2026-09-12", "2026-09-12T08:00:00")
        with self.assertRaises(ValueError):
            p.begin("2026-09-12", CUTOFF)

    def test_missing_research_never_publishes(self):
        with patch.object(p, "publish") as publish, self.assertRaises(ValueError):
            p.finish(self.state)
        publish.assert_not_called()

    def test_old_day_rejected(self):
        state = dict(self.state, date="2026-09-10")
        with self.assertRaises(ValueError):
            p.finish(state)

    def test_resume_pages_does_not_render_or_push(self):
        self.state["stage"] = "verifying_pages"
        with patch.object(p, "prepare") as prepare, patch.object(p, "publish") as publish, \
                patch.object(p, "verify_public") as verify, patch.object(p, "deliver") as deliver:
            p.finish(self.state)
        prepare.assert_not_called()
        publish.assert_not_called()
        verify.assert_called_once()
        deliver.assert_called_once()

    def test_verify_failure_never_calls_line(self):
        self.state["stage"] = "verifying_pages"
        with patch.object(p, "verify_public", side_effect=ValueError("stale")), \
                patch.object(p, "deliver") as deliver, self.assertRaises(ValueError):
            p.finish(self.state)
        deliver.assert_not_called()

    def test_line_requires_pages_gate(self):
        with patch.object(p, "command") as run, self.assertRaises(ValueError):
            p.deliver(self.state)
        run.assert_not_called()

    def test_alert_or_silent_exit_is_not_success(self):
        self.state["stage"] = "pages_verified"
        with patch.object(p, "command", return_value="Sent LINE missing-publish alert") as run, self.assertRaises(RuntimeError):
            p.deliver(self.state)
        self.assertEqual(run.call_count, 3)
        self.assertNotEqual(self.state["stage"], "complete")

    def test_watchdog_retry_uses_only_installed_path(self):
        self.state["stage"] = "pages_verified"
        (self.root / "line-sent-key").write_text(DAY)
        with patch.object(p, "command", side_effect=[RuntimeError("transient"), "LINE already sent"]) as run:
            p.deliver(self.state)
        self.assertEqual(self.state["stage"], "complete")
        self.assertTrue(all(call.args[0][-1] == str(self.root / "line_watchdog.py") for call in run.call_args_list))

    def test_wrong_date_delivery_rejected(self):
        self.state["stage"] = "pages_verified"
        (self.root / "line-sent-key").write_text("2026-09-10")
        with patch.object(p, "command", return_value="Sent LINE message"), self.assertRaises(RuntimeError):
            p.deliver(self.state)

    def test_completed_run_does_not_send_again(self):
        self.state["stage"] = "complete"
        (self.root / "line-sent-key").write_text(DAY)
        with patch.object(p, "deliver") as deliver:
            p.finish(self.state)
        deliver.assert_not_called()

    def test_atomic_checkpoint_is_readable(self):
        p.save(self.state, "publishing", commit="test")
        self.assertEqual(json.loads(p.state_path(DAY).read_text())["commit"], "test")

    def test_recovered_state_clears_previous_error(self):
        p.save(self.state, "verifying_pages", last_error="temporary")
        p.save(self.state, "pages_verified")
        self.assertNotIn("last_error", json.loads(p.state_path(DAY).read_text()))

    def test_pages_retry_then_exact_content_match(self):
        relative = f"wiki/daily/2026/09/{DAY}/slides-{DAY}.html"
        for name in [relative, "wiki/daily/latest-slides.html", "index.html"]:
            file = self.root / name
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_bytes(b"expected")
        with patch.object(p.watchdog, "public_deck", side_effect=[OSError("deploying"), (p.BASE + "/" + relative, DAY)]) as verify, \
                patch.object(p.watchdog, "fetch", return_value=b"expected"):
            p.verify_public(self.state, attempts=2)
        self.assertEqual(verify.call_count, 2)
        self.assertEqual(self.state["stage"], "pages_verified")

    def test_public_old_content_never_passes_gate(self):
        relative = f"wiki/daily/2026/09/{DAY}/slides-{DAY}.html"
        file = self.root / relative
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_bytes(b"expected")
        with patch.object(p.watchdog, "public_deck", return_value=(p.BASE + "/" + relative, DAY)), \
                patch.object(p.watchdog, "fetch", return_value=b"stale"), self.assertRaises(ValueError):
            p.verify_public(self.state, attempts=2)
        self.assertNotEqual(self.state["stage"], "pages_verified")


if __name__ == "__main__":
    unittest.main()
