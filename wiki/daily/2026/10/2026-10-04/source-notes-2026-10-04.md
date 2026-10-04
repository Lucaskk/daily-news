---
title: "2026-10-04 每日全球與科技 AI 新聞來源筆記"
type: source-notes
date: 2026-10-04
cutoff: 2026-10-04T08:02:10+08:00
status: research
tags: [daily-news, sources, provenance]
---

# 2026-10-04 來源筆記

## 研究時間窗

- 研究截點：`2026-10-04 08:02:10 Asia/Taipei`（`2026-10-04 00:02:10 UTC`）。
- 全球新聞 24 小時窗：`2026-10-03 08:02:10` 至 `2026-10-04 08:02:10 Asia/Taipei`（`2026-10-03 00:02:10` 至 `2026-10-04 00:02:10 UTC`）。
- 科技／AI 產品 14 日窗：`2026-09-20 08:02:10` 至 `2026-10-04 08:02:10 Asia/Taipei`（`2026-09-20 00:02:10` 至 `2026-10-04 00:02:10 UTC`）。
- 去重範圍限定 D-14 至 D-1：`2026-09-20` 至 `2026-10-03` 的 14 份日報；不查更早日報、來源筆記或完整歷史表。
- 選題前執行 `build_product_news_ledger.py --cutoff 2026-10-04T08:02:10+08:00`，產生 61 列 `product-news-recent-14d.md`。

## 科技來源掃描

- 第一輪廣泛掃描：CSV 啟用來源 Engadget、The Verge、TechCrunch、WIRED、Ars Technica、Cool3c、Yahoo 奇摩科技、TechOrange、數位時代、TechNews；另掃描 Techmeme 與官方搜尋結果。找到 4 個具明確可用性、排序、開源發布或修復狀態變更的候選。
- 第二輪官方定向補查：YouTube 官方 Community 公告、Meta Muse Gadgets 專案頁、AT&T 支援頁；Bitchat 下架以 Jack Dorsey 公開的 Apple 通知及 TechCrunch／PTI 交叉查證。Apple、Google 與印度 IT 部門未對 TechCrunch 回覆，已保留限制。
- Engadget 首頁亦檢查 Kindle 舊改版、評論、導購與操作教學；Cool3c 首頁／分類頁沒有找到比下列四項更明確且未收錄的產品變更。Vessev VS-9 是試乘既有單一原型與未定量產路線，排除。

## 科技候選去重與判定

### T1 Block／Bitchat｜印度 App Store 與 Google Play 下架

- 查詢：`Bitchat.*India|India.*Bitchat|bitchat-india-removal`；前 14 份日報無命中，輸出未截斷；再核對同窗 61 列產品表亦無相同事件。
- 時間依據：TechCrunch `2026-10-03 08:02 PDT`，換算 `2026-10-03 23:02 Asia/Taipei`；PTI／NDTV 同日 21:52 IST。
- 判定：保留。Bitchat 從印度 Apple App Store 與 Google Play 消失，TestFlight 與網站亦受限，是實際可用性重大變更。
- 限制：Apple 通知由 Dorsey 公開；Google、印度 IT 部門與 ISP 未回覆，Google Play／網站是否依同一命令行動尚未確認。
- 來源：https://techcrunch.com/2026/10/03/jack-dorseys-bitchat-disappears-from-app-stores-in-india-after-government-order/
- 來源：https://www.ndtv.com/india-news/bitchat-removed-from-apples-india-app-store-after-centres-order-12135008

### T2 YouTube｜Shorts 原創內容排序更新

- 查詢：`YouTube.*Shorts.*original|Shorts.*recommendation|youtube-shorts-original-content`；前 14 份日報無命中且未截斷；61 列產品表無相同事件。
- 時間依據：YouTube 官方 Community 公告日期 `2026-10-01`；頁面顯示時間但未提供可核實時區，日報保留日期。
- 判定：保留。Shorts 推薦系統提高原創內容權重，主要聚合或未增添實質內容的重傳頻道可能降低分發。
- 限制：官方未公開演算法權重、量化門檻或完整 rollout 範圍；不是全面禁止二創。
- 來源：https://support.google.com/youtube/blog/470890423/prioritizing-original-content-on-shorts?hl=en

### T3 Meta｜Muse Gadgets 與 Home Link

