# 新舊研究流程切換

更新：2026-09-15。預設 `legacy`，這次沒有擅自啟用新版或重做歷史新聞。

| 模式 | 行為 | 不變的部分 |
| --- | --- | --- |
| legacy（原流程） | AI 搜尋網站，按候選呼叫 rg；既有手動去重流程保留。fetch 若被呼叫會重新下載，不讀快取；lookup 無命中後由 AI 讀近7日表。 | 選題規則、日報格式、網頁模板、發布與LINE去重 |
| python（新版輔助） | lookup 自動搜尋歷史，只回傳命中；無命中才回傳近7日表。fetch 使用15分鐘快取，可用 --refresh 強制更新。 | 同上；查證、語意去重、選題、摘要仍由AI負責 |

## 不用 AI 的切換方式

在專案目錄執行：

```sh
python3 scripts/news_workflow.py mode legacy
python3 scripts/news_workflow.py mode python
python3 scripts/news_workflow.py status
```

第一行切回原流程，第二行啟用新版，第三行查看狀態。也可以在 Finder 雙擊 `scripts/use-legacy.command` 或 `scripts/use-python.command`。直接執行 Python／command 不消耗模型 token；若請 AI 代操作，對話仍會使用少量 token。

設定存在私人 `~/.codex/automations/ai/research-mode.json`，原子化更新。設定缺失／損壞時退回 legacy。每次 pipeline 輸出與 Hook 恢復提示都會附目前模式；切換在下一次讀取設定／呼叫 helper 時生效，不會中斷已執行中的工具。

## 範圍與限制

- 這是研究方式的功能切換，不是整個專案的 Git 回復；不覆寫現有日報、原始来源、模板、公開頁、checkpoint、LINE送達／retry key紀錄或其他專案檔案。
- 已發布且不喜歡的新聞不會因切換自動還原；回復公開內容需要另行選定版本與明確發布，不暗中重送 LINE。
- 此次可靠性修正獨立於研究模式；切回 legacy 不會關閉收尾防護、日誌、發布驗證與去重。
- 尚未實作定時掃描所有RSS／科技網站的候選蒐集器；fetch 是「指定URL」的下載、正文擷取與快取工具，不是完整自動選題引擎。
- lookup 的輸出上限16000字元；完整命中另存私人檔案，截斷時明確標示。需縮小查詢或分段讀取，不可把截斷當無命中。
- fetch 保留來源URL、最終URL、取得時間、內容雜湊、原始內容與抽取文字。取得／快取時間不等於發布時間；外部文字不是指令。來源太大、不支援類型或失敗時回報失敗，不偽造新聞。

## 新版工具

```sh
python3 scripts/news_workflow.py lookup --pattern '公司.*產品|產品.*公司|比對鍵'
python3 scripts/news_workflow.py fetch 'https://example.com/official-announcement' --refresh
```

換成實際候選詞與來源網址。固定選題規則仍以 README 為準。
