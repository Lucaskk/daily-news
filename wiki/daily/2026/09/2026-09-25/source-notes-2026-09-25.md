---
title: "2026-09-25 Daily News Source Notes"
type: source-notes
created: 2026-09-25
updated: 2026-09-25
status: research-complete
tags: [daily-news, provenance, deduplication]
sources: []
---

# 2026-09-25 每日新聞來源筆記

## 固定研究截點與時間窗

- Asia/Taipei 截點：`2026-09-25T08:00:49+08:00`。沿用當日私人 checkpoint，恢復研究時沒有移動截點。
- 全球新聞 24 小時窗：`2026-09-24 08:00:49` 至 `2026-09-25 08:00:49`（Asia/Taipei）；UTC 為 `2026-09-24T00:00:49Z` 至 `2026-09-25T00:00:49Z`。
- 科技產品 168 小時窗：`2026-09-18 08:00:49` 至 `2026-09-25 08:00:49`（Asia/Taipei）；UTC 為 `2026-09-18T00:00:49Z` 至 `2026-09-25T00:00:49Z`。
- 研究模式：`legacy`。AI 搜尋、來源查證與語意判讀候選；Python 負責產品歷史索引、固定渲染、結構驗證、GitHub Pages 發布與 LINE 配送。
- 選題前已執行 `python3 scripts/build_product_news_ledger.py`，結果為 603 筆產品變更／99 份既有日報。
- 完整產品歷史沒有整份讀入模型。每個候選先以公司、產品、更新動作及比對鍵窄搜 `product-news-ledger.md`、全部 `daily-news-*.md` 與 `source-notes-*.md`；無命中候選才完整核對 44 行／26 筆的最近七天表。
- 已直接檢查 Engadget 與 Cool3c。兩站只用於發現候選與補充脈絡，規格、價格及上線日期優先回查官方公告；折扣、導購、評測與沒有產品狀態變更的文章排除。

## 科技／AI 產品候選與去重