- 查詢：`Meta.*Muse Gadgets|Muse.*Home Link|muse-gadgets-launch`；前 14 份日報無命中且未截斷；61 列產品表無相同事件。9/28 的 Muse Charm 是不同硬體事件。
- 時間依據：TechCrunch `2026-10-02 17:45 PDT`，換算 `2026-10-03 08:45 Asia/Taipei`。
- 判定：保留。Meta 開源 Muse Gadgets firmware 與 Linux SDK，讓 Raspberry Pi／ESP32 等硬體連接 Muse；另製作 5,000 個 Home Link 贈送訂閱者。
- 限制：Home Link 數量有限、尚需數週出貨；開源專案不是 Meta 承諾量產的完整消費硬體系列。
- 來源：https://techcrunch.com/2026/10/02/meta-wants-you-to-build-your-own-muse-gadget/
- 來源：https://gadgets.muse.ai/

### T4 Apple／AT&T｜iPhone 18 Pro Max 網路問題修復與換機

- 查詢：`Apple.*iPhone 18 Pro Max.*AT.T|iOS 27.0.1.*AT.T|iphone18-att-network-fix`；前 14 份日報無命中且未截斷；61 列產品表無相同事件。
- 時間依據：Engadget 標示 `2026-10-02 22:10 EST`，依頁面字面換算 `2026-10-03 11:10 Asia/Taipei`；AT&T 支援頁最後更新日期 `2026-10-02`。
- 判定：保留。Apple 發布 iOS 27.0.1 與 carrier settings update 防止問題；已失去服務的少數裝置需向 Apple 或 AT&T 申請更換。
- 限制：AT&T 支援頁說更新可幫助防止問題，Engadget／Apple 聲明則說已受影響裝置無法靠軟體恢復；兩者適用情境不同，不能混寫成更新可修復所有裝置。
- 來源：https://www.att.com/support/article/wireless/KM1062174/
- 來源：https://www.engadget.com/2276489/apple-att-network-bug-iphone-18-pro-max/
- 來源：https://www.macrumors.com/2026/10/02/apple-statement-on-iphone-18-pro-max-att-issue/

## 科技排除

- 10/3 已收錄 ChatGPT 試穿、Shopify Canvas、Strands Decider、Legato Frames、Laytr、Audible beta 與 macOS Full Disk Access 路線，不重複。
- OpenAI DevDay 9/29 的 Dots、GPT-6.1 Sol、Codex cloud、ChatGPT Space 等已在 9/30–10/1 分別收錄；10/3 的評論文章不構成新發布。
- Vessev VS-9 為既有單一原型試乘與未定量產方向；Capcom AI 開發說法、前 OpenAI 員工安全評論、折扣與教學文章均不是合格產品狀態變更。

## 全球 Top 10 時間、去重與判定

### G1 續報｜Russia 攻擊 Ukraine 造成六死並損壞 Kyiv Northern Bridge

- 查詢：`Ukraine.*Northern Bridge|Kyiv.*Northern Bridge|bridge.*six killed` 無窄命中；廣查 `Ukraine|Kyiv` 命中多條不同事件，最近是 2026-10-03 的 FP-7 首次實戰使用。
- 時間依據：AP `2026-10-03 09:39:55 UTC`，即 `2026-10-03 17:39:55 Asia/Taipei`。
- 續報判定：前次 2026-10-03 收錄 Ukraine 使用 FP-7；今日新增是 Russia 另一輪攻擊造成至少六死、Northern Bridge 受損及交通中斷，屬不同攻擊與民生節點。
- 限制：Russia 對攻擊目標與後續行動的聲明未獲 Ukraine 獨立確認；傷亡仍可能調整。
- 來源：https://apnews.com/article/2cb9344e23445f69d5072ce661231eb3

### G2 Manchester 猶太會堂氯氣炸彈計畫案

- 查詢：`Manchester.*chlorine bomb|Iranian men.*synagogue|Heaton Park.*plot`；前 14 份日報無命中。
- 時間依據：AP `2026-10-03 13:49:50 UTC`，即 `2026-10-03 21:49:50 Asia/Taipei`。
- 判定：首次收錄。英國檢方指兩名伊朗男子監視 Heaton Park Hebrew Congregation 與 Jewish Museum，第三人涉嫌自 Iran 指揮並提供氯氣炸彈指示。
- 限制：案件仍在司法程序，兩名被告尚未答辯；指揮鏈與攻擊能力是檢方指控，不是定罪事實。警方表示目前沒有持續中的威脅。
- 來源：https://apnews.com/article/65bb5f95964b9df386790266cddfc6ce

