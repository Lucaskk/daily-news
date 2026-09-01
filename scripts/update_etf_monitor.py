#!/usr/bin/env python3
"""Fetch tracked Taiwan ETF data and generate a GitHub Pages HTML dashboard.

The first version intentionally avoids browser-side writes to GitHub. A static
GitHub Pages page cannot safely commit config changes unless a backend or GitHub
App mediates the write. The daily job reads wiki/etf/config/tracked-etfs.json.

Data sources:
- Intraday price snapshots: TWSE MIS getStockInfo endpoint.
- ETF holdings / PCF: currently Yuanta ETF PCF bridge for Yuanta ETFs.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import html
import json
import math
import os
from pathlib import Path
import re
import sys
import time
from typing import Any
import urllib.error
import urllib.parse
import urllib.request
from zoneinfo import ZoneInfo


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
TAIPEI = ZoneInfo("Asia/Taipei")

DEFAULT_CONFIG_PATH = REPO_ROOT / "wiki/etf/config/tracked-etfs.json"
DEFAULT_OUTPUT_ROOT = REPO_ROOT / "wiki/etf"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
)

PRICE_FIELDNAMES = [
    "timestamp",
    "date",
    "etf_code",
    "etf_name",
    "market",
    "price",
    "open",
    "high",
    "low",
    "previous_close",
    "change",
    "change_pct",
    "volume",
    "latest_volume",
    "trade_time",
    "source",
    "fetched_at",
]

HOLDING_FIELDNAMES = [
    "date",
    "etf_code",
    "etf_name",
    "stock_code",
    "stock_name",
    "shares",
    "lots",
    "weight",
    "source",
    "fetched_at",
]

SUMMARY_FIELDNAMES = [
    "date",
    "etf_code",
    "etf_name",
    "fund_size",
    "nav",
    "total_assets",
    "outstanding_units",
    "stock_value",
    "futures_value",
    "etf_value",
    "bond_value",
    "update_time",
    "source",
    "fetched_at",
]


def now_taipei() -> dt.datetime:
    return dt.datetime.now(TAIPEI)


def iso_now() -> str:
    return now_taipei().replace(microsecond=0).isoformat()


def repo_relative(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch tracked ETF prices/holdings and generate HTML dashboard.",
    )
    parser.add_argument("--config", default=str(DEFAULT_CONFIG_PATH), help="Tracked ETF config JSON path.")
    parser.add_argument("--output-root", default=str(DEFAULT_OUTPUT_ROOT), help="Output root under GitHub Pages.")
    parser.add_argument("--skip-prices", action="store_true", help="Do not fetch TWSE MIS intraday prices.")
    parser.add_argument("--skip-holdings", action="store_true", help="Do not fetch ETF holdings / PCF data.")
    parser.add_argument("--report-only", action="store_true", help="Only regenerate HTML from existing CSV data.")
    parser.add_argument("--add-etf", help="Add or update an ETF in the config, for example 0056.")
    parser.add_argument("--name", default="", help="ETF name used with --add-etf.")
    parser.add_argument("--market", default="twse", choices=["twse", "tpex", "auto"], help="ETF market.")
    parser.add_argument("--provider", default="auto", choices=["auto", "yuanta", "price-only"], help="Holdings provider.")
    parser.add_argument("--disable", action="store_true", help="Disable the ETF passed to --add-etf.")
    return parser.parse_args(argv)


def normalize_code(value: Any) -> str:
    text = str(value or "").strip().upper()
    match = re.search(r"(\d{1,6})([A-Z]?)", text)
    if not match:
        return ""
    digits, suffix = match.groups()
    if len(digits) < 4:
        digits = digits.zfill(4)
    return digits + suffix


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"updated_at": iso_now()[:10], "etfs": []}
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def add_or_update_etf(args: argparse.Namespace) -> None:
    path = Path(args.config)
    config = load_json(path)
    code = normalize_code(args.add_etf)
    if not re.fullmatch(r"\d{4,6}[A-Z]?", code):
        raise SystemExit(f"Invalid ETF code: {args.add_etf}")

    etfs = config.setdefault("etfs", [])
    existing = next((item for item in etfs if normalize_code(item.get("code")) == code), None)
    payload = {
        "code": code,
        "name": args.name.strip() or (existing or {}).get("name", ""),
        "market": args.market,
        "provider": args.provider,
        "enabled": not args.disable,
        "track_intraday": True,
        "track_holdings": args.provider != "price-only",
    }
    if existing:
        existing.update(payload)
    else:
        etfs.append(payload)
    config["updated_at"] = now_taipei().date().isoformat()
    save_json(path, config)
    print(f"Updated {repo_relative(path)}: {code}")


def tracked_etfs(config: dict[str, Any]) -> list[dict[str, Any]]:
    result = []
    for raw in config.get("etfs", []):
        code = normalize_code(raw.get("code"))
        if not code or raw.get("enabled") is False:
            continue
        item = dict(raw)
        item["code"] = code
        item["name"] = str(item.get("name") or code).strip()
        item["market"] = str(item.get("market") or "auto").strip().lower()
        item["provider"] = str(item.get("provider") or "auto").strip().lower()
        item["track_intraday"] = item.get("track_intraday", True) is not False
        item["track_holdings"] = item.get("track_holdings", True) is not False
        result.append(item)
    return result


def request_text(url: str, *, referer: str = "", retries: int = 2) -> str:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json,text/plain,*/*",
        "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8",
    }
    if referer:
        headers["Referer"] = referer

    last_error: Exception | None = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as response:
                return response.read().decode("utf-8", errors="replace")
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last_error = exc
            if attempt < retries:
                time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"Request failed: {url} ({last_error})")


def request_json(url: str, *, referer: str = "", retries: int = 2) -> Any:
    text = request_text(url, referer=referer, retries=retries)
    start = text.find("{")
    if start > 0:
        text = text[start:]
    return json.loads(text)


def to_float(value: Any) -> float | None:
    text = str(value or "").strip().replace(",", "")
    if not text or text in {"-", "--", "NaN", "nan"}:
        return None
    try:
        parsed = float(text)
    except ValueError:
        return None
    return parsed if math.isfinite(parsed) else None


def float_text(value: float | int | None, digits: int = 4) -> str:
    if value is None:
        return ""
    if isinstance(value, int) or abs(value - round(value)) < 1e-9:
        return str(int(round(value)))
    return f"{value:.{digits}f}".rstrip("0").rstrip(".")


def parse_yyyymmdd(value: Any) -> str:
    digits = re.sub(r"\D", "", str(value or ""))
    if len(digits) != 8:
        return now_taipei().date().isoformat()
    return f"{digits[:4]}-{digits[4:6]}-{digits[6:8]}"


def parse_twse_timestamp(row: dict[str, Any]) -> tuple[str, str]:
    date_value = parse_yyyymmdd(row.get("d") or row.get("^"))
    trade_time = str(row.get("t") or row.get("%") or "").strip()
    if not re.fullmatch(r"\d{2}:\d{2}:\d{2}", trade_time):
        trade_time = now_taipei().strftime("%H:%M:%S")
    return f"{date_value} {trade_time}", date_value


def price_change(price: float | None, previous: float | None) -> tuple[float | None, float | None]:
    if price is None or previous in (None, 0):
        return None, None
    change = price - previous
    return change, change / previous * 100


def market_channels(etf: dict[str, Any]) -> list[str]:
    code = etf["code"]
    market = etf.get("market", "auto")
    if market in {"twse", "tse", "listed"}:
        return [f"tse_{code}.tw"]
    if market in {"tpex", "otc"}:
        return [f"otc_{code}.tw"]
    return [f"tse_{code}.tw", f"otc_{code}.tw"]


def fetch_intraday_prices(etfs: list[dict[str, Any]]) -> tuple[list[dict[str, str]], dict[str, str]]:
    tracked = [item for item in etfs if item.get("track_intraday", True)]
    if not tracked:
        return [], {}

    code_to_etf = {item["code"]: item for item in tracked}
    channels = []
    for item in tracked:
        channels.extend(market_channels(item))

    params = {
        "ex_ch": "|".join(channels),
        "json": "1",
        "delay": "0",
        "_": str(int(time.time() * 1000)),
    }
    url = "https://mis.twse.com.tw/stock/api/getStockInfo.jsp?" + urllib.parse.urlencode(params)
    payload = request_json(url, referer="https://mis.twse.com.tw/stock/index.jsp")

    best_by_code: dict[str, dict[str, Any]] = {}
    for row in payload.get("msgArray", []):
        code = normalize_code(row.get("c"))
        if code not in code_to_etf:
            continue
        price = to_float(row.get("z")) or to_float(row.get("pz"))
        current = best_by_code.get(code)
        if current is None:
            best_by_code[code] = row
            continue
        current_price = to_float(current.get("z")) or to_float(current.get("pz"))
        if price is not None and current_price is None:
            best_by_code[code] = row

    fetched_at = iso_now()
    rows: list[dict[str, str]] = []
    missing: dict[str, str] = {}
    for code, etf in code_to_etf.items():
        raw = best_by_code.get(code)
        if not raw:
            missing[code] = "TWSE MIS returned no quote"
            continue
        timestamp, date_value = parse_twse_timestamp(raw)
        price = to_float(raw.get("z")) or to_float(raw.get("pz"))
        previous = to_float(raw.get("y"))
        change, change_pct = price_change(price, previous)
        rows.append({
            "timestamp": timestamp,
            "date": date_value,
            "etf_code": code,
            "etf_name": str(etf.get("name") or raw.get("n") or code),
            "market": str(raw.get("ex") or etf.get("market") or ""),
            "price": float_text(price),
            "open": float_text(to_float(raw.get("o"))),
            "high": float_text(to_float(raw.get("h"))),
            "low": float_text(to_float(raw.get("l"))),
            "previous_close": float_text(previous),
            "change": float_text(change),
            "change_pct": float_text(change_pct),
            "volume": float_text(to_float(raw.get("v")), digits=0),
            "latest_volume": float_text(to_float(raw.get("tv")), digits=0),
            "trade_time": str(raw.get("t") or ""),
            "source": "TWSE MIS",
            "fetched_at": fetched_at,
        })
    return rows, missing


def yuanta_pcf_url(code: str) -> str:
    params = {
        "APIType": "ETFAPI",
        "CompanyName": "YUANTAFUNDS",
        "PageName": f"/mrFund/fund/{code}/detail",
        "DeviceId": "null",
        "FuncId": "PCF/Daily",
        "AppName": "ETF",
        "Device": "3",
        "Platform": "ETF",
        "ticker": code,
    }
    return "https://api.yuantafunds.com/ectranslation/api/bridge?" + urllib.parse.urlencode(params)


def fetch_yuanta_holdings(etf: dict[str, Any]) -> tuple[list[dict[str, str]], dict[str, str], dict[str, Any]]:
    code = etf["code"]
    payload = request_json(yuanta_pcf_url(code), referer="https://www.yuantafunds.com/")
    pcf = payload.get("PCF") or {}
    weights = payload.get("FundWeights") or {}
    stock_weights = weights.get("StockWeights") or []
    summary = weights.get("Summary") or {}

    if not pcf or not stock_weights:
        raise RuntimeError("Yuanta PCF returned no stock holdings")

    date_value = parse_yyyymmdd(pcf.get("trandate"))
    etf_name = str(etf.get("name") or pcf.get("fundname") or code)
    fetched_at = iso_now()

    holding_rows = []
    for item in stock_weights:
        stock_code = normalize_code(item.get("code"))
        shares = to_float(item.get("qty"))
        weight = to_float(item.get("weights"))
        if not stock_code or shares is None:
            continue
        holding_rows.append({
            "date": date_value,
            "etf_code": code,
            "etf_name": etf_name,
            "stock_code": stock_code,
            "stock_name": str(item.get("name") or stock_code),
            "shares": float_text(shares, digits=0),
            "lots": float_text(shares / 1000, digits=3),
            "weight": float_text(weight),
            "source": "Yuanta PCF",
            "fetched_at": fetched_at,
        })

    summary_row = {
        "date": date_value,
        "etf_code": code,
        "etf_name": etf_name,
        "fund_size": float_text(to_float(summary.get("fundsize")) or to_float(pcf.get("totalav")), digits=0),
        "nav": float_text(to_float(pcf.get("nav"))),
        "total_assets": float_text(to_float(pcf.get("totalav")), digits=0),
        "outstanding_units": float_text(to_float(pcf.get("osunit")), digits=0),
        "stock_value": float_text(to_float(summary.get("stkvalues")), digits=0),
        "futures_value": float_text(to_float(summary.get("futvalues")), digits=0),
        "etf_value": float_text(to_float(summary.get("etfvalues")), digits=0),
        "bond_value": float_text(to_float(summary.get("bndvalues")), digits=0),
        "update_time": str(pcf.get("upddate") or ""),
        "source": "Yuanta PCF",
        "fetched_at": fetched_at,
    }
    return holding_rows, summary_row, payload


def fetch_holdings(etf: dict[str, Any]) -> tuple[list[dict[str, str]], dict[str, str], str]:
    provider = str(etf.get("provider") or "auto").lower()
    if provider == "price-only" or etf.get("track_holdings") is False:
        raise RuntimeError("Holdings disabled for this ETF")
    if provider in {"yuanta", "auto"}:
        rows, summary, _payload = fetch_yuanta_holdings(etf)
        return rows, summary, "Yuanta PCF"
    raise RuntimeError(f"Unsupported holdings provider: {provider}")


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def write_merged_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]], key_fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    merged: dict[tuple[str, ...], dict[str, str]] = {}
    for row in read_csv_rows(path):
        key = tuple(str(row.get(field, "")) for field in key_fields)
        merged[key] = {field: str(row.get(field, "")) for field in fieldnames}
    for row in rows:
        key = tuple(str(row.get(field, "")) for field in key_fields)
        merged[key] = {field: str(row.get(field, "")) for field in fieldnames}

    sorted_rows = sorted(
        merged.values(),
        key=lambda row: tuple(row.get(field, "") for field in key_fields),
    )
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted_rows)


def latest_by_key(rows: list[dict[str, str]], key: str) -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for row in rows:
        result[row.get(key, "")] = row
    return result


def sorted_dates(rows: list[dict[str, str]]) -> list[str]:
    return sorted({row.get("date", "") for row in rows if row.get("date")})


def compute_holding_changes(rows: list[dict[str, str]]) -> dict[str, Any]:
    dates = sorted_dates(rows)
    if not dates:
        return {"latest_date": "", "previous_date": "", "latest": [], "changes": []}
    latest_date = dates[-1]
    previous_date = dates[-2] if len(dates) >= 2 else ""
    latest_rows = [row for row in rows if row.get("date") == latest_date]
    previous_rows = [row for row in rows if row.get("date") == previous_date] if previous_date else []
    prev_by_stock = latest_by_key(previous_rows, "stock_code")

    latest_sorted = sorted(latest_rows, key=lambda row: to_float(row.get("weight")) or 0, reverse=True)
    changes = []
    seen = set()
    for row in latest_rows:
        stock_code = row.get("stock_code", "")
        seen.add(stock_code)
        prev = prev_by_stock.get(stock_code, {})
        lots = to_float(row.get("lots")) or 0
        prev_lots = to_float(prev.get("lots")) if prev else None
        weight = to_float(row.get("weight")) or 0
        prev_weight = to_float(prev.get("weight")) if prev else None
        lots_change = None if prev_lots is None else lots - prev_lots
        weight_change = None if prev_weight is None else weight - prev_weight
        if prev_lots is None:
            status = "新增"
        elif lots_change and lots_change > 0:
            status = "加碼"
        elif lots_change and lots_change < 0:
            status = "減碼"
        else:
            status = "持平"
        changes.append({
            "stock_code": stock_code,
            "stock_name": row.get("stock_name", stock_code),
            "status": status,
            "lots": lots,
            "prev_lots": prev_lots,
            "lots_change": lots_change,
            "weight": weight,
            "prev_weight": prev_weight,
            "weight_change": weight_change,
        })

    if previous_date:
        latest_by_stock = latest_by_key(latest_rows, "stock_code")
        for prev in previous_rows:
            stock_code = prev.get("stock_code", "")
            if stock_code in latest_by_stock:
                continue
            prev_lots = to_float(prev.get("lots")) or 0
            prev_weight = to_float(prev.get("weight")) or 0
            changes.append({
                "stock_code": stock_code,
                "stock_name": prev.get("stock_name", stock_code),
                "status": "刪除",
                "lots": 0,
                "prev_lots": prev_lots,
                "lots_change": -prev_lots,
                "weight": 0,
                "prev_weight": prev_weight,
                "weight_change": -prev_weight,
            })

    changes_sorted = sorted(
        changes,
        key=lambda row: abs(row["lots_change"] if row["lots_change"] is not None else 0),
        reverse=True,
    )
    return {
        "latest_date": latest_date,
        "previous_date": previous_date,
        "latest": [
            {
                "stock_code": row.get("stock_code", ""),
                "stock_name": row.get("stock_name", ""),
                "lots": to_float(row.get("lots")) or 0,
                "weight": to_float(row.get("weight")) or 0,
            }
            for row in latest_sorted
        ],
        "changes": changes_sorted,
    }


def top_history(rows: list[dict[str, str]], selected_codes: set[str]) -> dict[str, list[dict[str, Any]]]:
    history: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        stock_code = row.get("stock_code", "")
        if stock_code not in selected_codes:
            continue
        history.setdefault(stock_code, []).append({
            "date": row.get("date", ""),
            "lots": to_float(row.get("lots")) or 0,
            "weight": to_float(row.get("weight")) or 0,
            "stock_name": row.get("stock_name", stock_code),
        })
    for points in history.values():
        points.sort(key=lambda item: item["date"])
    return history


def public_edit_url(config_path: Path) -> str:
    repo = os.environ.get("GITHUB_REPOSITORY", "Lucaskk/daily-news").strip() or "Lucaskk/daily-news"
    branch = os.environ.get("GITHUB_BRANCH", "main").strip() or "main"
    return f"https://github.com/{repo}/edit/{branch}/{repo_relative(config_path)}"


def build_dashboard_payload(output_root: Path, config_path: Path, config: dict[str, Any], statuses: dict[str, Any]) -> dict[str, Any]:
    etfs = tracked_etfs(config)
    intraday_rows = read_csv_rows(output_root / "data/intraday_prices.csv")
    intraday: dict[str, list[dict[str, Any]]] = {}
    for row in intraday_rows:
        code = row.get("etf_code", "")
        if not code:
            continue
        intraday.setdefault(code, []).append({
            "timestamp": row.get("timestamp", ""),
            "date": row.get("date", ""),
            "price": to_float(row.get("price")),
            "volume": to_float(row.get("volume")),
            "change_pct": to_float(row.get("change_pct")),
            "market": row.get("market", ""),
            "source": row.get("source", ""),
        })
    for points in intraday.values():
        points.sort(key=lambda item: item["timestamp"])
        del points[:-360]

    holdings: dict[str, Any] = {}
    summaries: dict[str, Any] = {}
    for etf in etfs:
        code = etf["code"]
        rows = read_csv_rows(output_root / f"data/{code}/holdings.csv")
        summary_rows = read_csv_rows(output_root / f"data/{code}/summary.csv")
        changes = compute_holding_changes(rows)
        selected = {item["stock_code"] for item in changes["latest"][:10]}
        selected.update(item["stock_code"] for item in changes["changes"][:10])
        holdings[code] = {
            **changes,
            "history": top_history(rows, selected),
        }
        if summary_rows:
            latest_summary = sorted(summary_rows, key=lambda row: row.get("date", ""))[-1]
            summaries[code] = latest_summary

    return {
        "generated_at": iso_now(),
        "config_updated_at": config.get("updated_at", ""),
        "config_path": repo_relative(config_path),
        "config_edit_url": public_edit_url(config_path),
        "etfs": etfs,
        "statuses": statuses,
        "intraday": intraday,
        "holdings": holdings,
        "summaries": summaries,
    }


def html_page(payload: dict[str, Any]) -> str:
    data_json = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    generated = html.escape(payload["generated_at"])
    return f"""<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ETF 持股與盤中價格追蹤</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.5.0/dist/chart.umd.min.js"></script>
