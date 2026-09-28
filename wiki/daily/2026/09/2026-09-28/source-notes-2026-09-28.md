---
title: "2026-09-28 每日新聞來源與時間筆記"
date: 2026-09-28
type: source-notes
status: published
tags: [daily-news, sources, provenance, deduplication]
---

# 2026-09-28 每日新聞來源與時間筆記

## 研究範圍

- Asia/Taipei 研究截點：`2026-09-28 08:01:50 +08:00`
- 全球新聞 24 小時窗：`2026-09-27 08:01:50` 至 `2026-09-28 08:01:50`（Asia/Taipei）
- 全球新聞 UTC 窗：`2026-09-27T00:01:50Z` 至 `2026-09-28T00:01:50Z`
- 科技／AI 產品 7 日窗：`2026-09-21 08:01:50` 至 `2026-09-28 08:01:50`（Asia/Taipei）
- 科技／AI 產品 UTC 窗：`2026-09-21T00:01:50Z` 至 `2026-09-28T00:01:50Z`
- 研究模式：`legacy`。AI 負責搜尋、來源查證、事件語意去重與摘要；Python 負責索引、渲染、結構檢查、發布與配送。
- 選題前已執行 `python3 scripts/build_product_news_ledger.py`，重建 613 列產品變更索引；模型沒有讀取完整歷史表。
- 歷史去重範圍：`wiki/daily/` 下全部 `daily-news-*.md`、`source-notes-*.md` 與產品 ledger，均只用候選實體、產品、動作與比對鍵窄搜命中列。

## 科技產品來源池、時間與去重

本輪一次廣泛掃描 Engadget、The Verge、TechCrunch、WIRED、Ars Technica、Cool3c、Yahoo 奇摩科技、TechOrange 科技報橘與數位時代；搜尋結果另回查 Meta、F-Droid 與 Ando 官方頁。The Verge 封存頁無法由研究工具直接讀取；其餘來源沒有被反覆深挖。三個候選的完整歷史 `rg` 均無相同產品變更命中，因此依規則只完整讀取一次 `product-news-recent-7d.md`，也未發現相同變更。

| 項目 | 事件／發佈時間依據 | 窄化查詢、命中與判定 |
|---|---|---|
| T1 Meta／Muse Charm／首次揭露口袋型 AI 語音裝置／`meta-muse-charm` | Meta 官方 Connect 2026 整理頁標示 2026-09-24，未提供時分；官方明確揭露 Muse Charm 是可與 Muse 即時語音互動、可放入口袋的裝置，更多規格將於年內公布。https://about.fb.com/news/2026/09/the-biggest-news-from-connect-2026/ ; https://arstechnica.com/ai/2026/09/meta-puts-its-ai-assistant-on-a-keychain/ | 查詢 `Meta.*Muse Charm|Muse Charm.*Meta|meta-muse-charm` 無命中；最近七天表只有 Meta VR Glasses、Ray-Ban Meta Audio／Gen 3，產品與變更不同，首次收錄。官方未公布價格、完整規格或確切開賣日，正文保留不確定性。 |
| T2 F-Droid／F-Droid 2.0／正式發布與分階段推出／`fdroid-2-0-redesign` | F-Droid 官方於 2026-09-24 發布 2.0 公告，說明在 14 個測試版後於未來數週分批推出；Ars Technica 同日 15:30（頁面未標時區，僅作交叉來源）整理功能。https://f-droid.org/en/2026/09/24/f-droid-2.0-a-new-chapter-for-android-freedom.html ; https://arstechnica.com/gadgets/2026/09/f-droid-gets-its-biggest-update-in-a-decade-with-new-ui-and-smoother-app-installs/ | 查詢 `F-Droid.*(2.0|redesign|Kotlin Compose)|2.0.*F-Droid|fdroid-2-0` 無命中；最近七天表也無相同變更，首次收錄。官方套件頁仍顯示 rc1／分階段狀態，不能寫成所有裝置已立即收到。 |
| T3 Ando／Ando team messaging／公開推出 agent-native 團隊通訊平台／`ando-agent-native-messaging` | Ando 新聞稿於 2026-09-24 09:00 EDT 發布，即 2026-09-24 21:00 TPE；TechCrunch 於 07:31 PDT（22:31 TPE）報導公司從 stealth 公開產品。https://www.globenewswire.com/news-release/2026/09/24/3368344/0/en/Ando-Launches-Agent-Native-Messaging-Platform-Announces-20-Million-Seed.html ; https://www.ando.so/blog/introducing-ando ; https://techcrunch.com/2026/09/24/ando-eyes-slack-as-it-builds-team-messaging-platform-for-humans-and-agents-to-work-together/ | 查詢 `Ando.*(messaging|launch|agent)|agent-native.*Ando|ando-agent-messaging` 未命中相同產品；唯一泛化命中是 8 月 Hark browser agent，無關。最近七天表無 Ando，首次收錄。官網仍採申請／onboarding，未證明普遍自助註冊。 |

