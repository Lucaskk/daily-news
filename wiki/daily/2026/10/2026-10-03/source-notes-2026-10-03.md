---
title: "2026-10-03 每日全球與科技 AI 新聞來源筆記"
type: source-notes
date: 2026-10-03
cutoff: 2026-10-03T08:01:34+08:00
status: published
tags: [daily-news, sources, provenance]
---

# 2026-10-03 來源筆記

## 研究時間窗

- 研究截點：`2026-10-03 08:01:34 Asia/Taipei`（`2026-10-03 00:01:34 UTC`）。
- 全球新聞 24 小時窗：`2026-10-02 08:01:34` 至 `2026-10-03 08:01:34 Asia/Taipei`（`2026-10-02 00:01:34` 至 `2026-10-03 00:01:34 UTC`）。
- 科技／AI 產品 14 日窗：`2026-09-19 08:01:34` 至 `2026-10-03 08:01:34 Asia/Taipei`（`2026-09-19 00:01:34` 至 `2026-10-03 00:01:34 UTC`）。
- 去重範圍依新規則限定為 D-14 至 D-1：`2026-09-19` 至 `2026-10-02` 的 14 份日報；不查更早日報、來源筆記或完整歷史表。
- 選題前執行 `build_product_news_ledger.py --cutoff 2026-10-03T08:01:34+08:00`，產生 57 列 `product-news-recent-14d.md`。

## 科技來源掃描

- 第一輪廣泛掃描：CSV 啟用來源 Engadget、The Verge、TechCrunch、WIRED、Ars Technica、Cool3c、Yahoo 奇摩科技、TechOrange、數位時代、TechNews；另以聚合搜尋比對近期新品、公開測試、重大功能與權限變更。找到 7 個具明確產品狀態變更的候選。
- 第二輪官方定向補查：OpenAI release notes／購物支援頁、Shopify newsroom／changelog、Strands Labs GitHub、Legato 新聞稿、Laytr 官網／隱私政策、Audible newsroom、Apple Developer News。七項皆有官方或產品方資料，未以評論、折扣或傳聞補數。
- 技術限制：部分來源聚合頁或搜尋結果只提供日期；精確時間只在媒體 metadata 可驗證時換算，官方僅有日期者保留日期，不虛構時分。

## 科技候選去重與判定

### T1 OpenAI｜ChatGPT 虛擬試穿與 Favorites

- 查詢：`OpenAI.*virtual try-on|ChatGPT.*Favorites|chatgpt-shopping-try-on`；前 14 份日報無命中，輸出未截斷；再核對同窗 57 列產品表亦無相同事件。
- 時間依據：TechCrunch `2026-10-01 12:21 PDT`，換算 `2026-10-02 03:21 Asia/Taipei`；OpenAI release notes 段落日期 `2026-10-01`。
- 判定：保留。全球上線服飾／配件虛擬試穿與商品收藏，是新的購物功能發布。
- 限制：生成圖不保證實際尺寸、外觀或合身度；需查商家尺寸與退貨政策。
- 來源：https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- 來源：https://help.openai.com/en/articles/11128490-shopping-with-chatgpt-search
- 來源：https://techcrunch.com/2026/10/01/chatgpt-can-now-virtually-try-on-clothes-for-you/

### T2 Shopify｜Canvas

- 查詢：`Shopify.*Canvas|Canvas.*Sidekick|shopify-canvas-launch`；前 14 份日報無命中且未截斷；57 列產品表無相同事件。9/30 的 WebMCP checkout 是不同產品變更。
- 時間依據：TechCrunch `2026-10-01 09:44 PDT`，換算 `2026-10-02 00:44 Asia/Taipei`；Shopify 官方日期 `2026-10-01`。
- 判定：保留。Canvas 讓商家在整店視覺工作區以 Sidekick 對真實 theme code 即時編輯，並分批推出。
- 限制：首發為桌面版，尚不支援第三方 themes、Markets、翻譯、app blocks／embeds 與 theme updates。
- 來源：https://www.shopify.com/news/introducing-canvas
- 來源：https://changelog.shopify.com/posts/design-a-fully-bespoke-store-with-canvas
- 來源：https://techcrunch.com/2026/10/01/shopify-debuts-canvas-a-way-to-build-online-stores-by-chatting-with-ai/

### T3 Amazon／Strands Labs｜Strands Decider 2B

