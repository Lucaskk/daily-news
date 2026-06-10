#!/usr/bin/env python3
"""Generate a Taiwan stock analysis page for GitHub Pages.

The script accepts a Taiwan stock code or company name, fetches public quote
and financial-statement data, then writes a compact HTML dashboard plus JSON
and Markdown provenance files under wiki/stocks/.

This is research tooling only. It does not make investment recommendations.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html as html_lib
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import posixpath
import re
import sys
import time
from typing import Any
import urllib.error
import urllib.parse
import urllib.request


TWSE_QUOTES_URL = "https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL"
TPEX_QUOTES_URL = "https://www.tpex.org.tw/openapi/v1/tpex_mainboard_quotes"
GOODINFO_URL = "https://goodinfo.tw/tw/StockFinDetail.asp"
TAIPEI_TZ = dt.timezone(dt.timedelta(hours=8))
DEFAULT_OUTPUT_ROOT = Path("wiki/stocks")


class StockAnalysisError(RuntimeError):
    """Raised when a stock analysis page cannot be generated."""


class FinancialTableParser(HTMLParser):
    """Extract table rows from Goodinfo HTML with the Python standard library."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tables: list[list[list[str]]] = []
        self._stack: list[dict[str, Any]] = []
        self._cell: list[str] | None = None
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag in {"script", "style"}:
            self._skip_depth += 1
            return
        if self._skip_depth:
            return
        if tag == "table":
            table: list[list[str]] = []
            self.tables.append(table)
            self._stack.append({"rows": table, "row": None})
        elif tag == "tr" and self._stack:
            self._stack[-1]["row"] = []
        elif tag in {"td", "th"} and self._stack and self._stack[-1]["row"] is not None:
            self._cell = []

    def handle_data(self, data: str) -> None:
        if self._skip_depth or self._cell is None:
            return
        text = re.sub(r"\s+", " ", data)
        if text.strip():
            self._cell.append(text)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in {"script", "style"} and self._skip_depth:
            self._skip_depth -= 1
            return
        if self._skip_depth:
            return
        if tag in {"td", "th"} and self._stack and self._stack[-1]["row"] is not None:
            if self._cell is not None:
                self._stack[-1]["row"].append("".join(self._cell).strip())
                self._cell = None
        elif tag == "tr" and self._stack:
            row = self._stack[-1]["row"]
            if row and any(cell for cell in row):
                self._stack[-1]["rows"].append(row)
            self._stack[-1]["row"] = None
        elif tag == "table" and self._stack:
            self._stack.pop()


def now_taipei() -> dt.datetime:
    return dt.datetime.now(TAIPEI_TZ)


def read_url_bytes(url: str, headers: dict[str, str] | None = None, timeout: int = 20) -> bytes:
    request = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.read()
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")[:300]
        raise StockAnalysisError(f"HTTP {exc.code} while fetching {url}: {body}") from exc
    except urllib.error.URLError as exc:
        raise StockAnalysisError(f"Network error while fetching {url}: {exc}") from exc


def read_json(url: str) -> Any:
    raw = read_url_bytes(url, headers={"User-Agent": "Mozilla/5.0"})
    return json.loads(raw.decode("utf-8"))


def parse_number(value: Any) -> float | None:
    if value is None:
        return None
    text = str(value).strip()
    if not text or text in {"-", "N/A", "NA", "--"}:
        return None
    text = text.replace(",", "").replace("%", "").replace("％", "")
    text = text.replace("+", "").replace("億", "").replace("元", "").strip()
    text = re.sub(r"[^\d.\-]", "", text)
    if not text or text in {"-", "."}:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def fmt_number(value: float | None, digits: int = 1, suffix: str = "") -> str:
    if value is None:
        return "n/a"
    if abs(value) >= 1000 and suffix != "%":
        rendered = f"{value:,.0f}" if digits == 0 else f"{value:,.{digits}f}"
    else:
        rendered = f"{value:.{digits}f}"
    return rendered + suffix


def fmt_delta(value: float | None, digits: int = 1, suffix: str = "%") -> str:
    if value is None:
        return "n/a"
    sign = "+" if value > 0 else ""
    return f"{sign}{value:.{digits}f}{suffix}"


def safe_ratio(numerator: float | None, denominator: float | None) -> float | None:
    if numerator is None or denominator in (None, 0):
        return None
    return numerator / denominator * 100


def year_over_year(latest: float | None, previous: float | None) -> float | None:
    if latest is None or previous in (None, 0):
        return None
    return (latest - previous) / abs(previous) * 100


def roc_date_to_iso(value: str | None) -> str:
    if not value:
        return ""
    digits = re.sub(r"\D", "", str(value))
    if len(digits) == 7:
        year = int(digits[:3]) + 1911
        month = int(digits[3:5])
        day = int(digits[5:7])
    elif len(digits) == 8:
        year = int(digits[:4])
        month = int(digits[4:6])
        day = int(digits[6:8])
    else:
        return str(value)
    return f"{year:04d}-{month:02d}-{day:02d}"


def normalize_query(value: str) -> str:
    return re.sub(r"\s+", "", value.strip())


def stock_date_path(date_text: str, code: str) -> Path:
    date_value = dt.date.fromisoformat(date_text)
    return Path(f"{date_value:%Y/%m/%Y-%m-%d}") / code


def join_url(base: str, path: str) -> str:
    return base.rstrip("/") + "/" + path.lstrip("/")


def public_relative_path(output_root: Path, relative_html: Path) -> str | None:
    if not output_root.is_absolute():
        return f"{output_root.as_posix()}/{relative_html.as_posix()}"
    try:
        root = output_root.resolve().relative_to(Path.cwd().resolve())
    except ValueError:
        return None
    return f"{root.as_posix()}/{relative_html.as_posix()}"


def quote_from_twse(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "code": str(row.get("Code", "")).strip(),
        "name": str(row.get("Name", "")).strip(),
        "market": "TWSE",
        "market_label": "上市",
        "date": roc_date_to_iso(row.get("Date")),
        "close": parse_number(row.get("ClosingPrice")),
        "change": parse_number(row.get("Change")),
        "open": parse_number(row.get("OpeningPrice")),
        "high": parse_number(row.get("HighestPrice")),
        "low": parse_number(row.get("LowestPrice")),
        "volume": parse_number(row.get("TradeVolume")),
        "transactions": parse_number(row.get("Transaction")),
        "source_url": TWSE_QUOTES_URL,
    }


def quote_from_tpex(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "code": str(row.get("SecuritiesCompanyCode", "")).strip(),
        "name": str(row.get("CompanyName", "")).strip(),
        "market": "TPEx",
        "market_label": "上櫃",
        "date": roc_date_to_iso(row.get("Date")),
        "close": parse_number(row.get("Close")),
        "change": parse_number(row.get("Change")),
        "open": parse_number(row.get("Open")),
        "high": parse_number(row.get("High")),
        "low": parse_number(row.get("Low")),
        "volume": parse_number(row.get("TradingShares")),
        "transactions": parse_number(row.get("TransactionNumber")),
        "source_url": TPEX_QUOTES_URL,
    }


