---
title: "2026-09-27 每日新聞來源與時間筆記"
date: 2026-09-27
type: source-notes
status: research-complete
tags: [daily-news, sources, provenance, deduplication]
---

# 2026-09-27 每日新聞來源與時間筆記

## 研究範圍

- Asia/Taipei 研究截點：`2026-09-27 14:43:15 +08:00`
- 全球新聞 24 小時窗：`2026-09-26 14:43:15` 至 `2026-09-27 14:43:15`（Asia/Taipei）
- 全球新聞 UTC 窗：`2026-09-26T06:43:15Z` 至 `2026-09-27T06:43:15Z`
- 科技／AI 產品 7 日窗：`2026-09-20 14:43:15` 至 `2026-09-27 14:43:15`（Asia/Taipei）
- 科技／AI 產品 UTC 窗：`2026-09-20T06:43:15Z` 至 `2026-09-27T06:43:15Z`
- 研究模式：`legacy`。選題由 AI 查證；Python 負責索引、渲染、結構檢查、發布與配送。
- 選題前已執行 `build_product_news_ledger.py`，重建 611 列產品變更索引；模型沒有讀取完整歷史表。
- 去重範圍：`wiki/daily/` 下全部 `daily-news-*.md`、`source-notes-*.md` 與產品 ledger，只以候選實體、產品、動作和比對鍵窄搜命中列。

## 科技產品選題與去重

每次均檢查 Engadget、Cool3c 與官方頁。候選先窄搜完整歷史；WiCi 無命中後，依規則完整讀取最近七天表一次。Logitech 命中的是前一日「候選但未收錄」和不同產品 Yeti 2，並非相同產品變更。

| 項目 | 事件／發佈時間依據 | 窄化查詢與判定 |
|---|---|---|
| T1 WiCi／WiCi One／wireless external GPU／`wici-one-wireless-gpu` | Engadget 頁面標示 2026-09-26 15:45 EST，依頁面字面換算為 9/27 04:45 TPE；WiCi 官方頁提供 early access、US$1,999 起與 Q4 預期出貨，但未標精確發布時間。https://wici.ai/wici-one ; https://www.engadget.com/2269877/this-external-gpu-uses-wi-fi-to-transform-any-device-into-a-gaming-rig/ | 查詢 `WiCi One|wireless external GPU|Wi-Fi.*external GPU` 無歷史命中；再讀最近七天表無同一變更，首次收錄。Engadget 稱 preorder，官方只有 signup／reserve 表單，正文保留歧異。 |
| T2 Logitech G／PRO X3 SUPERSTRIKE、PRO X2 RAPID、PRO X3 LIGHTSPEED、PRO X CONTROL／正式發布／`logitech-pro-2026-lineup` | Logitech 官方公告日期 2026-09-23；Cool3c 發布 2026-09-24 00:00 TPE，確認台灣價格與展示。https://www.logitech.com/blog/2026/09/23/logitech-g-marks-10-years-of-pro-with-a-new-generation-of-competitive-gear/ ; https://www.cool3c.com/article/252187 | 查詢 `Logitech.*(PRO X3|PRO X2 RAPID|BLUE YETI 2)|PRO X3.*Logitech` 命中 9/26「候選未收錄」及 9/24 已收錄 Yeti 2。PRO 四款不是 Yeti 2，最近七天表也無相同列，首次收錄。 |

### 產品候選排除

- Meta Connect 2026 的 Meta VR Glasses 與 Ray-Ban Meta 已於 2026-09-25 收錄，9/26–9/27 沒有新的上市、權限或功能節點。
- Microsoft Copilot Home／Code／Autopilot、Google Gemini 3.8 Live Avatar、Cricut StickerPix 已於 2026-09-26 收錄，排除首頁重複。
- Logitech Yeti 2 已於 2026-09-24 收錄；本日只選不同的 PRO 產品線，不把同場活動合併重複。
- Cool3c 的 iPhone 18 Pro 重開機修復仍是「即將推出」，沒有已發布版本；折扣、評測、Shopping guide 與舊產品導購不收錄。
- Motorola Signature 27 與其他 Snapdragon Summit 新機雖在七日窗內，但本輪來源時間與正式全球上市節點較不明確，未優先於可核對的兩項產品。

## 全球 Top 10 時間、續報與歧異