- 查詢：`Amazon.*Strands Decider|Strands Decider.*2B|strands-decider-2b-release`；前 14 份日報無命中且未截斷；同窗產品表無相同事件。
- 時間依據：TechCrunch `2026-10-01 09:49 PDT`，換算 `2026-10-02 00:49 Asia/Taipei`；GitHub repository 在 10/1–10/2 有公開 release 活動。
- 判定：保留。1.9B 參數的開源決策模型針對 agent workflow 的選項分類、評分與信心校準，可本地執行。
- 限制：官方 benchmark 只有 231 個任務，且約 10 題以內差異可能落在重訓雜訊；不把單次榜單成績當成普遍效能保證。
- 來源：https://github.com/strands-labs/strands-decider
- 來源：https://techcrunch.com/2026/10/01/amazon-releases-its-own-jev-clone-as-decision-models-flood-the-web/

### T4 Legato｜Legato Frames

- 查詢：`Legato.*Frames|Frames.*hearing|legato-frames-launch`；前 14 份日報無命中且未截斷；同窗產品表無相同事件。
- 時間依據：產品方新聞稿 `2026-10-01 09:00 ET`，換算 `2026-10-01 21:00 Asia/Taipei`；TechCrunch 同日 06:00 PDT。
- 判定：保留。AI 聽力處理眼鏡正式在美國開賣，起價 999 美元，34 克、10–12 小時電力、無相機且在裝置端處理。
- 限制：產品方宣稱 HearAdvisor 4.6／5 與漏音降低 99%；前者有第三方測試背景，後者仍主要來自公司說法。
- 來源：https://www.globenewswire.com/news-release/2026/10/01/3372968/0/en/legato-frames-the-world-s-first-ai-based-hearing-glasses-are-now-available-in-the-u-s.html
- 來源：https://techcrunch.com/2026/10/01/hearing-tech-startup-legato-launches-its-ai-hearing-glasses/

### T5 Waitery｜Laytr

- 查詢：`Laytr.*save|Waitery.*Laytr|laytr-launch`；前 14 份日報無命中且未截斷；同窗產品表無相同事件。
- 時間依據：TechCrunch `2026-10-02 08:31 PDT`，換算 `2026-10-02 23:31 Asia/Taipei`。
- 判定：保留。Laytr 擴充 read-it-later 概念到文章、影片、PDF、截圖與分頁，跨 Apple 裝置以使用者自己的 iCloud 同步。
- 限制：免費版限 30 個項目；無帳號／無自有伺服器是產品方隱私設計，iCloud 仍受 Apple 條款與使用者設定約束。
- 來源：https://laytr.app/
- 來源：https://laytr.app/privacy
- 來源：https://techcrunch.com/2026/10/02/laytrs-new-app-lets-you-save-anything-you-find-online-not-just-articles-to-read/

### T6 Audible｜Character Guide、Interactive Story、Visual Explorer

- 查詢：`Audible.*Character Guide|Audible.*Interactive Story|audible-interactive-features`；前 14 份日報無命中且未截斷；同窗產品表無相同事件。
- 時間依據：TechCrunch `2026-10-01 06:00 PDT`，換算 `2026-10-01 21:00 Asia/Taipei`；Audible 官方日期 `2026-10-01`。
- 判定：保留。三項功能以限量 beta 向美英用戶推出，包含即時角色辨識、生成式 AI 角色對話與視覺延伸內容。
- 限制：首發作品和市場有限，互動故事並非全面套用整個 Audible 目錄。
- 來源：https://www.audible.com/about/newsroom/the-next-chapter-in-listening-new-ways-to-interact-with-stories-on-audible
- 來源：https://techcrunch.com/2026/10/01/audibles-new-features-let-you-explore-book-worlds-and-even-talk-to-characters/

### T7 Apple｜macOS Full Disk Access 未來控制

- 查詢：`Apple.*Full Disk Access|macOS.*Full Disk Access|full-disk-access-controls`；前 14 份日報無命中且未截斷；同窗產品表無相同事件。
- 時間依據：Apple Developer News 官方發布日期 `2026-10-02`，未提供可核實時分，保留日期格式。
- 判定：保留。Apple 宣布將提高 Full Disk Access 的明示操作門檻，直接以 AI agents 日益自主為風險理由。
- 限制：公告未給實施版本、日期或完整 UI；屬具體權限路線更新，不把未公布細節推定為已生效。
- 來源：https://developer.apple.com/news/?id=p6zjojqw

## 科技排除

- Reddit RSS／Data API、HP OmniBook／ProBook、Anthropic Government、Kindle 2026、OpenAI Dots／Space／Codex reusable environments、Gemini 4 Argon、Instinct Selections 等已在 10/1 或 10/2 日報收錄，不重複。
- OpenAI GPT-6.1 Sol 已在 9/30 收錄；不同媒體後續重述不構成新事件。
- 產品評論、折扣、募資、AI 產業評論與未正式發布的傳聞未列入。

## 全球新聞去重與判定