### G3 Latvia 國會選舉

- 查詢：`Latvia.*parliament|Latvians.*election|Kulbergs.*vote`；前 14 份日報無命中。
- 時間依據：AP `2026-10-03 08:09:36 UTC`，即 `2026-10-03 16:09:36 Asia/Taipei`；收錄的是投票開始與安全部署，結果在截點後才可能形成新事件。
- 判定：首次收錄。約 156 萬名合格選民改選 100 席 Saeima，政黨須跨過 5% 門檻；German Eurofighters 協助空域安全。
- 限制：截點前尚無最終結果；Latvia 安全部門表示未見系統性外部干預，不等於排除所有個別影響活動。
- 來源：https://apnews.com/article/6026bf32a75acf1f671da1e6f34bb520

### G4 續報｜Spain 多城住房抗議與 Valencia 警民衝突

- 查詢：`Spain.*housing protests|Maricarmen.*housing|Valencia.*rent protest` 命中 2026-09-28 的 Maricarmen 驅離與示威營地。
- 時間依據：抗議實際發生於 `2026-10-03`，落在全球視窗；AP 頁面較早建立，因此收錄依據是事件日，不以頁面更新時間當新事件。
- 續報判定：前次 2026-09-28 收錄個案驅離與 Madrid 露營；今日新增是議會否決緊急住房措施後，多城數萬人上街，Valencia 警方在防線遭突破後使用催淚瓦斯與橡膠彈。
- 限制：各城人數與執法細節仍可能更新；初步未報示威者受傷。
- 來源：https://apnews.com/article/a34d8626f4c07ec74b7eee8bf22e381c

### G5 Kenya Salama 多車事故造成 17 死

- 查詢：`Kenya.*17.*pilgrims|Salama.*crash|Mombasa.*pilgrims`；前 14 份日報無命中。
- 時間依據：AP `2026-10-03 08:34:14 UTC`，即 `2026-10-03 16:34:14 Asia/Taipei`。
- 判定：首次收錄。Salama 附近卡車超車失敗引發多車事故，廂型車司機與 16 名多為 Catholic pilgrims 的乘客死亡。
- 限制：初步事故原因來自警方；道路設計、車速與機械狀況仍待調查。
- 來源：https://apnews.com/article/d2f788a5ab157acec3b5caa3afd5330f

### G6 續報｜Houthis 宣稱攻擊 Riyadh Aramco 設施

- 查詢：`Houthis.*Aramco.*Riyadh|Aramco.*missiles.*drones|riyadh-aramco-attack` 無窄命中；廣查 `Houthi|Riyadh|Aramco` 命中 2026-09-20、09-22、09-23、09-26 與 09-30 的不同節點。
- 時間依據：Reuters 轉載頁發布於 `2026-10-03`；頁面時區未提供可核實資訊，日報只保留日期。
- 續報判定：前次相關攻擊收錄是 2026-09-20 的 Riyadh／Yanbu 攻擊宣稱；今日新增是 Houthis 宣稱以飛彈與 drones 攻擊 Riyadh Aramco 設施，理由為報復 Saudi 對 Yemen 的攻擊。
- 限制：Reuters 報導確認的是 Houthis 的聲明，不代表命中與損害已獨立證實；Saudi 與 Aramco 截點前未公布完整核實結果。
- 來源：https://www.investing.com/news/commodities-news/yemens-houthis-say-they-attacked-aramco-facility-in-riyadh-with-missiles-drones-4930877

### G7 續報｜Gaza City 公寓遭 Israeli strike 造成五死

- 查詢：`Gaza.*five.*women|Israeli strike.*five.*Gaza|gaza-apartment-strike` 無窄命中；廣查 `Gaza|Israeli strike` 命中 2026-10-01 的另一場 Gaza 攻擊。
- 時間依據：AP `2026-10-03 06:19:06 UTC`，即 `2026-10-03 14:19:06 Asia/Taipei`；Reuters／El Pais `2026-10-03 14:32:58 UTC` 提供後續交叉報導。
- 續報判定：前次 2026-10-01 收錄不同地點與傷亡的攻擊；今日新增是 Gaza City 公寓受擊，五名死者中有四名女性，另有兩人屬當地 Christian minority。
- 限制：現場傷亡由醫療與地方來源整理；攻擊目標與 Israeli military 的即時說明仍不足。
- 來源：https://apnews.com/article/a442d25ea0886133c080fbd749440cf2
- 來源：https://elpais.com/internacional/2026-10-03/varios-muertos-por-un-ataque-israeli-en-ciudad-de-gaza.html