def fetch_quotes() -> list[dict[str, Any]]:
    quotes: list[dict[str, Any]] = []
    for row in read_json(TWSE_QUOTES_URL):
        quote = quote_from_twse(row)
        if quote["code"]:
            quotes.append(quote)
    for row in read_json(TPEX_QUOTES_URL):
        quote = quote_from_tpex(row)
        if quote["code"]:
            quotes.append(quote)
    return quotes


def resolve_stock(query: str, quotes: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    clean = normalize_query(query)
    code_match = re.search(r"\b\d{4}\b", query) or re.search(r"\d{4}", clean)
    quotes = quotes if quotes is not None else fetch_quotes()

    if code_match:
        code = code_match.group(0)
        quote = next((item for item in quotes if item["code"] == code), None)
        if quote:
            return quote
        return {
            "code": code,
            "name": "",
            "market": "unknown",
            "market_label": "未知市場",
            "date": "",
            "close": None,
            "change": None,
            "open": None,
            "high": None,
            "low": None,
            "volume": None,
            "transactions": None,
            "source_url": "",
        }

    exact = [item for item in quotes if normalize_query(item["name"]) == clean]
    if len(exact) == 1:
        return exact[0]

    partial = [item for item in quotes if clean and clean in normalize_query(item["name"])]
    if len(partial) == 1:
        return partial[0]
    if len(partial) > 1:
        options = "、".join(f"{item['name']}({item['code']})" for item in partial[:8])
        raise StockAnalysisError(f"股票名稱不夠精確，找到多個可能標的：{options}")

    raise StockAnalysisError("找不到股票代碼或名稱。請輸入 4 位數代碼，例如 2330，或完整股票名稱。")


def goodinfo_client_key() -> tuple[str, float]:
    tz_offset = -480
    now_ms = time.time() * 1000
    days_since_epoch = now_ms / 86400000
    days_adjusted = days_since_epoch - tz_offset / 1440
    client_key = f"2.8|38057.1435627105|46946.0324515993|{tz_offset}|{days_adjusted}|{days_adjusted}"
    return client_key, days_adjusted


def fetch_goodinfo_html(stock_id: str, report_category: str) -> str:
    client_key, days_adjusted = goodinfo_client_key()
    query = urllib.parse.urlencode(
        {
            "RPT_CAT": report_category,
            "STOCK_ID": stock_id,
            "REINIT": f"{days_adjusted:.10f}",
        }
    )
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Referer": "https://goodinfo.tw/",
        "Cookie": f"CLIENT_KEY={client_key}",
    }
    raw = read_url_bytes(f"{GOODINFO_URL}?{query}", headers=headers)
    return raw.decode("utf-8", errors="replace")


def extract_goodinfo_name(html_text: str, stock_id: str) -> str:
    title_match = re.search(rf"<title>\s*{re.escape(stock_id)}\s+(.+?)\s+-", html_text)
    if title_match:
        return html_lib.unescape(title_match.group(1)).strip()
    return ""


def parse_goodinfo_table(html_text: str) -> tuple[dict[str, dict[str, float | None]], list[str]]:
    parser = FinancialTableParser()
    parser.feed(html_text)
    if len(parser.tables) < 7:
        raise StockAnalysisError("Goodinfo 回傳內容沒有找到預期的財報表格，可能是暫時被擋或該標的沒有財報資料。")
    rows = parser.tables[6]
    header_index = next(
        (
            idx
            for idx, row in enumerate(rows)
            if sum(1 for cell in row if re.fullmatch(r"\d{4}", cell.strip())) >= 2
        ),
        None,
    )
    if header_index is None:
        raise StockAnalysisError("無法解析 Goodinfo 財報年度欄位。")

    header = rows[header_index]
    years = [cell.strip() for cell in header if re.fullmatch(r"\d{4}", cell.strip())]
    if not years:
        raise StockAnalysisError("Goodinfo 財報表格沒有年度資料。")

    marker_row = rows[header_index + 1] if header_index + 1 < len(rows) else []
    paired_amount_percent = len(marker_row) >= len(years) * 2 and any(
        marker in cell for cell in marker_row for marker in ("％", "%")
    )

    data: dict[str, dict[str, float | None]] = {}
    for row in rows[header_index + 1 :]:
        if len(row) < 2:
            continue
        field = row[0].strip()
        if not field or field in {"金額", "％", "%"}:
            continue
        values: dict[str, float | None] = {}
        for index, year in enumerate(years):
            value_index = 1 + index * 2 if paired_amount_percent else 1 + index
            values[year] = parse_number(row[value_index]) if value_index < len(row) else None
        if any(value is not None for value in values.values()):
            data[field] = values
    return data, years


def fetch_financials(stock_id: str) -> dict[str, Any]:
    reports: dict[str, Any] = {}
    company_name = ""
    for key, category in (
        ("income_statement", "IS_YEAR"),
        ("balance_sheet", "BS_YEAR"),
        ("cash_flow", "CF_YEAR"),
    ):
        html_text = fetch_goodinfo_html(stock_id, category)
        if not company_name:
            company_name = extract_goodinfo_name(html_text, stock_id)
        table, years = parse_goodinfo_table(html_text)
        reports[key] = table
        reports.setdefault("years", years)
        time.sleep(0.4)
    reports["company_name"] = company_name
    return reports


def pick_field(table: dict[str, dict[str, float | None]], patterns: list[str], exclude: list[str] | None = None) -> str | None:
    exclude = exclude or []
    for pattern in patterns:
        for field in table:
            if field == pattern and not any(blocked in field for blocked in exclude):
                return field
    for pattern in patterns:
        for field in table:
            if pattern in field and not any(blocked in field for blocked in exclude):
                return field
    return None


def table_value(
    table: dict[str, dict[str, float | None]],
    year: str,
    patterns: list[str],
    exclude: list[str] | None = None,
) -> float | None:
    field = pick_field(table, patterns, exclude)
    if not field:
        return None
    return table.get(field, {}).get(year)


