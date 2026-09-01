# ETF Monitor

ETF Monitor 會讀取 `wiki/etf/config/tracked-etfs.json`，抓取追蹤 ETF 的盤中價格與可取得的官方 PCF / 持股資料，輸出 CSV 與 HTML 報表。

## 目前第一版支援

- 盤中價格：TWSE MIS，即交易時間 09:00–13:30 可定時抓取最新成交價。
- ETF 持股：元大 ETF PCF，例如 `0056`、`0050` 等元大 ETF。
- 報表：`wiki/etf/latest.html`。
- LINE：`scripts/send_line_daily_slides.py` 會在 ETF 報表存在時，於 Daily News 推播訊息多附上 ETF 報表連結。

## 更新資料與報表

```bash
python3 scripts/update_etf_monitor.py
```

只重生 HTML，不重新抓資料：

```bash
python3 scripts/update_etf_monitor.py --report-only
```

## 新增追蹤 ETF

元大 ETF，可抓持股：

```bash
python3 scripts/update_etf_monitor.py --add-etf 0050 --name 元大台灣50 --market twse --provider yuanta --report-only
```

其他投信 ETF 若尚未寫 provider，先用 price-only 追蹤盤中價格：

```bash
python3 scripts/update_etf_monitor.py --add-etf 00878 --name 國泰永續高股息 --market twse --provider price-only --report-only
```

## 盤中線圖建議排程

若要累積 09:00–13:30 的盤中價格線圖，可在交易日每分鐘或每 5 分鐘執行：

```bash
python3 scripts/update_etf_monitor.py --skip-holdings
```

收盤後再執行完整更新，抓持股 / PCF：

```bash
python3 scripts/update_etf_monitor.py
```

## 資料位置

- `wiki/etf/data/intraday_prices.csv`：ETF 盤中價格快照。
- `wiki/etf/data/<ETF代號>/holdings.csv`：ETF 每日持股。
- `wiki/etf/data/<ETF代號>/summary.csv`：ETF 每日基金規模、NAV 等摘要。
- `wiki/etf/run-status.json`：最近一次執行狀態。
