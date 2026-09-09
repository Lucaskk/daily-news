# 每日新聞配送機制

稽核日期：2026-09-09（Asia/Taipei）。

## 排程與完成條件

- 新聞產製：每天 08:00 一次，依使用者確認不增加備援產製排程。
- 發布：GitHub main 推送後驗證 GitHub Pages 當日頁與最新入口，再呼叫唯一 LINE watchdog。
- 配送補查：本機 LaunchAgent 每 900 秒執行，登入載入時也執行；不負責搜尋、產製或發布新聞。
- 缺件告警：10:00 後仍沒有可驗證的當日報告，當天告警一次；後續若完成發布，下次配送檢查可自動送出。
- 新聞成功：exit 0 且輸出 `Sent LINE message` 或 `already sent`。缺件告警不是新聞成功；API 接受亦不代表收件者已讀。

## 2026-09-09 修正

- 跨程序檔案鎖避免手動執行與排程同時通過去重檢查。
- 發送前保存 retry key、原始訊息及收件者雜湊，逾時／5xx 以同一 key 重試；收到帶 accepted request ID 的 409 視為先前已接受。超過安全重試期限或收件者改變時停止，不冒險重送。
- 去重與請求紀錄使用原子寫入；禁止強制繞過每日去重。
- 公開頁驗證可信網址、當日內嵌日期、全球 1–10、科技產品在前、文章 DOM 與資料一致及有效來源，不只看 HTTP 200。
- 公開頁讀取、解析失敗也納入缺件告警；告警後仍以失敗狀態表示當日新聞未完成。
- 每次檢查保存可讀狀態，避免安靜模式讓最後檢查時間無從確認。

實作依據：[LINE 官方重試規範](https://developers.line.biz/en/docs/messaging-api/retrying-api-request/)。LINE retry key 有效期為 24 小時，須保留相同訊息及收件者；API 接受不保證收件者實際收到。

## 維護與檢查

唯一正式入口為 `~/.codex/automations/ai/line_watchdog.py`。專案 `scripts/line_watchdog_source.py` 僅保存可版本控制的來源；修改需先通過測試，再安裝至正式入口。不得新增另一條 sender、執行舊 sender 或將私人設定提交到 Git。

```sh
/usr/bin/python3 -m unittest discover -s tests -p test_line_watchdog.py
```

私人目錄中的 `line-watchdog-status.json` 包含檢查時間與狀態：`already_sent`／`sent` 表示當日成功紀錄存在；`waiting_for_publish` 表示告警時間前等待；`publish_unavailable` 表示缺件；`delivery_failed`／`error` 表示需檢查錯誤。私人 token、收件者、待送訊息與狀態均不入庫。

2026-09-09 驗證：19 項模擬測試通過，包含併發、逾時、5xx、409、狀態寫入失敗、缺件告警與恢復、舊頁及不完整頁拒送。正式入口於 23:27:47 回報當日 `already sent`，LaunchAgent 再次執行 exit 0，未重複發送。今日實際補送時間為 10:07:40。

## 仍存在的限制

今天漏發源於產製流程中斷，並非確認的 LINE API 故障。中央規則已新增恢復與完成檢查，但保留每日一次產製，就不會在產製失敗後自行新增研究工作。告警後仍可能需要人工恢復。

本機關機、登出、網路故障、GitHub／LINE 或模型服務不可用，均可能延遲或阻止流程；本機 watchdog 本身停止時也無法自行發出告警。因此本機機制不能保證全年每天必定配送。
