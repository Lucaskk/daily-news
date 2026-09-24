---
title: "2026-09-24 Daily News Source Notes"
type: source-notes
created: 2026-09-24
updated: 2026-09-24
status: research-complete
tags: [daily-news, provenance, deduplication]
sources: []
---

# 2026-09-24 每日新聞來源筆記

## 固定研究截點與時間窗

- Asia/Taipei 截點：`2026-09-24T08:02:07+08:00`。沿用 08:02 建立的私人 checkpoint，恢復研究時沒有移動截點。
- 全球新聞 24 小時窗：`2026-09-23 08:02:07` 至 `2026-09-24 08:02:07`（Asia/Taipei）；UTC 為 `2026-09-23T00:02:07Z` 至 `2026-09-24T00:02:07Z`。
- 科技產品 168 小時窗：`2026-09-17 08:02:07` 至 `2026-09-24 08:02:07`（Asia/Taipei）；UTC 為 `2026-09-17T00:02:07Z` 至 `2026-09-24T00:02:07Z`。
- 研究模式：`legacy`。AI 搜尋與判讀候選；Python 負責歷史索引、渲染、驗證、GitHub Pages 發布與 LINE 配送。不是可選的 Python 研究快取模式。
- 選題前已執行 `python3 scripts/build_product_news_ledger.py`，結果為 598 筆產品變更／98 份既有日報。
- 完整產品歷史沒有整份讀入模型。每個候選先以公司、產品、更新動作及比對鍵窄搜 `product-news-ledger.md`、所有 `daily-news-*.md` 與 `source-notes-*.md`；候選均無命中後，才完整讀取 42 行／24 筆的最近七天表。
- 已直接檢查 Engadget 與 Cool3c。兩站用來發現候選；規格與日期優先回查官方產品頁或公司新聞稿。導購、折扣、舊評測、傳聞與截點後活動不列入。

## 科技／AI 產品候選與去重

| 公司／產品／更新／比對鍵 | 發布時間與來源 | 歷史查詢與判定 |
|---|---|---|
| Microsoft／Surface Pro 12、Surface Laptop 13／Snapdragon X2 Plus 新機預購／`surface-pro12-laptop13-x2plus` | Engadget 頁面標示 2026-09-23 16:30 EST；依頁面字面換算為 9/24 05:30 TPE。Microsoft 官方頁顯示新款 Pro 12、X2 Plus、US$1,149.99 與預購。https://www.engadget.com/2266680/microsofts-new-surface-pro-12-and-surface-laptop-13-feature-snapdragon-x2-plus-chips/ ; https://www.microsoft.com/en-us/surface/devices/surface-pro?icid=mscom_marcom_FH3a_SurfacePro12In_Fall27 | 窄搜 `Microsoft.*Surface (Pro 12|Laptop 13).*Snapdragon X2|Surface (Pro 12|Laptop 13).*Snapdragon X2.*Microsoft|surface-pro12-laptop13-x2plus` 無命中；最近七天表無命中，收錄 T1。媒體頁把美東時間寫成 EST，夏令時間標籤可能不精確，故保留原標示與換算依據。 |
| Xiaomi／18 Pro、18 Pro Max／中國發布並確認國際版本／`xiaomi-18-pro-launch` | Cool3c 於截點前約 3 小時顯示北京發布；El Español 2026-09-23 19:19 西班牙時間報導全球版本，約為 9/24 01:19 TPE。https://www.cool3c.com/ ; https://www.elespanol.com/elandroidelibre/20260923/xiaomi-confirma-llegada-moviles-pro-espana-bestia-pantallas-ultimo-chip-qualcomm/1003744394538_0.amp.html ; https://new.c.mi.com/global/post/2137775 | 窄搜 `Xiaomi.*18 Pro( Max)?|18 Pro( Max)?.*Xiaomi|xiaomi-18-pro-launch` 無命中；最近七天表無命中，收錄 T2。完整規格主要來自媒體與 Xiaomi Community 預告，未把全球上市日或所有價格寫成確定事實。 |
| Logitech／Yeti 2／USB 麥克風新一代正式上市／`logitech-yeti-2-release` | Engadget 頁面標示 2026-09-23 12:01 EST；依字面換算為 9/24 01:01 TPE。Logitech G 9/23 PLAY 活動頁可交叉確認當日新品發布。https://www.engadget.com/2265713/logitechs-yeti-2-brings-the-17-year-old-usb-mic-into-the-modern-age/ ; https://www.logitechg.com/en-us | 窄搜 `Logitech.*Yeti 2|Yeti 2.*Logitech|logitech-yeti-2-release` 無命中；最近七天表無命中，收錄 T3。AI 降噪成效及感測器體驗尚缺乏獨立長期測試。 |
| Eight Sleep／Pod 6／智慧床墊套新版本／`eight-sleep-pod-6-release` | Engadget 頁面標示 2026-09-23 07:00 EST；依字面換算為 9/23 20:00 TPE。官方頁在截點前列出 Pod 6、20% faster、9x sensors 與售價。https://www.engadget.com/2264386/eight-sleep-announces-the-pod-6-its-newest-smart-mattress-cover/ ; https://www.eightsleep.com/de/ | 窄搜 `Eight Sleep.*Pod 6|Pod 6.*Eight Sleep|eight-sleep-pod-6-release` 無命中；最近七天表無命中，收錄 T4。溫控與感測改善為公司宣稱，且使用仍需訂閱。 |
| Razer／Mako、Mako X／桌上型遊戲喇叭產品線／`razer-mako-2026-release` | Razer 官方新聞稿日期 2026-09-22；Cool3c 於截點前整理台灣價格。https://www.razer.com/newsroom/product-news/mako-line ; https://www.razer.com/eu-en/gaming-speakers/razer-mako-x ; https://www.cool3c.com/ | 窄搜 `Razer.*Mako( X)?|Mako( X)?.*Razer|razer-mako-2026-release` 無命中；最近七天表無命中，收錄 T5。官方 Mako X 頁面標示 10/6 可購買，與部分媒體「已發布」用語不同，區分宣布與實際開賣。 |
| Meta／Connect 2026 新品 | Engadget 首頁在截點附近開始出現現場消息。 | 活動與文章時間無法穩定證明早於凍結截點，排除；不能因恢復研究時已可見就延長時間窗。 |
| Logitech／PLAY 活動其他 Pro 配件 | 2026-09-23。 | 與 Yeti 2 同場、影響較小，避免用同一活動的多個周邊擠壓其他公司產品，排除。 |

