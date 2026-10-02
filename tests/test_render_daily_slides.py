import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("reader", ROOT / "scripts/render_daily_slides.py")
reader = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(reader)
REPORT = ROOT / "wiki/daily/2026/09/2026-09-08/daily-news-2026-09-08.md"


class ReaderTests(unittest.TestCase):
    def setUp(self):
        self.text = REPORT.read_text()
        self.report = reader.parse_report(self.text)

    def test_story_counts_and_product_first(self):
        self.assertEqual([s["rank"] for s in self.report["stories"]], ["T1", "T2", "T3"] + list(map(str, range(1, 11))))

    def test_zero_products_still_has_ten_world_stories(self):
        text = self.text[:self.text.index("### T1.")] + self.text[self.text.index("## 全球 Top 10"):]
        report = reader.parse_report(text)
        self.assertEqual(len(report["stories"]), 10)
        self.assertEqual(report["stories"][0]["rank"], "1")

    def test_new_policy_count_boundaries_and_window_label(self):
        prefix = self.text[:self.text.index("### T1.")].replace("2026-09-08", "2026-10-03")
        prefix = prefix.replace("科技／AI 產品 7 日視窗", "科技／AI 產品 14 日視窗")
        product = self.text[self.text.index("### T1."):self.text.index("### T2.")]
        world = self.text[self.text.index("## 全球 Top 10"):]
        for count in (1, 10):
            text = prefix + ''.join(product.replace('### T1.', f'### T{i}.')
                                    for i in range(1, count + 1)) + world
            report = reader.parse_report(text)
            self.assertEqual(report['tech_window_days'], 14)
        for count in (0, 11):
            text = prefix + ''.join(product.replace('### T1.', f'### T{i}.')
                                    for i in range(1, count + 1)) + world
            with self.assertRaisesRegex(ValueError, '1 to 10'):
                reader.parse_report(text)
        with self.assertRaisesRegex(ValueError, '14-day'):
            reader.parse_report((prefix + product + world).replace('14 日視窗', '7 日視窗'))
        with self.assertRaisesRegex(ValueError, 'uncaptured'):
            reader.parse_report((prefix + product + world).replace('### T1. ', '### T1. 續報｜'))

    def test_reject_missing_or_duplicate_world_rank(self):
        for text in [self.text.replace("### 10.", "### 9."), self.text.replace("### 10.", "## 10.")]:
            with self.assertRaises(ValueError):
                reader.parse_report(text)

    def test_time_precision(self):
        self.assertEqual(reader.machine_time("2026-09-03（Asia/Taipei；官方發布日期）"), "2026-09-03")
        self.assertEqual(reader.machine_time("2026-09-08 00:00:00（Asia/Taipei）"), "2026-09-07T16:00:00Z")
        with self.assertRaises(ValueError):
            reader.machine_time("2026-09-08 00:00:00")

    def test_no_unsafe_urls(self):
        for value in ["javascript:alert(1)", "//example.com", "/relative-source", "https://"]:
            with self.assertRaises(ValueError):
                reader.web_url(value)

    def test_source_links_and_query_parameters(self):
        sources = reader.sources_in("[A](https://example.com/news?a=1&b=2) [B](https://example.org/) [A](https://example.com/news?a=1&b=2)")
        self.assertEqual(len(sources), 2)
        self.assertEqual(sources[0]["url"], "https://example.com/news?a=1&b=2")

    def test_embedded_data_cannot_escape_script(self):
        data = reader.script_json({"title": "</script><script>alert(1)</script>\u2028"})
        self.assertNotIn("</script>", data)
        self.assertIn("\\u003c", data)

    def test_html_escapes_content(self):
        story = dict(self.report["stories"][0], title='<img src=x onerror="alert(1)">')
        html = reader.story_html(story, None, REPORT.parent)
        self.assertIn("&lt;img", html)
        self.assertNotIn("<img", html)

    def test_inline_report_and_per_item_sources(self):
        for story in self.report["stories"]:
            html = reader.story_html(story, None, REPORT.parent)
            self.assertIn('<details class="full-report"', html)
            self.assertIn('完整報告', html)
            self.assertIn(f'data-ask="{story["id"]}"', html)
            self.assertIn(f'data-share="{story["id"]}"', html)
            self.assertTrue(html.index('class="sources"') > html.index("尚待確認"))
            for source in story["sources"]:
                self.assertIn(reader.escape(source["url"]), html)

    def test_standalone_render(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / REPORT.name
            path.write_text(self.text)
            output, version = reader.render(path)
            html = output.read_text()
            self.assertEqual(html.count('class="story"'), 13)
            self.assertEqual(html.count('class="full-report"'), 13)
            self.assertEqual(html.count('class="share-action"'), 13)
            self.assertIn('?story=t1#t1', html)
            self.assertIn('?story=10#10', html)
            self.assertNotIn("@@", html)
            self.assertNotIn('<script src=', html)
            self.assertNotIn('<link rel="stylesheet"', html)
            self.assertIn(version, html)

    def test_local_media_paths_cannot_escape_report(self):
        with self.assertRaises(ValueError):
            reader.media_html({"src": "../daily-news.md"}, REPORT.parent)


if __name__ == "__main__":
    unittest.main()