| 公司／產品／更新／比對鍵 | 發布時間與來源 | 歷史查詢與判定 |
|---|---|---|
| Meta／Meta VR Glasses／Connect 2026 正式公布／`meta-vr-glasses-2026` | Meta 官方頁標示 2026-09-23／2026-09-24；官方確認約 100g、5K micro-OLED、Snapdragon Reality Elite、外接 puck、2027 年春季 US$1,299.99。https://about.fb.com/news/2026/09/introducing-meta-vr-glasses-3d-movies-immersive-live-sports-100-grams/ ; https://www.engadget.com/2267230/everything-announced-at-meta-connect-2026/ | 窄搜 `Meta.*VR Glasses|VR Glasses.*Meta|meta-vr-glasses-2026` 無命中；最近七天表無命中，收錄 T1。上市仍在 2027 年，今天是正式產品發布，不寫成已開賣。 |
| Meta／Ray-Ban Meta Audio、Ray-Ban Meta Gen 3／預購與正式上市／`ray-ban-meta-audio-gen3` | Meta 官方 2026-09-23 公告：Audio 即日起預購、10/13 出貨、US$349；Gen 3 即日起販售、US$449。https://about.fb.com/news/2026/09/introducing-ray-ban-meta-audio-glasses-new-styles-plus-muse/ ; https://www.engadget.com/2267213/ray-ban-meta-gen-3-hands-on-better-battery-life/ | 窄搜 `Meta.*Ray-Ban Meta (Audio|Gen 3)|Ray-Ban Meta (Audio|Gen 3).*Meta|ray-ban-meta-audio-gen3` 無命中；最近七天表無命中，收錄 T2。兩款是同場但不同定位的新產品，合併為一項發布事件，避免單一公司擠壓清單。 |
| Google／Health Guardian／Pixel Watch 功能開始上線／`pixel-watch-health-guardian-rollout` | Google 官方 2026-09-24 公告本週開始設定血壓趨勢、胰島素阻抗趨勢與睡眠呼吸品質，首批趨勢報告預計 10 月初。https://blog.google/products-and-platforms/products/google-health/health-guardian-features-live/ | 窄搜命中 2026-08-13 對 Pixel Watch 5 與 Health Guardian 的「coming soon」公告。**續報，前次收錄 2026-08-13；今日新進展是功能實際開始 rollout，並確定首批報告時程。** 收錄 T3。 |
| Razer／Kiyo V2 Pro／4K 60 FPS 網路攝影機正式發布與開賣／`razer-kiyo-v2-pro-release` | Razer 官方 2026-09-24 公告；商品頁顯示 US$299.99、Sony STARVIS 2、4K 60 FPS、AI auto-framing。https://www.razer.com/newsroom/product-reviews/kiyo-v2-pro ; https://www.razer.com/streaming-cameras/razer-kiyo-v2-pro/RZ19-05360100-R3U1 | 窄搜 `Razer.*Kiyo V2 Pro|Kiyo V2 Pro.*Razer|razer-kiyo-v2-pro-release` 無命中；最近七天表無命中，收錄 T4。與 2025 Kiyo V2 的 4K30 更新不同。 |
| Google／Google Photos／Redact pen 與四項相片功能更新／`google-photos-redact-rollout` | Google 官方 2026-09-24 公告；Redact pen 正向 Android 全球 rollout，另列 Gemini Spark、Wardrobe、Moods 與 Remix templates 的分區可用性。https://blog.google/products-and-platforms/products/photos/google-photos-updates/ | 窄搜 `Google.*Photos.*Redact|Redact.*Google Photos|google-photos-redact-rollout` 無命中；最近七天表無命中，收錄 T5。不同功能地區、平台與訂閱限制不同，不能概括成全球同時可用。 |
| Nikon／Z5 IIC | Cool3c 候選稱無 EVF、US$1,399.99、10 月中上市。 | 搜尋官方 Nikon 新聞稿與產品頁未取得足以確認的第一手公告，排除，不用媒體單一候選補位。 |
| Google／Pixel 11 Call For Me、太空 AI data center | Engadget 2026-09-24 候選。 | Call For Me 僅初步 rollout 且官方細節不足；太空資料中心屬實驗／計畫而非可用產品。與已選五項相比產品狀態較弱，排除。 |

## 全球新聞入選時間與續報依據（研究批次一）