## 全球新聞入選時間與續報依據（研究批次一）

| 編號／事件 | 事件或首次可靠發布時間 | 去重與判定 |
|---|---|---|
| G1 俄軍日間無人機重擊 Kyiv | AP 可讀轉載首發 2026-09-23 03:12 EDT = 9/23 15:12 TPE；Reuters 網路中斷更新為 9/23 14:28 EDT = 9/24 02:28 TPE；截點前另有彈道飛彈攻擊更新。 | **續報，前次收錄 2026-09-22。** 前次是 Zaporizhzhia／Kharkiv 攻擊；今日新增 Kyiv 日間 jet-powered drones、2 死至少 41 傷、約 10 萬戶網路受阻與鐵路、加油站、商業設施受損。https://www.local10.com/news/world/2026/09/23/russia-pounds-kyiv-with-drones-killing-2-and-wounding-41-before-zelenskyys-un-address/ ; https://www.marketscreener.com/news/russia-s-attacks-disrupt-internet-services-to-100-000-households-in-kyiv-ukrainian-ministry-says-ce785aded989f522 ; https://malaysia.news.yahoo.com/kyiv-under-missile-attack-emergency-225051151.html |
| G2 Altman、Amodei 向安理會談 AI 安全 | Guardian 2026-09-23 17:15 EDT = 9/24 05:15 TPE。 | **續報，前次收錄 2026-09-22。** 前次是聯合國 AI 科學小組首份專題簡報；今日新增兩大 AI 公司執行長直接向安全理事會提出 human control、禁止 AI 生物武器與全球模型測試標準，但沒有通過約束性決議。https://www.theguardian.com/world/2026/sep/23/unga-sam-altman-dario-amodei |
| G3 Harvey Weinstein 判刑 15 年 | Guardian 2026-09-23 17:56 CEST = 9/23 23:56 TPE；法院同日宣判。 | 窄搜 `Weinstein.*15 years|Miriam Haley` 無同一判刑事件命中，首次收錄。2024 撤銷舊判決與 2025 重審是背景，本次是新量刑。https://www.theguardian.com/world/2026/sep/23/harvey-weinstein-sentencing-prison |
| G4 伊朗總統聯大演說 | Guardian 2026-09-23 18:44 CEST = 9/24 00:44 TPE。 | **續報，前次收錄 2026-09-23。** 前次是美伊代表三小時直接會談；今日新增 Pezeshkian 公開表示願意談判但拒絕武力語言，美國代表退場，並暗示 Hormuz 未來可能要求檢查船舶。https://www.theguardian.com/world/2026/sep/23/iranian-leader-hits-back-at-bully-trump-signals-willingness-to-talk |
| G5 Chagos 協議與對 Mauritius 付款暫停 | Guardian 2026-09-23 06:11 EDT = 9/23 18:11 TPE。 | 歷史窄搜命中的是 2 月美方反對背景，未收錄今天的付款暫停。今日新節點是英國防相明確稱現有版本無美方支持不能推進，至少每年 £120m 付款暫停，收錄為實質政策變化。https://www.theguardian.com/world/2026/sep/23/chagos-islands-diego-garcia-streeting-us-support |

