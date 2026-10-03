---
title: "2026-10-03 每日全球與科技 AI 新聞"
date: 2026-10-03
type: daily-news
status: research-complete
tags: [daily-news, global-news, technology, ai]
---

# 2026-10-03 每日全球與科技 AI 新聞

研究截點｜2026-10-03 08:01:34（Asia/Taipei）
全球新聞 24 小時視窗｜2026-10-02 08:01:34 至 2026-10-03 08:01:34（Asia/Taipei）
科技／AI 產品 14 日視窗｜2026-09-19 08:01:34 至 2026-10-03 08:01:34（Asia/Taipei）

科技產品焦點放在購物試穿、商店設計、agent 決策、聽力穿戴、內容收藏、互動有聲書與 macOS 權限路線。全球新聞則集中於疫情、能源緊急調度、勞動市場、校園抗議，以及多個戰區與選舉制度的新節點。

## 科技／AI 產品 14 日視窗

### T1. ChatGPT 上線服飾虛擬試穿與 Favorites，購物流程從搜尋延伸到比較收藏
公司／產品｜OpenAI｜ChatGPT shopping、virtual try-on、Favorites
發佈時間｜2026-10-02 03:21（Asia/Taipei）
事件／發佈時間基準｜TechCrunch 2026-10-01 12:21 PDT 首次報導；OpenAI release notes 標示 2026-10-01。
續報／去重｜前 14 份日報與最近 14 日產品表無相同產品變更；首次收錄。
重點摘要｜ChatGPT 現可用使用者上傳照片生成服飾與配件的虛擬試穿圖，並將商品存進 Favorites，讓搜尋、視覺比較與後續購買在同一購物介面連接。
為何重要｜這把生成式影像直接放入消費決策，但畫面是模擬而非合身保證。使用者仍須核對尺寸、材質、商家退貨政策與商品頁原始資訊。
關鍵事實：
- 虛擬試穿面向服飾與配件，Favorites 用於保存商品。
- OpenAI 明示生成結果可能與實物外觀或尺寸不同。
來源｜[OpenAI ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) [OpenAI shopping 說明](https://help.openai.com/en/articles/11128490-shopping-with-chatgpt-search) [TechCrunch](https://techcrunch.com/2026/10/01/chatgpt-can-now-virtually-try-on-clothes-for-you/)
相關實體／概念｜OpenAI、ChatGPT、virtual try-on、Favorites、AI shopping
不確定性／歧異｜實際可用性可能依帳號、地區與商品類別分批開放；生成圖不能替代商家尺寸資料。

### T2. Shopify 推出 Canvas，以 Sidekick 對真實 theme code 即時設計整間網店
公司／產品｜Shopify｜Canvas、Sidekick
發佈時間｜2026-10-02 00:44（Asia/Taipei）
事件／發佈時間基準｜TechCrunch 2026-10-01 09:44 PDT；Shopify 官方公告日期 2026-10-01。
續報／去重｜前 14 份日報與最近 14 日產品表無 Canvas 發布事件；首次收錄。
重點摘要｜Canvas 提供整店視覺工作區，商家可以自然語言請 Sidekick 直接修改真實 theme code，並即時檢視頁面與元件變化，而非只生成一次性樣板。
為何重要｜AI 網站生成開始進入可持續維護的商店主題工作流。它能縮短設計迭代，但首發限制意味既有複雜商店不能直接假設完整相容。
關鍵事實：
- 先以桌面版分批推出，修改會落在 Shopify theme code。
- 首發尚不支援第三方 themes、Markets、翻譯、app blocks／embeds 與 theme updates。
來源｜[Shopify newsroom](https://www.shopify.com/news/introducing-canvas) [Shopify changelog](https://changelog.shopify.com/posts/design-a-fully-bespoke-store-with-canvas) [TechCrunch](https://techcrunch.com/2026/10/01/shopify-debuts-canvas-a-way-to-build-online-stores-by-chatting-with-ai/)
相關實體／概念｜Shopify、Canvas、Sidekick、theme code、AI commerce
不確定性／歧異｜推出採分批方式；官方未承諾所有商店或第三方主題立即可用。

### T3. Strands Labs 釋出 1.9B 參數 Strands Decider，讓 agent 在本地做選項評分
公司／產品｜Amazon／Strands Labs｜Strands Decider 2B
發佈時間｜2026-10-02 00:49（Asia/Taipei）
事件／發佈時間基準｜TechCrunch 2026-10-01 09:49 PDT；公開 repository 在 10/1 至 10/2 有 release 活動。
續報／去重｜前 14 份日報與最近 14 日產品表無此模型發布；首次收錄。
重點摘要｜Strands Decider 是約 1.9B 參數的開源決策模型，針對 agent workflow 的候選分類、評分與信心校準設計，可在本地環境執行並減少把決策資料送往外部服務。
為何重要｜小型決策模型可把 agent 的「選哪個動作」拆成可觀察元件，但它不是通用推理能力保證。部署者仍需用自身任務、失敗成本與安全界線評估。
關鍵事實：
- 模型與範例程式透過 Strands Labs GitHub 公開。
- 官方 benchmark 只有 231 個任務，小幅名次差異可能落在重訓雜訊。
來源｜[Strands Labs GitHub](https://github.com/strands-labs/strands-decider) [TechCrunch](https://techcrunch.com/2026/10/01/amazon-releases-its-own-jev-clone-as-decision-models-flood-the-web/)
相關實體／概念｜Amazon、Strands Labs、agent、decision model、local inference
不確定性／歧異｜公開 benchmark 規模有限，不能外推所有代理任務與硬體環境的效能。

### T4. Legato Frames 在美國開賣，把 AI 聽力處理放進無相機眼鏡
公司／產品｜Legato｜Legato Frames
發佈時間｜2026-10-01 21:00（Asia/Taipei）
事件／發佈時間基準｜產品方新聞稿 2026-10-01 09:00 ET；TechCrunch 同日發布。
續報／去重｜前 14 份日報與最近 14 日產品表無相同上市事件；首次收錄。
重點摘要｜Legato Frames 正式在美國供貨，起價 999 美元，將波束成形與 AI 聲音處理整合到 34 克眼鏡。產品無相機，主要處理在裝置端完成，標稱電力 10 至 12 小時。
為何重要｜聽力輔助正從傳統助聽器擴展到日常穿戴外型。價格、舒適度、語音清晰度與漏音表現仍需獨立長期測試，不能只依公司示範判斷。
關鍵事實：
- 產品起價 999 美元，首發市場為美國。
- 公司宣稱 HearAdvisor 評分 4.6／5、漏音降低 99%。
來源｜[Legato 新聞稿](https://www.globenewswire.com/news-release/2026/10/01/3372968/0/en/legato-frames-the-world-s-first-ai-based-hearing-glasses-are-now-available-in-the-u-s.html) [TechCrunch](https://techcrunch.com/2026/10/01/hearing-tech-startup-legato-launches-its-ai-hearing-glasses/)
相關實體／概念｜Legato、hearing glasses、on-device AI、assistive technology
不確定性／歧異｜HearAdvisor 有第三方測試背景；99% 漏音改善仍主要來自公司聲明，台灣供貨未公布。

### T5. Laytr 把 read-it-later 擴充到影片、PDF、截圖與分頁，資料走使用者 iCloud
公司／產品｜Waitery｜Laytr
發佈時間｜2026-10-02 23:31（Asia/Taipei）
事件／發佈時間基準｜TechCrunch 2026-10-02 08:31 PDT 首次報導。
續報／去重｜前 14 份日報與最近 14 日產品表無相同發布；首次收錄。
重點摘要｜Laytr 可保存文章、影片、PDF、截圖與瀏覽器分頁，並在 Apple 裝置間透過使用者自己的 iCloud 同步。產品強調不要求建立 Laytr 帳號，也不維護自有內容伺服器。
為何重要｜資訊收藏工具不再只處理文字文章，能減少多種媒體散落在分頁、照片與書籤中的問題。隱私設計仍取決於 iCloud 設定、分享內容與 Apple 平台條款。
關鍵事實：
- 支援 iPhone、iPad 與 Mac 的跨裝置收藏。
- 免費版最多保存 30 個項目。
來源｜[Laytr 官網](https://laytr.app/) [Laytr privacy](https://laytr.app/privacy) [TechCrunch](https://techcrunch.com/2026/10/02/laytrs-new-app-lets-you-save-anything-you-find-online-not-just-articles-to-read/)
相關實體／概念｜Waitery、Laytr、iCloud、read-it-later、privacy
不確定性／歧異｜無自有伺服器是產品方描述；實際資料路徑仍須依 Apple 帳號與同步設定判斷。

### T6. Audible 測試角色辨識、AI 角色對話與視覺探索三項互動功能
公司／產品｜Audible｜Character Guide、Interactive Story、Visual Explorer
發佈時間｜2026-10-01 21:00（Asia/Taipei）
事件／發佈時間基準｜TechCrunch 2026-10-01 06:00 PDT；Audible 官方公告日期 2026-10-01。
續報／去重｜前 14 份日報與最近 14 日產品表無相同 beta 發布；首次收錄。
重點摘要｜Audible 在美國與英國限量測試三項功能：即時辨識角色與關係、讓讀者和生成式 AI 角色互動，以及以地圖或圖片延伸故事世界。
為何重要｜有聲書從線性播放走向可查詢與互動敘事，但生成內容需避免劇透、角色失真與版權問題。首發作品有限，不能視為整個目錄已全面更新。
關鍵事實：
- Character Guide 提供隨閱讀進度變動的角色資訊。
- Interactive Story 與 Visual Explorer 只在部分作品、帳號與市場 beta。
來源｜[Audible newsroom](https://www.audible.com/about/newsroom/the-next-chapter-in-listening-new-ways-to-interact-with-stories-on-audible) [TechCrunch](https://techcrunch.com/2026/10/01/audibles-new-features-let-you-explore-book-worlds-and-even-talk-to-characters/)
相關實體／概念｜Audible、Amazon、audiobook、generative AI、interactive story
不確定性／歧異｜測試範圍與正式推出時間未定，角色回應品質需逐作品觀察。

### T7. Apple 預告提高 macOS Full Disk Access 的操作門檻，直接點名 AI agents 風險
公司／產品｜Apple｜macOS Full Disk Access controls
發佈時間｜2026-10-02（官方僅提供日期）
事件／發佈時間基準｜Apple Developer News 官方發布日期 2026-10-02。
續報／去重｜前 14 份日報與最近 14 日產品表無相同權限路線更新；首次收錄。
重點摘要｜Apple 表示未來 macOS 將要求使用者以更明確的動作授予 Full Disk Access，理由包含 AI agents 能自主存取大量資料。公告是具體安全路線，尚非已生效的版本更新。
為何重要｜代理工具取得全磁碟權限後的影響遠高於一般單檔存取。提高授權摩擦可降低誤授權，但企業部署、輔助工具與備份軟體也需要調整流程。
關鍵事實：
- Apple 將 Full Disk Access 與 AI agent 自主操作風險直接連結。
- 實施版本、日期及完整使用者介面尚未公布。
來源｜[Apple Developer News](https://developer.apple.com/news/?id=p6zjojqw)
相關實體／概念｜Apple、macOS、Full Disk Access、AI agents、least privilege
不確定性／歧異｜公告屬未來權限路線，不代表今日已改變所有 macOS 裝置行為。

## 全球 Top 10

### 1. Congo Ebola 死亡突破 4,000，流離失所者營地治療中心又遭焚毀
發佈時間｜2026-10-02 16:45:09（Asia/Taipei）
事件／發佈時間基準｜AP 2026-10-02 08:45:09 UTC 發布最新疫情與治療中心事件。
續報／去重｜前 14 份日報無同一 4,000 死亡節點；首次收錄。
重點摘要｜Congo Ebola 疫情累計死亡達 4,018、病例逾 8,300，至少 50 名醫護死亡。一座設於流離失所者營地的治療中心遭焚毀，約 19,000 人離開營地。
為何重要｜死亡里程碑與醫療設施被毀同時發生，表示疫情控制正遭安全與人口流動雙重削弱。通報仍可能補登，不能把目前數字視為最終規模。
關鍵事實：
- 累計 4,018 人死亡、逾 8,300 例。
- 治療中心起火原因仍待調查，外逃人口增加追蹤困難。
來源｜[Associated Press](https://apnews.com/article/4c79b59ec81a08675d2506c9e176d125)
相關實體／概念｜DR Congo、Ebola、WHO、health workers、displacement camps
不確定性／歧異｜病例與死亡會因遲報修正；中心遭焚毀的責任尚未確認。

### 2. G7 將釋出逾 1 億桶石油與柴油儲備，柴油在 20 天內優先投放
發佈時間｜2026-10-02 22:10:11（Asia/Taipei）
事件／發佈時間基準｜AP 2026-10-02 14:10:11 UTC 報導 G7 共同決定。
續報／去重｜前 14 份日報無相同共同釋儲行動；首次收錄。
重點摘要｜G7 同意在四個月內釋出超過 1 億桶石油與柴油儲備，並把柴油供應集中在前 20 天，希望緩解燃料價格與供應緊張。
為何重要｜共同釋儲是對能源衝擊的直接政策工具，可短期增加流動供應，但無法替代持久的產量、航運或煉製能力。實際降價幅度取決於配額與市場反應。
關鍵事實：
- 總量超過 1 億桶，預計分四個月投放。
- 柴油採前置投放，反映運輸與工業燃料壓力。
來源｜[Associated Press](https://apnews.com/article/774a360d1646d9ce8aba764fdd9959d2)
相關實體／概念｜G7、strategic reserves、diesel、oil prices、energy security
不確定性／歧異｜各國實際配額、釋出日期及終端價格效果仍待公布與觀察。

### 3. 美國 9 月僅新增 2.9 萬職位，失業率維持 4.2%
發佈時間｜2026-10-02 20:27:59（Asia/Taipei）
事件／發佈時間基準｜AP 2026-10-02 12:27:59 UTC 發布 9 月就業報告摘要。
續報／去重｜前 14 份日報無相同月份報告；首次收錄。
重點摘要｜美國 9 月非農就業只增加 29,000 人，低於市場預期約 84,000 人；失業率為 4.2%。8 月增幅修正為 133,000，7 月則減少 10,000。
為何重要｜就業放緩會影響聯準會利率、市場與家庭收入判斷。單月數據容易修正，應和薪資、工時與後續月份一起評估，不宜直接宣告衰退。
關鍵事實：
- 9 月新增 29,000，明顯低於預期。
- 平均工資年增約 3%，但月份敘述需以正式表格為準。
來源｜[Associated Press](https://apnews.com/article/304395b81b9c5717ce64019500a37083)
相關實體／概念｜United States、nonfarm payrolls、unemployment、Federal Reserve
不確定性／歧異｜就業數字仍會修正；AP 內文的工資月份文字有上下文歧義。

### 4. France 高中抗議擴大至 560 所學校，政府部署鎮暴警力
發佈時間｜2026-10-02 18:50:03（Asia/Taipei）
事件／發佈時間基準｜Le Monde 2026-10-02 10:50:03 UTC、AP 12:33:29 UTC 報導 10/2 升級。
續報／去重｜前 14 份日報無同一 10/2 升級節點；首次收錄。
重點摘要｜France 高中抗議持續擴散，政府表示 560 所學校受到影響，並向部分校園部署鎮暴警力。前一日全國逮捕人數超過 1,900，警察受傷數也上升。
為何重要｜教育資源與課時爭議已升級成全國公共秩序問題。不同來源的逮捕、受傷與學校數字截點不同，需避免把它們當成同一時間的精確總表。
關鍵事實：
- 10/2 有 560 所學校受影響。
- AP 報導前一日逮捕 1,900 人以上、305 名警員受傷。
來源｜[Associated Press](https://apnews.com/article/02787b4e98a2fe7291f1830510b0567d) [Le Monde](https://www.lemonde.fr/en/france/article/2026/10/02/facing-worsening-situation-in-high-schools-french-government-sends-riot-police_6758173_7.html)
相關實體／概念｜France、high schools、protests、riot police、education policy
不確定性／歧異｜官方與媒體統計更新時間不同；個別暴力事件責任仍須調查。

### 5. 油輪離開 Strait of Hormuz 時遭不明投射物擊中，無人傷亡
發佈時間｜2026-10-02 23:53（Asia/Taipei）
事件／發佈時間基準｜Reuters 轉載頁於 2026-10-02 18:53 Israel 夏令時間報導，換算為 23:53 Asia/Taipei；事件在全球 24 小時窗內首次可靠公開。
續報／去重｜前 14 份日報無相同船舶受擊事件；首次收錄。
重點摘要｜一艘油輪離開 Strait of Hormuz 時遭不明投射物擊中，船上出現小型火災與停電，船員已撲滅火勢，未報傷亡或環境污染。
為何重要｜Hormuz 是全球能源運輸關鍵航道，單一攻擊也會影響航運風險與保險成本。現階段不能把事件歸因任何國家或組織。
關鍵事實：
- 船員自行控制火勢，沒有通報人員傷亡。
- 投射物類型、來源及動機尚未查明。
來源｜[Reuters／Times of Israel](https://www.timesofisrael.com/liveblog_entry/tanker-hit-by-unknown-projectile-while-leaving-hormuz-no-casualties-reported/) [UKMTO](https://www.ukmto.org/)
相關實體／概念｜Strait of Hormuz、tanker、UKMTO、maritime security、shipping insurance
不確定性／歧異｜歸責未知；初步無污染的說法仍需後續船體檢查確認。

### 6. 續報｜Ethiopia 聯邦軍逼近 Mekelle，Tigray 區域戰爭風險升高
發佈時間｜2026-10-02 20:04（Asia/Taipei）
事件／發佈時間基準｜Reuters 轉載頁 2026-10-02 08:04 EDT；居民與外交消息人士描述聯邦軍位置。
續報／去重｜前次收錄 2026-09-29，當時新增鄰國介入指控與 Erebti 易手；今日新增軍隊進逼 Mekelle、城市商業關閉及 Milazat 易手說法。
重點摘要｜Ethiopia 聯邦軍與盟軍據報已進入可威脅 Tigray 首府 Mekelle 的位置，城內銀行與商店關閉。盟軍民兵宣稱奪取 Mekelle 東南約 20 公里的 Milazat。
為何重要｜若首府遭直接攻擊，2022 Pretoria 和平協議的殘餘框架可能快速崩解，並增加 Eritrea、Sudan 與其他鄰國被捲入的風險。
關鍵事實：
- 居民與外交官稱聯邦軍及盟軍逼近 Mekelle。
- Milazat 易手來自交戰方民兵聲明，未獨立驗證。
來源｜[Reuters／MarketScreener](https://www.marketscreener.com/news/ethiopian-forces-near-tigray-capital-fears-grow-of-wider-conflict-ce785ddad18bf524)
相關實體／概念｜Ethiopia、Tigray、Mekelle、TPLF、Pretoria agreement
不確定性／歧異｜前線位置與控制權缺乏獨立查證，通訊限制可能使情勢快速變動。

### 7. 續報｜Ukraine 首次實戰使用 FP-7 彈道飛彈，但拒絕公開目標
發佈時間｜2026-10-02 09:47（Asia/Taipei）
事件／發佈時間基準｜The Guardian 2026-10-01 21:47 EDT 首次完整報導 Zelenskyy 的確認。
續報／去重｜前次收錄 2026-10-01 的 Russia 對 Ukraine 能源設施攻擊；今日新增 Ukraine 自製 FP-7 首次實戰使用的武器里程碑。
重點摘要｜Zelenskyy 確認 Ukraine 已首次在實戰中使用 FP-7 彈道飛彈，但政府不透露攻擊目標。這顯示 Kyiv 正嘗試擴充可自主使用的遠程打擊能力。
為何重要｜本土飛彈可降低對外援武器使用限制的依賴，並改變縱深目標的風險計算。但在目標、命中與性能未公開前，不能推定戰果。
關鍵事實：
- 首次使用由 Zelenskyy 確認。
- 目標、射程運用與損害細節均未公開。
來源｜[The Guardian](https://www.theguardian.com/world/2026/oct/02/ukraine-war-briefing-zelenskyy-says-new-ballistic-missile-used-in-combat) [Kyiv Independent](https://kyivindependent.com/were-not-telling-ukraine-wont-say-what-first-fp-7-ballistic-missile-strike-hit/)
相關實體／概念｜Ukraine、Russia、FP-7、ballistic missile、long-range strike
不確定性／歧異｜其他同日俄境內攻擊不能全部歸因 FP-7；戰果未獲獨立核實。

### 8. Israel 最高法院推翻選委會禁令，恢復 Arab parties 與 Ofer Cassif 參選資格
發佈時間｜2026-10-02（來源僅提供日期）
事件／發佈時間基準｜Al Jazeera 與 DW 均於 2026-10-02 報導法院裁決，未提供可核實時分。
續報／去重｜前 14 份日報無相同法院裁決；首次收錄。
重點摘要｜Israel 最高法院一致恢復 Ra'am 與 Joint List 的選舉資格，並以 7 比 2 恢復議員 Ofer Cassif 參選，推翻中央選舉委員會的禁令。
為何重要｜裁決直接影響 Arab voters 的代表權與選舉競爭，也再次凸顯選委會政治決定與司法審查的張力。個別候選人的程序狀態仍須看最終名單。
關鍵事實：
- Ra'am 與 Joint List 的恢復決定為一致裁決。
- Ofer Cassif 以 7 比 2 恢復資格。
來源｜[Al Jazeera](https://www.aljazeera.com/news/2026/10/2/israels-supreme-court-overturns-election-panel-ban-on-arab-parties) [DW](https://www.dw.com/en/israel-court-overturns-arab-parties-ban-election/a-79519184)
相關實體／概念｜Israel、Supreme Court、Ra'am、Joint List、Ofer Cassif、election law
不確定性／歧異｜Sami Abu Shehadeh 的最終候選安排仍受撤回與名單程序影響。

### 9. South Korea 因 North Korean 戰俘消息外洩揚言對 Ukraine 採取措施
發佈時間｜2026-10-02 19:26:42（Asia/Taipei）
事件／發佈時間基準｜AP 2026-10-02 11:26:42 UTC 報導 Seoul 與 Kyiv 的公開爭議。
續報／去重｜前 14 份日報無相同外交爭議；首次收錄。
重點摘要｜South Korea 指控 Ukraine 在 North Korean 戰俘轉移談判中違反保密安排，並表示將採取未具體說明的措施。Ukraine 否認雙方曾達成保密協議。
為何重要｜爭議牽涉戰俘保護、對 Russia 戰場上的 North Korean 部隊情報，以及 Seoul 與 Kyiv 的合作信任。雙方說法直接衝突，不能把任何一方版本當成已證實事實。
關鍵事實：
- Seoul 稱 Kyiv 未遵守不公開談判的承諾。
- Kyiv 否認存在保密協議；South Korea 未說明可能措施。
來源｜[Associated Press](https://apnews.com/article/330e1b3f1e2c40c274964c6939c03a10)
相關實體／概念｜South Korea、Ukraine、North Korea、prisoners of war、diplomatic trust
不確定性／歧異｜保密承諾是否存在沒有共同文件公開，後續措施內容不明。

### 10. 續報｜North Korea 從 Wonsan 再射彈道飛彈，邊境地雷爭議同步升溫
發佈時間｜2026-10-03 06:01:25（Asia/Taipei）
事件／發佈時間基準｜AP 2026-10-02 22:01:25 UTC；South Korea 軍方在截點前確認至少一枚發射。
續報／去重｜前次收錄 2026-09-21 的兩枚飛彈發射；本次是新的 10/3 發射，且發生在邊境地雷爆炸責任爭議之後。
重點摘要｜North Korea 從東岸 Wonsan 地區向海上至少發射一枚彈道飛彈。South Korea 隨即提高監視並與 U.S.、Japan 分享資料；NHK 稱飛彈可能落在 Japan 專屬經濟區外。
為何重要｜新發射把武器測試與無軍事熱線下的邊境地雷爭議疊加，增加誤判風險。射程與型號尚未公布，不能據早期通報判斷能力升級。
關鍵事實：
- South Korea 軍方偵測到至少一枚從 Wonsan 發射。
- Japan 初步資訊指向其 EEZ 外，完整飛行資料尚待公布。
來源｜[Associated Press](https://apnews.com/article/0b5b69e919f9c9a2358f3cd3346649e7)
相關實體／概念｜North Korea、South Korea、Wonsan、ballistic missile、DMZ mines
不確定性／歧異｜發射數量、型號、射程與落點仍可能更新；地雷責任另有雙方爭議。

## 後續追蹤

- Congo 治療中心被毀後的接觸者追蹤、醫護替補與營地人口流向。來源：[Associated Press](https://apnews.com/article/4c79b59ec81a08675d2506c9e176d125)
- G7 各國實際釋儲配額、柴油到市時間及價格效果。來源：[Associated Press](https://apnews.com/article/774a360d1646d9ce8aba764fdd9959d2)
- Ethiopia 軍隊是否進入 Mekelle、是否恢復 Pretoria framework；Ukraine 是否公開 FP-7 目標與可驗證戰果。來源：[Reuters／MarketScreener](https://www.marketscreener.com/news/ethiopian-forces-near-tigray-capital-fears-grow-of-wider-conflict-ce785ddad18bf524) [The Guardian](https://www.theguardian.com/world/2026/oct/02/ukraine-war-briefing-zelenskyy-says-new-ballistic-missile-used-in-combat)
- Apple 公布 Full Disk Access 新控制的 macOS 版本、日期與企業部署方式。來源：[Apple Developer News](https://developer.apple.com/news/?id=p6zjojqw)
