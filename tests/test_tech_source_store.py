"""CSV source edits are readable by the research helper."""
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import tech_source_store as store
import news_workflow as workflow


class SourceStoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'sources.csv'
        store.write_sources([], self.path)

    def test_add_deduplicates_and_records_metadata(self):
        self.assertTrue(store.add_source('https://example.com/news#fragment', website='Example',
                                         origin='line', path=self.path))
        self.assertFalse(store.add_source('https://example.com/news', path=self.path))
        row, = store.read_sources(self.path)
        self.assertEqual(row['website'], 'Example')
        self.assertEqual(row['origin'], 'line')
        self.assertEqual(row['url'], 'https://example.com/news')
        self.assertIn('+08:00', row['added_at'])

    def test_disabled_row_is_not_used_for_research(self):
        store.add_source('https://example.com/', path=self.path)
        with patch.object(store, 'CSV_PATH', self.path), patch.object(workflow, 'read_sources',
                                                                     lambda: store.read_sources(self.path)):
            self.assertEqual(workflow.discovery_sources(), [('example.com', 'https://example.com/')])
        rows = store.read_sources(self.path); rows[0]['enabled'] = 'false'
        store.write_sources(rows, self.path)
        with patch.object(workflow, 'read_sources', lambda: store.read_sources(self.path)):
            self.assertEqual(workflow.discovery_sources(), [])

    def test_rejects_bad_urls(self):
        for url in ('http://example.com', 'https://user:pass@example.com', 'not-a-url'):
            with self.assertRaises(ValueError): store.add_source(url, path=self.path)

    def test_local_symlink_edits_preserve_background_csv(self):
        link = self.path.parent / 'local.csv'
        link.symlink_to(self.path)
        store.add_source('https://example.com/', path=link)
        self.assertTrue(link.is_symlink())
        self.assertEqual(store.read_sources(self.path)[0]['url'], 'https://example.com/')


if __name__ == '__main__':
    unittest.main()

class SourceListingTests(unittest.TestCase):
    def test_all_fields_and_disabled_sources_are_included(self):
        row = dict(zip(store.FIELDS, ['https://example.com/', '', 'Example', '科技', 'false', 'local', '測試備註']))
        messages = store.source_list_messages([row], '2026-10-01T12:00:00+08:00')
        body = '\n'.join(messages)
        for label in ('網址', '加入時間', '網站名稱', '類別', '啟用狀態', '加入來源', '備註'):
            self.assertIn(label + '：', body)
        self.assertIn('停用', body)
        self.assertIn('未記錄', body)

    def test_long_unicode_messages_are_split_without_losing_content(self):
        row = dict(zip(store.FIELDS, ['https://example.com/', '', 'Example', '科技', 'true', 'local', '🚀' * 6000]))
        messages = store.source_list_messages([row], 'now')
        self.assertGreater(len(messages), 1)
        self.assertEqual(sum(message.count('🚀') for message in messages), 6000)
        self.assertTrue(all(len(message.encode('utf-16-le')) // 2 <= 5000 for message in messages))
