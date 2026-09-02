#!/usr/bin/env python3
"""Generate a Taiwan stock analysis page for GitHub Pages.

The script accepts a Taiwan stock code or company name, fetches public quote
data plus FinMind financial statements, validates the latest income/balance
sheet values against TWSE/TPEx official OpenAPI when available, then writes a
compact HTML dashboard plus JSON and Markdown provenance files under
wiki/stocks/.

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
from typing import Any
import urllib.error
import urllib.parse
import urllib.request


TWSE_QUOTES_URL = "https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL"
TPEX_QUOTES_URL = "https://www.tpex.org.tw/openapi/v1/tpex_mainboard_quotes"
TWSE_MIS_QUOTE_URL = "https://mis.twse.com.tw/stock/api/getStockInfo.jsp"
TWSE_MIS_PAGE_URL = "https://mis.twse.com.tw/stock/"
FINMIND_API_URL = "https://api.finmindtrade.com/api/v4/data"
FINMIND_FUNDAMENTAL_URL = "https://finmind.github.io/tutor/TaiwanMarket/Fundamental/"
FINMIND_LOOKBACK_YEARS = 7
FINMIND_PRICE_DATASET = "TaiwanStockPrice"
PRICE_LOOKBACK_DAYS = 900
MAX_PRICE_BARS = 560
TWSE_OFFICIAL_BASE_URL = "https://openapi.twse.com.tw/v1/opendata"
TPEX_OFFICIAL_BASE_URL = "https://www.tpex.org.tw/openapi/v1"
OFFICIAL_REPORT_VARIANTS = ("ci", "bd", "fh", "ins", "mim", "basi")
TAIPEI_TZ = dt.timezone(dt.timedelta(hours=8))
DEFAULT_OUTPUT_ROOT = Path("wiki/stocks")
YEAR_PERIOD_PATTERN = re.compile(r"\d{4}")
QUARTER_PERIOD_PATTERN = re.compile(r"\d{4}Q[1-4]", re.IGNORECASE)


class StockAnalysisError(RuntimeError):
    """Raised when a stock analysis page cannot be generated."""


class FinancialTableParser(HTMLParser):
    """Extract table rows from a legacy financial HTML page with the Python standard library."""

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


def format_taipei_time(value: str | dt.datetime) -> str:
    """Format an instant as Taiwan local time without a timezone suffix."""
    if isinstance(value, dt.datetime):
        parsed = value
    else:
        try:
            parsed = dt.datetime.fromisoformat(value)
        except ValueError:
            return value

    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=TAIPEI_TZ)
    else:
        parsed = parsed.astimezone(TAIPEI_TZ)
    return parsed.strftime("%Y-%m-%d %H:%M:%S")


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


def read_json(url: str, headers: dict[str, str] | None = None) -> Any:
    request_headers = {"User-Agent": "daily-news-stock-analysis/1.0"}
    if headers:
        request_headers.update(headers)
    raw = read_url_bytes(url, headers=request_headers)
    return json.loads(raw.decode("utf-8-sig"))


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
    errors: list[str] = []
    for url, parser in (
        (TWSE_QUOTES_URL, quote_from_twse),
        (TPEX_QUOTES_URL, quote_from_tpex),
    ):
        try:
            rows = read_json(url)
        except StockAnalysisError as exc:
            errors.append(str(exc))
            continue
        for row in rows:
            quote = parser(row)
            if quote["code"]:
                quotes.append(quote)
    if not quotes:
        detail = "；".join(errors) if errors else "來源沒有回傳資料"
        raise StockAnalysisError(f"TWSE/TPEx 每日行情目前無法取得：{detail}")
    return quotes


def intraday_market_channels(stock: dict[str, Any]) -> list[str]:
    market = str(stock.get("market") or "").upper()
    if market == "TWSE":
        return ["tse"]
    if market == "TPEX":
        return ["otc"]
    return ["tse", "otc"]


def intraday_quote_url(stock_code: str, channel: str) -> str:
    query = urllib.parse.urlencode(
        {
            "ex_ch": f"{channel}_{stock_code}.tw",
            "json": "1",
            "delay": "0",
        }
    )
    return f"{TWSE_MIS_QUOTE_URL}?{query}"


def first_order_book_price(value: Any) -> float | None:
    return parse_number(str(value or "").split("_")[0])


def parse_intraday_quote(
    row: dict[str, Any],
    stock: dict[str, Any],
    current_time: dt.datetime | None = None,
) -> dict[str, Any] | None:
    code = str(row.get("c") or "").strip()
    if not code or code != str(stock.get("code") or ""):
        return None

    quote_date = roc_date_to_iso(str(row.get("d") or ""))
    quote_clock = str(row.get("t") or "").strip()
    previous_close = parse_number(row.get("y"))
    now = current_time or now_taipei()
    is_today = quote_date == now.date().isoformat()
    market_open = (
        is_today
        and now.weekday() < 5
        and dt.time(9, 0) <= now.timetz().replace(tzinfo=None) <= dt.time(13, 35)
    )
    best_bid = first_order_book_price(row.get("b"))
    best_ask = first_order_book_price(row.get("a"))
    price = parse_number(row.get("z"))
    if price is None:
        price = parse_number(row.get("pz"))
    price_basis = "latest_trade"
    if price is None and market_open and (best_bid is not None or best_ask is not None):
        if best_bid is not None and best_ask is not None:
            price = (best_bid + best_ask) / 2
        else:
            price = best_bid if best_bid is not None else best_ask
        price_basis = "bid_ask_midpoint"
    if price is None:
        return None

    change = price - previous_close if previous_close is not None else None
    change_percent = safe_ratio(change, previous_close)
    if market_open and price_basis == "latest_trade":
        quote_kind = "盤中最新成交價"
    elif market_open:
        quote_kind = "盤中參考價（買賣中間）"
    elif is_today:
        quote_kind = "今日最新成交價"
    else:
        quote_kind = "最新成交價"

    volume_lots = parse_number(row.get("v"))
    quote_time = f"{quote_date} {quote_clock}".strip()
    return {
        "code": code,
        "name": str(row.get("n") or stock.get("name") or "").strip(),
        "date": quote_date,
        "quote_time": quote_time,
        "price": price,
        "previous_close": previous_close,
        "change": change,
        "change_percent": change_percent,
        "open": parse_number(row.get("o")),
        "high": parse_number(row.get("h")),
        "low": parse_number(row.get("l")),
        "volume_lots": volume_lots,
        "volume": volume_lots * 1000 if volume_lots is not None else None,
        "best_bid": best_bid,
        "best_ask": best_ask,
        "price_basis": price_basis,
        "quote_kind": quote_kind,
        "is_intraday": market_open,
        "source": "TWSE MIS 盤中資訊",
        "source_url": TWSE_MIS_PAGE_URL,
    }


def fetch_intraday_quote(stock: dict[str, Any]) -> dict[str, Any] | None:
    last_error: StockAnalysisError | None = None
    for channel in intraday_market_channels(stock):
        url = intraday_quote_url(stock["code"], channel)
        try:
            payload = read_json(
                url,
                headers={
                    "Referer": "https://mis.twse.com.tw/stock/index.jsp",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
                },
            )
        except StockAnalysisError as exc:
            last_error = exc
            continue
        for row in payload.get("msgArray") or []:
            parsed = parse_intraday_quote(row, stock)
            if parsed:
                parsed["api_url"] = url
                parsed["market"] = "TWSE" if channel == "tse" else "TPEX"
                parsed["market_label"] = "上市" if channel == "tse" else "上櫃"
                return parsed
    if last_error and len(intraday_market_channels(stock)) == 1:
        raise last_error
    return None


def enrich_stock_quote(stock: dict[str, Any]) -> dict[str, Any]:
    enriched = dict(stock)
    daily_close = parse_number(stock.get("close"))
    daily_change = parse_number(stock.get("change"))
    daily_previous_close = (
        daily_close - daily_change if daily_close is not None and daily_change is not None else None
    )
    enriched["daily_quote"] = {
        "date": stock.get("date"),
        "close": stock.get("close"),
        "change": stock.get("change"),
        "open": stock.get("open"),
        "high": stock.get("high"),
        "low": stock.get("low"),
        "volume": stock.get("volume"),
        "source_url": stock.get("source_url"),
    }
    enriched.setdefault("quote_kind", "最新收盤價")
    enriched.setdefault("quote_time", str(stock.get("date") or ""))
    enriched.setdefault("previous_close", daily_previous_close)
    enriched.setdefault("change_percent", safe_ratio(daily_change, daily_previous_close))
    enriched.setdefault("is_intraday", False)
    try:
        quote = fetch_intraday_quote(stock)
    except StockAnalysisError as exc:
        enriched["quote_warning"] = str(exc)
        return enriched
    if not quote:
        enriched["quote_warning"] = "TWSE MIS 暫無可用盤中成交資料，已改用每日行情。"
        return enriched

    enriched.update(
        {
            "name": quote.get("name") or enriched.get("name"),
            "market": quote.get("market") or enriched.get("market"),
            "market_label": quote.get("market_label") or enriched.get("market_label"),
            "date": quote["date"],
            "close": quote["price"],
            "change": quote["change"],
            "change_percent": quote["change_percent"],
            "open": quote["open"],
            "high": quote["high"],
            "low": quote["low"],
            "volume": quote["volume"],
            "volume_lots": quote["volume_lots"],
            "previous_close": quote["previous_close"],
            "best_bid": quote["best_bid"],
            "best_ask": quote["best_ask"],
            "price_basis": quote["price_basis"],
            "quote_kind": quote["quote_kind"],
            "quote_time": quote["quote_time"],
            "is_intraday": quote["is_intraday"],
            "quote_source": quote["source"],
            "source_url": quote["source_url"],
            "quote_api_url": quote["api_url"],
        }
    )
    return enriched


def finmind_price_url(stock_id: str, start_date: str) -> str:
    query = urllib.parse.urlencode(
        {
            "dataset": FINMIND_PRICE_DATASET,
            "data_id": stock_id,
            "start_date": start_date,
        }
    )
    return f"{FINMIND_API_URL}?{query}"


def normalize_price_history(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    bars: dict[str, dict[str, Any]] = {}
    for row in rows:
        date_text = str(row.get("date") or "")[:10]
        try:
            dt.date.fromisoformat(date_text)
        except ValueError:
            continue
        open_price = parse_number(row.get("open"))
        high = parse_number(row.get("max"))
        low = parse_number(row.get("min"))
        close = parse_number(row.get("close"))
        if None in {open_price, high, low, close}:
            continue
        bars[date_text] = {
            "time": date_text,
            "open": open_price,
            "high": high,
            "low": low,
            "close": close,
            "volume": parse_number(row.get("Trading_Volume")) or 0,
            "turnover": parse_number(row.get("Trading_turnover")),
        }
    return [bars[key] for key in sorted(bars)][-MAX_PRICE_BARS:]


def merge_current_quote_bar(
    bars: list[dict[str, Any]],
    stock: dict[str, Any],
) -> list[dict[str, Any]]:
    quote_date = str(stock.get("date") or "")
    close = parse_number(stock.get("close"))
    if not quote_date or close is None or not stock.get("quote_time"):
        return bars
    try:
        dt.date.fromisoformat(quote_date)
    except ValueError:
        return bars

    existing = next((dict(item) for item in bars if item["time"] == quote_date), {})
    open_price = parse_number(stock.get("open"))
    high = parse_number(stock.get("high"))
    low = parse_number(stock.get("low"))
    current_bar = {
        "time": quote_date,
        "open": open_price if open_price is not None else existing.get("open", close),
        "high": high if high is not None else existing.get("high", close),
        "low": low if low is not None else existing.get("low", close),
        "close": close,
        "volume": parse_number(stock.get("volume")) or existing.get("volume", 0),
        "turnover": existing.get("turnover"),
        "intraday": bool(stock.get("is_intraday")),
    }
    merged = [dict(item) for item in bars if item["time"] != quote_date]
    merged.append(current_bar)
    return sorted(merged, key=lambda item: item["time"])[-MAX_PRICE_BARS:]


def fetch_market_history(stock: dict[str, Any]) -> dict[str, Any]:
    start_date = (now_taipei().date() - dt.timedelta(days=PRICE_LOOKBACK_DAYS)).isoformat()
    url = finmind_price_url(stock["code"], start_date)
    payload = read_json(url, headers=finmind_headers())
    if str(payload.get("status", "")) != "200":
        message = payload.get("msg") or payload.get("message") or "unknown error"
        raise StockAnalysisError(f"FinMind {FINMIND_PRICE_DATASET} 取得失敗：{message}")
    bars = normalize_price_history(payload.get("data") or [])
    if not bars:
        raise StockAnalysisError(f"FinMind {FINMIND_PRICE_DATASET} 沒有 {stock['code']} 的可用資料。")
    bars = merge_current_quote_bar(bars, stock)
    return {
        "bars": bars,
        "source": "FinMind 日成交資料、TWSE MIS 盤中資訊",
        "history_url": url,
        "intraday_url": stock.get("source_url") or "",
        "intraday_api_url": stock.get("quote_api_url") or "",
        "updated_at": stock.get("quote_time") or stock.get("date") or "",
    }


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


def normalize_financial_period(value: str) -> str:
    return re.sub(r"\s+", "", value).upper()


def financial_period_sort_key(period: str) -> tuple[int, int]:
    normalized = normalize_financial_period(period)
    match = QUARTER_PERIOD_PATTERN.fullmatch(normalized)
    if match:
        return int(normalized[:4]), int(normalized[-1])
    if YEAR_PERIOD_PATTERN.fullmatch(normalized):
        return int(normalized), 0
    return 0, 0


def display_financial_period(period: str) -> str:
    normalized = normalize_financial_period(period)
    if QUARTER_PERIOD_PATTERN.fullmatch(normalized):
        return f"{normalized[:4]} Q{normalized[-1]}"
    if YEAR_PERIOD_PATTERN.fullmatch(normalized):
        return f"{normalized} 年"
    return period


def parse_legacy_financial_html_table(
    html_text: str,
    period_kind: str = "year",
) -> tuple[dict[str, dict[str, float | None]], list[str]]:
    parser = FinancialTableParser()
    parser.feed(html_text)
    if len(parser.tables) < 7:
        raise StockAnalysisError("舊版財報 HTML 沒有找到預期的財報表格，可能是暫時被擋或該標的沒有財報資料。")
    rows = parser.tables[6]
    period_pattern = QUARTER_PERIOD_PATTERN if period_kind == "quarter" else YEAR_PERIOD_PATTERN
    header_index = next(
        (
            idx
            for idx, row in enumerate(rows)
            if sum(1 for cell in row if period_pattern.fullmatch(normalize_financial_period(cell))) >= 2
        ),
        None,
    )
    if header_index is None:
        label = "季度" if period_kind == "quarter" else "年度"
        raise StockAnalysisError(f"無法解析舊版財報 HTML 的{label}欄位。")

    header = rows[header_index]
    periods = [
        normalize_financial_period(cell)
        for cell in header
        if period_pattern.fullmatch(normalize_financial_period(cell))
    ]
    if not periods:
        label = "季度" if period_kind == "quarter" else "年度"
        raise StockAnalysisError(f"舊版財報 HTML 沒有{label}資料。")

    marker_row = rows[header_index + 1] if header_index + 1 < len(rows) else []
    paired_amount_percent = len(marker_row) >= len(periods) * 2 and any(
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
        for index, period in enumerate(periods):
            value_index = 1 + index * 2 if paired_amount_percent else 1 + index
            values[period] = parse_number(row[value_index]) if value_index < len(row) else None
        if any(value is not None for value in values.values()):
            data[field] = values
    return data, periods


def select_latest_quarter(periods_by_report: list[list[str]]) -> tuple[str, str | None, list[str]]:
    if not periods_by_report:
        raise StockAnalysisError("沒有可判斷的季度財報期間。")
    common_periods = set(normalize_financial_period(item) for item in periods_by_report[0])
    for periods in periods_by_report[1:]:
        common_periods &= {normalize_financial_period(item) for item in periods}
    valid_periods = sorted(
        (period for period in common_periods if QUARTER_PERIOD_PATTERN.fullmatch(period)),
        key=financial_period_sort_key,
        reverse=True,
    )
    if not valid_periods:
        raise StockAnalysisError("三張季報沒有共同的財報季度，暫時無法進行同期比較。")

    latest = valid_periods[0]
    comparison = f"{int(latest[:4]) - 1}Q{latest[-1]}"
    if comparison not in common_periods:
        comparison = None
    return latest, comparison, valid_periods


FINMIND_DATASETS = {
    "income_statement": "TaiwanStockFinancialStatements",
    "balance_sheet": "TaiwanStockBalanceSheet",
    "cash_flow": "TaiwanStockCashFlowsStatement",
}

FINMIND_FIELD_MAPPINGS = {
    "income_statement": {
        "Revenue": "營業收入",
        "GrossProfit": "營業毛利",
        "OperatingExpenses": "營業費用",
        "OperatingIncome": "營業利益",
        "IncomeAfterTaxes": "本期淨利",
        "TotalConsolidatedProfitForThePeriod": "本期淨利",
        "EquityAttributableToOwnersOfParent": "歸屬於母公司業主之本期淨利",
        "EPS": "EPS",
        "SellingExpenses": "推銷費用",
        "SalesAndMarketingExpenses": "推銷費用",
        "AdministrativeExpenses": "管理費用",
        "GeneralAndAdministrativeExpenses": "管理費用",
        "ResearchAndDevelopmentExpenses": "研究發展費用",
    },
    "balance_sheet": {
        "CashAndCashEquivalents": "現金及約當現金",
        "Inventories": "存貨",
        "CurrentAssets": "流動資產合計",
        "CurrentLiabilities": "流動負債合計",
        "Liabilities": "負債總額",
        "TotalAssets": "資產總額",
        "Equity": "權益總額",
        "EquityAttributableToOwnersOfParent": "股東權益總額",
    },
    "cash_flow": {
        "CashFlowsFromOperatingActivities": "營業活動之淨現金流入(出)",
        "NetCashInflowFromOperatingActivities": "營業活動之淨現金流入(出)",
        "CashProvidedByInvestingActivities": "投資活動之淨現金流入(出)",
        "CashFlowsProvidedFromFinancingActivities": "融資活動之淨現金流入(出)",
        "PropertyAndPlantAndEquipment": "不動產、廠房及設備",
        "CashDividendsPaid": "發放現金股利",
        "DividendsPaid": "發放現金股利",
    },
}

FINMIND_FIELD_PRIORITIES = {
    "cash_flow": {
        "CashFlowsFromOperatingActivities": 1,
        "NetCashInflowFromOperatingActivities": 2,
    }
}

FINMIND_MONEY_FIELDS = {
    "營業收入",
    "營業毛利",
    "營業費用",
    "推銷費用",
    "管理費用",
    "研究發展費用",
    "營業利益",
    "本期淨利",
    "歸屬於母公司業主之本期淨利",
    "現金及約當現金",
    "存貨",
    "流動資產合計",
    "流動負債合計",
    "負債總額",
    "資產總額",
    "權益總額",
    "股東權益總額",
    "營業活動之淨現金流入(出)",
    "投資活動之淨現金流入(出)",
    "融資活動之淨現金流入(出)",
    "不動產、廠房及設備",
    "發放現金股利",
}


def finmind_headers() -> dict[str, str]:
    headers = {
        "Accept": "application/json",
        "User-Agent": "daily-news-stock-analysis/1.0",
    }
    token = os.environ.get("FINMIND_TOKEN") or os.environ.get("FINMIND_API_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def finmind_dataset_url(dataset_key: str, stock_id: str, start_date: str) -> str:
    query = urllib.parse.urlencode(
        {
            "dataset": FINMIND_DATASETS[dataset_key],
            "data_id": stock_id,
            "start_date": start_date,
        }
    )
    return f"{FINMIND_API_URL}?{query}"


def fetch_finmind_dataset(dataset_key: str, stock_id: str, start_date: str) -> list[dict[str, Any]]:
    url = finmind_dataset_url(dataset_key, stock_id, start_date)
    payload = read_json(url, headers=finmind_headers())
    status = str(payload.get("status", ""))
    if status != "200":
        message = payload.get("msg") or payload.get("message") or "unknown error"
        raise StockAnalysisError(f"FinMind {FINMIND_DATASETS[dataset_key]} 取得失敗：{message}")
    rows = payload.get("data") or []
    if not rows:
        raise StockAnalysisError(f"FinMind {FINMIND_DATASETS[dataset_key]} 沒有 {stock_id} 的可用資料。")
    return rows


def period_from_date(value: Any) -> str | None:
    if not value:
        return None
    try:
        date_value = dt.date.fromisoformat(str(value)[:10])
    except ValueError:
        return None
    quarter = (date_value.month - 1) // 3 + 1
    if quarter < 1 or quarter > 4:
        return None
    return f"{date_value.year}Q{quarter}"


def quarter_number(period: str) -> int:
    normalized = normalize_financial_period(period)
    if not QUARTER_PERIOD_PATTERN.fullmatch(normalized):
        return 0
    return int(normalized[-1])


def field_from_finmind_row(dataset_key: str, row: dict[str, Any]) -> str | None:
    row_type = str(row.get("type") or "")
    if row_type.endswith("_per"):
        return None

    mapped = FINMIND_FIELD_MAPPINGS.get(dataset_key, {}).get(row_type)
    if mapped:
        return mapped

    origin = str(row.get("origin_name") or "")
    if dataset_key == "income_statement":
        if "營業收入" in origin:
            return "營業收入"
        if "營業毛利" in origin:
            return "營業毛利"
        if "推銷費用" in origin or "銷售費用" in origin:
            return "推銷費用"
        if "管理費用" in origin:
            return "管理費用"
        if "研究發展費用" in origin or "研發費用" in origin:
            return "研究發展費用"
        if "營業費用" in origin:
            return "營業費用"
        if "營業利益" in origin:
            return "營業利益"
        if "歸屬於母公司業主" in origin and "淨利" in origin:
            return "歸屬於母公司業主之本期淨利"
        if "本期淨利" in origin:
            return "本期淨利"
        if "每股盈餘" in origin or "EPS" in row_type.upper():
            return "EPS"
    elif dataset_key == "balance_sheet":
        if "現金及約當現金" in origin:
            return "現金及約當現金"
        if "存貨" in origin:
            return "存貨"
        if "流動資產" in origin and "非流動" not in origin:
            return "流動資產合計"
        if "流動負債" in origin and "非流動" not in origin:
            return "流動負債合計"
        if "負債總" in origin:
            return "負債總額"
        if "資產總" in origin:
            return "資產總額"
        if "權益總" in origin:
            return "權益總額"
        if "股東權益" in origin or "母公司業主之權益" in origin:
            return "股東權益總額"
    elif dataset_key == "cash_flow":
        if "營業活動" in origin and ("現金流入" in origin or "現金流量" in origin):
            return "營業活動之淨現金流入(出)"
        if "投資活動" in origin and ("現金流入" in origin or "現金流量" in origin):
            return "投資活動之淨現金流入(出)"
        if ("籌資活動" in origin or "融資活動" in origin) and ("現金流入" in origin or "現金流量" in origin):
            return "融資活動之淨現金流入(出)"
        if "取得不動產" in origin or "不動產、廠房及設備" in origin or "固定資產" in origin:
            return "不動產、廠房及設備"
        if "現金股利" in origin:
            return "發放現金股利"
    return None


def finmind_value_to_table_value(field: str, value: Any) -> float | None:
    parsed = parse_number(value)
    if parsed is None:
        return None
    if field == "EPS":
        return parsed
    if field in FINMIND_MONEY_FIELDS:
        return parsed / 100_000_000
    return parsed


def finmind_rows_to_table(dataset_key: str, rows: list[dict[str, Any]]) -> dict[str, dict[str, float | None]]:
    table: dict[str, dict[str, float | None]] = {}
    priorities: dict[str, dict[str, int]] = {}
    for row in rows:
        period = period_from_date(row.get("date"))
        field = field_from_finmind_row(dataset_key, row)
        if not period or not field:
            continue
        value = finmind_value_to_table_value(field, row.get("value"))
        if value is None:
            continue

        row_type = str(row.get("type") or "")
        priority = FINMIND_FIELD_PRIORITIES.get(dataset_key, {}).get(row_type, 100)
        previous_priority = priorities.setdefault(field, {}).get(period, 999)
        if priority <= previous_priority:
            table.setdefault(field, {})[period] = value
            priorities[field][period] = priority
    return table


def table_periods(table: dict[str, dict[str, float | None]]) -> list[str]:
    periods = {
        normalize_financial_period(period)
        for values in table.values()
        for period in values
        if QUARTER_PERIOD_PATTERN.fullmatch(normalize_financial_period(period))
    }
    return sorted(periods, key=financial_period_sort_key, reverse=True)


def cash_flow_quarterly_from_cumulative(
    cumulative: dict[str, dict[str, float | None]],
) -> dict[str, dict[str, float | None]]:
    quarterly: dict[str, dict[str, float | None]] = {}
    for field, values in cumulative.items():
        converted: dict[str, float | None] = {}
        for period in sorted(values, key=financial_period_sort_key):
            quarter = quarter_number(period)
            current = values.get(period)
            if current is None:
                converted[period] = None
                continue
            if quarter <= 1:
                converted[period] = current
                continue
            previous_period = f"{period[:4]}Q{quarter - 1}"
            previous = values.get(previous_period)
            converted[period] = current - previous if previous is not None else current
        quarterly[field] = converted
    return quarterly


def aggregate_annual_table(
    dataset_key: str,
    quarterly: dict[str, dict[str, float | None]],
    cumulative: dict[str, dict[str, float | None]] | None = None,
) -> dict[str, dict[str, float | None]]:
    annual: dict[str, dict[str, float | None]] = {}
    source = cumulative if dataset_key == "cash_flow" and cumulative is not None else quarterly
    years = sorted(
        {
            period[:4]
            for values in source.values()
            for period in values
            if QUARTER_PERIOD_PATTERN.fullmatch(normalize_financial_period(period))
        },
        reverse=True,
    )
    for field, values in source.items():
        for year in years:
            if dataset_key == "balance_sheet" or dataset_key == "cash_flow":
                value = values.get(f"{year}Q4")
                if value is not None:
                    annual.setdefault(field, {})[year] = value
                continue

            quarter_values = [values.get(f"{year}Q{quarter}") for quarter in range(1, 5)]
            if all(value is not None for value in quarter_values):
                annual.setdefault(field, {})[year] = sum(value for value in quarter_values if value is not None)
    return annual


def annual_years(*tables: dict[str, dict[str, float | None]]) -> list[str]:
    year_sets: list[set[str]] = []
    for table in tables:
        years = {
            period
            for values in table.values()
            for period, value in values.items()
            if YEAR_PERIOD_PATTERN.fullmatch(period) and value is not None
        }
        year_sets.append(years)
    if not year_sets:
        return []
    common = set.intersection(*year_sets)
    return sorted(common, key=lambda item: int(item), reverse=True)


def official_financial_urls(market: str, report: str) -> list[str]:
    market_key = (market or "").upper()
    if market_key == "TWSE":
        prefix = f"{TWSE_OFFICIAL_BASE_URL}/t187ap06_L" if report == "income" else f"{TWSE_OFFICIAL_BASE_URL}/t187ap07_L"
        return [f"{prefix}_{variant}" for variant in OFFICIAL_REPORT_VARIANTS]
    if market_key == "TPEX":
        prefix = f"{TPEX_OFFICIAL_BASE_URL}/mopsfin_t187ap06_O" if report == "income" else f"{TPEX_OFFICIAL_BASE_URL}/mopsfin_t187ap07_O"
        return [f"{prefix}_{variant}" for variant in OFFICIAL_REPORT_VARIANTS]
    return []


def official_stock_code(row: dict[str, Any]) -> str:
    return str(row.get("公司代號") or row.get("SecuritiesCompanyCode") or "").strip()


def official_period(row: dict[str, Any]) -> str | None:
    raw_year = parse_number(row.get("年度") or row.get("Year"))
    raw_quarter = parse_number(row.get("季別") or row.get("Season"))
    if raw_year is None or raw_quarter is None:
        return None
    year = int(raw_year)
    if year < 1911:
        year += 1911
    quarter = int(raw_quarter)
    if quarter < 1 or quarter > 4:
        return None
    return f"{year}Q{quarter}"


def official_amount_to_billion(value: Any) -> float | None:
    parsed = parse_number(value)
    return parsed / 100_000 if parsed is not None else None


def official_find_row(stock_id: str, urls: list[str]) -> tuple[dict[str, Any] | None, str]:
    for url in urls:
        try:
            rows = read_json(url)
        except Exception:
            continue
        if not isinstance(rows, list):
            continue
        row = next((item for item in rows if official_stock_code(item) == stock_id), None)
        if row:
            return row, url
    return None, ""


def official_snapshot_from_row(kind: str, row: dict[str, Any], url: str) -> dict[str, Any]:
    period = official_period(row)
    values: dict[str, float | None] = {}
    if kind == "income":
        values = {
            "revenue": official_amount_to_billion(row.get("營業收入")),
            "gross_profit": official_amount_to_billion(row.get("營業毛利（毛損）") or row.get("營業毛利")),
            "operating_income": official_amount_to_billion(row.get("營業利益（損失）") or row.get("營業利益")),
            "net_income": official_amount_to_billion(
                row.get("淨利（淨損）歸屬於母公司業主")
                or row.get("歸屬於母公司業主之淨利（淨損）")
                or row.get("本期淨利（淨損）")
            ),
            "eps": parse_number(row.get("基本每股盈餘（元）") or row.get("基本每股盈餘")),
        }
    elif kind == "balance":
        values = {
            "current_assets": official_amount_to_billion(row.get("流動資產") or row.get("流動資產合計")),
            "current_liabilities": official_amount_to_billion(row.get("流動負債") or row.get("流動負債合計")),
            "assets": official_amount_to_billion(row.get("資產總計") or row.get("資產總額")),
            "liabilities": official_amount_to_billion(row.get("負債總計") or row.get("負債總額")),
            "equity": official_amount_to_billion(
                row.get("歸屬於母公司業主之權益合計") or row.get("權益總計") or row.get("權益總額")
            ),
        }
    return {
        "period": period,
        "url": url,
        "values": {key: value for key, value in values.items() if value is not None},
    }


def fetch_official_financial_snapshot(stock: dict[str, Any]) -> dict[str, Any]:
    stock_id = stock["code"]
    market = stock.get("market") or ""
    income_row, income_url = official_find_row(stock_id, official_financial_urls(market, "income"))
    balance_row, balance_url = official_find_row(stock_id, official_financial_urls(market, "balance"))
    market_key = market.upper()
    source_name = "TWSE OpenAPI" if market_key == "TWSE" else "TPEx OpenAPI" if market_key == "TPEX" else "TWSE/TPEx OpenAPI"
    snapshot: dict[str, Any] = {
        "source": source_name,
        "income": official_snapshot_from_row("income", income_row, income_url) if income_row else None,
        "balance": official_snapshot_from_row("balance", balance_row, balance_url) if balance_row else None,
    }
    periods = [
        item.get("period")
        for item in (snapshot.get("income"), snapshot.get("balance"))
        if item and item.get("period")
    ]
    snapshot["period"] = sorted(periods, key=financial_period_sort_key, reverse=True)[0] if periods else None
    snapshot["available"] = bool(periods)
    return snapshot


def cumulative_metric(metrics: dict[str, dict[str, float | None]], period: str, key: str) -> float | None:
    quarter = quarter_number(period)
    if quarter <= 0:
        return None
    values = [metric(metrics, f"{period[:4]}Q{item}", key) for item in range(1, quarter + 1)]
    if any(value is None for value in values):
        return None
    return sum(value for value in values if value is not None)


def verify_official_financials(
    stock: dict[str, Any],
    quarterly_metrics: dict[str, dict[str, float | None]],
    available_periods: list[str],
    official_snapshot: dict[str, Any] | None,
) -> dict[str, Any]:
    if not official_snapshot or not official_snapshot.get("available"):
        return {
            "status": "unavailable",
            "message": "尚未從 TWSE/TPEX 官方 OpenAPI 找到可比對的最新財報資料。",
            "checks": [],
        }

    checks: list[dict[str, Any]] = []
    labels = {
        "revenue": "營業收入",
        "gross_profit": "營業毛利",
        "operating_income": "營業利益",
        "net_income": "母公司淨利",
        "eps": "EPS",
        "current_assets": "流動資產",
        "current_liabilities": "流動負債",
        "assets": "資產總額",
        "liabilities": "負債總額",
        "equity": "權益總額",
    }

    for group, cumulative in (("income", True), ("balance", False)):
        official_group = official_snapshot.get(group) or {}
        official_period = official_group.get("period")
        if not official_period or official_period not in available_periods:
            continue
        for key, official_value in (official_group.get("values") or {}).items():
            finmind_value = (
                cumulative_metric(quarterly_metrics, official_period, key)
                if cumulative
                else metric(quarterly_metrics, official_period, key)
            )
            if official_value is None or finmind_value is None:
                continue
            diff = finmind_value - official_value
            diff_pct = diff / abs(official_value) * 100 if official_value else 0.0
            checks.append(
                {
                    "field": labels.get(key, key),
                    "period": official_period,
                    "finmind": finmind_value,
                    "official": official_value,
                    "diff": diff,
                    "diff_pct": diff_pct,
                    "pass": abs(diff_pct) <= 2 or abs(diff) <= 0.05,
                    "source_url": official_group.get("url") or "",
                }
            )

    failed = [item for item in checks if not item["pass"]]
    if failed:
        fields = "、".join(item["field"] for item in failed[:5])
        return {
            "status": "warn",
            "message": f"FinMind 與官方 OpenAPI 有 {len(failed)} 個欄位差異超過 2%：{fields}。",
            "checks": checks,
        }
    if checks:
        return {
            "status": "pass",
            "message": f"已用 {official_snapshot.get('source')} 核對 {len(checks)} 個最新累計/季末欄位，差異在容許範圍內。",
            "checks": checks,
        }
    return {
        "status": "partial",
        "message": "已找到官方財報端點，但沒有與 FinMind 共同期間或共同欄位可自動比對。",
        "checks": [],
    }


def fetch_financials(stock_id: str, stock: dict[str, Any] | None = None) -> dict[str, Any]:
    start_date = (now_taipei().date() - dt.timedelta(days=FINMIND_LOOKBACK_YEARS * 366)).isoformat()
    income_rows = fetch_finmind_dataset("income_statement", stock_id, start_date)
    balance_rows = fetch_finmind_dataset("balance_sheet", stock_id, start_date)
    cash_flow_rows = fetch_finmind_dataset("cash_flow", stock_id, start_date)

    quarterly_income = finmind_rows_to_table("income_statement", income_rows)
    quarterly_balance = finmind_rows_to_table("balance_sheet", balance_rows)
    cash_flow_cumulative = finmind_rows_to_table("cash_flow", cash_flow_rows)
    quarterly_cash_flow = cash_flow_quarterly_from_cumulative(cash_flow_cumulative)

    annual_income = aggregate_annual_table("income_statement", quarterly_income)
    annual_balance = aggregate_annual_table("balance_sheet", quarterly_balance)
    annual_cash_flow = aggregate_annual_table("cash_flow", quarterly_cash_flow, cumulative=cash_flow_cumulative)
    years = annual_years(annual_income, annual_balance, annual_cash_flow)
    if not years:
        raise StockAnalysisError("FinMind 財報資料不足，無法組成共同年度的損益表、資產負債表與現金流量表。")

    quarterly_periods_by_report = [
        table_periods(quarterly_income),
        table_periods(quarterly_balance),
        table_periods(quarterly_cash_flow),
    ]
    latest_quarter, comparison_quarter, available_quarters = select_latest_quarter(quarterly_periods_by_report)
    selected_quarters = [latest_quarter]
    if comparison_quarter:
        selected_quarters.append(comparison_quarter)

    quarterly = {
        "income_statement": quarterly_income,
        "balance_sheet": quarterly_balance,
        "cash_flow": quarterly_cash_flow,
        "periods": selected_quarters,
        "available_periods": available_quarters,
        "latest_period": latest_quarter,
        "comparison_period": comparison_quarter,
        "notes": [
            "FinMind 損益表採單季值；年度損益由四季相加。",
            "FinMind 現金流量表採年初至該季累計值；本工具已轉為單季差額，年度現金流採 Q4 累計值。",
            "EPS 年度值由四季 EPS 加總，遇除權、股本變動時仍需以公司公告核對。",
        ],
    }

    reports: dict[str, Any] = {
        "income_statement": annual_income,
        "balance_sheet": annual_balance,
        "cash_flow": annual_cash_flow,
        "years": years,
        "quarterly": quarterly,
        "company_name": "",
        "data_source": "FinMind API",
        "source_notes": quarterly["notes"],
        "finmind_urls": {
            key: finmind_dataset_url(key, stock_id, start_date) for key in FINMIND_DATASETS
        },
    }
    if stock:
        reports["official_snapshot"] = fetch_official_financial_snapshot(stock)
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


def compute_metrics(
    financials: dict[str, Any],
    periods: list[str] | None = None,
) -> dict[str, dict[str, float | None]]:
    income = financials["income_statement"]
    balance = financials["balance_sheet"]
    cash_flow = financials["cash_flow"]
    periods = periods if periods is not None else financials["years"][:3]
    metrics: dict[str, dict[str, float | None]] = {}

    for period in periods:
        revenue = table_value(income, period, ["營業收入合計", "營業收入"], ["率"])
        gross_profit = table_value(income, period, ["營業毛利", "毛利"], ["率"])
        selling = table_value(income, period, ["推銷費用", "銷售費用"])
        admin = table_value(income, period, ["管理費用"])
        research = table_value(income, period, ["研究發展費用", "研發費用"])
        operating_income = table_value(income, period, ["營業利益", "營業利益(損失)", "營業利益（損失）"], ["率"])
        net_income = table_value(income, period, ["歸屬於母公司業主之本期淨利", "稅後淨利", "本期淨利"], ["率"])
        eps = table_value(income, period, ["每股稅後盈餘", "每股盈餘", "EPS"])

        current_assets = table_value(balance, period, ["流動資產合計", "流動資產總額"])
        current_liabilities = table_value(balance, period, ["流動負債合計", "流動負債總額"])
        liabilities = table_value(balance, period, ["負債總額", "負債總計"])
        assets = table_value(balance, period, ["資產總額", "資產總計"])
        equity = table_value(balance, period, ["股東權益總額", "權益總額"])
        cash = table_value(balance, period, ["現金及約當現金", "現金"])
        inventory = table_value(balance, period, ["存貨"])

        operating_cf = table_value(cash_flow, period, ["營業活動之淨現金流入(出)", "營業活動之淨現金流入"])
        investing_cf = table_value(cash_flow, period, ["投資活動之淨現金流入(出)", "投資活動之淨現金流入"])
        financing_cf = table_value(cash_flow, period, ["融資活動之淨現金流入(出)", "融資活動之淨現金流入"])
        capex = table_value(cash_flow, period, ["固定資產(增加)減少", "固定資產（增加）減少", "不動產、廠房及設備"])
        dividends = table_value(cash_flow, period, ["發放現金股利", "現金股利"])
        expense_values = [selling, admin, research]
        operating_expenses = (
            sum(value for value in expense_values if value is not None)
            if any(value is not None for value in expense_values)
            else table_value(income, period, ["營業費用"], ["率"])
        )

        metrics[period] = {
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


def build_metadata(
    stock: dict[str, Any],
    years: list[str],
    quarterly_periods: list[str],
    fetched_at: str,
    financials: dict[str, Any] | None = None,
    market_data: dict[str, Any] | None = None,
) -> dict[str, Any]:
    stock_id = stock["code"]
    finmind_urls = (financials or {}).get("finmind_urls", {})
    return {
        "fetched_at": fetched_at,
        "source": "FinMind API, TWSE MIS, TWSE OpenAPI, TPEx OpenAPI, 公開資訊觀測站",
        "source_urls": {
            "finmind_fundamental": FINMIND_FUNDAMENTAL_URL,
            "finmind_income_statement": finmind_urls.get("income_statement") or finmind_dataset_url("income_statement", stock_id, "2018-01-01"),
            "finmind_balance_sheet": finmind_urls.get("balance_sheet") or finmind_dataset_url("balance_sheet", stock_id, "2018-01-01"),
            "finmind_cash_flow": finmind_urls.get("cash_flow") or finmind_dataset_url("cash_flow", stock_id, "2018-01-01"),
            "twse_income_statement": f"{TWSE_OFFICIAL_BASE_URL}/t187ap06_L_ci",
            "twse_balance_sheet": f"{TWSE_OFFICIAL_BASE_URL}/t187ap07_L_ci",
            "tpex_income_statement": f"{TPEX_OFFICIAL_BASE_URL}/mopsfin_t187ap06_O_ci",
            "tpex_balance_sheet": f"{TPEX_OFFICIAL_BASE_URL}/mopsfin_t187ap07_O_ci",
            "quote": stock.get("source_url") or "",
            "quote_api": stock.get("quote_api_url") or "",
            "price_history": (market_data or {}).get("history_url") or "",
            "mops_listed": f"https://mops.twse.com.tw/mops/web/t05st01?step=1&co_id={stock_id}&TYPEK=sii",
            "mops_otc": f"https://mops.twse.com.tw/mops/web/t05st01?step=1&co_id={stock_id}&TYPEK=otc",
        },
        "years_covered": years,
        "quarters_covered": quarterly_periods,
        "currency": "TWD 億元；股價為 TWD",
        "source_notes": (financials or {}).get("source_notes", []),
        "disclaimer": "僅供財務研究與學習參考，不構成投資建議。",
    }


def metric(metrics: dict[str, dict[str, float | None]], year: str, key: str) -> float | None:
    return metrics.get(year, {}).get(key)


def compare_text(metrics: dict[str, dict[str, float | None]], years: list[str], key: str, suffix: str = "%") -> str:
    if len(years) < 2:
        return "缺少前期比較"
    latest, previous = years[0], years[1]
    change = year_over_year(metric(metrics, latest, key), metric(metrics, previous, key))
    return f"較 {display_financial_period(previous)} {fmt_delta(change, suffix=suffix)}"


def point_delta_text(metrics: dict[str, dict[str, float | None]], years: list[str], key: str) -> str:
    if len(years) < 2:
        return "缺少前期比較"
    latest, previous = years[0], years[1]
    latest_value = metric(metrics, latest, key)
    previous_value = metric(metrics, previous, key)
    if latest_value is None or previous_value is None:
        return "缺少前期比較"
    delta = latest_value - previous_value
    return f"較 {display_financial_period(previous)} {delta:+.1f} 個百分點"


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
            f"{stock.get('quote_kind') or '最新公開報價'}為 {fmt_number(stock.get('close'), 2)} 元，"
            f"時間 {stock.get('quote_time') or stock.get('date') or '未標示'}，"
            f"較昨收 {fmt_delta(stock.get('change'), 2, ' 元')}（{fmt_delta(stock.get('change_percent'), 2)}）。"
        )

    return {
        "snapshot": [
            quote_line,
            f"最近財報年度 {display_financial_period(latest)}營收 {fmt_number(latest_metrics.get('revenue'), 0)} 億元，{compare_text(metrics, years, 'revenue')}。",
            f"{display_financial_period(latest)}EPS 為 {fmt_number(latest_metrics.get('eps'), 2)} 元，ROE 為 {fmt_number(latest_metrics.get('roe'), 1, '%')}。",
        ],
        "operations": [
            f"{display_financial_period(latest)}毛利率 {fmt_number(latest_metrics.get('gross_margin'), 1, '%')}，{point_delta_text(metrics, years, 'gross_margin')}。",
            f"營業利益率 {fmt_number(latest_metrics.get('op_margin'), 1, '%')}，三費率合計 {fmt_number(latest_metrics.get('opex_ratio'), 1, '%')}。",
            f"營收年增率 {fmt_delta(revenue_growth)}，請搭配產業循環與價格假設解讀。",
        ],
        "profit": [
            f"{display_financial_period(latest)}稅後淨利 {fmt_number(latest_metrics.get('net_income'), 0)} 億元，年增率 {fmt_delta(net_growth)}。",
            f"淨利率 {fmt_number(latest_metrics.get('net_margin'), 1, '%')}，{point_delta_text(metrics, years, 'net_margin')}。",
            f"ROA 為 {fmt_number(latest_metrics.get('roa'), 1, '%')}，用來觀察資產投入是否有效轉成獲利。",
        ],
        "financial": [
            f"流動比率 {fmt_number(latest_metrics.get('current_ratio'), 1, '%')}，負債比率 {fmt_number(latest_metrics.get('debt_ratio'), 1, '%')}。",
            f"營業現金流 {fmt_number(latest_metrics.get('operating_cf'), 0)} 億元，年增率 {fmt_delta(op_cf_growth)}。",
            f"自由現金流估算 {fmt_number(latest_metrics.get('free_cash_flow'), 0)} 億元；資本支出使用 FinMind 現金流量表「取得不動產、廠房及設備」欄位作代理。",
        ],
    }


def build_quarterly_insights(
    metrics: dict[str, dict[str, float | None]],
    periods: list[str],
) -> list[str]:
    latest = periods[0]
    latest_metrics = metrics[latest]
    latest_label = display_financial_period(latest)
    if len(periods) < 2:
        return [
            f"最新共同季報為 {latest_label}，但該公司沒有可用的去年同季資料。",
            f"單季營收 {fmt_number(latest_metrics.get('revenue'), 0)} 億元，EPS {fmt_number(latest_metrics.get('eps'), 2)} 元。",
        ]

    previous = periods[1]
    previous_metrics = metrics[previous]
    previous_label = display_financial_period(previous)
    revenue_growth = year_over_year(latest_metrics.get("revenue"), previous_metrics.get("revenue"))
    net_growth = year_over_year(latest_metrics.get("net_income"), previous_metrics.get("net_income"))
    operating_cf_growth = year_over_year(latest_metrics.get("operating_cf"), previous_metrics.get("operating_cf"))
    return [
        f"系統已確認三張財報的最新共同季度為 {latest_label}，比較基準為 {previous_label}。",
        f"單季營收 {fmt_number(previous_metrics.get('revenue'), 0)} → {fmt_number(latest_metrics.get('revenue'), 0)} 億元，同比 {fmt_delta(revenue_growth)}。",
        f"單季稅後淨利 {fmt_number(previous_metrics.get('net_income'), 0)} → {fmt_number(latest_metrics.get('net_income'), 0)} 億元，同比 {fmt_delta(net_growth)}。",
        f"EPS {fmt_number(previous_metrics.get('eps'), 2)} → {fmt_number(latest_metrics.get('eps'), 2)} 元；毛利率 {fmt_number(previous_metrics.get('gross_margin'), 1, '%')} → {fmt_number(latest_metrics.get('gross_margin'), 1, '%')}。",
        f"單季營業現金流 {fmt_number(previous_metrics.get('operating_cf'), 0)} → {fmt_number(latest_metrics.get('operating_cf'), 0)} 億元，同比 {fmt_delta(operating_cf_growth)}。",
    ]


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


def render_market_overview(stock: dict[str, Any]) -> str:
    change = parse_number(stock.get("change"))
    direction = "up" if change is not None and change > 0 else "down" if change is not None and change < 0 else "flat"
    direction_mark = "▲" if direction == "up" else "▼" if direction == "down" else "■"
    quote_time = stock.get("quote_time") or stock.get("date") or "未標示"
    volume_lots = parse_number(stock.get("volume_lots"))
    volume_text = f"{fmt_number(volume_lots, 0)} 張" if volume_lots is not None else "n/a"
    return f"""
      <section class="market-overview" aria-label="最新市場行情">
        <div class="market-price-block">
          <div class="market-price-label">{html_lib.escape(stock.get('quote_kind') or '最新公開報價')}</div>
          <div class="market-price {direction}">{fmt_number(stock.get('close'), 2)}</div>
          <div class="market-change {direction}">
            {direction_mark} {fmt_delta(change, 2, ' 元')}（{fmt_delta(stock.get('change_percent'), 2)}）
          </div>
          <div class="market-time">成交時間 {html_lib.escape(str(quote_time))}</div>
        </div>
        <dl class="market-stats">
          <div><dt>開盤</dt><dd>{fmt_number(stock.get('open'), 2)}</dd></div>
          <div><dt>最高</dt><dd>{fmt_number(stock.get('high'), 2)}</dd></div>
          <div><dt>最低</dt><dd>{fmt_number(stock.get('low'), 2)}</dd></div>
          <div><dt>昨收</dt><dd>{fmt_number(stock.get('previous_close'), 2)}</dd></div>
          <div><dt>最佳買價</dt><dd>{fmt_number(stock.get('best_bid'), 2)}</dd></div>
          <div><dt>最佳賣價</dt><dd>{fmt_number(stock.get('best_ask'), 2)}</dd></div>
          <div><dt>成交量</dt><dd>{html_lib.escape(volume_text)}</dd></div>
        </dl>
      </section>
    """


def render_technical_panel(market_data: dict[str, Any]) -> str:
    warning = market_data.get("warning")
    warning_html = (
        f'<div class="technical-warning">{html_lib.escape(str(warning))}</div>' if warning else ""
    )
    return f"""
      <section class="technical-tool" aria-label="K 線與技術指標">
        <div class="technical-toolbar">
          <div class="timeframe-control" role="group" aria-label="K 線週期">
            <button class="timeframe active" type="button" data-timeframe="day">日</button>
            <button class="timeframe" type="button" data-timeframe="week">週</button>
            <button class="timeframe" type="button" data-timeframe="month">月</button>
          </div>
          <div class="indicator-controls" aria-label="技術指標">
            <label><input type="checkbox" data-indicator="ma" checked> 均線</label>
            <label><input type="checkbox" data-indicator="bollinger" checked> 布林</label>
            <label><input type="checkbox" data-indicator="volume" checked> 成交量</label>
            <label><input type="checkbox" data-indicator="macd" checked> MACD</label>
            <label><input type="checkbox" data-indicator="rsi"> RSI</label>
            <label><input type="checkbox" data-indicator="kd"> KD</label>
          </div>
        </div>
        <div id="technical-empty" class="technical-empty" hidden>目前沒有足夠的日成交資料可繪製 K 線。</div>
        {warning_html}
        <div id="technical-charts">
          <div id="ohlc-summary" class="ohlc-summary" aria-live="polite"></div>
          <div id="kline-chart" class="kline-chart" aria-label="股價 K 線圖"></div>
          <div id="indicator-legend" class="indicator-legend"></div>
          <section id="macd-panel" class="indicator-panel">
            <h3>MACD（12, 26, 9）</h3>
            <div id="macd-chart" class="indicator-chart"></div>
          </section>
          <section id="rsi-panel" class="indicator-panel" hidden>
            <h3>RSI（6, 12）</h3>
            <div id="rsi-chart" class="indicator-chart"></div>
          </section>
          <section id="kd-panel" class="indicator-panel" hidden>
            <h3>KD（9, 3, 3）</h3>
            <div id="kd-chart" class="indicator-chart"></div>
          </section>
        </div>
        <p class="technical-source">
          日線來源為 FinMind TaiwanStockPrice；當日 OHLC 與最新成交價使用 TWSE MIS 公開資訊補入。
          盤中資料可能有傳輸延遲，技術指標僅供研究參考。
        </p>
      </section>
    """


def technical_chart_script() -> str:
    return r"""
    const technicalState = {
      timeframe: "day",
      charts: [],
      observers: []
    };

    function aggregatePriceBars(rows, timeframe) {
      if (timeframe === "day") return rows.map(item => ({ ...item }));
      const groups = new Map();
      rows.forEach(item => {
        const date = new Date(item.time + "T00:00:00Z");
        let key;
        if (timeframe === "month") {
          key = item.time.slice(0, 7);
        } else {
          const day = date.getUTCDay() || 7;
          date.setUTCDate(date.getUTCDate() - day + 1);
          key = date.toISOString().slice(0, 10);
        }
        const group = groups.get(key);
        if (!group) {
          groups.set(key, { ...item });
          return;
        }
        group.time = item.time;
        group.high = Math.max(group.high, item.high);
        group.low = Math.min(group.low, item.low);
        group.close = item.close;
        group.volume = (group.volume || 0) + (item.volume || 0);
        group.intraday = Boolean(item.intraday);
      });
      return [...groups.values()].sort((a, b) => a.time.localeCompare(b.time));
    }

    function sma(values, period) {
      let total = 0;
      return values.map((value, index) => {
        total += value;
        if (index >= period) total -= values[index - period];
        return index >= period - 1 ? total / period : null;
      });
    }

    function ema(values, period) {
      const multiplier = 2 / (period + 1);
      let previous = null;
      return values.map(value => {
        previous = previous === null ? value : value * multiplier + previous * (1 - multiplier);
        return previous;
      });
    }

    function bollinger(values, period = 20, multiplier = 2) {
      const middle = sma(values, period);
      return values.map((value, index) => {
        if (index < period - 1) return { middle: null, upper: null, lower: null };
        const window = values.slice(index - period + 1, index + 1);
        const mean = middle[index];
        const variance = window.reduce((sum, item) => sum + Math.pow(item - mean, 2), 0) / period;
        const deviation = Math.sqrt(variance) * multiplier;
        return { middle: mean, upper: mean + deviation, lower: mean - deviation };
      });
    }

    function macd(values) {
      const fast = ema(values, 12);
      const slow = ema(values, 26);
      const dif = values.map((_, index) => fast[index] - slow[index]);
      const signal = ema(dif, 9);
      return dif.map((value, index) => ({ dif: value, signal: signal[index], histogram: value - signal[index] }));
    }

    function rsi(values, period) {
      const output = Array(values.length).fill(null);
      if (values.length <= period) return output;
      let gain = 0;
      let loss = 0;
      for (let index = 1; index <= period; index += 1) {
        const delta = values[index] - values[index - 1];
        gain += Math.max(delta, 0);
        loss += Math.max(-delta, 0);
      }
      let averageGain = gain / period;
      let averageLoss = loss / period;
      output[period] = averageLoss === 0 ? 100 : 100 - 100 / (1 + averageGain / averageLoss);
      for (let index = period + 1; index < values.length; index += 1) {
        const delta = values[index] - values[index - 1];
        averageGain = (averageGain * (period - 1) + Math.max(delta, 0)) / period;
        averageLoss = (averageLoss * (period - 1) + Math.max(-delta, 0)) / period;
        output[index] = averageLoss === 0 ? 100 : 100 - 100 / (1 + averageGain / averageLoss);
      }
      return output;
    }

    function stochastic(bars, period = 9) {
      let k = 50;
      let d = 50;
      return bars.map((bar, index) => {
        if (index < period - 1) return { k: null, d: null, j: null };
        const window = bars.slice(index - period + 1, index + 1);
        const high = Math.max(...window.map(item => item.high));
        const low = Math.min(...window.map(item => item.low));
        const rsv = high === low ? 50 : (bar.close - low) / (high - low) * 100;
        k = (2 * k + rsv) / 3;
        d = (2 * d + k) / 3;
        return { k, d, j: 3 * k - 2 * d };
      });
    }

    function lineData(bars, values) {
      return bars.flatMap((bar, index) => Number.isFinite(values[index]) ? [{ time: bar.time, value: values[index] }] : []);
    }

    function checkedIndicator(name) {
      return Boolean(document.querySelector(`[data-indicator="${name}"]`)?.checked);
    }

    function disposeTechnicalCharts() {
      technicalState.observers.forEach(observer => observer.disconnect());
      technicalState.charts.forEach(chartItem => chartItem.remove());
      technicalState.observers = [];
      technicalState.charts = [];
      ["kline-chart", "macd-chart", "rsi-chart", "kd-chart"].forEach(id => {
        const element = document.getElementById(id);
        if (element) element.replaceChildren();
      });
    }

    function createTechnicalChart(containerId, height, priceScaleMargins = undefined) {
      const container = document.getElementById(containerId);
      if (!container || typeof LightweightCharts === "undefined") return null;
      const chartItem = LightweightCharts.createChart(container, {
        width: Math.max(container.clientWidth, 280),
        height,
        layout: { background: { color: "#ffffff" }, textColor: "#475569" },
        grid: { vertLines: { color: "#eef2f7" }, horzLines: { color: "#e2e8f0" } },
        rightPriceScale: { borderColor: "#cbd5e1", scaleMargins: priceScaleMargins },
        timeScale: { borderColor: "#cbd5e1", timeVisible: false, rightOffset: 5 },
        crosshair: { mode: LightweightCharts.CrosshairMode.Normal },
        localization: { locale: "zh-TW" }
      });
      const observer = new ResizeObserver(entries => {
        const width = entries[0]?.contentRect.width;
        if (width) chartItem.applyOptions({ width });
      });
      observer.observe(container);
      technicalState.charts.push(chartItem);
      technicalState.observers.push(observer);
      return chartItem;
    }

    function addIndicatorLine(chartItem, bars, values, options) {
      const series = chartItem.addLineSeries({
        lineWidth: 2,
        priceLineVisible: false,
        lastValueVisible: false,
        crosshairMarkerVisible: false,
        ...options
      });
      series.setData(lineData(bars, values));
      return series;
    }

    function setRecentRange(chartItem, count, preferred) {
      chartItem.timeScale().setVisibleLogicalRange({
        from: Math.max(0, count - preferred),
        to: count + 4
      });
    }

    function renderTechnicalCharts() {
      const sourceBars = analysis.market_data?.bars || [];
      const empty = document.getElementById("technical-empty");
      const chartRoot = document.getElementById("technical-charts");
      if (!sourceBars.length || typeof LightweightCharts === "undefined") {
        if (empty) {
          empty.hidden = false;
          empty.textContent = typeof LightweightCharts === "undefined"
            ? "線圖元件載入失敗，請確認網路後重新開啟頁面。"
            : "目前沒有足夠的日成交資料可繪製 K 線。";
        }
        if (chartRoot) chartRoot.hidden = true;
        return;
      }
      if (empty) empty.hidden = true;
      if (chartRoot) chartRoot.hidden = false;
      disposeTechnicalCharts();

      const bars = aggregatePriceBars(sourceBars, technicalState.timeframe);
      const closes = bars.map(item => item.close);
      const latest = bars[bars.length - 1];
      const previous = bars[bars.length - 2];
      const delta = previous ? latest.close - previous.close : null;
      const deltaPercent = previous && previous.close ? delta / previous.close * 100 : null;
      const summary = document.getElementById("ohlc-summary");
      if (summary) {
        const sign = delta > 0 ? "+" : "";
        summary.innerHTML = `<strong>${latest.time}</strong><span>開 ${latest.open.toFixed(2)}</span><span>高 ${latest.high.toFixed(2)}</span><span>低 ${latest.low.toFixed(2)}</span><span>收 ${latest.close.toFixed(2)}</span><span>量 ${Math.round((latest.volume || 0) / 1000).toLocaleString()} 張</span><span class="${delta > 0 ? "price-up" : delta < 0 ? "price-down" : ""}">${Number.isFinite(delta) ? sign + delta.toFixed(2) : "n/a"}（${Number.isFinite(deltaPercent) ? sign + deltaPercent.toFixed(2) + "%" : "n/a"}）</span>`;
      }

      const mainHeight = window.matchMedia("(max-width: 820px)").matches ? 360 : 480;
      const mainChart = createTechnicalChart("kline-chart", mainHeight, { top: 0.08, bottom: 0.24 });
      if (!mainChart) return;
      const candleSeries = mainChart.addCandlestickSeries({
        upColor: "#ef4444",
        downColor: "#16a34a",
        borderUpColor: "#ef4444",
        borderDownColor: "#16a34a",
        wickUpColor: "#ef4444",
        wickDownColor: "#16a34a",
        priceLineVisible: true
      });
      candleSeries.setData(bars.map(({ time, open, high, low, close }) => ({ time, open, high, low, close })));

      if (checkedIndicator("volume")) {
        const volumeSeries = mainChart.addHistogramSeries({
          priceFormat: { type: "volume" },
          priceScaleId: "volume",
          priceLineVisible: false,
          lastValueVisible: false
        });
        mainChart.priceScale("volume").applyOptions({ scaleMargins: { top: 0.80, bottom: 0 } });
        volumeSeries.setData(bars.map(item => ({
          time: item.time,
          value: item.volume || 0,
          color: item.close >= item.open ? "rgba(239,68,68,.55)" : "rgba(22,163,74,.55)"
        })));
      }

      const averages = { 5: sma(closes, 5), 20: sma(closes, 20), 60: sma(closes, 60), 240: sma(closes, 240) };
      if (checkedIndicator("ma")) {
        addIndicatorLine(mainChart, bars, averages[5], { color: "#eab308", lineWidth: 2 });
        addIndicatorLine(mainChart, bars, averages[20], { color: "#d946ef", lineWidth: 2 });
        addIndicatorLine(mainChart, bars, averages[60], { color: "#06b6d4", lineWidth: 2 });
        addIndicatorLine(mainChart, bars, averages[240], { color: "#2563eb", lineWidth: 2 });
      }
      const bands = bollinger(closes);
      if (checkedIndicator("bollinger")) {
        addIndicatorLine(mainChart, bars, bands.map(item => item.upper), { color: "#0f766e", lineWidth: 1 });
        addIndicatorLine(mainChart, bars, bands.map(item => item.lower), { color: "#0f766e", lineWidth: 1 });
      }
      setRecentRange(mainChart, bars.length, technicalState.timeframe === "day" ? 90 : 70);

      const latestIndex = bars.length - 1;
      const legend = document.getElementById("indicator-legend");
      if (legend) {
        const parts = [];
        if (checkedIndicator("ma")) {
          [5, 20, 60, 240].forEach(period => {
            const value = averages[period][latestIndex];
            if (Number.isFinite(value)) parts.push(`<span>MA${period} <strong>${value.toFixed(2)}</strong></span>`);
          });
        }
        if (checkedIndicator("bollinger") && Number.isFinite(bands[latestIndex]?.upper)) {
          parts.push(`<span>布林上 ${bands[latestIndex].upper.toFixed(2)}</span>`);
          parts.push(`<span>中 ${bands[latestIndex].middle.toFixed(2)}</span>`);
          parts.push(`<span>下 ${bands[latestIndex].lower.toFixed(2)}</span>`);
        }
        legend.innerHTML = parts.join("");
      }

      const panelVisibility = {
        macd: checkedIndicator("macd"),
        rsi: checkedIndicator("rsi"),
        kd: checkedIndicator("kd")
      };
      Object.entries(panelVisibility).forEach(([name, visible]) => {
        const panel = document.getElementById(`${name}-panel`);
        if (panel) panel.hidden = !visible;
      });

      if (panelVisibility.macd) {
        const values = macd(closes);
        const chartItem = createTechnicalChart("macd-chart", 190, { top: 0.12, bottom: 0.12 });
        const histogram = chartItem.addHistogramSeries({ priceLineVisible: false, lastValueVisible: false });
        histogram.setData(bars.map((bar, index) => ({
          time: bar.time,
          value: values[index].histogram,
          color: values[index].histogram >= 0 ? "rgba(239,68,68,.68)" : "rgba(22,163,74,.68)"
        })));
        addIndicatorLine(chartItem, bars, values.map(item => item.dif), { color: "#ea580c" });
        addIndicatorLine(chartItem, bars, values.map(item => item.signal), { color: "#eab308" });
        setRecentRange(chartItem, bars.length, technicalState.timeframe === "day" ? 90 : 70);
      }

      if (panelVisibility.rsi) {
        const chartItem = createTechnicalChart("rsi-chart", 180, { top: 0.12, bottom: 0.12 });
        const rsi6 = addIndicatorLine(chartItem, bars, rsi(closes, 6), { color: "#7c3aed" });
        addIndicatorLine(chartItem, bars, rsi(closes, 12), { color: "#0ea5e9" });
        rsi6.createPriceLine({ price: 70, color: "#dc2626", lineStyle: 2, axisLabelVisible: true, title: "70" });
        rsi6.createPriceLine({ price: 30, color: "#16a34a", lineStyle: 2, axisLabelVisible: true, title: "30" });
        setRecentRange(chartItem, bars.length, technicalState.timeframe === "day" ? 90 : 70);
      }

      if (panelVisibility.kd) {
        const values = stochastic(bars);
        const chartItem = createTechnicalChart("kd-chart", 180, { top: 0.12, bottom: 0.12 });
        const kSeries = addIndicatorLine(chartItem, bars, values.map(item => item.k), { color: "#eab308" });
        addIndicatorLine(chartItem, bars, values.map(item => item.d), { color: "#d946ef" });
        addIndicatorLine(chartItem, bars, values.map(item => item.j), { color: "#06b6d4" });
        kSeries.createPriceLine({ price: 80, color: "#dc2626", lineStyle: 2, axisLabelVisible: true, title: "80" });
        kSeries.createPriceLine({ price: 20, color: "#16a34a", lineStyle: 2, axisLabelVisible: true, title: "20" });
        setRecentRange(chartItem, bars.length, technicalState.timeframe === "day" ? 90 : 70);
      }
    }

    document.querySelectorAll(".timeframe").forEach(button => {
      button.addEventListener("click", () => {
        technicalState.timeframe = button.dataset.timeframe;
        document.querySelectorAll(".timeframe").forEach(item => item.classList.toggle("active", item === button));
        renderTechnicalCharts();
      });
    });
    document.querySelectorAll("[data-indicator]").forEach(input => input.addEventListener("change", renderTechnicalCharts));
    """


def render_html(analysis: dict[str, Any]) -> str:
    stock = analysis["stock"]
    years = analysis["years"]
    metrics = analysis["metrics"]
    quarterly = analysis["quarterly"]
    quarterly_periods = quarterly["periods"]
    quarterly_metrics = quarterly["metrics"]
    metadata = analysis["metadata"]
    insights = analysis["insights"]
    latest = years[0]
    latest_quarter = quarterly_periods[0]
    latest_quarter_label = display_financial_period(latest_quarter)
    comparison_quarter_label = (
        display_financial_period(quarterly_periods[1]) if len(quarterly_periods) > 1 else "無去年同期資料"
    )
    json_payload = json.dumps(analysis, ensure_ascii=False)
    title = f"{stock['name']} ({stock['code']}) 股票分析"
    source_urls = metadata["source_urls"]
    fetched_at_display = format_taipei_time(metadata["fetched_at"])
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
    quarterly_cards = "".join(
        [
            kpi_card(
                f"{latest_quarter_label} 營收",
                f"{fmt_number(metric(quarterly_metrics, latest_quarter, 'revenue'), 0)} 億",
                compare_text(quarterly_metrics, quarterly_periods, "revenue"),
                "blue",
            ),
            kpi_card(
                "單季稅後淨利",
                f"{fmt_number(metric(quarterly_metrics, latest_quarter, 'net_income'), 0)} 億",
                compare_text(quarterly_metrics, quarterly_periods, "net_income"),
                "green",
            ),
            kpi_card(
                "單季 EPS",
                f"{fmt_number(metric(quarterly_metrics, latest_quarter, 'eps'), 2)} 元",
                compare_text(quarterly_metrics, quarterly_periods, "eps"),
                "purple",
            ),
            kpi_card(
                "單季毛利率",
                fmt_number(metric(quarterly_metrics, latest_quarter, "gross_margin"), 1, "%"),
                point_delta_text(quarterly_metrics, quarterly_periods, "gross_margin"),
                "orange",
            ),
        ]
    )

    return f"""<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html_lib.escape(title)}</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.5.0/dist/chart.umd.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/lightweight-charts@4.2.2/dist/lightweight-charts.standalone.production.js"></script>
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
    .market-overview {{
      max-width: 1180px;
      margin: 18px auto 0;
      display: grid;
      grid-template-columns: minmax(220px, .8fr) minmax(0, 1.5fr);
      gap: 18px;
      padding: 18px;
      color: var(--ink);
      background: rgba(255,255,255,.96);
      border: 1px solid rgba(255,255,255,.48);
      border-radius: 8px;
    }}
    .market-price-label {{ color: var(--muted); font-size: 13px; font-weight: 760; }}
    .market-price {{ margin-top: 4px; font-size: clamp(38px, 6vw, 58px); font-weight: 800; line-height: 1; }}
    .market-change {{ margin-top: 8px; font-weight: 760; }}
    .market-price.up, .market-change.up, .price-up {{ color: #dc2626; }}
    .market-price.down, .market-change.down, .price-down {{ color: #15803d; }}
    .market-price.flat, .market-change.flat {{ color: #475569; }}
    .market-time {{ margin-top: 8px; color: var(--muted); font-size: 12px; }}
    .market-stats {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(96px, 1fr));
      gap: 8px;
      margin: 0;
      align-content: center;
    }}
    .market-stats div {{ padding: 10px; border-left: 1px solid var(--line); }}
    .market-stats dt {{ color: var(--muted); font-size: 12px; }}
    .market-stats dd {{ margin: 4px 0 0; font-size: 18px; font-weight: 760; white-space: nowrap; }}
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
    .technical-tool {{
      background: var(--surface);
      border: 1px solid var(--line);
      border-radius: 8px;
      overflow: hidden;
      margin-bottom: 18px;
    }}
    .technical-toolbar {{ padding: 12px 14px; border-bottom: 1px solid var(--line); background: #f8fafc; }}
    .timeframe-control {{ display: inline-flex; border: 1px solid var(--line); border-radius: 8px; overflow: hidden; }}
    .timeframe {{
      min-width: 58px;
      height: 40px;
      border: 0;
      border-right: 1px solid var(--line);
      background: white;
      color: var(--muted);
      font-weight: 760;
      cursor: pointer;
    }}
    .timeframe:last-child {{ border-right: 0; }}
    .timeframe.active {{ background: var(--ink); color: white; }}
    .indicator-controls {{ display: flex; flex-wrap: wrap; gap: 8px 14px; margin-top: 12px; }}
    .indicator-controls label {{ display: inline-flex; align-items: center; gap: 5px; font-size: 13px; font-weight: 700; color: #334155; }}
    .indicator-controls input {{ width: 17px; height: 17px; accent-color: var(--blue); }}
    .ohlc-summary, .indicator-legend {{ display: flex; flex-wrap: wrap; gap: 8px 14px; padding: 10px 14px; font-size: 13px; }}
    .ohlc-summary {{ border-bottom: 1px solid var(--line); background: #fff; }}
    .indicator-legend {{ color: var(--muted); border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); }}
    .indicator-legend strong {{ color: var(--ink); }}
    .kline-chart {{ width: 100%; height: 480px; }}
    .indicator-panel {{ padding-top: 8px; border-top: 1px solid var(--line); }}
    .indicator-panel h3 {{ margin: 0; padding: 8px 14px 2px; font-size: 13px; color: #334155; }}
    .indicator-panel[hidden] {{ display: none; }}
    .indicator-chart {{ width: 100%; height: 190px; }}
    .technical-source {{ margin: 0; padding: 12px 14px; color: var(--muted); font-size: 12px; line-height: 1.55; border-top: 1px solid var(--line); }}
    .technical-empty, .technical-warning {{ padding: 18px; color: var(--muted); }}
    .technical-warning {{ background: #fff7ed; color: #9a3412; border-bottom: 1px solid #fed7aa; }}
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
      .market-overview {{ grid-template-columns: 1fr; }}
      .market-stats {{ grid-template-columns: repeat(3, minmax(0, 1fr)); }}
      .market-stats div {{ border-left: 0; border-top: 1px solid var(--line); padding-left: 0; }}
      .market-stats dd {{ font-size: 16px; }}
      .kline-chart {{ height: 360px; }}
    }}
  </style>
</head>
<body>
  <header class="hero">
    <div class="eyebrow">台灣股票財務分析 | 僅供研究參考</div>
    <h1>{html_lib.escape(stock['name'])} ({html_lib.escape(stock['code'])})</h1>
    <div class="subtitle">
      資料更新：{html_lib.escape(fetched_at_display)}；市場：{html_lib.escape(stock.get('market_label') or '未知')}；
      最新季報：{html_lib.escape(latest_quarter_label)}，同比 {html_lib.escape(comparison_quarter_label)}；
      年度財報：{html_lib.escape(' / '.join(years))}。本頁使用公開資料自動產生，請以公司公告與公開資訊觀測站核對。
    </div>
    <div class="source-row">
      <a href="{html_lib.escape(source_urls['finmind_fundamental'])}">FinMind 財報文件</a>
      <a href="{html_lib.escape(source_urls['finmind_income_statement'])}">FinMind 損益表 API</a>
      <a href="{html_lib.escape(source_urls['finmind_balance_sheet'])}">FinMind 資產負債表 API</a>
      <a href="{html_lib.escape(source_urls['finmind_cash_flow'])}">FinMind 現金流量表 API</a>
      <a href="{html_lib.escape(source_urls['twse_income_statement'])}">TWSE 官方損益</a>
      <a href="{html_lib.escape(source_urls['twse_balance_sheet'])}">TWSE 官方資產負債</a>
      <a href="{html_lib.escape(source_urls['tpex_income_statement'])}">TPEX 官方損益</a>
      <a href="{html_lib.escape(source_urls['tpex_balance_sheet'])}">TPEX 官方資產負債</a>
      <a href="{html_lib.escape(source_urls['quote'])}">TWSE 盤中行情</a>
      <a href="{html_lib.escape(source_urls['price_history'])}">FinMind 日成交資料</a>
      <a href="{html_lib.escape(source_urls['mops_listed'])}">MOPS 上市公告</a>
      <a href="{html_lib.escape(source_urls['mops_otc'])}">MOPS 上櫃公告</a>
    </div>
    {render_market_overview(stock)}
  </header>

  <nav class="tabs" aria-label="股票分析分頁">
    <button class="tab active" type="button" data-tab="snapshot">總覽</button>
    <button class="tab" type="button" data-tab="technical">技術線圖</button>
    <button class="tab" type="button" data-tab="quarterly">最新季報</button>
    <button class="tab" type="button" data-tab="operations">經營分析</button>
    <button class="tab" type="button" data-tab="profit">獲利分析</button>
    <button class="tab" type="button" data-tab="financial">財務健全度</button>
  </nav>

  <main class="layout">
    <section id="snapshot" class="tab-content active">
      <h2 class="section-title">總覽</h2>
      <div class="snapshot-grid">
        {kpi_card(stock.get('quote_kind') or "最新收盤價", f"{fmt_number(stock.get('close'), 2)} 元", f"時間 {stock.get('quote_time') or stock.get('date') or 'n/a'}；變動 {fmt_delta(stock.get('change'), 2, ' 元')}（{fmt_delta(stock.get('change_percent'), 2)}）", "blue")}
        {kpi_card(f"{latest_quarter_label} 營收", f"{fmt_number(metric(quarterly_metrics, latest_quarter, 'revenue'), 0)} 億", compare_text(quarterly_metrics, quarterly_periods, "revenue"), "green")}
        {kpi_card("最近營收年度", f"{fmt_number(metric(metrics, latest, 'revenue'), 0)} 億", compare_text(metrics, years, "revenue"), "orange")}
        {kpi_card("合理性檢查", "通過" if not sanity else f"{len(sanity)} 項提醒", "有提醒不代表資料錯誤，需人工核對", "purple")}
      </div>
      {insight_box("今日摘要", insights["snapshot"])}
      {warning_block}
    </section>

    <section id="technical" class="tab-content">
      <h2 class="section-title">K 線與技術指標</h2>
      {render_technical_panel(analysis.get('market_data') or {})}
    </section>

    <section id="quarterly" class="tab-content">
      <h2 class="section-title">最新季報同期比較</h2>
      <div class="kpi-row">{quarterly_cards}</div>
      {insight_box("最新季報重點", quarterly["insights"])}
      <div class="charts-grid">
        <article class="chart-card"><div class="chart-title">單季營收與毛利率</div><div class="chart-container"><canvas id="quarterRevenueChart"></canvas></div></article>
        <article class="chart-card"><div class="chart-title">單季淨利與淨利率</div><div class="chart-container"><canvas id="quarterProfitChart"></canvas></div></article>
      </div>
      {metric_table(quarterly_metrics, quarterly_periods, [
        ("單季營收（億元）", "revenue", "", 0),
        ("單季營業利益（億元）", "operating_income", "", 0),
        ("單季稅後淨利（億元）", "net_income", "", 0),
        ("單季 EPS（元）", "eps", "", 2),
        ("毛利率", "gross_margin", "%", 1),
        ("營業利益率", "op_margin", "%", 1),
        ("淨利率", "net_margin", "%", 1),
      ])}
      {metric_table(quarterly_metrics, quarterly_periods, [
        ("現金及約當現金（億元）", "cash", "", 0),
        ("存貨（億元）", "inventory", "", 0),
        ("資產總額（億元）", "assets", "", 0),
        ("負債比率", "debt_ratio", "%", 1),
        ("流動比率", "current_ratio", "%", 1),
        ("單季營業現金流（億元）", "operating_cf", "", 0),
        ("單季自由現金流（億元）", "free_cash_flow", "", 0),
      ])}
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
      來源：FinMind API、TWSE MIS、TWSE OpenAPI、TPEx OpenAPI、公開資訊觀測站。金額單位若未特別標示均為新台幣億元。
      本分析由程式自動整理，僅供財務研究與學習參考，不構成買賣建議或投資招攬。
      背景圖來源：Unsplash。
    </p>
  </main>

  <script>
    const analysis = {json_payload};
    const years = [...analysis.years].reverse();
    const metrics = analysis.metrics;
    const quarterPeriods = [...analysis.quarterly.periods].reverse();
    const quarterMetrics = analysis.quarterly.metrics;
    const colors = {{
      blue: "#2463eb",
      green: "#15803d",
      orange: "#c05a1a",
      purple: "#6d49b7",
      red: "#b42318",
      gray: "#64748b"
    }};
    {technical_chart_script()}
    const value = key => years.map(year => metrics[year]?.[key] ?? null);
    const quarterValue = key => quarterPeriods.map(period => quarterMetrics[period]?.[key] ?? null);
    const moneyAxis = {{ ticks: {{ callback: v => v.toLocaleString() }} }};
    const percentAxis = {{ position: "right", grid: {{ display: false }}, ticks: {{ callback: v => v + "%" }} }};

    document.querySelectorAll(".tab").forEach(button => {{
      button.addEventListener("click", () => {{
        document.querySelectorAll(".tab").forEach(item => item.classList.remove("active"));
        document.querySelectorAll(".tab-content").forEach(item => item.classList.remove("active"));
        button.classList.add("active");
        document.getElementById(button.dataset.tab).classList.add("active");
        if (button.dataset.tab === "technical") {{
          window.setTimeout(renderTechnicalCharts, 0);
        }}
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

    chart("quarterRevenueChart", {{
      type: "bar",
      data: {{ labels: quarterPeriods, datasets: [
        {{ label: "單季營收", data: quarterValue("revenue"), backgroundColor: colors.blue + "33", borderColor: colors.blue, borderWidth: 2, yAxisID: "y" }},
        {{ label: "毛利率", data: quarterValue("gross_margin"), type: "line", borderColor: colors.green, backgroundColor: colors.green, yAxisID: "y2", tension: .25, pointRadius: 4 }}
      ] }},
      options: mixedOptions()
    }});
    chart("quarterProfitChart", {{
      type: "bar",
      data: {{ labels: quarterPeriods, datasets: [
        {{ label: "單季稅後淨利", data: quarterValue("net_income"), backgroundColor: colors.green + "33", borderColor: colors.green, borderWidth: 2, yAxisID: "y" }},
        {{ label: "淨利率", data: quarterValue("net_margin"), type: "line", borderColor: colors.orange, backgroundColor: colors.orange, yAxisID: "y2", tension: .25, pointRadius: 4 }}
      ] }},
      options: mixedOptions()
    }});

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
    fetched_at_display = format_taipei_time(metadata["fetched_at"])
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
  - FinMind API
  - TWSE OpenAPI
  - TPEx OpenAPI
  - 公開資訊觀測站
---

# {stock['name']} ({stock['code']}) 股票分析

{link_line}- 產生時間：{fetched_at_display}
- 市場：{stock.get('market_label') or '未知'}
- 最新行情日期：{stock.get('date') or 'n/a'}
- 最新季報：{display_financial_period(analysis['quarterly']['periods'][0])}
- 同期比較：{display_financial_period(analysis['quarterly']['periods'][1]) if len(analysis['quarterly']['periods']) > 1 else '無去年同期資料'}
- 財報年度：{', '.join(analysis['years'])}

## 摘要

{insight_lines}

## 來源

- [FinMind 財報文件]({sources['finmind_fundamental']})
- [FinMind 損益表 API]({sources['finmind_income_statement']})
- [FinMind 資產負債表 API]({sources['finmind_balance_sheet']})
- [FinMind 現金流量表 API]({sources['finmind_cash_flow']})
- [TWSE 官方損益表]({sources['twse_income_statement']})
- [TWSE 官方資產負債表]({sources['twse_balance_sheet']})
- [TPEX 官方損益表]({sources['tpex_income_statement']})
- [TPEX 官方資產負債表]({sources['tpex_balance_sheet']})
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
    stock = enrich_stock_quote(resolve_stock(query))
    try:
        market_data = fetch_market_history(stock)
    except StockAnalysisError as exc:
        market_data = {
            "bars": [],
            "source": "盤中與歷史行情暫時無法完整取得",
            "history_url": finmind_price_url(
                stock["code"],
                (now_taipei().date() - dt.timedelta(days=PRICE_LOOKBACK_DAYS)).isoformat(),
            ),
            "intraday_url": stock.get("source_url") or "",
            "intraday_api_url": stock.get("quote_api_url") or "",
            "updated_at": stock.get("quote_time") or stock.get("date") or "",
            "warning": str(exc),
        }
    financials = fetch_financials(stock["code"], stock)
    if not stock.get("name"):
        stock["name"] = financials.get("company_name") or stock["code"]
    years = financials["years"][:3]
    if not years:
        raise StockAnalysisError("沒有可分析的年度財報資料。")

    metrics = compute_metrics(financials)
    quarterly_financials = financials["quarterly"]
    quarterly_periods = quarterly_financials["periods"]
    quarterly_metrics = compute_metrics(quarterly_financials, quarterly_periods)
    all_quarterly_metrics = compute_metrics(quarterly_financials, quarterly_financials["available_periods"])
    fetched_at = now_taipei().replace(microsecond=0).isoformat()
    metadata = build_metadata(stock, years, quarterly_periods, fetched_at, financials, market_data)
    official_verification = verify_official_financials(
        stock,
        all_quarterly_metrics,
        quarterly_financials["available_periods"],
        financials.get("official_snapshot"),
    )
    sanity = sanity_check(quarterly_metrics, quarterly_periods) + sanity_check(metrics, years)
    if official_verification["status"] != "pass":
        sanity.append(
            {
                "level": "warn",
                "field": "TWSE/TPEX 官方驗證",
                "message": official_verification["message"],
            }
        )
    verification = {
        "sanity": sanity,
        "sanity_pass": True,
        "official": official_verification,
    }
    verification["sanity_pass"] = all(item["level"] != "error" for item in verification["sanity"])

    analysis = {
        "stock": stock,
        "market_data": market_data,
        "years": years,
        "metrics": metrics,
        "quarterly": {
            "periods": quarterly_periods,
            "latest_period": quarterly_financials["latest_period"],
            "comparison_period": quarterly_financials["comparison_period"],
            "available_periods": quarterly_financials["available_periods"],
            "metrics": quarterly_metrics,
            "insights": build_quarterly_insights(quarterly_metrics, quarterly_periods),
        },
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