def compute_metrics(financials: dict[str, Any]) -> dict[str, dict[str, float | None]]:
    income = financials["income_statement"]
    balance = financials["balance_sheet"]
    cash_flow = financials["cash_flow"]
    years = financials["years"][:3]
    metrics: dict[str, dict[str, float | None]] = {}

    for year in years:
        revenue = table_value(income, year, ["營業收入合計", "營業收入"], ["率"])
        gross_profit = table_value(income, year, ["營業毛利", "毛利"], ["率"])
        selling = table_value(income, year, ["推銷費用", "銷售費用"])
        admin = table_value(income, year, ["管理費用"])
        research = table_value(income, year, ["研究發展費用", "研發費用"])
        operating_income = table_value(income, year, ["營業利益", "營業利益(損失)", "營業利益（損失）"], ["率"])
        net_income = table_value(income, year, ["歸屬於母公司業主之本期淨利", "稅後淨利", "本期淨利"], ["率"])
        eps = table_value(income, year, ["每股稅後盈餘", "每股盈餘", "EPS"])

        current_assets = table_value(balance, year, ["流動資產合計", "流動資產總額"])
        current_liabilities = table_value(balance, year, ["流動負債合計", "流動負債總額"])
        liabilities = table_value(balance, year, ["負債總額", "負債總計"])
        assets = table_value(balance, year, ["資產總額", "資產總計"])
        equity = table_value(balance, year, ["股東權益總額", "權益總額"])
        cash = table_value(balance, year, ["現金及約當現金", "現金"])
        inventory = table_value(balance, year, ["存貨"])

        operating_cf = table_value(cash_flow, year, ["營業活動之淨現金流入(出)", "營業活動之淨現金流入"])
        investing_cf = table_value(cash_flow, year, ["投資活動之淨現金流入(出)", "投資活動之淨現金流入"])
        financing_cf = table_value(cash_flow, year, ["融資活動之淨現金流入(出)", "融資活動之淨現金流入"])
        capex = table_value(cash_flow, year, ["固定資產(增加)減少", "固定資產（增加）減少", "不動產、廠房及設備"])
        dividends = table_value(cash_flow, year, ["發放現金股利", "現金股利"])
        expense_values = [selling, admin, research]
        operating_expenses = (
            sum(value for value in expense_values if value is not None)
            if any(value is not None for value in expense_values)
            else None
        )

        metrics[year] = {
            "revenue": revenue,
            "gross_profit": gross_profit,
            "selling_expense": selling,
            "admin_expense": admin,
            "rd_expense": research,
            "operating_expenses": operating_expenses,
            "operating_income": operating_income,
            "net_income": net_income,
            "eps": eps,
            "current_assets": current_assets,
            "current_liabilities": current_liabilities,
            "liabilities": liabilities,
            "assets": assets,
            "equity": equity,
            "cash": cash,
            "inventory": inventory,
            "operating_cf": operating_cf,
            "investing_cf": investing_cf,
            "financing_cf": financing_cf,
            "capex": capex,
            "dividends": dividends,
            "free_cash_flow": (operating_cf + capex) if operating_cf is not None and capex is not None else None,
            "gross_margin": safe_ratio(gross_profit, revenue),
            "op_margin": safe_ratio(operating_income, revenue),
            "net_margin": safe_ratio(net_income, revenue),
            "selling_ratio": safe_ratio(selling, revenue),
            "admin_ratio": safe_ratio(admin, revenue),
            "rd_ratio": safe_ratio(research, revenue),
            "opex_ratio": safe_ratio(operating_expenses, revenue),
            "current_ratio": safe_ratio(current_assets, current_liabilities),
            "debt_ratio": safe_ratio(liabilities, assets),
            "roe": safe_ratio(net_income, equity),
            "roa": safe_ratio(net_income, assets),
            "cash_to_assets": safe_ratio(cash, assets),
        }
    return metrics


def sanity_check(metrics: dict[str, dict[str, float | None]], years: list[str]) -> list[dict[str, str]]:
    warnings: list[dict[str, str]] = []
    for year in years:
        item = metrics.get(year, {})
        gross_margin = item.get("gross_margin")
        if gross_margin is not None and gross_margin > 100:
            warnings.append({"level": "error", "field": f"{year} 毛利率", "message": f"{gross_margin:.1f}% 超過 100%"})
        if gross_margin is not None and gross_margin < -50:
            warnings.append({"level": "error", "field": f"{year} 毛利率", "message": f"{gross_margin:.1f}% 低於 -50%"})
        current_ratio = item.get("current_ratio")
        if current_ratio is not None and current_ratio < 0:
            warnings.append({"level": "error", "field": f"{year} 流動比率", "message": f"{current_ratio:.1f}% 為負值"})
        debt_ratio = item.get("debt_ratio")
        if debt_ratio is not None and debt_ratio > 100:
            warnings.append({"level": "warn", "field": f"{year} 負債比率", "message": f"{debt_ratio:.1f}% 超過 100%"})
        roe = item.get("roe")
        if roe is not None and roe > 100:
            warnings.append({"level": "warn", "field": f"{year} ROE", "message": f"{roe:.1f}% 超過 100%"})

    ordered = [(year, metrics[year].get("net_margin")) for year in years if year in metrics]
    for index in range(1, len(ordered)):
        previous_year, previous_value = ordered[index - 1]
        current_year, current_value = ordered[index]
        if previous_value is None or current_value is None:
            continue
        delta = current_value - previous_value
        if abs(delta) > 30:
            warnings.append(
                {
                    "level": "warn",
                    "field": f"{previous_year}->{current_year} 淨利率",
                    "message": f"波動 {delta:+.1f} 個百分點，建議確認是否有一次性損益",
                }
            )
    return warnings


def build_metadata(stock: dict[str, Any], years: list[str], fetched_at: str) -> dict[str, Any]:
    stock_id = stock["code"]
    return {
        "fetched_at": fetched_at,
        "source": "Goodinfo.tw, TWSE OpenAPI, TPEx OpenAPI",
        "source_urls": {
            "income_statement": f"{GOODINFO_URL}?RPT_CAT=IS_YEAR&STOCK_ID={stock_id}",
            "balance_sheet": f"{GOODINFO_URL}?RPT_CAT=BS_YEAR&STOCK_ID={stock_id}",
            "cash_flow": f"{GOODINFO_URL}?RPT_CAT=CF_YEAR&STOCK_ID={stock_id}",
            "quote": stock.get("source_url") or "",
            "mops_listed": f"https://mops.twse.com.tw/mops/web/t05st01?step=1&co_id={stock_id}&TYPEK=sii",
            "mops_otc": f"https://mops.twse.com.tw/mops/web/t05st01?step=1&co_id={stock_id}&TYPEK=otc",
        },
        "years_covered": years,
        "currency": "TWD 億元；股價為 TWD",
        "disclaimer": "僅供財務研究與學習參考，不構成投資建議。",
    }


def metric(metrics: dict[str, dict[str, float | None]], year: str, key: str) -> float | None:
    return metrics.get(year, {}).get(key)


def compare_text(metrics: dict[str, dict[str, float | None]], years: list[str], key: str, suffix: str = "%") -> str:
    if len(years) < 2:
        return "缺少前期比較"
    latest, previous = years[0], years[1]
    change = year_over_year(metric(metrics, latest, key), metric(metrics, previous, key))
    return f"較 {previous} 年 {fmt_delta(change, suffix=suffix)}"