| 編號／事件 | 事件或首次可靠發布時間 | 去重與判定 |
|---|---|---|
| G1 Trump 與 Xi 在白宮會談、美中延長貿易休戰 | Reuters 轉載頁更新 2026-09-24 19:46 IST = 9/24 22:16 TPE；白宮會談同日舉行，財長 Scott Bessent 已宣布休戰延長至 2027-01-10。 | 窄搜 `Trump.*Xi|Xi.*Trump|trade truce.*January` 命中的是 5 月北京峰會後續背景，沒有 9/24 華府國是訪問與本次兩個月延長，首次收錄此事件節點。https://www.business-standard.com/author/reuters ; https://www.hurriyetdailynews.com/amp/trump-welcomes-xi-to-washington-with-lavish-praise-227314 |
| G2 伊朗提出 Hormuz 七項條件與四至五天期限 | Guardian 2026-09-24 15:13 EDT = 9/25 03:13 TPE。 | **續報，前次收錄 2026-09-24。** 前次是 Pezeshkian 聯大表示願談但拒絕武力語言；今日新增 Mohsen Rezaei 公開四至五天期限、七項條件須一次完成，以及英國外相 Ed Miliband 與 Abbas Araghchi 會面。https://www.theguardian.com/world/2026/sep/24/ed-miliband-meets-iran-foreign-minister-us-ultimatum-strait-hormuz |
| G3 Ethiopia 北部戰事擴至 Afar、Amhara | Guardian 首發 2026-09-24 09:43 EDT = 9/24 21:43 TPE；Al Jazeera 同日報導衝突擴大。 | 窄搜 `Tigray.*TPLF.*offensive|TPLF.*Afar.*Amhara` 無同一新攻勢命中，首次收錄。TPLF 稱聯邦政府先發動全面攻勢，政府顧問反稱 TPLF 先攻；雙方傷亡說法未獨立驗證。https://www.theguardian.com/world/2026/sep/24/fears-return-to-war-tigray-rebels-launch-offensive-against-ethiopian-army ; https://www.aljazeera.com/news/2026/9/24/fighting-widens-across-ethiopia-as-tigray-clashes-escalate |
| G4 美國參議院以 49 比 50 否決最新 Iran war powers 案 | CBS 2026-09-24 14:45 EDT = 9/25 02:45 TPE。 | **續報，前次收錄 2026-07-24。** 前次是 House 通過停止戰事案、Senate 否決類似案；今日是新的 concurrent resolution 與新一輪 49–50 表決，四名共和黨議員支持、John Fetterman 為唯一反對的民主黨員。https://www.cbsnews.com/news/senate-iran-war-powers-resolution-vote/ |
| G5 California 最高法院命令 Riverside sheriff 歸還約 65 萬張選票 | Guardian 2026-09-24 14:55 EDT = 9/25 02:55 TPE；California Supreme Court 同日一致裁決。 | 窄搜 `Chad Bianco|Riverside.*ballot` 無既有日報命中，首次收錄。法院稱扣押違法並要求停止進一步處理；不把先前未經證實的舞弊申訴寫成事實。https://www.theguardian.com/us-news/2026/sep/24/california-sheriff-ballots-chad-bianco ; https://www.wral.com/news/ap/e77a7-california-supreme-court-orders-riverside-county-sheriff-to-return-650-000-seized-ballots/ |

## 全球新聞入選時間與續報依據（研究批次二）

| 編號／事件 | 事件或首次可靠發布時間 | 去重與判定 |
|---|---|---|
| G6 法官暫時恢復 CNN、MS NOW、Politico 白宮採訪權 | CBS 2026-09-24 13:43 EDT 更新 = 9/25 01:43 TPE；臨時限制令在 9/24 凌晨作成，記者中午重新進入。 | **續報，前次收錄 2026-09-22。** 前次是三家媒體對白宮禁令提告；今日新增 Judge Timothy Kelly 認為 due process 主張可能成立、下令暫時恢復 hard pass，且記者已重新入場。命令效期 14 天，司法部預計上訴。https://www.cbsnews.com/news/judge-blocks-trump-ban-cnn-ms-now-politico-restoring-white-house-access/ |
| G7 Abbas 重申 11 月 28 日舉行 Palestinian 立法選舉 | Reuters／MarketScreener 2026-09-24 12:45 EDT = 9/25 00:45 TPE；Abbas 同日在聯大演說。 | 窄搜 `Abbas.*November 28|Palestinian.*parliamentary election` 無同一具體日期承諾命中，首次收錄。這是改革承諾，不是已完成投票；Hamas 參與、Gaza 與 East Jerusalem 投票安排仍未確定。https://www.marketscreener.com/news/abbas-pledges-first-palestinian-parliamentary-vote-in-20-years-as-doubts-mount-ce785aded08eff25 |
| G8 Krasnodar 因 drone attacks 阻礙 grain exports 宣布緊急狀態 | Reuters／MarketScreener 2026-09-24（只有日期，未提供時分）；地方政府同日公布。 | **續報，前次收錄 2026-08-13。** 前次是 Ukraine 攻擊 Novorossiysk 海軍、港口與 grain terminals；今日新增 Krasnodar governor 以出口受阻為由宣布區域緊急狀態，使受影響者可申請補償。https://www.marketscreener.com/news/russia-s-krasnodar-region-declares-state-of-emergency-as-drone-attacks-slow-grain-exports-ce785adede89f022 |
| G9 美國海軍確認 USS Abraham Lincoln strike group 有 8 次自殺未遂 | Guardian 2026-09-23 20:53 EDT = 9/24 08:53 TPE；代理海軍部長 Hung Cao 的回函首次給出總數。 | 窄搜 `USS Abraham Lincoln.*suicide|Lincoln.*自殺` 無既有收錄，首次收錄。8 次分布於整個 strike group，不全都發生在航母上；官方沒有公布個案身分，且均未死亡。https://www.theguardian.com/us-news/2026/sep/23/uss-lincoln-suicide-attempts |
| G10 Paris 法院判 child pickpocket network 首腦 8 年徒刑 | Guardian 2026-09-24 05:00 EDT = 9/24 17:00 TPE；法院同日量刑。 | 窄搜 `Hamidovic|child pickpocketing|兒童扒手` 無命中，首次收錄。Roberto Hamidovic 判法定最高 8 年及 €500,000 罰金；其妻與五名親屬另判 5 至 7 年。被告否認控罪，辯方稱 trafficking 證據不足。https://www.theguardian.com/world/2026/sep/24/clan-leader-in-paris-sentenced-to-eight-years-for-human-trafficking |