### G8 Libya 統一談判受 Saddam Haftar 無人機攻擊指控衝擊

- 查詢：`Libya.*Saddam Haftar|Zawiya.*unity talks|Haftar.*drone attacks`；前 14 份日報無命中。
- 時間依據：The Guardian `2026-10-03 05:00 EDT`，即 `2026-10-03 17:00 Asia/Taipei`，首次可靠公開談判受阻與嫌疑人供詞內容。
- 判定：首次收錄。舊背景是 August 的 drone attacks 與 9/5 arrests；視窗內的新節點是 GNU 消息人士表示難以再與 Saddam Haftar 合作，美國支持的安全力量整合方案因此受阻。
- 限制：Haftar 關聯主要來自遭逮捕嫌疑人供詞與 GNU 消息人士，尚非公開司法裁判；不能把 August 攻擊誤寫成 10/3 新攻擊。
- 來源：https://www.theguardian.com/world/2026/oct/03/libyan-unity-talks-warlord-son-linked-drone-attack-khalifa-haftar

### G9 ShinyHunters 涉案關鍵人物在 Jordan 被拘留

- 查詢：`ShinyHunters.*Jordan|Saif al-Din Khader|FBI.*ShinyHunters` 與廣查 `ShinyHunters|FBI data theft`；前 14 份日報均無命中。
- 時間依據：Reuters 轉載頁 `2026-10-03 11:15 EDT`，即 `2026-10-03 23:15 Asia/Taipei`。
- 判定：首次收錄。兩名消息人士稱 Saif al-Din Khader（Rey）在 Jordan 被拘留，正協助辨識其他 hackers；FBI 表示調查持續，但拒絕確認個案細節。
- 限制：合作內容與拘留程序來自匿名消息人士，尚無公開起訴文件完整佐證。
- 來源：https://www.marketscreener.com/news/key-shinyhunters-hacker-detained-in-jordan-is-cooperating-sources-say-ce785ddbdd81f22d
- 來源：https://www.aol.com/articles/exclusive-key-shinyhunters-hacker-detained-151707000.html

### G10 續報｜North Korea 將 10/3 發射辨識為可變軌中程飛彈

- 查詢：`North Korea.*intermediate-range|missile.*maneuverable|Wonsan.*700 kilometers` 無窄命中；廣查 `North Korea|Wonsan` 命中 2026-10-03 的同次發射初報。
- 時間依據：前一日 AP 初報為 `2026-10-02 22:01:25 UTC`，早於本次下界，不作今天時間基礎；The Hindu／PTI 於 `2026-10-03 20:51 IST`（`2026-10-03 23:21 Asia/Taipei`）首次在視窗內可靠報導 North Korea 對型號與能力的新說法。
- 續報判定：前次 2026-10-03 收錄發射本身，當時型號與最終性能未明；今日新增是 KCNA 稱其為 intermediate-range strategic missile、具低空變軌與 AI 能力。
- 限制：South Korea 估計飛行超過 700 公里、Japan 約 680 公里；South Korea 未立即確認 North Korea 的可變軌與 AI 宣稱。
- 來源：https://werindia.com/news/world/thehindu/North-Korea-says-it-test-fired-an-intermediate-range-missile-as-tensions-grow-over-mine-blasts-86951699
- 來源：https://apnews.com/article/0b5b69e919f9c9a2358f3cd3346649e7

## 全球排除與取捨

- India 示威的 AP 主報導發佈於 10/2、早於全球下界；Reuters 10/3 的拘留更新雖在窗內，但全球重要性與可驗證細節低於入選項目，未以舊事件更新補位。
- Nigeria 另有 20 死交通事故候選；為避免同日兩則高度相似道路事故占用名額，保留有明確 Catholic pilgrims 群體與 Salama 黑點脈絡的 Kenya 事件。
- Flydubai 事件本身發生較早，10/3 僅增加身分與極端主義背景；Brazil 選舉前瞻、Czar 遺骸與多篇政策分析屬預告、儀式或背景，均不作 24 小時新事件。
- Libya 項目僅以 10/3 公開的談判受阻與新指控為新節點；August drone attacks 只作背景。North Korea 項目僅以視窗內官方辨識與能力宣稱為新節點，不重列視窗外的發射初報。