### 產品候選排除

- Spotify Partner Program 擴至逾 35 個市場：TechCrunch 首頁在本輪再次突出，但 Spotify 官方原始公告日期為 2026-09-17，早於七日下限，排除。
- Meta VR Glasses、Ray-Ban Meta Audio／Gen 3：已於 2026-09-25 收錄；本次只收錄同場活動中先前未捕捉、且是獨立硬體變更的 Muse Charm。
- WiCi One 與 Logitech G PRO 系列：已於 2026-09-27 收錄，排除重複。
- Engadget 首頁多數為評測、教學、比較與舊產品導購；BYD 固態電池仍屬開發進度敘述，沒有可核對的上市節點，未收錄。
- Cool3c 的折扣、評測、募資小物、購物指南與 iOS 27.0.1「即將修復」預告不構成已發布產品變更；沒有用來補數。
- TechCrunch 的 Huawei AI 晶片為計畫性報導、Pinterest Restyle 為 teaser；Spotify、Roku 與 Apple 候選缺乏在本輪窗口內可確認且未重複的重大公開節點，未列入。

## 全球 Top 10 時間、去重與歧異

| 項目 | 視窗內依據與去重結果 |
|---|---|
| G1 RAF Fairford 反恐拘捕 | AP／Washington Post 於 2026-09-27 15:15 EDT 首次可靠完整發布，即 2026-09-28 03:15 TPE。警方接報時間 00:45 BST 換算約 07:45 TPE，略早於下限，但首次可靠發布在窗內，因此以發布基準收錄。窄搜 `RAF Fairford|Whelford.*terror|three suspicious vehicles` 無歷史命中。https://www.washingtonpost.com/world/2026/09/27/britain-explosives-us-air-base-fairford/7f918276-ba48-11f1-94cb-d3d8f22a8c8b_story.html |
| G2 South Africa 兩宗大規模槍擊 | Guardian 首發 2026-09-27 04:19 EDT，即 16:19 TPE；警方稱 Wedela 與 Lwandle 兩案合計至少 27 死、26 傷。窄搜 `South Africa.*(Wedela|Lwandle)|mass shootings.*27` 無命中。警方尚未證實兩案相關，動機線索分開呈現。https://www.theguardian.com/world/2026/sep/27/mass-shootings-south-africa-johannesburg-cape-town |
| G3 Russia–Ukraine 新一輪空襲 | AP／Washington Post 於 2026-09-27 13:11 EDT，即 2026-09-28 01:11 TPE；報導彙整星期日夜間至白天空襲，Ukraine 至少八死、Russia 一死。9/27 已收錄的是 Germany–Russia 外長會談，不是這一輪具體攻擊；窄搜地點、傷亡與 data center strike 無同一事件命中，按獨立戰場事件首次收錄。https://www.washingtonpost.com/world/2026/09/27/russia-ukraine-war-germany-drones-strikes/8db364ae-ba5d-11f1-81fc-9b76f8343b6c_story.html |
| G4 Serbia 總統辭職轉戰總理 | Guardian／AP 於 2026-09-27 21:09 CEST 發布，即 2026-09-28 03:09 TPE；Vučić 公開宣讀辭呈並宣布領導 SNS 參與 10 月 25 日提前大選。窄搜只命中 8 月與其會談的無關背景，無相同辭職事件。https://www.theguardian.com/world/2026/sep/27/serbia-president-aleksandar-vucic-resigns-run-prime-minister |
| G5 Switzerland 否決緊縮中立公投 | Guardian 於 2026-09-27 11:05 EDT 發布，即 23:05 TPE；最終結果顯示所有 canton、約 70% 選民反對。窄搜 `Swiss.*neutrality|Switzerland.*Nato.*referendum` 無命中。https://www.theguardian.com/world/2026/sep/27/swiss-vote-reject-stricter-neutrality-rules-nato |
| G6 Afghanistan–Pakistan 邊境指控 | AP／Washington Post 於 2026-09-27 08:37 EDT 發布，即 20:37 TPE；Afghanistan 稱在 Nuristan 擊斃 28 人、俘虜 32 人，Pakistan 全面否認支援或派遣。窄搜 `Nuristan.*28|Afghanistan.*32 captured|Pakistan.*Islamic State.*Nuristan` 無命中；雙方說法沒有獨立驗證。https://www.washingtonpost.com/world/2026/09/27/afghanistan-pakistan-incursions/39252dce-ba70-11f1-81fc-9b76f8343b6c_story.html |
| G7 Bangkok 淹水持續迫使居民進避難所 | Guardian／AFP 於 2026-09-27 02:09 EDT 發布，即 14:09 TPE；星期日新節點是近 4,900 人進避難所、約 52,000 戶受影響及學校停課安排。災區宣布本身在前一日，但本庫未曾收錄；以窗內官方人數與持續疏散首次收錄。窄搜無命中。https://www.theguardian.com/world/2026/sep/27/our-house-was-under-water-bangkok-floods-force-thousands-into-shelters-as-disaster-declared |
| G8 Nepal Himlung 雪崩 | AP／Washington Post 於 2026-09-27 10:05 EDT 發布，即 22:05 TPE；星期日雪崩造成至少兩死、12 人失蹤，10 名生還者已由直升機送下山。窄搜 `Himlung|Nepal.*avalanche.*12 missing` 無命中。https://www.washingtonpost.com/world/2026/09/27/nepal-mountain-avalanche-climbers/8526eb2a-ba7c-11f1-81fc-9b76f8343b6c_story.html |
| G9 Pope Leo 與法國教會性侵倖存者會面 | Guardian 首發 2026-09-27 14:20 CEST，即 20:20 TPE；星期日 Pope Leo 私下會見七名倖存者，並在 Lourdes 要求教會面對「深層傷口」。窄搜 `Pope.*Lourdes.*survivor|Leo.*French clergy abuse` 無同一事件命中。部分倖存者團體批評受邀者由教會挑選，保留反方意見。https://www.theguardian.com/world/2026/sep/27/pope-leo-france-child-sexual-abuse-survivors |
| G10 Madrid 住房抗議擴大成過夜紮營 | AP／Washington Post 於 2026-09-27 15:38 EDT 發布，即 2026-09-28 03:38 TPE；星期日抗議者延續第二天並在 Puerta del Sol 紮營，要求禁止沒有替代住房的驅逐與更強租客保障。窄搜 `Puerta del Sol.*housing|Maricarmen.*eviction|Madrid.*encampment` 無命中。主辦方與政府對參與人數估計差距大，不採單一確定值。https://www.washingtonpost.com/world/2026/09/27/spain-evictions-madrid-housing-protest/953236a2-ba66-11f1-81fc-9b76f8343b6c_story.html |