### G1 Congo Ebola 死亡突破 4,000

- 查詢：`Congo.*Ebola.*4,000|Ebola.*4,018|treatment center.*burned`；前 14 份日報無相同節點命中，輸出未截斷。
- 時間依據：AP `2026-10-02T08:45:09Z`，換算 `2026-10-02 16:45:09 Asia/Taipei`。
- 判定：保留。新增節點是累計死亡達 4,018、病例逾 8,300，且流離失所者營地治療中心遭焚毀。
- 限制：病例與死亡仍可能隨通報補登；中心起火原因及完整損失仍待調查。
- 來源：https://apnews.com/article/4c79b59ec81a08675d2506c9e176d125

### G2 G7 釋出 1 億桶石油與柴油儲備

- 查詢：`G7.*100 million barrels|diesel.*reserve release`；前 14 份日報無相同事件命中，輸出未截斷。
- 時間依據：AP `2026-10-02T14:10:11Z`，換算 `2026-10-02 22:10:11 Asia/Taipei`。
- 判定：保留。G7 決定四個月內釋出逾 1 億桶儲備，柴油在前 20 天前置投放，是新的共同政策行動。
- 限制：各國配額、實際上市節奏及對終端價格的影響尚未完全明朗。
- 來源：https://apnews.com/article/774a360d1646d9ce8aba764fdd9959d2

### G3 美國 9 月僅新增 2.9 萬職位

- 查詢：`U.S..*29,000 jobs|September jobs.*29,000|unemployment.*4.2`；前 14 份日報無相同報告命中，輸出未截斷。
- 時間依據：AP `2026-10-02T12:27:59Z`，換算 `2026-10-02 20:27:59 Asia/Taipei`。
- 判定：保留。9 月非農就業僅增 2.9 萬、失業率 4.2%，明顯低於市場預估。
- 限制：就業數據會修正；AP 文中工資月份敘述可能有上下文歧義，日報只採年增 3% 的可核實數字。
- 來源：https://apnews.com/article/304395b81b9c5717ce64019500a37083

### G4 France 高中抗議與鎮暴部署

- 查詢：`France.*school protests|1,949.*arrests|400 high schools`；前 14 份日報無同一 10/2 升級節點命中，輸出未截斷。
- 時間依據：Le Monde `2026-10-02T10:50:03Z`、AP `2026-10-02T12:33:29Z`，均在窗口內。
- 判定：保留。10/2 新進展是 560 所學校受影響、政府向校園派鎮暴警力，前一日逮捕數字上升至 1,900 人以上。
- 限制：受影響學校、逮捕與受傷數字由不同機構在不同截點發布，不能直接視為同一統計口徑。
- 來源：https://apnews.com/article/02787b4e98a2fe7291f1830510b0567d
- 來源：https://www.lemonde.fr/en/france/article/2026/10/02/facing-worsening-situation-in-high-schools-french-government-sends-riot-police_6758173_7.html

### G5 Strait of Hormuz 油輪遭不明投射物擊中

- 查詢：`Strait of Hormuz.*tanker|tanker.*unknown projectile`；前 14 份日報無相同事件命中，輸出未截斷。
- 時間依據：Reuters 轉載頁標示 `2026-10-02 18:53`（Israel 夏令時間），換算 `2026-10-02 23:53 Asia/Taipei`；事件在全球 24 小時窗內首次可靠公開。
- 判定：保留。油輪離開 Hormuz 時遭不明投射物擊中，一度起火與停電，船員撲滅火勢且未報傷亡或污染。
- 限制：投射物來源、攻擊者與動機未知；UKMTO／船方通報仍是主要依據。
- 來源：https://www.timesofisrael.com/liveblog_entry/tanker-hit-by-unknown-projectile-while-leaving-hormuz-no-casualties-reported/
- 來源：https://www.ukmto.org/

### G6 續報｜Ethiopia 聯邦軍逼近 Mekelle

- 查詢：`Ethiopia|Tigray|Mekelle`；命中 9/25、9/27、9/29 的 Tigray 戰事。前次收錄日期採最近的 `2026-09-29`。
- 時間依據：Reuters 轉載頁 `2026-10-02 08:04 EDT`，即 `2026-10-02T12:04:00Z`／`20:04 Asia/Taipei`。
- 判定：續報。新進展是聯邦軍及盟軍進逼 Mekelle、銀行與商店關閉；民兵宣稱奪取東南方約 20 公里的 Milazat。
- 限制：軍事位置依居民、外交官與交戰方說法；Milazat 易手未獲獨立確認。
- 來源：https://www.marketscreener.com/news/ethiopian-forces-near-tigray-capital-fears-grow-of-wider-conflict-ce785ddad18bf524

