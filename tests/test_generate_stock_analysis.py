import importlib.util
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).parents[1] / "scripts" / "generate_stock_analysis.py"
SPEC = importlib.util.spec_from_file_location("generate_stock_analysis", MODULE_PATH)
assert SPEC and SPEC.loader
stock_analysis = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(stock_analysis)


def goodinfo_page(rows: str) -> str:
    filler = "".join("<table></table>" for _ in range(6))
    return f"<html><body>{filler}<table>{rows}</table></body></html>"


class FinancialPeriodTests(unittest.TestCase):
    def test_parse_quarterly_amount_and_percentage_columns(self) -> None:
        page = goodinfo_page(
            """
            <tr><th>本業獲利</th><th>2026Q1</th><th>2025Q1</th></tr>
            <tr><td>金額</td><td>％</td><td>金額</td><td>％</td></tr>
            <tr><td>營業收入</td><td>1,234</td><td>100</td><td>1,000</td><td>100</td></tr>
            <tr><td>營業毛利</td><td>600</td><td>48.6</td><td>450</td><td>45</td></tr>
            """
        )

        table, periods = stock_analysis.parse_goodinfo_table(page, period_kind="quarter")

        self.assertEqual(periods, ["2026Q1", "2025Q1"])
        self.assertEqual(table["營業收入"], {"2026Q1": 1234.0, "2025Q1": 1000.0})
        self.assertEqual(table["營業毛利"], {"2026Q1": 600.0, "2025Q1": 450.0})

    def test_selects_latest_quarter_shared_by_all_three_reports(self) -> None:
        latest, comparison, available = stock_analysis.select_latest_quarter(
            [
                ["2026Q2", "2026Q1", "2025Q1"],
                ["2026Q2", "2026Q1", "2025Q1"],
                ["2026Q1", "2025Q1"],
            ]
        )

        self.assertEqual(latest, "2026Q1")
        self.assertEqual(comparison, "2025Q1")
        self.assertEqual(available, ["2026Q1", "2025Q1"])

    def test_switches_to_new_quarter_only_when_same_quarter_comparison_exists(self) -> None:
        periods = ["2026Q2", "2026Q1", "2025Q2", "2025Q1"]
        latest, comparison, _ = stock_analysis.select_latest_quarter([periods, periods, periods])

        self.assertEqual(latest, "2026Q2")
        self.assertEqual(comparison, "2025Q2")

    def test_marks_missing_prior_year_quarter_without_using_previous_quarter(self) -> None:
        periods = ["2026Q2", "2026Q1"]
        latest, comparison, _ = stock_analysis.select_latest_quarter([periods, periods, periods])

        self.assertEqual(latest, "2026Q2")
        self.assertIsNone(comparison)


if __name__ == "__main__":
    unittest.main()