def point_delta_text(metrics: dict[str, dict[str, float | None]], years: list[str], key: str) -> str:
    if len(years) < 2:
        return "缺少前期比較"
    latest, previous = years[0], years[1]
    latest_value = metric(metrics, latest, key)
    previous_value = metric(metrics, previous, key)
    if latest_value is None or previous_value is None:
        return "缺少前期比較"
    delta = latest_value - previous_value
    return f"較 {previous} 年 {delta:+.1f} 個百分點"


def build_insights(stock: dict[str, Any], metrics: dict[str, dict[str, float | None]], years: list[str]) -> dict[str, list[str]]:
    latest = years[0]
    previous = years[1] if len(years) > 1 else None
    latest_metrics = metrics[latest]
    previous_metrics = metrics.get(previous or "", {})
    revenue_growth = year_over_year(latest_metrics.get("revenue"), previous_metrics.get("revenue"))
    net_growth = year_over_year(latest_metrics.get("net_income"), previous_metrics.get("net_income"))
    op_cf_growth = year_over_year(latest_metrics.get("operating_cf"), previous_metrics.get("operating_cf"))

    quote_line = "尚未取得今日市場報價。"
    if stock.get("close") is not None:
        quote_line = (
            f"最新公開報價日期為 {stock.get('date') or '未標示'}，收盤價 "
            f"{fmt_number(stock.get('close'), 2)} 元，單日變動 {fmt_delta(stock.get('change'), 2, ' 元')}。"
        )

    return {
        "snapshot": [
            quote_line,
            f"最近財報年度 {latest} 年營收 {fmt_number(latest_metrics.get('revenue'), 0)} 億元，{compare_text(metrics, years, 'revenue')}。",
            f"{latest} 年 EPS 為 {fmt_number(latest_metrics.get('eps'), 2)} 元，ROE 為 {fmt_number(latest_metrics.get('roe'), 1, '%')}。",
        ],
        "operations": [
            f"{latest} 年毛利率 {fmt_number(latest_metrics.get('gross_margin'), 1, '%')}，{point_delta_text(metrics, years, 'gross_margin')}。",
            f"營業利益率 {fmt_number(latest_metrics.get('op_margin'), 1, '%')}，三費率合計 {fmt_number(latest_metrics.get('opex_ratio'), 1, '%')}。",
            f"營收年增率 {fmt_delta(revenue_growth)}，請搭配產業循環與價格假設解讀。",
        ],
        "profit": [
            f"{latest} 年稅後淨利 {fmt_number(latest_metrics.get('net_income'), 0)} 億元，年增率 {fmt_delta(net_growth)}。",
            f"淨利率 {fmt_number(latest_metrics.get('net_margin'), 1, '%')}，{point_delta_text(metrics, years, 'net_margin')}。",
            f"ROA 為 {fmt_number(latest_metrics.get('roa'), 1, '%')}，用來觀察資產投入是否有效轉成獲利。",
        ],
        "financial": [
            f"流動比率 {fmt_number(latest_metrics.get('current_ratio'), 1, '%')}，負債比率 {fmt_number(latest_metrics.get('debt_ratio'), 1, '%')}。",
            f"營業現金流 {fmt_number(latest_metrics.get('operating_cf'), 0)} 億元，年增率 {fmt_delta(op_cf_growth)}。",
            f"自由現金流估算 {fmt_number(latest_metrics.get('free_cash_flow'), 0)} 億元；資本支出使用 Goodinfo 固定資產增加減少欄位作代理。",
        ],
    }


def kpi_card(label: str, value: str, change: str, accent: str = "blue") -> str:
    return f"""
      <article class="kpi-card {accent}">
        <div class="kpi-label">{html_lib.escape(label)}</div>
        <div class="kpi-value">{html_lib.escape(value)}</div>
        <div class="kpi-change">{html_lib.escape(change)}</div>
      </article>
    """


def insight_box(title: str, items: list[str]) -> str:
    rows = "\n".join(f"<li>{html_lib.escape(item)}</li>" for item in items)
    return f"""
      <section class="insight-box">
        <h3>{html_lib.escape(title)}</h3>
        <ul>{rows}</ul>
      </section>
    """


def metric_table(metrics: dict[str, dict[str, float | None]], years: list[str], rows: list[tuple[str, str, str, int]]) -> str:
    headings = "".join(f"<th>{html_lib.escape(year)}</th>" for year in years)
    body = []
    for label, key, suffix, digits in rows:
        values = "".join(f"<td>{html_lib.escape(fmt_number(metric(metrics, year, key), digits, suffix))}</td>" for year in years)
        body.append(f"<tr><td>{html_lib.escape(label)}</td>{values}</tr>")
    return f"""
      <div class="table-wrap">
        <table class="data-table">
          <thead><tr><th>指標</th>{headings}</tr></thead>
          <tbody>{''.join(body)}</tbody>
        </table>
      </div>
    """