### G7 續報｜Ukraine 首次實戰使用 FP-7 彈道飛彈

- 查詢：`Ukraine.*missile|Russian.*Ukraine|Ukraine.*FP-7`；命中 9/22、9/30、10/1 的戰事與飛彈報導。前次收錄日期採 `2026-10-01`。
- 時間依據：The Guardian `2026-10-01 21:47 EDT`，即 `2026-10-02T01:47:00Z`／`09:47 Asia/Taipei`。
- 判定：續報。新進展是 Zelenskyy 首度確認 FP-7 已投入實戰；目標未公開。
- 限制：官方未披露命中位置、戰果與完整性能；其他同日俄境內目標不可全部歸因 FP-7。
- 來源：https://www.theguardian.com/world/2026/oct/02/ukraine-war-briefing-zelenskyy-says-new-ballistic-missile-used-in-combat
- 來源：https://kyivindependent.com/were-not-telling-ukraine-wont-say-what-first-fp-7-ballistic-missile-strike-hit/

### G8 Israel 最高法院推翻 Arab parties 禁選

- 查詢：`Israel.*election|Arab parties|Ofer Cassif`；前 14 份日報無相同裁決命中，輸出未截斷。
- 時間依據：Al Jazeera 與 DW 均標示 `2026-10-02`；原頁未提供可核實時分，因此報告保留日期格式。
- 判定：保留。最高法院恢復 Ra'am、Joint List 參選資格，並以 7 比 2 恢復 Ofer Cassif 資格。
- 限制：Sami Abu Shehadeh 的最終候選狀態仍受撤回／程序安排影響；以法院裁決與候選名單後續公告為準。
- 來源：https://www.aljazeera.com/news/2026/10/2/israels-supreme-court-overturns-election-panel-ban-on-arab-parties
- 來源：https://www.dw.com/en/israel-court-overturns-arab-parties-ban-election/a-79519184

### G9 South Korea 揚言因 North Korean 戰俘披露對 Ukraine 採取措施

- 查詢：`South Korea.*Ukraine|Seoul.*Ukraine|North Korean.*soldiers|North Korean.*prisoners`；前 14 份日報無命中，輸出未截斷。
- 時間依據：AP `2026-10-02T11:26:42Z`，換算 `2026-10-02 19:26:42 Asia/Taipei`。
- 判定：保留。Seoul 指控 Kyiv 違反未公開戰俘轉移談判的保密安排並揚言採取措施；Ukraine 否認存在協議。
- 限制：雙方對是否有保密承諾直接矛盾，South Korea 也未說明措施內容。
- 來源：https://apnews.com/article/330e1b3f1e2c40c274964c6939c03a10

### G10 續報｜North Korea 再射彈道飛彈

- 查詢：`North Korea.*ballistic missile|missile.*sea.*mine blasts`；命中 `2026-09-21` 已收錄的兩枚飛彈事件。
- 時間依據：AP `2026-10-02T22:01:25Z`，換算 `2026-10-03 06:01:25 Asia/Taipei`。
- 判定：續報。新進展是 10/3 清晨從 Wonsan 至少發射一枚彈道飛彈，時點緊接邊境地雷爆炸責任爭議。
- 限制：截點前 South Korea 尚未公布射程與型號；NHK 僅稱可能落在 Japan 專屬經濟區外。
- 來源：https://apnews.com/article/0b5b69e919f9c9a2358f3cd3346649e7

## 全球排除

- U.S. 派出第三艘航空母艦的 AP 報導時間為 `2026-10-01T18:38:27Z`，早於全球窗口，不因後續轉載納入。
- Ethiopia 與 Eritrea 斷交、Sikh 釋放、Tennessee 執行死刑中止及 Brazil 檢察長事件的原始事件或首次可靠發布時間皆早於窗口。
- Brazil 選前領事服務暫停與 Argentina 投資入籍雖在窗口內，但在有限 Top 10 中，跨境能源、傳染病、就業、軍事與法院裁決的全球外溢性較高，列為備選而未收錄。

## 發布收據

- pipeline 內容 commit：`00ca56686c5db7b279156448fecd61781f1dd8b3`。
- GitHub Pages 日期頁、latest 入口與根入口均通過 HTTP 及完整位元組雜湊驗證。
- 公開網址：https://lucaskk.github.io/daily-news/wiki/daily/2026/10/2026-10-03/slides-2026-10-03.html?v=20261003-081500-reader
- 唯一私人 LINE watchdog：`2026-10-03T08:15:48+08:00 Sent LINE message`。
- `daily_news_pipeline.py check --date 2026-10-03`：exit 0，`stage=complete`。
