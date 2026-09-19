---
title: "每日新聞來源筆記｜2026-09-19"
date: 2026-09-19
type: source-notes
status: research-complete
---

# 2026-09-19 來源與去重筆記

研究截點固定為 **2026-09-19 08:01:30 Asia/Taipei**（`2026-09-19T00:01:30Z`）；同日接續不得重設。

- 全球 24 小時：2026-09-18 08:01:30 至 2026-09-19 08:01:30（Asia/Taipei），UTC 為 `2026-09-18T00:01:30Z` 至 `2026-09-19T00:01:30Z`。
- 科技產品 168 小時：2026-09-12 08:01:30 至 2026-09-19 08:01:30（Asia/Taipei），UTC 為 `2026-09-12T00:01:30Z` 至 `2026-09-19T00:01:30Z`。
- 研究模式：`legacy`。已讀中央規則並執行 `build_product_news_ledger.py`：580 筆／93 份既有日報。完整歷史僅用候選組合窄搜，未整份讀取產品歷史表或全部日報。

## 全球 Top 10 時間與去重

| 項目 | 事件／首次可靠發布時間依據 | 歷史判斷、來源與限制 |
|---|---|---|
| G1 巴基斯坦 Kohat 攻擊 | AP `2026-09-18T09:34:26Z` = 9/18 17:34:26 TPE；攻擊當日發生 | https://apnews.com/article/ebfc29859f724630e25f8549116859c8 。窄搜 Kohat／21死80傷無命中。無組織立即認領，TTP 僅為懷疑方向。 |
| G2 俄羅斯國會投票開始 | AP `2026-09-18T06:20:12Z` = 9/18 14:20:12 TPE；9/18 開票 | https://apnews.com/article/7f10803a87456051be876c0c33375af8 。選前分析不等於投票開始；無相同事件命中。結果未出。 |
| G3 Trend 油輪 | AP `2026-09-18T06:34:56Z` = 9/18 14:34:56 TPE；伊朗稱 9/17 夜間攻擊 | https://apnews.com/article/024350a0820dfc5dd433b4e13445fab5 。滚動頁只採 Trend 段落。新船舶／新攻擊宣稱，AP 未獨立證實；另一 UKMTO 案分開。 |
| G4 台灣攻擊無人機聯演 | AP `2026-09-18T12:20:34Z` = 9/18 20:20:34 TPE；9/18 演習 | https://apnews.com/article/e7c1c16040f6f9ca5e7672a3fda0ab60 。窄搜無同次首度聯演；型號與成效未全公布。 |
| G5 法國基礎設施計畫 | AP `2026-09-18T14:35:45Z` = 9/18 22:35:45 TPE；Macron 9/18 下令擬計畫 | https://apnews.com/article/29767a3fe6723ecffed343f0a4847e95 。新政府規劃命令，不寫成已部署；無歷史命中。 |
| G6 Carpathian Eight | AP `2026-09-18T11:17:27Z` = 9/18 19:17:27 TPE；首屆峰會 9/18 舉行 | https://apnews.com/article/b05ea50c3ed8b64cf25e254783a17d39 。新框架／首屆峰會無歷史命中；非共同防禦條約。 |
| G7 越南洪災 | AP `2026-09-18T10:43:28Z` = 9/18 18:43:28 TPE；9/18 官方新數字 | https://apnews.com/article/9e3f3d0af82b62c50b475c88bce3be79 。**續報**：2026-09-18 捕獲逾2,000戶淹水／逾1,000戶隔離；今天新增4死、逾16,000戶與24,000公頃農損。 |
| G8 菲律賓校園槍擊 | AP `2026-09-18T08:57:58Z` = 9/18 16:57:58 TPE；9/18 當日事件 | https://apnews.com/article/0fb2a2443f64829985e0aab1368d2ee8 。歷史無命中。網路社群與犯案原因未建立因果。 |
| G9 萬那杜渡輪 | AP `2026-09-18T06:04:37Z` = 9/18 14:04:37 TPE；海上搜救結束與責任程序新節點 | https://apnews.com/article/ba025ba8fe032beacdc0af14d7a3ce9d 。沉船本身為9/11，不能寫成今日事故；本庫未捕獲舊事件，今天以結束搜救、39人被認為死亡及刑事申訴首次收錄。 |
| G10 WFP 任命 | AP `2026-09-18T23:07:48Z` = 9/19 07:07:48 TPE；聯合國9/18宣布 | https://apnews.com/article/96aa238f519ef1ab7f8bf71217324867 。在截點前54分鐘；無同次任命歷史命中。未公布完整上任日程。 |