def render_html(analysis: dict[str, Any]) -> str:
    stock = analysis["stock"]
    years = analysis["years"]
    metrics = analysis["metrics"]
    metadata = analysis["metadata"]
    insights = analysis["insights"]
    latest = years[0]
    json_payload = json.dumps(analysis, ensure_ascii=False)
    title = f"{stock['name']} ({stock['code']}) 股票分析"
    source_urls = metadata["source_urls"]
    sanity = analysis["verification"]["sanity"]
    warning_items = "".join(
        f"<li><strong>{html_lib.escape(item['field'])}</strong>：{html_lib.escape(item['message'])}</li>"
        for item in sanity
    )
    warning_block = (
        f"<section class=\"warning-box\"><h3>資料合理性提醒</h3><ul>{warning_items}</ul></section>"
        if warning_items
        else "<section class=\"ok-box\">資料合理性檢查未發現重大錯誤；仍請以公開資訊觀測站與公司公告核對。</section>"
    )

    ops_cards = "".join(
        [
            kpi_card("營收", f"{fmt_number(metric(metrics, latest, 'revenue'), 0)} 億", compare_text(metrics, years, "revenue"), "blue"),
            kpi_card("毛利率", fmt_number(metric(metrics, latest, "gross_margin"), 1, "%"), point_delta_text(metrics, years, "gross_margin"), "green"),
            kpi_card("營業利益率", fmt_number(metric(metrics, latest, "op_margin"), 1, "%"), point_delta_text(metrics, years, "op_margin"), "orange"),
            kpi_card("三費率", fmt_number(metric(metrics, latest, "opex_ratio"), 1, "%"), "推銷、管理、研發合計", "purple"),
        ]
    )
    profit_cards = "".join(
        [
            kpi_card("稅後淨利", f"{fmt_number(metric(metrics, latest, 'net_income'), 0)} 億", compare_text(metrics, years, "net_income"), "green"),
            kpi_card("EPS", f"{fmt_number(metric(metrics, latest, 'eps'), 2)} 元", compare_text(metrics, years, "eps"), "blue"),
            kpi_card("ROE", fmt_number(metric(metrics, latest, "roe"), 1, "%"), "股東權益報酬率", "purple"),
            kpi_card("淨利率", fmt_number(metric(metrics, latest, "net_margin"), 1, "%"), point_delta_text(metrics, years, "net_margin"), "orange"),
        ]
    )
    finance_cards = "".join(
        [
            kpi_card("流動比率", fmt_number(metric(metrics, latest, "current_ratio"), 1, "%"), "短期償債能力", "blue"),
            kpi_card("負債比率", fmt_number(metric(metrics, latest, "debt_ratio"), 1, "%"), "總負債 / 總資產", "orange"),
            kpi_card("營業現金流", f"{fmt_number(metric(metrics, latest, 'operating_cf'), 0)} 億", compare_text(metrics, years, "operating_cf"), "green"),
            kpi_card("自由現金流", f"{fmt_number(metric(metrics, latest, 'free_cash_flow'), 0)} 億", "營業 CF + 固定資產增減", "purple"),
        ]
    )

    return f"""<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html_lib.escape(title)}</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.5.0/dist/chart.umd.min.js"></script>
  <style>
    :root {{
      --ink: #18202f;
      --muted: #617085;
      --line: #d8e0ea;
      --surface: #ffffff;
      --soft: #f5f7fb;
      --blue: #2463eb;
      --green: #15803d;
      --orange: #c05a1a;
      --purple: #6d49b7;
      --red: #b42318;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Noto Sans TC", "Microsoft JhengHei", sans-serif;
      color: var(--ink);
      background: var(--soft);
      letter-spacing: 0;
    }}
    a {{ color: inherit; }}
    .hero {{
      background:
        linear-gradient(135deg, rgba(24,32,47,.94), rgba(36,99,235,.78)),
        url("https://images.unsplash.com/photo-1642790106117-e829e14a795f?auto=format&fit=crop&w=1800&q=80");
      background-size: cover;
      background-position: center;
      color: white;
      padding: 32px clamp(18px, 4vw, 48px) 26px;
    }}
    .eyebrow {{ font-size: 13px; color: rgba(255,255,255,.75); margin-bottom: 8px; }}
    h1 {{ margin: 0; font-size: clamp(30px, 5vw, 56px); line-height: 1.05; }}
    .subtitle {{ margin-top: 12px; color: rgba(255,255,255,.82); max-width: 980px; line-height: 1.55; }}
    .source-row {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: 18px; }}
    .source-row a {{
      border: 1px solid rgba(255,255,255,.28);
      color: white;
      padding: 7px 10px;
      border-radius: 8px;
      font-size: 13px;
      text-decoration: none;
      background: rgba(255,255,255,.08);
    }}
    .layout {{ max-width: 1180px; margin: 0 auto; padding: 18px; }}
    .snapshot-grid, .kpi-row {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 12px;
      margin-bottom: 16px;
    }}
    .kpi-card, .quote-card, .chart-card, .insight-box, .warning-box, .ok-box, .table-wrap {{
      background: var(--surface);
      border: 1px solid var(--line);
      border-radius: 8px;
      box-shadow: 0 1px 3px rgba(15,23,42,.06);
    }}
    .quote-card, .kpi-card {{ padding: 16px; border-top: 4px solid var(--blue); min-height: 108px; }}
    .kpi-card.green, .quote-card.green {{ border-top-color: var(--green); }}
    .kpi-card.orange, .quote-card.orange {{ border-top-color: var(--orange); }}
    .kpi-card.purple, .quote-card.purple {{ border-top-color: var(--purple); }}
    .kpi-label {{ color: var(--muted); font-size: 12px; font-weight: 700; text-transform: uppercase; }}
    .kpi-value {{ font-size: clamp(22px, 3vw, 31px); font-weight: 760; margin-top: 6px; line-height: 1.05; }}
    .kpi-change {{ color: var(--muted); font-size: 13px; margin-top: 8px; line-height: 1.35; }}
    .tabs {{
      position: sticky;
      top: 0;
      z-index: 3;
      display: flex;
      gap: 4px;
      padding: 10px 18px;
      background: rgba(245,247,251,.94);
      border-bottom: 1px solid var(--line);
      backdrop-filter: blur(10px);
      overflow-x: auto;
    }}
    .tab {{
      appearance: none;
      border: 1px solid var(--line);
      background: white;
      color: var(--muted);
      border-radius: 8px;
      padding: 10px 14px;
      font-weight: 700;
      cursor: pointer;
      white-space: nowrap;
    }}
    .tab.active {{ color: white; background: var(--ink); border-color: var(--ink); }}
    .tab-content {{ display: none; }}
    .tab-content.active {{ display: block; }}
    .section-title {{ font-size: 22px; margin: 10px 0 14px; }}
    .insight-box, .warning-box, .ok-box {{ padding: 16px 18px; margin-bottom: 16px; }}
    .insight-box h3, .warning-box h3 {{ margin: 0 0 8px; font-size: 15px; }}
    .insight-box ul, .warning-box ul {{ margin: 0; padding-left: 20px; color: var(--muted); line-height: 1.65; }}
    .warning-box {{ border-color: #f4b7ad; background: #fff7f5; color: #7a271a; }}
    .ok-box {{ color: #14532d; background: #f0fdf4; border-color: #bbf7d0; }}
    .charts-grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 14px;
      margin-bottom: 16px;
    }}
    .chart-card {{ padding: 16px; }}
    .chart-title {{ font-weight: 760; margin-bottom: 12px; color: #334155; }}
    .chart-container {{ position: relative; height: 280px; }}
    .table-wrap {{ overflow-x: auto; margin-bottom: 18px; }}
    .data-table {{ width: 100%; border-collapse: collapse; font-size: 14px; min-width: 620px; }}
    .data-table th {{ background: #263245; color: white; text-align: right; padding: 10px; }}
    .data-table th:first-child, .data-table td:first-child {{ text-align: left; }}
    .data-table td {{ padding: 10px; border-bottom: 1px solid var(--line); text-align: right; background: white; }}
    .data-table tr:nth-child(even) td {{ background: #f8fafc; }}
    .footer-note {{ color: var(--muted); font-size: 13px; line-height: 1.6; margin: 20px 0 32px; }}
    @media (max-width: 820px) {{
      .snapshot-grid, .kpi-row, .charts-grid {{ grid-template-columns: 1fr; }}
      .hero {{ padding-top: 26px; }}
      .chart-container {{ height: 240px; }}
    }}
  </style>
</head>
<body>
  <header class="hero">
    <div class="eyebrow">台灣股票財務分析 | 僅供研究參考</div>
    <h1>{html_lib.escape(stock['name'])} ({html_lib.escape(stock['code'])})</h1>
    <div class="subtitle">
      資料更新：{html_lib.escape(metadata['fetched_at'])}；市場：{html_lib.escape(stock.get('market_label') or '未知')}；
      財報期間：{html_lib.escape(' / '.join(years))}。本頁使用公開資料自動產生，請以公司公告與公開資訊觀測站核對。
    </div>
    <div class="source-row">
      <a href="{html_lib.escape(source_urls['income_statement'])}">Goodinfo 損益表</a>
      <a href="{html_lib.escape(source_urls['balance_sheet'])}">Goodinfo 資產負債表</a>
      <a href="{html_lib.escape(source_urls['cash_flow'])}">Goodinfo 現金流量表</a>
      <a href="{html_lib.escape(source_urls['mops_listed'])}">MOPS 上市公告</a>
      <a href="{html_lib.escape(source_urls['mops_otc'])}">MOPS 上櫃公告</a>
    </div>
  </header>

  <nav class="tabs" aria-label="股票分析分頁">
    <button class="tab active" type="button" data-tab="snapshot">總覽</button>
    <button class="tab" type="button" data-tab="operations">經營分析</button>
    <button class="tab" type="button" data-tab="profit">獲利分析</button>
    <button class="tab" type="button" data-tab="financial">財務健全度</button>
  </nav>

  <main class="layout">
    <section id="snapshot" class="tab-content active">
      <h2 class="section-title">總覽</h2>
      <div class="snapshot-grid">
        {kpi_card("最新收盤價", f"{fmt_number(stock.get('close'), 2)} 元", f"日期 {stock.get('date') or 'n/a'}；變動 {fmt_delta(stock.get('change'), 2, ' 元')}", "blue")}
        {kpi_card("成交量", f"{fmt_number(stock.get('volume'), 0)} 股", "TWSE / TPEx 公開行情", "green")}
        {kpi_card("最近營收年度", f"{fmt_number(metric(metrics, latest, 'revenue'), 0)} 億", compare_text(metrics, years, "revenue"), "orange")}
        {kpi_card("合理性檢查", "通過" if not sanity else f"{len(sanity)} 項提醒", "有提醒不代表資料錯誤，需人工核對", "purple")}
      </div>
      {insight_box("今日摘要", insights["snapshot"])}
      {warning_block}
    </section>

    <section id="operations" class="tab-content">
      <h2 class="section-title">經營分析</h2>
      <div class="kpi-row">{ops_cards}</div>
      {insight_box("經營重點", insights["operations"])}
      <div class="charts-grid">
        <article class="chart-card"><div class="chart-title">營收與毛利率</div><div class="chart-container"><canvas id="revenueChart"></canvas></div></article>
        <article class="chart-card"><div class="chart-title">三費結構</div><div class="chart-container"><canvas id="expenseChart"></canvas></div></article>
        <article class="chart-card"><div class="chart-title">利潤率比較</div><div class="chart-container"><canvas id="marginChart"></canvas></div></article>
        <article class="chart-card"><div class="chart-title">營業利益與營益率</div><div class="chart-container"><canvas id="opIncomeChart"></canvas></div></article>
      </div>
      {metric_table(metrics, years, [
        ("營收（億元）", "revenue", "", 0),
        ("毛利率", "gross_margin", "%", 1),
        ("營業利益（億元）", "operating_income", "", 0),
        ("營業利益率", "op_margin", "%", 1),
        ("推銷費用率", "selling_ratio", "%", 1),
        ("管理費用率", "admin_ratio", "%", 1),
        ("研發費用率", "rd_ratio", "%", 1),
      ])}
    </section>

    <section id="profit" class="tab-content">
      <h2 class="section-title">獲利分析</h2>
      <div class="kpi-row">{profit_cards}</div>
      {insight_box("獲利重點", insights["profit"])}
      <div class="charts-grid">
        <article class="chart-card"><div class="chart-title">稅後淨利與淨利率</div><div class="chart-container"><canvas id="netIncomeChart"></canvas></div></article>
        <article class="chart-card"><div class="chart-title">EPS 趨勢</div><div class="chart-container"><canvas id="epsChart"></canvas></div></article>
        <article class="chart-card"><div class="chart-title">ROE / ROA</div><div class="chart-container"><canvas id="returnChart"></canvas></div></article>
        <article class="chart-card"><div class="chart-title">現金股利</div><div class="chart-container"><canvas id="dividendChart"></canvas></div></article>
      </div>
      {metric_table(metrics, years, [
        ("稅後淨利（億元）", "net_income", "", 0),
        ("EPS（元）", "eps", "", 2),
        ("淨利率", "net_margin", "%", 1),
        ("ROE", "roe", "%", 1),
        ("ROA", "roa", "%", 1),
        ("現金股利（億元）", "dividends", "", 0),
      ])}
    </section>

    <section id="financial" class="tab-content">
      <h2 class="section-title">財務健全度</h2>
      <div class="kpi-row">{finance_cards}</div>
      {insight_box("財務結構重點", insights["financial"])}
      <div class="charts-grid">
        <article class="chart-card"><div class="chart-title">資產、負債、權益</div><div class="chart-container"><canvas id="structureChart"></canvas></div></article>
        <article class="chart-card"><div class="chart-title">現金流量三表</div><div class="chart-container"><canvas id="cashFlowChart"></canvas></div></article>
        <article class="chart-card"><div class="chart-title">流動比率與負債比率</div><div class="chart-container"><canvas id="ratioChart"></canvas></div></article>
        <article class="chart-card"><div class="chart-title">現金與自由現金流</div><div class="chart-container"><canvas id="cashChart"></canvas></div></article>
      </div>
      {metric_table(metrics, years, [
        ("現金及約當現金（億元）", "cash", "", 0),
        ("存貨（億元）", "inventory", "", 0),
        ("資產總額（億元）", "assets", "", 0),
        ("負債總額（億元）", "liabilities", "", 0),
        ("股東權益（億元）", "equity", "", 0),
        ("流動比率", "current_ratio", "%", 1),
        ("負債比率", "debt_ratio", "%", 1),
        ("營業現金流（億元）", "operating_cf", "", 0),
        ("自由現金流（億元）", "free_cash_flow", "", 0),
      ])}
    </section>

    <p class="footer-note">
      來源：Goodinfo.tw、TWSE OpenAPI、TPEx OpenAPI、公開資訊觀測站。金額單位若未特別標示均為新台幣億元。
      本分析由程式自動整理，僅供財務研究與學習參考，不構成買賣建議或投資招攬。
      背景圖來源：Unsplash。
    </p>
  </main>

  <script>
    const analysis = {json_payload};
    const years = [...analysis.years].reverse();
    const metrics = analysis.metrics;
    const colors = {{
      blue: "#2463eb",
      green: "#15803d",
      orange: "#c05a1a",
      purple: "#6d49b7",
      red: "#b42318",
      gray: "#64748b"
    }};
    const value = key => years.map(year => metrics[year]?.[key] ?? null);
    const moneyAxis = {{ ticks: {{ callback: v => v.toLocaleString() }} }};
    const percentAxis = {{ position: "right", grid: {{ display: false }}, ticks: {{ callback: v => v + "%" }} }};

    document.querySelectorAll(".tab").forEach(button => {{
      button.addEventListener("click", () => {{
        document.querySelectorAll(".tab").forEach(item => item.classList.remove("active"));
        document.querySelectorAll(".tab-content").forEach(item => item.classList.remove("active"));
        button.classList.add("active");
        document.getElementById(button.dataset.tab).classList.add("active");
      }});
    }});

    function chart(id, config) {{
      const canvas = document.getElementById(id);
      if (!canvas || typeof Chart === "undefined") return;
      new Chart(canvas, config);
    }}
    function mixedOptions() {{
      return {{
        responsive: true,
        maintainAspectRatio: false,
        interaction: {{ mode: "index", intersect: false }},
        scales: {{ x: {{ grid: {{ display: false }} }}, y: moneyAxis, y2: percentAxis }},
        plugins: {{ legend: {{ labels: {{ boxWidth: 12 }} }} }}
      }};
    }}
    function lineDataset(label, key, color, axis = "y2") {{
      return {{ label, data: value(key), type: "line", borderColor: color, backgroundColor: color, yAxisID: axis, tension: .25, pointRadius: 4 }};
    }}
    function barDataset(label, key, color, axis = "y") {{
      return {{ label, data: value(key), backgroundColor: color + "33", borderColor: color, borderWidth: 2, yAxisID: axis }};
    }}

    chart("revenueChart", {{
      type: "bar",
      data: {{ labels: years, datasets: [barDataset("營收", "revenue", colors.blue), lineDataset("毛利率", "gross_margin", colors.green)] }},
      options: mixedOptions()
    }});
    chart("expenseChart", {{
      type: "bar",
      data: {{ labels: years, datasets: [
        barDataset("推銷費用", "selling_expense", colors.orange),
        barDataset("管理費用", "admin_expense", colors.purple),
        barDataset("研發費用", "rd_expense", colors.green)
      ] }},
      options: {{ responsive: true, maintainAspectRatio: false, scales: {{ x: {{ stacked: true, grid: {{ display: false }} }}, y: {{ ...moneyAxis, stacked: true }} }} }}
    }});
    chart("marginChart", {{
      type: "line",
      data: {{ labels: years, datasets: [
        lineDataset("毛利率", "gross_margin", colors.green, "y"),
        lineDataset("營益率", "op_margin", colors.blue, "y"),
        lineDataset("淨利率", "net_margin", colors.orange, "y")
      ] }},
      options: {{ responsive: true, maintainAspectRatio: false, scales: {{ x: {{ grid: {{ display: false }} }}, y: {{ ticks: {{ callback: v => v + "%" }} }} }} }}
    }});
    chart("opIncomeChart", {{
      type: "bar",
      data: {{ labels: years, datasets: [barDataset("營業利益", "operating_income", colors.blue), lineDataset("營益率", "op_margin", colors.orange)] }},
      options: mixedOptions()
    }});
    chart("netIncomeChart", {{
      type: "bar",
      data: {{ labels: years, datasets: [barDataset("稅後淨利", "net_income", colors.green), lineDataset("淨利率", "net_margin", colors.orange)] }},
      options: mixedOptions()
    }});
    chart("epsChart", {{
      type: "line",
      data: {{ labels: years, datasets: [lineDataset("EPS", "eps", colors.blue, "y")] }},
      options: {{ responsive: true, maintainAspectRatio: false, scales: {{ x: {{ grid: {{ display: false }} }}, y: {{ grid: {{ color: "rgba(0,0,0,.05)" }} }} }} }}
    }});
    chart("returnChart", {{
      type: "line",
      data: {{ labels: years, datasets: [lineDataset("ROE", "roe", colors.purple, "y"), lineDataset("ROA", "roa", colors.green, "y")] }},
      options: {{ responsive: true, maintainAspectRatio: false, scales: {{ x: {{ grid: {{ display: false }} }}, y: {{ ticks: {{ callback: v => v + "%" }} }} }} }}
    }});
    chart("dividendChart", {{
      type: "bar",
      data: {{ labels: years, datasets: [barDataset("現金股利", "dividends", colors.orange)] }},
      options: {{ responsive: true, maintainAspectRatio: false, scales: {{ x: {{ grid: {{ display: false }} }}, y: moneyAxis }} }}
    }});
    chart("structureChart", {{
      type: "bar",
      data: {{ labels: years, datasets: [
        barDataset("負債", "liabilities", colors.orange),
        barDataset("權益", "equity", colors.green)
      ] }},
      options: {{ responsive: true, maintainAspectRatio: false, scales: {{ x: {{ stacked: true, grid: {{ display: false }} }}, y: {{ ...moneyAxis, stacked: true }} }} }}
    }});
    chart("cashFlowChart", {{
      type: "bar",
      data: {{ labels: years, datasets: [
        barDataset("營業 CF", "operating_cf", colors.green),
        barDataset("投資 CF", "investing_cf", colors.orange),
        barDataset("融資 CF", "financing_cf", colors.purple)
      ] }},
      options: {{ responsive: true, maintainAspectRatio: false, scales: {{ x: {{ grid: {{ display: false }} }}, y: moneyAxis }} }}
    }});
    chart("ratioChart", {{
      type: "line",
      data: {{ labels: years, datasets: [lineDataset("流動比率", "current_ratio", colors.blue, "y"), lineDataset("負債比率", "debt_ratio", colors.orange, "y")] }},
      options: {{ responsive: true, maintainAspectRatio: false, scales: {{ x: {{ grid: {{ display: false }} }}, y: {{ ticks: {{ callback: v => v + "%" }} }} }} }}
    }});
    chart("cashChart", {{
      type: "bar",
      data: {{ labels: years, datasets: [barDataset("現金", "cash", colors.blue), lineDataset("自由現金流", "free_cash_flow", colors.green, "y")] }},
      options: {{ responsive: true, maintainAspectRatio: false, scales: {{ x: {{ grid: {{ display: false }} }}, y: moneyAxis }} }}
    }});
  </script>
</body>
</html>
"""