| 項目 | 視窗內依據與去重結果 |
|---|---|
| G1 Iran 拒絕退讓 Hormuz 條件 | Al Jazeera live blog `datePublished=2026-09-27T00:00:00Z`，即 08:00 TPE。歷史窄搜命中 2026-09-25 Iran 七項條件與回應期限，因此標示續報；新進展是 Trump 拒絕提案與 Iran 表明不退讓。直播頁只採截點前內容。https://www.aljazeera.com/news/liveblog/2026/9/27/iran-war-live-tehran-awaits-official-response-as-trump-rejects-hormuz-plan |
| G2 Ethiopia 軍方表態與 Eritrea 指控 | Al Jazeera `datePublished=2026-09-27T04:59:50Z`，即 12:59:50 TPE。命中 2026-09-25 Tigray 戰事擴至 Afar／Amhara，標示續報；新進展是軍方首長首度正式表態、戰略克制與直接指控 Eritrea，Eritrea 否認。https://www.aljazeera.com/news/2026/9/27/ethiopias-army-promises-restraint-amid-fears-of-new-civil-war |
| G3 Germany–Russia 外長會談 | Al Jazeera `datePublished=2026-09-27T03:36:19Z`，即 11:36:19 TPE；AP 另報會談在 UN 場邊約 20 分鐘。窄搜 `Germany.*Russia.*Wadephul.*Lavrov|first foreign ministers meeting` 無同一事件命中，首次收錄。https://www.aljazeera.com/news/2026/9/27/german-russian-foreign-ministers-hold-rare-talks-amid-rising-tensions ; https://www.stamfordadvocate.com/news/world/article/german-russian-foreign-ministers-have-rare-22450492.php |
| G4 Venezuela 釋放 39 名政治犯 | Al Jazeera `datePublished=2026-09-27T01:42:46Z`，即 09:42:46 TPE；釋放發生於星期五至星期六並在第二輪談判後確認。窄搜 `Venezuela.*(prisoner|release|amnesty)|委內瑞拉.*(政治犯|釋放)` 無同一事件命中。JEP、Foro Penal 剩餘人數不同，保留歧異。https://www.aljazeera.com/news/2026/9/27/venezuela-frees-39-political-prisoners-after-post-maduro-talks |
| G5 EU 逾 €710m 人道援助 | Al Jazeera `datePublished=2026-09-27T01:27:13Z`，即 09:27:13 TPE。窄搜 `European Union.*710 million.*humanitarian|EU.*710m.*Africa` 無同一配置命中。原文另有年度累計疑似誤植，本報不採該句，只列可逐項核對的本輪金額。https://www.aljazeera.com/news/2026/9/27/eu-unlocks-humanitarian-aid-for-africa-and-other-crisis-hit-regions |
| G6 Athens 爆炸確認六死 | 爆炸在窗口前發生；窗口內重大新節點是 9/26 確認尋獲六名死者。Al Jazeera `datePublished=2026-09-26T23:26:31Z`，即 9/27 07:26:31 TPE；Guardian 首發 9/26 12:54 EDT，即 9/27 00:54 TPE。窄搜無命中，首次收錄。原因仍未確認，疑似 gas leak 不寫成定論。https://www.aljazeera.com/news/2026/9/26/four-american-tourists-among-6-killed-in-suspected-gas-leak-blast-in-athens ; https://www.theguardian.com/world/2026/sep/26/greek-authorities-seek-answers-after-six-killed-in-athens-apartment-block-explosion |
| G7 美國東北 nor'easter | Al Jazeera `datePublished=2026-09-26T22:51:57Z`，即 9/27 06:51:57 TPE。窄搜 storm name、73,000 outages 與 NYC fallen tree 無命中，首次收錄。停電與航班為動態快照。https://www.aljazeera.com/news/2026/9/26/powerful-storm-brings-flooding-power-outages-to-northeastern-united-states ; https://www.theguardian.com/us-news/2026/sep/26/noreaster-north-east-us |
| G8 Saint Vincent 槍擊 | 槍擊 9/25 22:30 AST = 9/26 10:30 TPE，早於下限；窗口內重大節點是 9/26 警方確認四死四傷、展開追捕並調查關聯案件。Al Jazeera `datePublished=2026-09-26T22:38:01Z`，即 9/27 06:38:01 TPE。窄搜無命中，首次收錄。年度謀殺累計來源為 37–39，不覆寫歧異。https://www.aljazeera.com/news/2026/9/26/deadly-shooting-hits-caribbean-islands-of-saint-vincent-and-the-grenadines ; https://www.thehour.com/news/world/article/shooting-leaves-4-dead-in-caribbean-nation-known-22450637.php |
| G9 Trump 放寬燃油經濟標準 | Al Jazeera `datePublished=2026-09-26T21:51:56Z`，即 9/27 05:51:56 TPE；Trump 9/26 宣布核准。窄搜本次核准節點無命中。正式細節尚待星期一，34.5 mpg 只標示為先前方案。https://www.aljazeera.com/news/2026/9/26/trump-says-he-is-rolling-back-biden-era-us-fuel-economy-rules-for-cars ; https://apnews.com/article/363fcad4bb90a0859f6906d086aeac69 |
| G10 Colombia 引渡 Rojas | Al Jazeera `datePublished=2026-09-26T19:21:53Z`，即 9/27 03:21:53 TPE。窄搜 `Colombia.*Geovany Andrés Rojas|Comandos de la Frontera.*extradition|the Spider.*Colombia` 無同一事件命中，首次收錄。指控未判決，使用 allegedly／被指而不寫成定罪。https://www.aljazeera.com/news/2026/9/26/colombia-extradites-leader-of-armed-group-to-us-in-shift-towards-washington |

## 未入選候選與原因

- Brazil fixed-odds betting ban：Guardian 文章首發在 24 小時窗內，但 Brazil 官方行動與政府公告日期為 2026-09-25，早於世界新聞下限；不能因後續報導時間而當成新事件，排除。
- Ukraine 最大鋼廠因攻擊停產：Guardian 首發換算約 2026-09-26 09:00 TPE，早於下限 14:43:15，排除。
- AP／Reuters UN General Assembly 本週整理：首發約 2026-09-26 13:01 TPE，早於下限，且多為已發生事件總結，排除。
- Hamas 批評 Board of Peace 不與 UNRWA 合作：視窗內主要是反應性聲明，政策決定本身較早，重要性低於保留項目。
- Iraq 尋求 Iranian flights 禁令豁免：視窗內但仍是請求階段，沒有批准或執行結果，未列入 Top 10。
- Trump–Xi 峰會、UN settlement-company database、Meta Connect 等主線已於 9/25–9/26 收錄，沒有足以再次占用名額的新節點。

## 發布紀錄

- 尚待 pipeline 完成後補記 Git commit、Pages 位元組驗證、LINE watchdog 與 localhost 狀態。
