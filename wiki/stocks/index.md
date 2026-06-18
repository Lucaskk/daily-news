---
title: "股票分析索引"
type: overview
created: 2026-06-11
updated: 2026-06-19
status: active
tags: [stocks, taiwan-stocks]
sources: []
---

# 股票分析索引

股票分析頁會放在 `wiki/stocks/YYYY/MM/YYYY-MM-DD/<stock-code>/`。

- [Latest Analysis](latest-analysis.html) - 最新一次產生的股票分析頁。

## 使用方式

LINE webhook 收到股票代碼或名稱後，會把代碼放進 GitHub 待處理清單並回傳等候頁。Mac 每 15 分鐘處理一次；完成後等候頁會自動前往 `by-code/<股票代碼>/` 的最新成功分析。

## 資料來源與限制

- 行情資料：TWSE / TPEx 公開 API。
- 財報資料：Goodinfo.tw 財報頁。
- 每次產生分析時，會檢查損益表、資產負債表及現金流量表的共同最新季度，並與去年同一季度比較；不以不同季度或全年資料替代同期基準。
- 驗證連結：公開資訊觀測站 MOPS。
- 產生頁面僅供研究與學習參考，不構成投資建議。
- 同一股票每天最多重新抓取一次；來源暫時失敗時保留上一次成功頁。