## 排除、衝突與邊界判斷

- Trump–Xi 會談與貿易休戰採納的是 9/24 華府國是訪問與休戰延長，不重複 5 月北京峰會；截至截點沒有共同完整協議文本，不把禮遇或領袖發言寫成全面和解。
- Iran Hormuz 是 9/24 的續報。四至五天期限與七項條件來自 Iranian senior officials；未說明逾期的下一步，美方也未接受，因此標為 ultimatum／條件而非已生效協議。
- Ethiopia 對「誰先發動攻勢」、Eritrea 是否支援以及雙方戰果各有衝突，來源筆記保留 TPLF、政府與第三方說法，不選邊覆寫。
- Senate war powers 不能寫成首次或最終表決；歷史已有多次議案。本次只收錄 9/24 新的 49–50 結果及議員陣營變化。
- California ballot 案的原始舞弊申訴遭地方選務官員否定；本文只確認最高法院對 custody 與 sheriff 權限的裁決。
- USS Lincoln 報導涉及自殺未遂，只記錄官方確認的總數、部署長度與支援資源爭議，不推論個人原因；如讀者有立即危機，應聯繫所在地緊急或危機支援服務。
- Paris 案採法院量刑與庭審證據；沒有以族裔作為犯罪解釋，也不把尚未在庭上作證的兒童個案細節擴寫。
- Morocco 選舉分析、Germany 105 歲前集中營守衛調查、Naoero 名稱倡議與 Google 太空資料中心實驗均曾評估；相較入選事件的制度結果、戰事升級或可用產品節點，影響或時間證據較弱，排除。
- 世界 Top 10 排序綜合 Reuters、AP、CBS、Guardian、Al Jazeera、官方公告與跨區域影響；這是編輯綜合，不宣稱有精確全球社群討論量排行。
- 所有來源時間以頁面首次發布或明確更新換算；只有日期的官方／Reuters 頁保留日期層級，不虛構 00:00 時分。

## 發布紀錄

- pipeline 內容 commit：`0334df35808814d6dc5282cff9d46b7456557d51`。
- GitHub Pages 日期頁、`latest-slides.html` 與根入口均通過 HTTP 與完整位元組 SHA-256 比對。
- 唯一私人 LINE watchdog 於 `2026-09-25T08:13:13+08:00` 回報 `Sent LINE message`，exit code 0；未使用 `scripts/send_line_daily_slides.py`。
- 公開頁：https://lucaskk.github.io/daily-news/wiki/daily/2026/09/2026-09-25/slides-2026-09-25.html?v=20260925-081224-reader
- pipeline checkpoint 已進入 `complete`；強制 `check --date 2026-09-25` exit 0。本機 Playwright 套件未安裝，視覺 QA 屬非阻擋項目。
