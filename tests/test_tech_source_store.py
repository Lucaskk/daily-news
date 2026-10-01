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


if __name__ == '__main__':
    unittest.main()