## 全球新聞入選時間與續報依據（研究批次二）

| 編號／事件 | 事件或首次可靠發布時間 | 去重與判定 |
|---|---|---|
| G6 北韓升級 240mm 多管火箭炮 | Yonhap 2026-09-24 07:22 KST = 9/24 06:22 TPE；KCNA 同日上午首次公開 9/22 測試。 | **續報，前次收錄 2026-09-23。** 前次是 Hwasong-11Ma 飛彈型號揭露；今日是不同武器系統，新增 240mm 導引火箭、100／115 公里射程與南部邊界部署訊號。性能來自 KCNA，未獨立驗證。https://en.yna.co.kr/view/AEN20260924000400315 |
| G7 South Africa 高階警官遭起訴 | Guardian 2026-09-23 05:38 EDT = 9/23 17:38 TPE；週一逮捕、週二出庭，首次可靠國際報導落在視窗內。 | 窄搜 `Shadrack Sibiya` 無命中，首次收錄。所有罪名均為控方指控，被告尚未答辯；不把起訴寫成定罪。https://www.theguardian.com/world/2026/sep/23/south-africa-top-police-officer-shadrack-sibiya-charged-rape-grooming |
| G8 日本首相公開支持 ICC | Guardian 2026-09-23 14:48 AEST = 9/23 12:48 TPE；演說發生於 9/22，首次可靠發布在視窗內。 | 窄搜 `Takaichi.*ICC|Japan.*International Criminal Court` 無同一聲明命中，首次收錄。這是政策立場，不是日本新法律或對美制裁。https://www.theguardian.com/world/2026/sep/23/japan-pm-sanae-takaichi-un-speech-support-for-icc-trump |
| G9 Jamaica 奴隸賠償請願轉交 Privy Council | Guardian 2026-09-22 21:15 EDT = 9/23 09:15 TPE；Jamaica 文化部長 9/22 在國會宣布。 | 9/7 提交請願是背景，今天新節點是 King Charles 已轉交 Judicial Committee。歷史窄搜無同一轉交事件命中，首次收錄。意見不會自動命令英國賠償。https://www.theguardian.com/world/2026/sep/23/jamaica-king-charles-to-refer-slavery-reparations-petition-to-privy-council |
| G10 Paris 地底古牆發現 | Guardian／AFP 2026-09-23 13:06 BST = 9/23 20:06 TPE；法國文化部同日公布。 | 窄搜 `ancient wall.*Paris|Lutetia.*wall` 無命中，首次收錄。牆體是否即 Parisii 的 Lutetia 防禦工事仍需考古驗證。https://www.theguardian.com/world/2026/sep/23/ancient-wall-paris-first-settlement-archaeology-roman |

## 排除、衝突與邊界判斷

- Hurricane Polo 已在 2026-09-23 收錄升為五級與沿岸停課、關港；截點前沒有比該項更重大的新登陸或災情節點，因此不因持續受關注而重列。
- Chagos 不是把 2 月川普撤回支持改寫成新事件；本次只收錄 9/23 英國政府暫停付款及確認現有協議無法推進的新政策節點。
- 北韓 240mm 火箭炮測試發生於 9/22，但 KCNA／Yonhap 在 9/24 06:22 TPE 才首次可靠公開，故依首次可靠發布時間入窗；與 9/23 的 Hwasong-11Ma 是不同武器事件。
- Jamaica 原請願於 9/7 提交，本次只收錄王室已轉交 Privy Council 的新法律程序；不把舊請願重新包裝。
- 世界 Top 10 排序綜合 AP、Reuters、Guardian、Yonhap／KCNA、國際媒體首頁顯著性與跨區域影響，不宣稱有精確的全球社群討論量排行。
- 傷亡數、武器性能、產品效能與全球上市安排保留來源限制；官方或公司單方宣稱不寫成獨立驗證結果。

## 發布紀錄

- pipeline 內容 commit：`943c1c1a0a2d91a00a145f253f17be886640abc2`。
- GitHub Pages 日期頁、`latest-slides.html` 與根入口均通過 HTTP 與完整位元組 SHA-256 比對。
- 唯一私人 LINE watchdog 於 `2026-09-24T08:13:55+08:00` 回報 `Sent LINE message`，exit code 0；未使用 `scripts/send_line_daily_slides.py`。
- 公開頁：https://lucaskk.github.io/daily-news/wiki/daily/2026/09/2026-09-24/slides-2026-09-24.html?v=20260924-081313-reader
- pipeline checkpoint 已進入 `complete`；強制 `check` 與 localhost 結果另於收尾後記入 wiki log。