<style>
:root {{
  color-scheme: light;
  --bg: #f6f7fb;
  --card: #ffffff;
  --text: #162033;
  --muted: #65758b;
  --line: #dde5ef;
  --blue: #2563eb;
  --green: #059669;
  --red: #dc2626;
  --amber: #b45309;
  --shadow: 0 16px 45px rgba(15, 23, 42, .08);
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans TC", sans-serif;
  background: var(--bg);
  color: var(--text);
}}
a {{ color: var(--blue); text-decoration: none; }}
.hero {{
  padding: 42px 20px 28px;
  background:
    radial-gradient(circle at 15% 20%, rgba(37, 99, 235, .32), transparent 35%),
    linear-gradient(135deg, #111827, #1e3a8a 55%, #0f766e);
  color: white;
}}
.wrap {{ max-width: 1180px; margin: 0 auto; }}
h1 {{ margin: 0; font-size: clamp(30px, 5vw, 54px); line-height: 1.05; }}
.subtitle {{ margin-top: 14px; color: rgba(255,255,255,.82); max-width: 860px; line-height: 1.65; }}
.stamp {{ margin-top: 18px; color: rgba(255,255,255,.68); font-size: 13px; }}
main {{ padding: 22px 20px 48px; }}
.grid {{ display: grid; grid-template-columns: repeat(12, 1fr); gap: 16px; }}
.card {{
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: 18px;
  box-shadow: var(--shadow);
}}
.span-12 {{ grid-column: span 12; }}
.span-8 {{ grid-column: span 8; }}
.span-6 {{ grid-column: span 6; }}
.span-4 {{ grid-column: span 4; }}
.kpi {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
  margin-bottom: 16px;
}}
.kpi .card {{ box-shadow: none; }}
.label {{ color: var(--muted); font-size: 13px; }}
.value {{ font-size: 28px; font-weight: 760; margin-top: 6px; }}
.tabs {{ display: flex; gap: 8px; flex-wrap: wrap; margin: 6px 0 18px; }}
.tab {{
  border: 1px solid var(--line);
  background: white;
  color: var(--text);
  padding: 10px 14px;
  border-radius: 999px;
  cursor: pointer;
  font-weight: 650;
}}
.tab.active {{ background: var(--blue); color: white; border-color: var(--blue); }}
.section-title {{ display: flex; align-items: baseline; justify-content: space-between; gap: 12px; margin-bottom: 10px; }}
.section-title h2 {{ margin: 0; font-size: 21px; }}
.small {{ color: var(--muted); font-size: 13px; line-height: 1.55; }}
table {{ border-collapse: collapse; width: 100%; font-size: 14px; }}
th, td {{ padding: 10px 9px; border-bottom: 1px solid var(--line); text-align: right; white-space: nowrap; }}
th:first-child, td:first-child, th:nth-child(2), td:nth-child(2) {{ text-align: left; }}
th {{ color: var(--muted); font-weight: 700; background: #f8fafc; position: sticky; top: 0; }}
.table-wrap {{ overflow: auto; max-height: 430px; border: 1px solid var(--line); border-radius: 14px; }}
.up {{ color: var(--red); font-weight: 700; }}
.down {{ color: var(--green); font-weight: 700; }}
.flat {{ color: var(--muted); }}
.pill {{
  display: inline-flex;
  align-items: center;
  padding: 3px 8px;
  border-radius: 999px;
  background: #eef2ff;
  color: #3730a3;
  font-size: 12px;
  font-weight: 700;
}}
.controls {{ display: grid; grid-template-columns: 1fr auto; gap: 10px; margin-top: 12px; }}
input, textarea, select {{
  width: 100%;
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 10px 12px;
  font: inherit;
}}
textarea {{ min-height: 150px; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; }}
button, .button {{
  border: 0;
  background: var(--blue);
  color: white;
  padding: 10px 14px;
  border-radius: 12px;
  font: inherit;
  font-weight: 700;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}}
.button.secondary {{ background: #e2e8f0; color: #172033; }}
.chart-box {{ min-height: 320px; }}
.empty {{ color: var(--muted); padding: 18px; border: 1px dashed var(--line); border-radius: 14px; background: #f8fafc; }}
@media (max-width: 900px) {{
  .span-8, .span-6, .span-4 {{ grid-column: span 12; }}
  .kpi {{ grid-template-columns: repeat(2, 1fr); }}
}}
@media (max-width: 560px) {{
  .kpi {{ grid-template-columns: 1fr; }}
  .controls {{ grid-template-columns: 1fr; }}
}}
</style>
</head>
<body>
<header class="hero">
  <div class="wrap">
    <h1>ETF 持股與盤中價格追蹤</h1>
    <div class="subtitle">每天讀取追蹤清單，抓取 ETF 盤中價格快照與可取得的官方 PCF / 持股資料，保存成 CSV，再產生這份 HTML 線圖報表。GitHub Pages 負責展示，資料抓取由本機或排程執行。</div>
    <div class="stamp">產生時間：{generated}</div>
  </div>
</header>
<main class="wrap">
  <section class="kpi" id="kpi"></section>
  <section class="card span-12">
    <div class="section-title">
      <h2>追蹤清單</h2>
      <span class="small" id="configInfo"></span>
    </div>
    <div id="tabs" class="tabs"></div>
    <div class="grid">
      <div class="span-8">
        <div class="card">
          <div class="section-title">
            <h2 id="priceTitle">盤中價格線圖</h2>
            <span class="small">交易時段 09:00–13:30 可定時抓取；非交易時段通常顯示最後揭示價。</span>
          </div>
          <div class="chart-box"><canvas id="priceChart"></canvas></div>
        </div>
      </div>
      <div class="span-4">
        <div class="card">
          <div class="section-title"><h2>最新 ETF 摘要</h2></div>
          <div id="summaryBox" class="small"></div>
        </div>
      </div>
      <div class="span-6">
        <div class="card">
          <div class="section-title"><h2>持股張數線圖</h2></div>
          <select id="holdingSelect"></select>
          <div class="chart-box"><canvas id="holdingChart"></canvas></div>
        </div>
      </div>
      <div class="span-6">
        <div class="card">
          <div class="section-title"><h2>最新持股權重 Top 10</h2></div>
          <div class="chart-box"><canvas id="weightChart"></canvas></div>
        </div>
      </div>
      <div class="span-12">
        <div class="card">
          <div class="section-title">
            <h2>今日持股變動</h2>
            <span class="small" id="changeDate"></span>
          </div>
          <div class="table-wrap">
            <table>
              <thead><tr><th>股票</th><th>狀態</th><th>目前張數</th><th>變動張數</th><th>目前權重</th><th>權重變動</th></tr></thead>
              <tbody id="changeTable"></tbody>
            </table>
          </div>
        </div>
      </div>
      <div class="span-12">
        <div class="card">
          <div class="section-title"><h2>管理追蹤 ETF</h2></div>
          <p class="small">這個頁面是靜態 GitHub Pages，不能安全地直接寫入 GitHub。你可以在下面輸入 ETF 代號產生新版 JSON，然後按「到 GitHub 編輯設定檔」貼上。若之後要做到真正網頁一按就新增，需要加一個安全後端或 GitHub App。</p>
          <div class="controls">
            <input id="newEtfCode" placeholder="輸入 ETF 代號，例如 0056、00878">
            <button id="addEtf">產生設定</button>
          </div>
          <textarea id="configJson" spellcheck="false"></textarea>
          <p><a class="button" id="editConfig" target="_blank" rel="noopener">到 GitHub 編輯設定檔</a></p>
        </div>
      </div>
    </div>
  </section>
</main>
<script id="dashboard-data" type="application/json">{data_json}</script>
<script>
const dashboard = JSON.parse(document.getElementById('dashboard-data').textContent);
let activeCode = dashboard.etfs[0]?.code || '';
let charts = {{}};

const nf0 = new Intl.NumberFormat('zh-TW', {{ maximumFractionDigits: 0 }});
const nf2 = new Intl.NumberFormat('zh-TW', {{ maximumFractionDigits: 2 }});

function byId(id) {{ return document.getElementById(id); }}
function fmt(value, digits = 2) {{
  if (value === null || value === undefined || Number.isNaN(Number(value))) return '—';
  return Number(value).toLocaleString('zh-TW', {{ maximumFractionDigits: digits }});
}}
function signed(value, digits = 2) {{
  if (value === null || value === undefined || Number.isNaN(Number(value))) return '—';
  const n = Number(value);
  const sign = n > 0 ? '+' : '';
  return sign + n.toLocaleString('zh-TW', {{ maximumFractionDigits: digits }});
}}
function cls(value) {{
  const n = Number(value || 0);
  if (n > 0) return 'up';
  if (n < 0) return 'down';
  return 'flat';
}}
function destroyChart(id) {{
  if (charts[id]) charts[id].destroy();
  charts[id] = null;
}}
function renderKpi() {{
  const priceCount = Object.values(dashboard.intraday).reduce((sum, rows) => sum + rows.length, 0);
  const holdingCount = Object.values(dashboard.holdings).filter(item => item.latest_date).length;
  byId('kpi').innerHTML = [
    ['追蹤 ETF', dashboard.etfs.length],
    ['盤中價資料點', priceCount],
    ['有持股資料 ETF', holdingCount],
    ['設定更新', dashboard.config_updated_at || '—'],
  ].map(([label, value]) => `<div class="card"><div class="label">${{label}}</div><div class="value">${{value}}</div></div>`).join('');
}}
function renderTabs() {{
  byId('tabs').innerHTML = dashboard.etfs.map(etf => (
    `<button class="tab ${{etf.code === activeCode ? 'active' : ''}}" data-code="${{etf.code}}">${{etf.code}} ${{etf.name || ''}}</button>`
  )).join('');
  document.querySelectorAll('.tab').forEach(tab => tab.addEventListener('click', () => {{
    activeCode = tab.dataset.code;
    renderAll();
  }}));
}}
function renderPriceChart() {{
  const etf = dashboard.etfs.find(item => item.code === activeCode) || {{}};
  const rows = dashboard.intraday[activeCode] || [];
  byId('priceTitle').textContent = `${{activeCode}} ${{etf.name || ''}} 盤中價格線圖`;
  destroyChart('priceChart');
  if (!rows.length) {{
    byId('priceChart').replaceWith(Object.assign(document.createElement('canvas'), {{ id: 'priceChart' }}));
    return;
  }}
  charts.priceChart = new Chart(byId('priceChart'), {{
    type: 'line',
    data: {{
      labels: rows.map(row => row.timestamp.slice(5, 16)),
      datasets: [{{
        label: '成交價',
        data: rows.map(row => row.price),
        borderColor: '#2563eb',
        backgroundColor: 'rgba(37,99,235,.12)',
        tension: .25,
        pointRadius: rows.length > 80 ? 0 : 3,
        fill: true,
      }}]
    }},
    options: {{ responsive: true, maintainAspectRatio: false, scales: {{ y: {{ ticks: {{ callback: v => fmt(v, 2) }} }} }} }}
  }});
}}
function renderSummary() {{
  const etf = dashboard.etfs.find(item => item.code === activeCode) || {{}};
  const summary = dashboard.summaries[activeCode] || {{}};
  const prices = dashboard.intraday[activeCode] || [];
  const lastPrice = prices[prices.length - 1] || {{}};
  const status = dashboard.statuses?.holdings?.[activeCode] || dashboard.statuses?.prices?.[activeCode] || '';
  byId('summaryBox').innerHTML = `
    <p><span class="pill">${{activeCode}}</span> ${{etf.name || ''}}</p>
    <p>最新成交價：<strong>${{fmt(lastPrice.price, 2)}}</strong>，漲跌幅：<span class="${{cls(lastPrice.change_pct)}}">${{signed(lastPrice.change_pct, 2)}}%</span></p>
    <p>價格時間：${{lastPrice.timestamp || '—'}}</p>
    <p>持股資料日：${{dashboard.holdings[activeCode]?.latest_date || '—'}}</p>
    <p>淨值 NAV：${{summary.nav || '—'}}；基金規模：${{summary.fund_size ? nf0.format(Number(summary.fund_size) / 100000000) + ' 億' : '—'}}</p>
    <p>資料來源：${{summary.source || lastPrice.source || '—'}}</p>
    ${{status ? `<p>狀態：${{status}}</p>` : ''}}
  `;
}}
function renderHoldingSelect() {{
  const holding = dashboard.holdings[activeCode] || {{}};
  const history = holding.history || {{}};
  const options = Object.entries(history).map(([code, rows]) => {{
    const name = rows[rows.length - 1]?.stock_name || code;
    return `<option value="${{code}}">${{code}} ${{name}}</option>`;
  }}).join('');
  byId('holdingSelect').innerHTML = options || '<option>無持股歷史資料</option>';
  byId('holdingSelect').onchange = renderHoldingChart;
}}
function renderHoldingChart() {{
  const holding = dashboard.holdings[activeCode] || {{}};
  const history = holding.history || {{}};
  const code = byId('holdingSelect').value;
  const rows = history[code] || [];
  destroyChart('holdingChart');
  charts.holdingChart = new Chart(byId('holdingChart'), {{
    type: 'line',
    data: {{
      labels: rows.map(row => row.date),
      datasets: [{{
        label: `${{code}} 持股張數`,
        data: rows.map(row => row.lots),
        borderColor: '#059669',
        backgroundColor: 'rgba(5,150,105,.12)',
        tension: .25,
        pointRadius: 4,
        fill: true,
      }}]
    }},
    options: {{ responsive: true, maintainAspectRatio: false }}
  }});
}}
function renderWeightChart() {{
  const rows = (dashboard.holdings[activeCode]?.latest || []).slice(0, 10);
  destroyChart('weightChart');
  charts.weightChart = new Chart(byId('weightChart'), {{
    type: 'bar',
    data: {{
      labels: rows.map(row => `${{row.stock_code}} ${{row.stock_name}}`),
      datasets: [{{
        label: '權重 %',
        data: rows.map(row => row.weight),
        backgroundColor: '#2563eb',
      }}]
    }},
    options: {{ responsive: true, maintainAspectRatio: false, indexAxis: 'y' }}
  }});
}}
function renderChangeTable() {{
  const holding = dashboard.holdings[activeCode] || {{}};
  const changes = holding.changes || [];
  byId('changeDate').textContent = holding.previous_date ? `${{holding.previous_date}} → ${{holding.latest_date}}` : `${{holding.latest_date || '尚無資料'}}`;
  byId('changeTable').innerHTML = changes.slice(0, 80).map(row => `
    <tr>
      <td>${{row.stock_code}} ${{row.stock_name}}</td>
      <td><span class="pill">${{row.status}}</span></td>
      <td>${{fmt(row.lots, 3)}}</td>
      <td class="${{cls(row.lots_change)}}">${{signed(row.lots_change, 3)}}</td>
      <td>${{fmt(row.weight, 2)}}%</td>
      <td class="${{cls(row.weight_change)}}">${{signed(row.weight_change, 2)}}%</td>
    </tr>
  `).join('') || '<tr><td colspan="6" class="flat">尚無可比較的持股變動；第一次抓取後需要等下一個交易日才會有變動。</td></tr>';
}}
function renderConfigHelper() {{
  byId('configInfo').textContent = `設定檔：${{dashboard.config_path}}`;
  byId('editConfig').href = dashboard.config_edit_url;
  const config = {{
    updated_at: new Date().toISOString().slice(0, 10),
    etfs: dashboard.etfs.map(etf => ({{
      code: etf.code,
      name: etf.name || '',
      market: etf.market || 'twse',
      provider: etf.provider || 'auto',
      enabled: etf.enabled !== false,
      track_intraday: etf.track_intraday !== false,
      track_holdings: etf.track_holdings !== false,
    }}))
  }};
  const render = () => byId('configJson').value = JSON.stringify(config, null, 2);
  render();
  byId('addEtf').onclick = () => {{
    const raw = byId('newEtfCode').value.toUpperCase().replace(/[^0-9A-Z]/g, '');
    const match = raw.match(/^(\\d{{1,6}})([A-Z]?)$/);
    if (!match) return alert('請輸入有效 ETF 代號');
    const code = match[1].padStart(4, '0') + match[2];
    if (!config.etfs.some(item => item.code === code)) {{
      config.etfs.push({{ code, name: '', market: 'twse', provider: 'auto', enabled: true, track_intraday: true, track_holdings: true }});
      render();
    }}
  }};
}}
function renderAll() {{
  renderTabs();
  renderPriceChart();
  renderSummary();
  renderHoldingSelect();
  renderHoldingChart();
  renderWeightChart();
  renderChangeTable();
}}
renderKpi();
renderConfigHelper();
renderAll();
</script>
</body>
</html>
"""


def write_dashboard(output_root: Path, config_path: Path, config: dict[str, Any], statuses: dict[str, Any]) -> Path:
    payload = build_dashboard_payload(output_root, config_path, config, statuses)
    output_root.mkdir(parents=True, exist_ok=True)
    latest = output_root / "latest.html"
    latest.write_text(html_page(payload), encoding="utf-8")
    index = output_root / "index.html"
    index.write_text(
        """<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="0; url=latest.html">
<title>ETF Monitor</title>
</head>
<body>
<p>正在開啟 ETF 追蹤報表：<a href="latest.html">latest.html</a></p>
<script>location.replace("latest.html");</script>
</body>
</html>
""",
        encoding="utf-8",
    )
    return latest


def run_update(config_path: Path, output_root: Path, *, report_only: bool, skip_prices: bool, skip_holdings: bool) -> dict[str, Any]:
    config = load_json(config_path)
    etfs = tracked_etfs(config)
    status_path = output_root / "run-status.json"
    statuses: dict[str, Any] = {
        "run_at": iso_now(),
        "prices": {},
        "holdings": {},
        "errors": {},
    }

    if report_only and status_path.exists():
        try:
            statuses = json.loads(status_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
        statuses["report_regenerated_at"] = iso_now()

    if not report_only and not skip_prices:
        try:
            price_rows, missing = fetch_intraday_prices(etfs)
            if price_rows:
                write_merged_csv(
                    output_root / "data/intraday_prices.csv",
                    PRICE_FIELDNAMES,
                    price_rows,
                    ["timestamp", "etf_code"],
                )
            for row in price_rows:
                statuses["prices"][row["etf_code"]] = f"OK {row['timestamp']} price={row['price']}"
            for code, message in missing.items():
                statuses["prices"][code] = message
        except Exception as exc:
            statuses["errors"]["prices"] = str(exc)

    if not report_only and not skip_holdings:
        for etf in etfs:
            code = etf["code"]
            if not etf.get("track_holdings", True):
                statuses["holdings"][code] = "Skipped: holdings disabled"
                continue
            try:
                holding_rows, summary_row, provider = fetch_holdings(etf)
                write_merged_csv(
                    output_root / f"data/{code}/holdings.csv",
                    HOLDING_FIELDNAMES,
                    holding_rows,
                    ["date", "etf_code", "stock_code"],
                )
                write_merged_csv(
                    output_root / f"data/{code}/summary.csv",
                    SUMMARY_FIELDNAMES,
                    [summary_row],
                    ["date", "etf_code"],
                )
                statuses["holdings"][code] = f"OK {provider} {summary_row['date']} rows={len(holding_rows)}"
            except Exception as exc:
                statuses["holdings"][code] = f"Failed: {exc}"

    output_root.mkdir(parents=True, exist_ok=True)
    status_path.write_text(json.dumps(statuses, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    latest = write_dashboard(output_root, config_path, config, statuses)
    statuses["latest_html"] = repo_relative(latest)
    status_path.write_text(json.dumps(statuses, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return statuses


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args.add_etf:
        add_or_update_etf(args)

    config_path = Path(args.config)
    output_root = Path(args.output_root)
    statuses = run_update(
        config_path,
        output_root,
        report_only=args.report_only,
        skip_prices=args.skip_prices,
        skip_holdings=args.skip_holdings,
    )
    print(json.dumps(statuses, ensure_ascii=False, indent=2))
    return 0 if not statuses.get("errors") else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
