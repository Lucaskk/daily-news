# 2026-09-15 來源筆記

- 研究截點：2026-09-15 08:02:14 Asia/Taipei = 2026-09-15 00:02:14 UTC。
- 全球 24 小時：2026-09-14 08:02:14 至 2026-09-15 08:02:14 Asia/Taipei；UTC 2026-09-14 00:02:14 至 2026-09-15 00:02:14。
- 產品 168 小時：2026-09-08 08:02:14 至 2026-09-15 08:02:14 Asia/Taipei；UTC 2026-09-08 00:02:14 至 2026-09-15 00:02:14。
- 研究模式：`legacy`。排序依 AP、Reuters、BBC、主要國際媒體、官方公告與可取得的聚合訊號綜合判斷，不宣稱有精確全球討論量排行。
- 本次已查看 Engadget 與 Cool3c 作產品候選發現；首頁及搜尋結果多為舊消息、評論、促銷或已收錄產品，未因媒體頁面更新而入選。

## 去重紀錄

產製前重建產品歷史表：570 筆產品變更、89 份日報。完整歷史不整份載入模型；先以一次 `rg -n -i` 搜尋世界新聞候選的實體、事件詞與地名，只讀命中列。Microsoft Excel 產品另以 `Microsoft.*COPILOT.*Excel|Excel.*=COPILOT|COPILOT.*function|=COPILOT` 搜尋完整 ledger 及歷史日報，無命中後才完整讀取最近 7 天表 16 列，亦無同項。

| 候選 | 歷史命中與判定 |
| --- | --- |
| 烏克蘭對等停打能源設施、最高法院郵寄選票、EPA 電廠規則、B'Tselem 報告、俄艦敘利亞補給、川普 AI 風險表態 | 無同一新事件；首次收錄 |
| 哈尼什群島 | 9/12 已報摩卡及另一紅海島嶼；本次新增 Greater／Lesser Hanish，續報 |
| 英國三地共同備忘錄 | 9/13 已報川普愛爾蘭統一言論；本次三地領袖簽署文件，續報 |
| 瑞典初步結果 | 9/14 已報投票；本次新增 176 對 173 初步席次與待計票，續報 |
| Virgo Transport 8 | 9/14 已報 6 死、108 生還、129 失蹤；本次新增 622 人、17 船、5 航空器部署，續報 |
| Excel =COPILOT | 完整歷史 `rg` 無命中；最近 7 天表亦無同項，首次收錄 |

## 產品候選

### T1 Microsoft Excel =COPILOT 函數
- 官方更新明示：自 2026-09-14 起，Excel 的 =COPILOT 函數不再可用；Copilot 側邊欄仍可執行許多相近 AI 任務。官方只提供日期，不虛構時分。
- https://techcommunity.microsoft.com/blog/microsoft365insiderblog/bring-ai-to-your-formulas-with-the-copilot-function-in-excel/4443487/replies/4467621
- 原頁主體是先前 Insider 預覽介紹；本次入選的是明確的停用狀態更新。未取得既有活頁簿錯誤行為及遷移細節。

### 排除的產品候選
- NVIDIA CUDA-Q Logical：9/14 有官方研究頁，但目前可確認的是研究／編譯器工作介紹，未證實面向一般使用者的具體產品發布節點，排除。
- Akuity Agentic Control Plane：可找到現行文件，但缺足夠可靠的首次發布時間證據，排除。
- Apple iOS 27、NVIDIA CUDA 13.4、Blizzard STARCRAFT 等已在最近 7 天表收錄，不重複。
- Engadget／Cool3c 的折扣、評測、傳聞及僅重述既有發布者不列入。

## 全球入選項目時間基準

### 1 烏克蘭有條件停打能源設施
- AP 2026-09-14T11:35:50Z = 台北 19:35:50；Reuters 另於台北 9/15 01:47 發布澤倫斯基要求具體方案。
- https://apnews.com/article/russia-ukraine-war-poland-nato-drones-dbba56f09562f337aa731f7d4bbd1235
- https://au.marketscreener.com/news/ukraine-wants-specifics-from-partners-on-halting-strikes-zelenskiy-says-ce785bdcde8cfe20
- 川普稱已有協議；烏方只表示在俄方有真實承諾時準備停止，俄方未立即確認。三者不可合併為已生效停火。

### 2 美國最高法院郵寄選票命令
- AP 即時頁 2026-09-14T12:32:27Z = 台北 20:32:27 首次通報裁定；獨立整理稿 23:36:33Z 仍在窗口內。
- https://apnews.com/article/c1fd92ed754f6d320006c270cffbece7
- https://apnews.com/article/78a4fbeb48d9c5fd27d1c865529fc65f
- 只寫「本次期中選舉前暫不實施」，不寫行政權限爭議已終局解決。