def render_markdown_summary(analysis: dict[str, Any], html_public_url: str | None) -> str:
    stock = analysis["stock"]
    metadata = analysis["metadata"]
    today = now_taipei().date().isoformat()
    sources = metadata["source_urls"]
    link_line = f"- 分析頁：{html_public_url}\n" if html_public_url else ""
    insight_lines = "\n".join(f"- {item}" for item in analysis["insights"]["snapshot"])
    return f"""---
title: "{stock['name']} ({stock['code']}) 股票分析"
type: stock-analysis
created: {today}
updated: {today}
status: active
tags: [stocks, taiwan-stocks]
sources:
  - Goodinfo.tw
  - TWSE OpenAPI
  - TPEx OpenAPI
---

# {stock['name']} ({stock['code']}) 股票分析

{link_line}- 產生時間：{metadata['fetched_at']}
- 市場：{stock.get('market_label') or '未知'}
- 最新行情日期：{stock.get('date') or 'n/a'}
- 財報年度：{', '.join(analysis['years'])}

## 摘要

{insight_lines}

## 來源

- [Goodinfo 損益表]({sources['income_statement']})
- [Goodinfo 資產負債表]({sources['balance_sheet']})
- [Goodinfo 現金流量表]({sources['cash_flow']})
- [公開資訊觀測站 上市]({sources['mops_listed']})
- [公開資訊觀測站 上櫃]({sources['mops_otc']})

## 投資提醒

本頁僅供財務研究與學習參考，不構成投資建議。若資料與公司公告或公開資訊觀測站不一致，應以官方公告為準。
"""