## 產品候選查詢與判斷

候選先執行：`rg -n -i -C 1 'Life Sciences Verification Program|LSVP.*application|GitLab 19\.4|MCP.*tool.*govern|Expert Intelligence.*Gemini Notebook|Gemini Notebook.*100,000' wiki/daily/product-news-ledger.md wiki/daily --glob 'daily-news-*.md' --glob 'source-notes-*.md'`。只有舊 MCP 通用敘述，無相同產品變更；因此依規則完整讀取 `product-news-recent-7d.md`（16 列）二次確認，仍無 T1／T2 相同變更。LSVP 另對 2026-09-02 Mythos 5.1 必要段落窄搜，確認需標重大續報。

| 候選與比對鍵 | 官方時間／來源 | 命中與決定 |
|---|---|---|
| GitLab／19.4／Duo CLI `/goal`／MCP tools governance | 2026-09-17；https://about.gitlab.com/press/releases/2026-09-17-gitlab-19-4-brings-new-agentic-automation-at-a-lower-cost/ ; https://about.gitlab.com/whats-new/19-4/ | 無相同版本命中，最近七天表亦無；收錄 T1。公開測試、GA 與實驗狀態分開。 |
| Google／Gemini Notebook／Expert Intelligence／100,000 books | 2026-09-17；https://workspaceupdates.googleblog.com/2026/09/introducing-expert-intelligence-in-Gemini-Notebook.html | 無命中，最近七天表亦無；收錄 T2。贈書活動不作核心產品功能。 |
| Anthropic／LSVP／applications／Standard Use／High-risk Use | 2026-09-17；https://www.anthropic.com/news/life-sciences-verification-program | 精確 LSVP 無命中，但 2026-09-02 已收錄 Mythos 5.1 受審核存取分層。9/17 新增正式 beta 申請與 grants／監測規則，收錄 T3 並標續報。 |
| Anthropic／Accenture／embedded evaluation | 2026-09-18；https://www.anthropic.com/news/accenture-embedded-evaluation | 屬合作與治理安排，非使用者可用產品節點；未列產品。 |

已檢查 Engadget 與 Cool3c 最新頁。Engadget 的舊產品評測、媒體訴訟與觀點不作新品；Waymo Singapore、Clicks Communicator 等可作後續候選，但今日三項官方 AI／開發產品的重要性與可驗證狀態較高。Cool3c 首頁以導購、開箱及公關稿為主，不以折扣或單一轉載補位。

## 排除與不確定性

- Gaza 建築倒塌的 AP 9/18 長文主要延伸 9/16 已收錄事件背景，無足以再次入選的新事故節點，排除。
- Guterres 專訪、能源停滯性通膨分析及選前評論不是新的制度或事件節點，排除。
- 羅馬尼亞被提名總理 9/18 宣布三黨合作方案，是 9/18 已收錄提名後的初步談判，尚未提出或通過內閣；以較新且獨立的重要事件替代。
- Iran Trend 油輪資訊只按伊朗宣稱呈現；Vanuatu 的39人為2具遺體加37失蹤的推定總數；WFP 的2.66億急性飢餓人口與1.1億目標受援人口不可混寫。

## 發布紀錄

pipeline 內容 commit `d0cd5531efe82b4fbef70367282689880f27ca5f`。GitHub Pages 日期頁、最新入口及根入口均通過 HTTP 與完整位元組雜湊驗證。唯一私人 LINE watchdog 於 2026-09-19 08:08:14 Asia/Taipei 回報 `Sent LINE message`，exit 0；pipeline `check` exit 0。研究模式為 `legacy`，未重複傳送。

公開網頁：https://lucaskk.github.io/daily-news/wiki/daily/2026/09/2026-09-19/slides-2026-09-19.html?v=20260919-080717-reader
