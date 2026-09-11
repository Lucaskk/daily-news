# 每日新聞配送機制

稽核日期：2026-09-11（Asia/Taipei）。

## 2026-09-11 產製中斷根因與修正

- 已核對當日執行紀錄：08:00:53 開始新聞研究，最後卻回覆「維持 08:00 一次」的排程偏好並結束；沒有當日日報目錄。10:13:51 watchdog 成功發出缺件告警，公開入口仍指向 9/10。這是產製未完成，不是本次已觀察到的 LINE 或 GitHub 推送失敗。
- 使用者再次確認保留同一對話、不新增獨立任務；每日產製仍一次。修正採持久化 checkpoint 與單一發布指令，不建立另一個排程。
- `scripts/daily_news_pipeline.py begin/status` 保存並顯示當日截點與待辦階段；`finish` 串接渲染、驗證、乾淨 clone 推送、Pages 等待及既有 watchdog；`check` 是收尾驗證。詳見中央 README。
- 新增跨程序鎖與發布 allowlist，排除私密設定及其他股票工作。Git push、Pages 部署與 LINE 短暫失敗在同一指令內有限重試；完成日期確認與 LINE 去重不能繞過。
- 修改只降低「研究後漏接發布步驟」及「網路暫時失敗」風險。未完成的研究仍需模型接續；此腳本不是自動新聞產生器，也不能保證模型提前結束時自行復活。
- 本次實機驗證：新流程發布 commit `edb7595`，Pages 三個入口雜湊符合，10:38:59 LINE 成功；45 項 Python 測試與公開頁手機／桌面檢查通過。

```sh
python3 scripts/daily_news_pipeline.py status
python3 scripts/daily_news_pipeline.py finish
python3 scripts/daily_news_pipeline.py check
python3 -m unittest discover -s tests -p test_daily_news_pipeline.py
```

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