def write_latest_redirect(output_root: Path, relative_html: Path) -> Path:
    latest_path = output_root / "latest-analysis.html"
    target = relative_html.as_posix()
    latest_path.write_text(
        f"""<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0; url={html_lib.escape(target)}">
  <title>Latest Stock Analysis</title>
</head>
<body>
  <p><a href="{html_lib.escape(target)}">Open latest stock analysis</a></p>
</body>
</html>
""",
        encoding="utf-8",
    )
    return latest_path


def write_code_redirect(output_root: Path, code: str, relative_html: Path) -> Path:
    code_dir = Path("by-code") / code
    code_path = output_root / code_dir / "index.html"
    code_path.parent.mkdir(parents=True, exist_ok=True)
    target = posixpath.relpath(relative_html.as_posix(), code_dir.as_posix())
    code_path.write_text(
        f"""<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0; url={html_lib.escape(target)}">
  <meta name="robots" content="noindex">
  <title>{html_lib.escape(code)} 最新股票分析</title>
</head>
<body>
  <p><a href="{html_lib.escape(target)}">開啟 {html_lib.escape(code)} 最新股票分析</a></p>
</body>
</html>
""",
        encoding="utf-8",
    )
    return code_path


def write_stock_index(output_root: Path) -> Path:
    index_path = output_root / "index.md"
    today = now_taipei().date().isoformat()
    if index_path.exists():
        return index_path
    index_path.write_text(
        f"""---
title: "股票分析索引"
type: overview
created: {today}
updated: {today}
status: active
tags: [stocks, taiwan-stocks]
sources: []
---

# 股票分析索引

股票分析頁會放在 `wiki/stocks/YYYY/MM/YYYY-MM-DD/<stock-code>/`。

- [Latest Analysis](latest-analysis.html) - 最新一次產生的股票分析頁。

## 使用方式

LINE webhook 收到股票代碼或名稱後，會產生 HTML 分析頁並回傳短連結。完整內容放在網頁，LINE 只保留日期、標的與連結，以降低訊息長度與使用費用。
""",
        encoding="utf-8",
    )
    return index_path


