---
title: "股票分析索引"
type: overview
created: 2026-06-11
updated: 2026-06-11
status: active
tags: [stocks, taiwan-stocks]
sources: []
---

# 股票分析索引

股票分析頁會放在 `wiki/stocks/YYYY/MM/YYYY-MM-DD/<stock-code>/`。

- [Latest Analysis](latest-analysis.html) - 最新一次產生的股票分析頁。

## 使用方式

LINE webhook 收到股票代碼或名稱後，會產生 HTML 分析頁並回傳短連結。完整內容放在網頁，LINE 只保留日期、標的與連結，以降低訊息長度與使用費用。

## 資料來源與限制

- 行情資料：TWSE / TPEx 公開 API。
- 財報資料：FinMind API 為主資料源，TWSE / TPEx 官方 OpenAPI 用於最新財報備援與交叉驗證。
- 驗證連結：TWSE / TPEx 官方 OpenAPI 與公開資訊觀測站 MOPS。
- 產生頁面僅供研究與學習參考，不構成投資建議。
