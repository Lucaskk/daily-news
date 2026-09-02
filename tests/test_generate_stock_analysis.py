import importlib.util
from pathlib import Path
import unittest
from unittest import mock


MODULE_PATH = Path(__file__).parents[1] / "scripts" / "generate_stock_analysis.py"
SPEC = importlib.util.spec_from_file_location("generate_stock_analysis", MODULE_PATH)
assert SPEC and SPEC.loader
stock_analysis = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(stock_analysis)


def legacy_financial_page(rows: str) -> str:
    filler = "".join("<table></table>" for _ in range(6))
    return f"<html><body>{filler}<table>{rows}</table></body></html>"


class FinancialPeriodTests(unittest.TestCase):
    def test_parse_quarterly_amount_and_percentage_columns(self) -> None:
        page = legacy_financial_page(
            """
            <tr><th>本業獲利</th><th>2026Q1</th><th>2025Q1</th></tr>
            <tr><td>金額</td><td>％</td><td>金額</td><td>％</td></tr>
            <tr><td>營業收入</td><td>1,234</td><td>100</td><td>1,000</td><td>100</td></tr>
            <tr><td>營業毛利</td><td>600</td><td>48.6</td><td>450</td><td>45</td></tr>
            """
        )

        table, periods = stock_analysis.parse_legacy_financial_html_table(page, period_kind="quarter")

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


class FinMindConversionTests(unittest.TestCase):
    def test_finmind_date_to_quarter_period(self) -> None:
        self.assertEqual(stock_analysis.period_from_date("2026-06-30"), "2026Q2")
        self.assertEqual(stock_analysis.period_from_date("2026-12-31"), "2026Q4")

    def test_finmind_money_fields_convert_to_billion_but_eps_stays_per_share(self) -> None:
        table = stock_analysis.finmind_rows_to_table(
            "income_statement",
            [
                {"date": "2026-03-31", "type": "Revenue", "value": 120_000_000_000, "origin_name": "營業收入"},
                {"date": "2026-03-31", "type": "EPS", "value": 2.5, "origin_name": "基本每股盈餘"},
            ],
        )

        self.assertEqual(table["營業收入"]["2026Q1"], 1200.0)
        self.assertEqual(table["EPS"]["2026Q1"], 2.5)

    def test_cash_flow_cumulative_values_are_converted_to_single_quarter_values(self) -> None:
        quarterly = stock_analysis.cash_flow_quarterly_from_cumulative(
            {
                "營業活動之淨現金流入(出)": {"2026Q1": 100.0, "2026Q2": 260.0},
                "不動產、廠房及設備": {"2026Q1": -40.0, "2026Q2": -120.0},
            }
        )

        self.assertEqual(quarterly["營業活動之淨現金流入(出)"]["2026Q1"], 100.0)
        self.assertEqual(quarterly["營業活動之淨現金流入(出)"]["2026Q2"], 160.0)
        self.assertEqual(quarterly["不動產、廠房及設備"]["2026Q2"], -80.0)

    def test_annual_aggregation_sums_income_and_uses_fourth_quarter_balance_sheet(self) -> None:
        income = stock_analysis.aggregate_annual_table(
            "income_statement",
            {
                "營業收入": {"2025Q1": 100.0, "2025Q2": 110.0, "2025Q3": 120.0, "2025Q4": 130.0},
                "EPS": {"2025Q1": 1.0, "2025Q2": 1.2, "2025Q3": 1.3, "2025Q4": 1.5},
            },
        )
        balance = stock_analysis.aggregate_annual_table(
            "balance_sheet",
            {"資產總額": {"2025Q1": 900.0, "2025Q4": 1000.0}},
        )
        cash_flow = stock_analysis.aggregate_annual_table(
            "cash_flow",
            {"營業活動之淨現金流入(出)": {"2025Q4": 100.0}},
            cumulative={"營業活動之淨現金流入(出)": {"2025Q4": 460.0}},
        )

        self.assertEqual(income["營業收入"]["2025"], 460.0)
        self.assertAlmostEqual(income["EPS"]["2025"], 5.0)
        self.assertEqual(balance["資產總額"]["2025"], 1000.0)
        self.assertEqual(cash_flow["營業活動之淨現金流入(出)"]["2025"], 460.0)

    def test_official_openapi_amounts_are_thousand_twd(self) -> None:
        self.assertEqual(stock_analysis.official_amount_to_billion("2404483690.00"), 24044.8369)


class MarketDataTests(unittest.TestCase):
    def test_daily_quote_sources_fail_independently(self) -> None:
        twse_rows = [
            {
                "Code": "3037",
                "Name": "欣興",
                "Date": "20260901",
                "ClosingPrice": "971",
                "Change": "-28",
            }
        ]

        def fake_read_json(url: str, headers=None):
            if url == stock_analysis.TWSE_QUOTES_URL:
                return twse_rows
            raise stock_analysis.StockAnalysisError("TPEx temporarily unavailable")

        with mock.patch.object(stock_analysis, "read_json", side_effect=fake_read_json):
            quotes = stock_analysis.fetch_quotes()

        self.assertEqual(len(quotes), 1)
        self.assertEqual(quotes[0]["code"], "3037")

    def test_parses_twse_mis_intraday_quote_with_taiwan_timestamp(self) -> None:
        quote = stock_analysis.parse_intraday_quote(
            {
                "c": "3037",
                "n": "欣興",
                "d": "20260902",
                "t": "12:39:56",
                "z": "970.0000",
                "y": "971.0000",
                "o": "955.0000",
                "h": "988.0000",
                "l": "948.0000",
                "v": "20494",
            },
            {"code": "3037", "name": "欣興"},
            current_time=stock_analysis.dt.datetime(2026, 9, 2, 12, 40, tzinfo=stock_analysis.TAIPEI_TZ),
        )

        self.assertIsNotNone(quote)
        assert quote is not None
        self.assertEqual(quote["quote_kind"], "盤中最新成交價")
        self.assertEqual(quote["quote_time"], "2026-09-02 12:39:56")
        self.assertEqual(quote["price"], 970.0)
        self.assertEqual(quote["change"], -1.0)
        self.assertAlmostEqual(quote["change_percent"], -100 / 971)
        self.assertEqual(quote["volume"], 20_494_000)

    def test_normalizes_daily_bars_and_merges_current_intraday_candle(self) -> None:
        bars = stock_analysis.normalize_price_history(
            [
                {
                    "date": "2026-09-01",
                    "open": 921,
                    "max": 994,
                    "min": 911,
                    "close": 971,
                    "Trading_Volume": 94_479_548,
                    "Trading_turnover": 178_512,
                }
            ]
        )
        merged = stock_analysis.merge_current_quote_bar(
            bars,
            {
                "date": "2026-09-02",
                "quote_time": "2026-09-02 12:39:56",
                "close": 970,
                "open": 955,
                "high": 988,
                "low": 948,
                "volume": 20_494_000,
                "is_intraday": True,
            },
        )

        self.assertEqual(len(merged), 2)
        self.assertEqual(merged[-1]["time"], "2026-09-02")
        self.assertEqual(merged[-1]["close"], 970)
        self.assertEqual(merged[-1]["volume"], 20_494_000)
        self.assertTrue(merged[-1]["intraday"])

    def test_technical_chart_script_includes_requested_indicators(self) -> None:
        script = stock_analysis.technical_chart_script()

        self.assertIn("addCandlestickSeries", script)
        self.assertIn("MACD", script.upper())
        self.assertIn("function rsi", script)
        self.assertIn("function stochastic", script)
        self.assertIn('timeframe === "month"', script)


if __name__ == "__main__":
    unittest.main()