## 未入選候選與原因

- Trump 拒絕 Iran 七日 Hormuz 提案：Guardian 原文首發 2026-09-26 11:31 CEST，早於世界新聞下限，且 2026-09-27 已以 Iran 不退讓的重大回應收錄；本輪沒有足以再占一則的新節點。
- Germany–Russia 外長會談、Venezuela 釋囚、EU 人道援助、美國東北風暴、Saint Vincent 槍擊、燃油經濟標準與 Colombia 引渡均已在 2026-09-27 收錄，不重刊。
- Gaza 61m 噸瓦礫是 9/27 發表的深度報導，但核心 61m 數字可追溯至 2025 年，清運進度也是長期背景，不能僅依文章新發布當成新事件。
- Etna 航班中斷、Munich 旅遊巴士事故、Atlanta 熊貓抵達與 Northern Ireland 遊行均在窗口內，但全球制度影響與跨媒體關注度低於入選項目。
- Indonesia 渡輪死亡人數上修與 Lake Kivu 翻船屬重大事故候選，但本輪可讀來源對事件時間、前次節點與最新數字的細節不足，未優先採用。
- Brazil 選舉人物專訪、Oleshky 與 Poland 軍費為特寫或趨勢分析，沒有在 24 小時窗內可獨立辨識的新事件節點。

## 發布紀錄

- 固定 renderer 產生版本 `20260928-081337-reader`；pipeline 以乾淨 clone 限定檔案推送 content commit `a59f5b716f1fbcfd2b02c7f08e336473bf2ebee6`。
- GitHub Pages 的日期頁、`latest-slides.html` 與根入口均通過 HTTP 200 及完整位元組雜湊核對。公開頁：https://lucaskk.github.io/daily-news/wiki/daily/2026/09/2026-09-28/slides-2026-09-28.html?v=20260928-081337-reader
- 唯一私人 LINE watchdog 於 `2026-09-28 08:14:39 +08:00` 回報 `Sent LINE message`、exit 0；沒有執行其他 sender 或重送。
- `python3 scripts/daily_news_pipeline.py check --date 2026-09-28` exit 0，checkpoint 為 `complete`。68 項 Python 測試與 JavaScript 語法檢查通過；本機 `http://localhost:4173/wiki/daily/latest-slides.html` 回應 HTTP 200。Chrome／Playwright 在 320、390、1440px 驗證圖片、頁內完整報告、逐篇來源、分享定位、單篇 ChatGPT context 與鍵盤導覽，測試攔截 ChatGPT 網址而未送出提問。