def generate_analysis(query: str, output_root: Path = DEFAULT_OUTPUT_ROOT, public_base_url: str | None = None) -> dict[str, Any]:
    stock = resolve_stock(query)
    financials = fetch_financials(stock["code"])
    if not stock.get("name"):
        stock["name"] = financials.get("company_name") or stock["code"]
    years = financials["years"][:3]
    if not years:
        raise StockAnalysisError("沒有可分析的年度財報資料。")

    metrics = compute_metrics(financials)
    fetched_at = now_taipei().replace(microsecond=0).isoformat()
    metadata = build_metadata(stock, years, fetched_at)
    verification = {
        "sanity": sanity_check(metrics, years),
        "sanity_pass": True,
    }
    verification["sanity_pass"] = all(item["level"] != "error" for item in verification["sanity"])

    analysis = {
        "stock": stock,
        "years": years,
        "metrics": metrics,
        "metadata": metadata,
        "verification": verification,
        "insights": build_insights(stock, metrics, years),
    }

    date_text = now_taipei().date().isoformat()
    relative_dir = stock_date_path(date_text, stock["code"])
    target_dir = output_root / relative_dir
    target_dir.mkdir(parents=True, exist_ok=True)
    output_root.mkdir(parents=True, exist_ok=True)

    html_name = f"stock-analysis-{stock['code']}-{date_text}.html"
    json_name = f"stock-analysis-{stock['code']}-{date_text}.json"
    md_name = f"stock-analysis-{stock['code']}-{date_text}.md"
    html_path = target_dir / html_name
    json_path = target_dir / json_name
    md_path = target_dir / md_name

    relative_html = relative_dir / html_name
    public_path = public_relative_path(output_root, relative_html)
    public_url = join_url(public_base_url, public_path) if public_base_url and public_path else None
    html_path.write_text(render_html(analysis), encoding="utf-8")
    json_path.write_text(json.dumps(analysis, ensure_ascii=False, indent=2), encoding="utf-8")
    md_path.write_text(render_markdown_summary(analysis, public_url), encoding="utf-8")
    latest_path = write_latest_redirect(output_root, relative_html)
    code_latest_path = write_code_redirect(output_root, stock["code"], relative_html)
    index_path = write_stock_index(output_root)

    analysis["artifacts"] = {
        "html_path": html_path.as_posix(),
        "json_path": json_path.as_posix(),
        "markdown_path": md_path.as_posix(),
        "latest_path": latest_path.as_posix(),
        "code_latest_path": code_latest_path.as_posix(),
        "index_path": index_path.as_posix(),
        "relative_html_path": public_path or f"{output_root.as_posix()}/{relative_html.as_posix()}",
        "public_url": public_url,
    }
    return analysis


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a Taiwan stock analysis HTML page.")
    parser.add_argument("query", help="Stock code or company name, for example 2330 or 台積電")
    parser.add_argument("--output-root", default=str(DEFAULT_OUTPUT_ROOT), help="Output root, defaults to wiki/stocks")
    parser.add_argument(
        "--public-base-url",
        default=os.environ.get("PUBLIC_STOCK_BASE_URL") or os.environ.get("PUBLIC_SLIDES_BASE_URL") or "",
        help="Public GitHub Pages base URL, for example https://lucaskk.github.io/daily-news",
    )
    parser.add_argument("--json", action="store_true", help="Print artifact metadata as JSON")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    try:
        analysis = generate_analysis(
            args.query,
            output_root=Path(args.output_root),
            public_base_url=args.public_base_url.strip() or None,
        )
    except StockAnalysisError as exc:
        print(f"Stock analysis failed: {exc}", file=sys.stderr)
        return 1

    artifacts = analysis["artifacts"]
    if args.json:
        print(json.dumps({"stock": analysis["stock"], "artifacts": artifacts}, ensure_ascii=False, indent=2))
    else:
        print(f"Generated {analysis['stock']['name']} ({analysis['stock']['code']})")
        print(f"HTML: {artifacts['html_path']}")
        if artifacts.get("public_url"):
            print(f"URL: {artifacts['public_url']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
