"""Private watchdog tests. All HTTP and LINE calls are mocked; no real delivery."""
import fcntl
import importlib.util
import json
import os
import sqlite3
from pathlib import Path
import tempfile
import unittest
from datetime import datetime, timedelta
from unittest.mock import patch
from urllib.error import HTTPError, URLError

MODULE = Path(os.environ.get('LINE_WATCHDOG_MODULE_PATH',
                            str(Path(__file__).resolve().parents[1] / 'scripts/line_watchdog_source.py')))
spec = importlib.util.spec_from_file_location('watchdog', MODULE)
w = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w)
NOW = datetime(2026, 9, 9, 10, 15, tzinfo=w.TAIPEI)
BASE = 'https://example.com/daily-news'
DAY = '2026-09-09'
URL = f'{BASE}/wiki/daily/2026/09/{DAY}/slides-{DAY}.html?v=test'


def latest(day=DAY, external=False):
    url = f'2026/09/{day}/slides-{day}.html?v=test'
    if external:
        url = 'https://untrusted.example/slides-2026-09-09.html'
    return f'<meta http-equiv="refresh" content="0; url={url}">'.encode()


def deck(day=DAY, count=10):
    stories = [{'rank': str(i), 'category': 'world', 'sources': [{'label': 'Source', 'url': BASE}]}
               for i in range(1, count + 1)]
    articles = ''.join(f'<article data-rank="{s["rank"]}"></article>' for s in stories)
    report = json.dumps({'date': day, 'stories': stories})
    return (articles + f'<script id="report-data" type="application/json">{report}</script>').encode()


class WatchdogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        changes = {'ROOT': self.root, 'STATE_PATH': self.root/'line-sent-key',
                   'ALERT_STATE_PATH': self.root/'line-missing-alert-key',
                   'HISTORY_DB': self.root/'history.sqlite'}
        for name, value in changes.items():
            p = patch.object(w, name, value); p.start(); self.addCleanup(p.stop)
        p = patch.object(w, 'load_env', return_value={'PUBLIC_SLIDES_BASE_URL': BASE,
                         'LINE_CHANNEL_ACCESS_TOKEN': 'fake-token', 'LINE_TO_ID': 'fake-recipient'})
        p.start(); self.addCleanup(p.stop)
        for name in ['log']:
            p = patch.object(w, name); p.start(); self.addCleanup(p.stop)
        p = patch.object(w.time, 'sleep'); p.start(); self.addCleanup(p.stop)
        p = patch.object(w, 'fetch', side_effect=AssertionError('Unexpected HTTP call'))
        self.fetch = p.start(); self.addCleanup(p.stop)
        p = patch.dict(os.environ, {'FORCE_LINE_PUSH': '0', 'LINE_WATCHDOG_QUIET': '0'})
        p.start(); self.addCleanup(p.stop)

    def status(self):
        return json.loads((self.root/'line-watchdog-status.json').read_text())

    def test_success_and_daily_dedup(self):
        self.fetch.side_effect = [latest(), deck(), b'{}']
        self.assertEqual(w.run_once(NOW), 0)
        self.assertEqual(w.STATE_PATH.read_text().strip(), DAY)
        self.assertEqual(self.status()['status'], 'sent')
        self.assertEqual(w.run_once(NOW), 0)
        self.assertEqual(self.fetch.call_count, 3)
        self.assertEqual(self.status()['status'], 'already_sent')
        pending = self.root/f'line-request-news-{DAY}.json'
        self.assertEqual(pending.stat().st_mode & 0o777, 0o600)
        self.assertNotIn('fake-token', pending.read_text())
        self.assertNotIn('fake-recipient', pending.read_text())

    def test_missing_before_deadline_waits_without_sending(self):
        self.fetch.return_value = latest('2026-09-08'); self.fetch.side_effect = None
        self.assertEqual(w.run_once(NOW.replace(hour=8)), 0)
        self.assertEqual(self.status()['status'], 'waiting_for_publish')
        self.assertFalse(w.STATE_PATH.exists())
        self.assertEqual(self.fetch.call_count, 1)

    def test_missing_alert_is_not_delivery_and_can_recover(self):
        self.fetch.side_effect = [latest('2026-09-08'), b'{}', latest('2026-09-08'), latest(), deck(), b'{}']
        self.assertEqual(w.run_once(NOW), 1)
        self.assertTrue(w.ALERT_STATE_PATH.exists())
        self.assertFalse(w.STATE_PATH.exists())
        self.assertEqual(w.run_once(NOW), 1)
        self.assertEqual(self.fetch.call_count, 3)
        self.assertEqual(w.run_once(NOW), 0)
        self.assertTrue(w.STATE_PATH.exists())
        posts = [c for c in self.fetch.call_args_list if c.kwargs.get('method') == 'POST']
        self.assertEqual(len(posts), 2)
        self.assertNotEqual(posts[0].kwargs['headers']['X-Line-Retry-Key'], posts[1].kwargs['headers']['X-Line-Retry-Key'])

    def test_public_network_failure_alerts(self):
        self.fetch.side_effect = [URLError('offline'), b'{}']
        self.assertEqual(w.run_once(NOW), 1)
        self.assertEqual(self.status()['status'], 'publish_unavailable')
        self.assertFalse(w.STATE_PATH.exists())

    def test_incomplete_deck_never_sends_news(self):
        self.fetch.side_effect = [latest(), deck(count=9), b'{}']
        self.assertEqual(w.run_once(NOW), 1)
        self.assertFalse(w.STATE_PATH.exists())

    def test_wrong_embedded_date_never_sends_news(self):
        self.fetch.side_effect = [latest(), deck(day='2026-09-08'), b'{}']
        self.assertEqual(w.run_once(NOW), 1)
        self.assertFalse(w.STATE_PATH.exists())

    def test_external_redirect_never_fetched(self):
        self.fetch.side_effect = [latest(external=True), b'{}']
        self.assertEqual(w.run_once(NOW), 1)
        self.assertEqual(self.fetch.call_count, 2)
        self.assertFalse(any('untrusted.example' in c.args[0] for c in self.fetch.call_args_list))

    def test_malformed_report_and_missing_html_are_rejected(self):
        bad = [b'<script id="report-data">[]</script>',
               deck().replace(b'<article data-rank="1"></article>', b''),
               deck().replace(b'"label": "Source"', b'"label": ""'),
               deck().replace(BASE.encode(), b'javascript:alert(1)')]
        for html in bad:
            self.fetch.side_effect = [latest(), html]
            with self.assertRaises(ValueError):
                w.public_deck(BASE, BASE+'/wiki/daily/latest-slides.html', DAY)

    def test_timeout_retries_identical_key_and_payload(self):
        self.fetch.side_effect = [TimeoutError(), URLError('offline'), b'{}']
        self.assertTrue(w.push_text('token', 'user', 'text', 'key'))
        calls = self.fetch.call_args_list
        self.assertEqual(len(calls), 3)
        self.assertTrue(all(c.kwargs == calls[0].kwargs for c in calls))

    def test_500_then_confirmed_409_is_success(self):
        self.fetch.side_effect = [HTTPError(URL, 500, 'error', {}, None),
                                 HTTPError(URL, 409, 'accepted', {'x-line-accepted-request-id': 'id'}, None)]
        self.assertTrue(w.push_text('token', 'user', 'text', 'key'))

    def test_400_is_not_retried_and_generic_409_is_not_success(self):
        for code in [400, 409, 429]:
            self.fetch.reset_mock()
            self.fetch.side_effect = HTTPError(URL, code, 'error', {}, None)
            self.assertFalse(w.push_text('token', 'user', 'text', 'key'))
            self.assertEqual(self.fetch.call_count, 1)

    def test_pending_request_preserves_original_text_and_key(self):
        with patch.object(w, 'push_text', side_effect=[False, True]) as send:
            self.assertFalse(w.send_once('token', 'user', 'original', 'news', NOW, w.STATE_PATH))
            self.assertTrue(w.send_once('token', 'user', 'changed', 'news', NOW, w.STATE_PATH))
            self.assertEqual(send.call_args_list[0], send.call_args_list[1])

    def test_state_write_failure_can_reconcile_without_new_key(self):
        original_write = w.write_atomic
        def broken_write(path, text):
            if path == w.STATE_PATH: raise OSError('disk error')
            return original_write(path, text)
        with patch.object(w, 'push_text', return_value=True) as send:
            with patch.object(w, 'write_atomic', side_effect=broken_write):
                with self.assertRaises(OSError):
                    w.send_once('token', 'user', 'original', 'news', NOW, w.STATE_PATH)
            self.assertTrue(w.send_once('token', 'user', 'changed', 'news', NOW, w.STATE_PATH))
            self.assertEqual(send.call_args_list[0], send.call_args_list[1])

    def test_expired_request_and_changed_recipient_fail_closed(self):
        with patch.object(w, 'push_text', return_value=False) as send:
            w.send_once('token', 'user', 'text', 'news', NOW, w.STATE_PATH)
            path = self.root/f'line-request-news-{DAY}.json'
            request = json.loads(path.read_text())
            request['created_at'] = (NOW - timedelta(hours=24)).isoformat()
            path.write_text(json.dumps(request))
            with self.assertRaises(ValueError): w.send_once('token', 'user', 'text', 'news', NOW, w.STATE_PATH)
            request['created_at'] = NOW.isoformat(); path.write_text(json.dumps(request))
            with self.assertRaises(ValueError): w.send_once('token', 'other', 'text', 'news', NOW, w.STATE_PATH)
            self.assertEqual(send.call_count, 1)

    def test_concurrent_run_does_not_execute(self):
        with (self.root/'line-watchdog.lock').open('a+') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            with patch.object(w, 'run_once') as run:
                self.assertEqual(w.main(), 0)
                run.assert_not_called()

    def test_forced_duplicate_disabled(self):
        with patch.dict(os.environ, {'FORCE_LINE_PUSH': '1'}):
            with self.assertRaises(ValueError): w.run_once(NOW)
        self.fetch.assert_not_called()

    def test_exhausted_delivery_retries_remain_pending(self):
        self.fetch.side_effect = [latest(), deck(), TimeoutError(), TimeoutError(), TimeoutError()]
        self.assertEqual(w.run_once(NOW), 1)
        self.assertEqual(self.status()['status'], 'delivery_failed')
        self.assertFalse(w.STATE_PATH.exists())
        self.assertTrue((self.root/f'line-request-news-{DAY}.json').exists())

    def test_failed_alert_does_not_mark_either_message_sent(self):
        self.fetch.side_effect = [latest('2026-09-08'), HTTPError(URL, 401, 'unauthorized', {}, None)]
        self.assertEqual(w.run_once(NOW), 1)
        self.assertFalse(self.status()['alert_accepted'])
        self.assertFalse(w.ALERT_STATE_PATH.exists())
        self.assertFalse(w.STATE_PATH.exists())

    def test_next_day_is_not_blocked_by_previous_delivery(self):
        w.STATE_PATH.write_text(DAY + '\n')
        self.fetch.side_effect = [latest('2026-09-10'), deck(day='2026-09-10'), b'{}']
        self.assertEqual(w.run_once(NOW + timedelta(days=1)), 0)
        self.assertEqual(w.STATE_PATH.read_text().strip(), '2026-09-10')

    def add_execution(self, status='failed', info='usageLimitExceeded', message='private-token must never be sent',
                      started=None, completed=None, thread=None):
        with sqlite3.connect(w.HISTORY_DB) as db:
            db.execute('CREATE TABLE IF NOT EXISTS thread_turns (thread_id TEXT, status TEXT, error_json TEXT, '
                       'started_at INTEGER, completed_at INTEGER, rollout_ordinal INTEGER)')
            start = int((started or NOW - timedelta(minutes=5)).timestamp())
            end = int((completed or NOW - timedelta(minutes=4)).timestamp())
            error = json.dumps({'message': message, 'codexErrorInfo': info}) if status == 'failed' else None
            db.execute('INSERT INTO thread_turns VALUES (?,?,?,?,?,?)',
                       (thread or w.NEWS_THREAD_ID, status, error, start, end, start))

    def write_production(self, stage='research_pending', **extra):
        value = {'date': DAY, 'stage': stage, 'checked_at': (NOW - timedelta(hours=2)).isoformat(), **extra}
        (self.root/f'production-{DAY}.json').write_text(json.dumps(value))

    def test_usage_limit_alert_uses_system_code_without_leaking_error(self):
        self.add_execution()
        self.write_production()
        self.fetch.side_effect = [latest('2026-09-08'), b'{}']
        self.assertEqual(w.run_once(NOW), 1)
        post = self.fetch.call_args_list[-1]
        text = json.loads(post.kwargs['data'])['messages'][0]['text']
        self.assertIn('模型使用額度已達上限', text)
        self.assertIn('恢復時間', text)
        self.assertIn('10:11:00', text)
        self.assertNotIn('private-token', text)
        self.assertEqual(self.status()['diagnosis']['code'], 'model_quota')

    def test_previous_day_other_thread_and_future_errors_ignored(self):
        self.add_execution(started=NOW-timedelta(days=1), completed=NOW-timedelta(days=1))
        self.add_execution(thread='another-thread')
        self.add_execution(started=NOW+timedelta(hours=1), completed=NOW+timedelta(hours=1))
        self.assertEqual(w.latest_execution(NOW), {})
        self.assertEqual(w.alert_diagnosis(NOW, ValueError('stale'))['code'], 'unknown')

    def test_newer_execution_supersedes_old_quota_error(self):
        self.add_execution()
        self.add_execution(status='completed', started=NOW-timedelta(minutes=2), completed=NOW-timedelta(minutes=1))
        diagnosis = w.alert_diagnosis(NOW, ValueError('stale'))
        self.assertEqual(diagnosis['code'], 'production_incomplete')
        self.assertNotIn('額度已達', diagnosis['reason'])

    def test_newer_checkpoint_supersedes_old_quota_error(self):
        self.add_execution()
        self.write_production(stage='publishing', checked_at=(NOW-timedelta(minutes=1)).isoformat(), last_error='git push exited 128')
        self.assertEqual(w.alert_diagnosis(NOW, ValueError('stale'))['code'], 'git_publish_failed')

    def test_legacy_usage_error_message_is_classified_but_not_forwarded(self):
        self.add_execution(info=None, message="You've hit your usage limit. private-token try again at 1:01 PM")
        text, diagnostic = w.missing_alert(NOW, ValueError('stale'))
        self.assertEqual(diagnostic['code'], 'model_quota')
        self.assertNotIn('private-token', text)
        self.assertNotIn('1:01 PM', text)

    def test_rate_limit_is_not_mislabeled_as_quota(self):
        self.add_execution(info='rateLimitExceeded')
        diagnostic = w.alert_diagnosis(NOW, ValueError('stale'))
        self.assertEqual(diagnostic['code'], 'model_rate_limit')

    def test_unknown_model_error_does_not_forward_sensitive_text(self):
        self.add_execution(info='unknown')
        text, diagnostic = w.missing_alert(NOW, ValueError('private-url'))
        self.assertEqual(diagnostic['code'], 'model_execution_failed')
        self.assertNotIn('private-token', text)
        self.assertNotIn('private-url', text)

    def test_schema_change_or_corrupt_database_falls_back_to_unknown(self):
        w.HISTORY_DB.write_bytes(b'not a database')
        self.assertEqual(w.alert_diagnosis(NOW, ValueError('stale'))['code'], 'unknown')

    def test_malformed_checkpoint_is_ignored(self):
        for value in ['[1]', '{', '{"checked_at":"bad"}', '{"stage":{},"date":"2026-09-09"}']:
            (self.root/f'production-{DAY}.json').write_text(value)
            self.assertEqual(w.production_state(NOW), {})

    def test_pipeline_error_shows_safe_stage_only(self):
        for stage, code in [('publishing', 'git_publish_failed'), ('verifying_pages', 'pages_verification_failed'),
                            ('pages_verified', 'line_delivery_failed'), ('research_pending', 'production_failed')]:
            self.write_production(stage=stage, last_error='secret-path secret-token')
            text, diagnostic = w.missing_alert(NOW, ValueError('stale'))
            self.assertEqual(diagnostic['code'], code)
            self.assertNotIn('secret-', text)

    def test_missing_history_does_not_blame_quota_for_http_error(self):
        diagnostic = w.alert_diagnosis(NOW, HTTPError('secret-url', 503, 'error', {}, None))
        self.assertEqual(diagnostic['code'], 'public_connection_failed')
        self.assertIn('HTTP 503', diagnostic['reason'])
        self.assertNotIn('secret-url', json.dumps(diagnostic))

    def test_running_task_is_not_declared_failed(self):
        self.add_execution(status='inProgress')
        self.assertEqual(w.alert_diagnosis(NOW, ValueError('stale'))['code'], 'in_progress')

    def test_diagnosis_failure_does_not_read_or_modify_other_history(self):
        self.add_execution()
        before = w.HISTORY_DB.read_bytes()
        w.latest_execution(NOW)
        self.assertEqual(w.HISTORY_DB.read_bytes(), before)


if __name__ == '__main__':
    unittest.main()
