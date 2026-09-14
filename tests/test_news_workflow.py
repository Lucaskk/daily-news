"""Research mode switching never calls a model, publishes, or sends messages."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import news_workflow as w


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(); self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        for name, value in [('ROOT', self.root), ('PRIVATE', self.root/'private')]:
            p = patch.object(w, name, value); p.start(); self.addCleanup(p.stop)
        self.daily = self.root/'wiki/daily'; self.daily.mkdir(parents=True)

    def test_default_legacy_and_switch_back_leaves_artifacts_unchanged(self):
        report = self.daily/'daily-news-2026-09-14.md'; report.write_text('existing news')
        self.assertEqual(w.profile(), 'legacy')
        w.set_profile('python'); self.assertEqual(w.profile(), 'python')
        w.set_profile('legacy'); self.assertEqual(w.profile(), 'legacy')
        self.assertEqual(report.read_text(), 'existing news')
        self.assertFalse((w.PRIVATE/'line-sent-key').exists())

    def test_bad_mode_rejected_and_corrupt_config_falls_back(self):
        with self.assertRaises(ValueError): w.set_profile('untrusted')
        w.set_profile('python'); (w.PRIVATE/'research-mode.json').write_text('broken')
        self.assertEqual(w.profile(), 'legacy')

    def test_lookup_only_history_hits_no_recent_read(self):
        (self.daily/'product-news-ledger.md').write_text('Company Product update-key\n')
        (self.daily/'source-notes-2026-09-13.md').write_text('update-key already captured\n')
        (self.daily/'unrelated.md').write_text('update-key\n')
        w.set_profile('python')
        result = w.lookup('update-key')
        self.assertTrue(result['historical_match'])
        self.assertFalse(result['recent_fallback'])
        self.assertNotIn('unrelated.md', result['result'])

    def test_no_hit_recent_fallback_only_python(self):
        (self.daily/'product-news-ledger.md').write_text('old')
        (self.daily/'product-news-recent-7d.md').write_text('recent table')
        self.assertEqual(w.lookup('missing')['result'], '')
        w.set_profile('python')
        self.assertEqual(w.lookup('missing')['result'], 'recent table')

    def test_failed_search_never_claims_no_hits(self):
        with patch.object(w.subprocess, 'run', return_value=subprocess.CompletedProcess([], 2, '', 'bad')):
            with self.assertRaises(ValueError): w.lookup('[')

    def test_truncation_retains_evidence(self):
        output = 'match\n' * 4000
        with patch.object(w.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, output, '')):
            result = w.lookup('match')
        self.assertTrue(result['truncated'])
        self.assertEqual(Path(result['full_result_path']).read_text(), output)

    def test_python_cache_and_legacy_bypass(self):
        w.set_profile('python')
        payload = (b'<p>Facts</p><script>secret script</script>', 'https://example.com/final', 'utf-8', 'text/html')
        with patch.object(w, 'download', return_value=payload) as download:
            first = w.fetch_source('https://example.com/news')
            second = w.fetch_source('https://example.com/news')
            self.assertFalse(first['cache_hit']); self.assertTrue(second['cache_hit'])
            self.assertNotIn('secret script', first['content'])
            self.assertEqual(download.call_count, 1)
            w.fetch_source('https://example.com/news', refresh=True)
            self.assertEqual(download.call_count, 2)
            w.set_profile('legacy'); w.fetch_source('https://example.com/news')
            self.assertEqual(download.call_count, 3)

    def test_expired_cache_refreshes(self):
        w.set_profile('python')
        with patch.object(w, 'download', return_value=(b'facts', 'https://example.com', 'utf-8', 'text/plain')) as download:
            first = w.fetch_source('https://example.com')
            path = Path(first['evidence_path']); data = json.loads(path.read_text())
            data['retrieved_at'] = '2020-01-01T00:00:00+00:00'; path.write_text(json.dumps(data))
            self.assertFalse(w.fetch_source('https://example.com')['cache_hit'])
            self.assertEqual(download.call_count, 2)

    def test_unsafe_scheme_and_embedded_credentials_rejected(self):
        for url in ['file:///etc/passwd', 'http://example.com', 'https://user:password@example.com']:
            with self.assertRaises(ValueError): w.fetch_source(url)


if __name__ == '__main__': unittest.main()
