# 每日新聞：Python 與 Codex 分工

更新：2026-09-14。目標是讓固定流程不經模型，AI 只處理新聞判讀；不能承諾固定節省比例，需量測實際 token。

| 工作 | 執行者 | 現況／建議 |
| --- | --- | --- |
| 凍結截點、24 小時／168 小時時間計算 | Python | pipeline 已保存截點；來源時間含糊仍交 AI 判讀 |
| RSS／官方公告下載、快取、重試、正文擷取 | Python | 可新增候選蒐集器；無法擷取時保留 URL 與失敗狀態，不以舊內容補位 |
| 完整歷史產品表、近 7 天索引 | Python | build_product_news_ledger.py 已有 |
| 用公司／產品／比對鍵查所有歷史，只返回命中列 | Python／rg | 可封裝單一查詢指令；無命中才返回近 7 天表，不輸出完整歷史 |
| 同事件跨語言判斷、重大續報與舊聞辨識 | Codex | 關鍵字去重只能預篩，不能取代語意判讀 |
| 全球重要性排序、選 10 則、產品是否值得收錄 | Codex | 須交叉查證來源，不機械湊數 |
| 真實發布時間、矛盾報導與不確定性 | Codex + Python | Python 檢查確定時間是否越界；AI 核對時間代表首次發布還是修改 |
| 繁體中文摘要、影響、背景、來源對應 | Codex | 分批產出結構化內容並立即落檔 |
| HTML、展開功能、文章 ChatGPT 內容編碼 | Python／既有 JS 模板 | render_daily_slides.py 已有，不每天重寫樣式 |
| 篇數、欄位、來源 URL、日期、順序檢查 | Python | 現有 renderer／watchdog；結構正確不等於事實正確 |
| 圖片下載、連結狀態、尺寸／載入檢查 | Python／瀏覽器測試 | 圖片是否為真正產品或誤導配圖仍需 AI／人工判斷 |
| 限定檔案 commit/push、Pages 驗證、重試 | Python | daily_news_pipeline.py 已有 |
| LINE 發送、成功日期、retry key、去重 | Python | 僅私人 line_watchdog.py，不新增新聞 sender |
| 已知錯誤分類、缺檔檢查、LINE 指令診斷 | Python | 本次新增；沒有系統證據時明寫未知，不能推測額度耗盡 |
| 不明錯誤修復、研究不足、來源衝突 | Codex | 只提供精簡狀態與相關錯誤，不載入全部歷史／所有 log |

## 「重新產出」指令

此版依使用者要求先自動確認問題，不代表自動重新撰寫新聞。

1. 既有 Vercel LINE Webhook 驗證 LINE 簽章後，精確識別「重新產出」（容許前後空白），只接受目前新聞收件人的一對一訊息。其他使用者／群組不觸發。此分支不呼叫 OpenAI，也不把指令交給一般聊天 Bot。
2. Bot 在 daily-news main 的 `wiki/daily/commands/YYYY-MM-DD.json` 保留當日最新請求；只含日期、diagnose 動作、事件 ID 雜湊與時間，不寫入 user ID、reply token、對話或密鑰。重送及較舊事件不覆蓋較新請求。多個尚未處理請求合併成最新一次。
3. 原有每 15 分鐘 watchdog 檢查請求、當日 checkpoint、可辨識的模型錯誤、本機日報／來源筆記、公開頁與 LINE 成功日期，再回覆診斷。電腦須開機、可連網；不是即時回覆或保證 15 分鐘內抵達。
4. 診斷使用獨立的事件去重紀錄，不改每日新聞成功紀錄、不繞過防重送、不重設截點、不喚醒 AI、不新增產製排程。研究未完成仍需 Codex 接續。公開頁已合格且未配送時，原本 watchdog 流程可接續配送。
5. 功能以私人 `~/.codex/automations/ai/line-command-enabled` 開關啟用。LINE 接收端在 `Lucaskk/gpt-ai-assistant`，不是這個新聞庫；部署後仍需用真實 LINE 訊息驗證接收至診斷配送的完整路徑。

## 後續最值得節省的部分

先新增候選蒐集／快取與窄化去重查詢工具，讓 Codex 一次只看到候選摘要、時間依據、網址及少量歷史命中。AI 完成查證與選題後，直接呼叫現有 finish，不再逐條操作渲染、Git、Pages、LINE。本次未新增候選蒐集器或 AI 自動喚醒程序。

LINE 規範：[接收 Webhook、事件去重](https://developers.line.biz/en/docs/messaging-api/receiving-messages/)、[簽章驗證](https://developers.line.biz/en/docs/messaging-api/verify-webhook-signature/)。