### 3 EPA 電廠溫室氣體規則
- AP 2026-09-14T13:46:12Z = 台北 21:46:12；EPA 官方技術資料確認 9/14 最終撤銷 2024 標準大部分條款，並另提案撤銷剩餘規範。
- https://apnews.com/article/cac1c2c75f8656d8eaf5f0a240edae15
- https://www.epa.gov/system/files/documents/2026-09/fact-sheet_final-and-supp_technical_september2026_1.pdf
- 3,000 億美元為 EPA 宣稱的成本估算，環保團體反對且預告訴訟；最終撤銷與另案提案分開表述。

### 4 胡塞武裝奪取兩座哈尼什島
- AP 2026-09-14T10:08:01Z = 台北 18:08:01；胡塞官員週一宣布控制兩島。
- https://apnews.com/article/mideast-iran-yemen-houthis-israel-saudi-oil-b95a5a6c73a26bbbb1caddcbf365ca62
- 前次：[[daily-news-2026-09-12]]。本次新地理增量是 Greater Hanish 與 Lesser Hanish；控制可能隨反攻改變。

### 5 英國三地領袖共同備忘錄
- AP 2026-09-14T17:01:06Z = 台北 9/15 01:01:06；週一簽署事件。
- https://apnews.com/article/wales-scotland-northern-ireland-independence-uk-devolution-4242b7fd6987520211562a2250f093a1
- 前次：[[daily-news-2026-09-13]] 的川普政治表態。新內容是三地領袖共同文本與公投要求；文件無直接法律效果。

### 6 瑞典初步結果
- AP 2026-09-14T07:31:11Z = 台北 15:31:11；近 95% 選區計票的新結果。
- https://apnews.com/article/sweden-election-parliament-andersson-kristersson-ce72489ed01f77a7cb1a40dd442ff82c
- https://www.val.se/english/election-results/elections-to-the-riksdag-and-regional-and-municipal-councils/election-results-2026
- 前次：[[daily-news-2026-09-14]] 的投票日。176 對 173 為初步席次，海外／提前票待計，最終結果與組閣分開。

### 7 印尼 Virgo Transport 8 擴大搜救
- Reuters 轉載 2026-09-14 10:55 AEST = 00:55 UTC = 台北 08:55；修改時間不用來充新。
- https://au.marketscreener.com/news/indonesia-rescuers-searching-for-129-people-still-missing-after-passenger-ship-capsizes-ce785bdcd889f32c
- 前次：[[daily-news-2026-09-14]]。新內容是 622 人、17 艘船與 5 架直升機及飛機；死傷與失蹤數暫未變。

### 8 B'Tselem《The Elimination Project》
- Le Monde 2026-09-14T08:34:29Z = 台北 16:34:29；Guardian 9/14 03:23 EDT 亦在窗口內。
- https://www.lemonde.fr/en/international/article/2026/09/14/israel-pursuing-elimination-project-of-palestinians-in-the-occupied-west-bank-ngo-b-tselem-says_6757493_4.html
- https://www.theguardian.com/world/ng-interactive/2026/sep/14/israel-palestinian-living-conditions-eliminated-west-bank-human-rights-report
- 新報告的系統性與法律政治定性是 B'Tselem 結論；本次未取得以色列政府對全報告的逐項回應，明確標示組織指控。

### 9 俄羅斯艦隊補給敘利亞設施
- Reuters 轉載 2026-09-15 02:16 AEST = 9/14 16:16 UTC = 台北 9/15 00:16，落窗。
- https://au.marketscreener.com/news/russian-convoy-resupplies-syria-coastal-facilities-for-first-time-since-moscow-damascus-deal-ce785bdcde88f725
- 船隊 9/7 抵達、9/8 靠港；只因本窗口內首次可靠發布而入選，不把舊事件改寫成 9/14 發生。衛星影像與船舶軌跡可核，彈藥內容未獨立確認。

### 10 川普反對 AI 新護欄
- AP 2026-09-14T14:14:30Z = 台北 22:14:30；新社群貼文及政策反應。
- https://apnews.com/article/trump-ai-guardrails-data-centers-b85df16775ff7e9611a456b061a0e4b9
- 川普稱 AI 生存風險為騙局，是政治主張而非科學結論；Mike Johnson 所稱白宮會議尚未排定。

## 呈現與發布

- 沿用單欄手機閱讀頁：產品在第一頁最前方，每則顯示時間、出處與摘要，完整報告在原頁展開，並提供單篇 ChatGPT 後續問題。
- 圖片來源寫入 `presentation-2026-09-15.json`；地球圖為全球新聞主題圖，非事件照片。

