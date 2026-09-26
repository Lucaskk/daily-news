---
title: "2026-09-26 Daily News Source Notes"
type: source-notes
created: 2026-09-26
updated: 2026-09-26
status: research-complete
tags: [daily-news, provenance, deduplication]
sources: []
---

# 2026-09-26 每日新聞來源筆記

## 固定研究截點與時間窗

- Asia/Taipei 截點：`2026-09-26T08:01:24+08:00`。沿用當日私人 checkpoint；研究接續時沒有移動截點。
- 全球新聞 24 小時窗：`2026-09-25 08:01:24` 至 `2026-09-26 08:01:24`（Asia/Taipei）；UTC 為 `2026-09-25T00:01:24Z` 至 `2026-09-26T00:01:24Z`。
- 科技產品 168 小時窗：`2026-09-19 08:01:24` 至 `2026-09-26 08:01:24`（Asia/Taipei）；UTC 為 `2026-09-19T00:01:24Z` 至 `2026-09-26T00:01:24Z`。
- 研究模式：`legacy`。AI 負責搜尋、來源查證、語意去重、排序與摘要；Python 負責索引、固定渲染、結構驗證、發布與 LINE 配送。
- 選題前已執行 `python3 scripts/build_product_news_ledger.py`，結果為 608 筆產品變更／100 份既有日報。
- 完整產品歷史沒有整份讀入模型。每個候選先用公司、產品、更新動作及比對鍵窄搜 `product-news-ledger.md`、全部 `daily-news-*.md` 與 `source-notes-*.md`；Microsoft 有歷史命中，Google 與 Cricut 無命中後，才完整核對最近七天表。
- 已檢查 Engadget 與 Cool3c。兩站用於發現候選與補充產品脈絡；規格、上線日期與狀態優先回查官方公告。促銷、導購、評論與未形成可驗證產品狀態的內容排除。

## 科技／AI 產品候選與去重

| 公司／產品／更新／比對鍵 | 發布時間與來源 | 歷史查詢與判定 |
|---|---|---|
| Microsoft／Copilot Home、Code、Autopilot／正式介紹新 Copilot 架構與 Managed Runtime public preview／`microsoft-copilot-home-code-autopilot` | Microsoft 官方索引標示 2026-09-25；Engadget metadata 為 `2026-09-25T12:00:00Z`，即 9/25 20:00 TPE。https://www.microsoft.com/en-us/copilot/blog/content-type/news/ ; https://partner.microsoft.com/en-us/blog/article/ai-at-work-marketing-moment ; https://www.engadget.com/2268096/microsofts-copilot-app-adds-office-natural-coding-and-automation/ | 窄搜 `Microsoft.*Copilot.*(Home|Code|Autopilot)|(Home|Code|Autopilot).*Copilot.*Microsoft|microsoft-copilot-home-code-autopilot` 命中 2026-07-30 的 Microsoft roadmap。**續報，前次收錄 2026-07-30；前次是 super app 將整合 chat、Cowork、Autopilots 與 code 的規畫，今日新進展是 Home／Code／Autopilot 正式成為產品入口，並公布 Managed Runtime public preview。** 收錄 T1。 |
| Google／Gemini 3.8 Live with Live Avatar／在 Gemini Enterprise 上線／`gemini-3-8-live-avatar-enterprise` | Google 官方發布日期 2026-09-24；宣布當日起在 Gemini Enterprise 提供。https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-with-live-avatar/ ; https://www.engadget.com/2268587/google-video-avatars-gemini-3-8-live-agent/ | 窄搜 `Google.*Gemini 3\.8 Live.*Avatar|Gemini 3\.8 Live.*Avatar.*Google|gemini-3-8-live-avatar-enterprise` 無命中；因此完整讀取最近七天表，仍無相同變更，收錄 T2。 |
| Cricut／StickerPix Print、StickerPix Print + Cut／新品正式發布與開賣／`cricut-stickerpix-print-cut-release` | Cricut 官方發布日期 2026-09-24；官方稱兩款全新機種，Engadget 報導起價 US$169／US$299。https://cricut.com/blog/introducing-cricut-stickerpix/ ; https://www.engadget.com/2269278/cricuts-new-diy-machines-let-you-print-and-cut-your-own-stickers/ | 窄搜 `Cricut.*StickerPix|StickerPix.*Cricut|cricut-stickerpix-print-cut-release` 無命中；因此完整讀取最近七天表，仍無相同變更，收錄 T3。 |
| Xiaomi／Smart Band 11 | Cool3c 首頁候選。 | 主要是媒體產品消息，與三項有官方公告、企業功能或全新品類的候選相比優先度較低，未用來補位。 |
| Logitech／PRO X3 SUPERSTRIKE | Cool3c 首頁候選。 | 屬遊戲周邊新品候選，但本次只保留跨軟體、企業 AI 與新創作設備三項最高價值產品；未把數量湊滿當作理由。 |
| Meta VR Glasses、Google Photos Redact、Razer Kiyo V2 Pro | Engadget／科技首頁仍有討論。 | 都已於 2026-09-25 收錄，沒有新的上市、權限、版本或重大功能狀態，排除重複。 |

## 全球新聞入選時間與續報依據（研究批次一）

| 編號／事件 | 事件或首次可靠發布時間 | 去重與判定 |
|---|---|---|
| G1 Trump–Xi 峰會結束，未形成重大 AI 協議 | Guardian RSS `2026-09-25T22:11:52Z`，即 9/26 06:11:52 TPE；峰會在研究窗內結束。 | **續報，前次收錄 2026-09-25。** 前次是會談開始與貿易休戰延至 2027-01-10；今日新增是峰會結束後的成果盤點：未就 AI、Taiwan、Iran 或全面貿易方案形成重大突破，只有有限成果與後續會晤可能。https://www.theguardian.com/technology/2026/sep/25/trump-xi-ai-arms-race ; https://www.theguardian.com/us-news/2026/sep/25/key-takeaways-trump-xi-summit-whitehouse-china-ai-trade |
| G2 美國最高法院允許 Trump 政府使用 SAVE 協助選民資格核驗 | Al Jazeera 2026-09-25 發布；最高法院同日作成 emergency order。 | 窄搜 `SAVE.*voter|voter verification.*SAVE|Supreme Court.*SAVE` 無同一裁定命中，首次收錄。這是緊急程序，不是實體爭議的最終判決；三名 liberal justices 反對。https://www.aljazeera.com/news/2026/9/25/us-top-court-allows-trump-to-use-controversial-voter-verification-system |
| G3 聯合國把 61 家公司加入以色列屯墾區活動資料庫 | Reuters 2026-09-25 10:45 EDT，即 9/25 22:45 TPE；UN Human Rights Office 同日更新。 | 窄搜 `61 companies.*settlements|settlement database.*214|UN.*companies.*settlements` 無同一更新命中，首次收錄。新增 61 家、移除 5 家後共 214 家；名單採 reasonable grounds 標準，不等同法院定罪或自動制裁。https://www.marketscreener.com/news/un-expands-list-of-companies-linked-to-israeli-settlements-ce785adfde8cf122 ; https://1-e8259.azureedge.net/news/2026/9/25/un-expands-list-of-firms-involved-in-illegal-israeli-settlement-activities |
| G4 南非外長警告美國若制裁 ICC 機構本身將擾亂運作 | Guardian RSS `2026-09-25T18:33:54Z`，即 9/26 02:33:54 TPE；Ronald Lamola 在 UN 活動發言。 | **續報，前次相關收錄為 2026-08-19、2026-08-27 與 2026-09-24。** 前次分別是個人制裁、ICC 向日本求援及日本首相支持 ICC；今日新增是對「制裁法院機構本身」的具體警告，影響層級由個人資產與往來擴大到法院運作。https://www.theguardian.com/world/2026/sep/25/trump-israel-icc-threats |
| G5 Houthi 攻擊增加後，Saudi allies 動員且 France 向 Yanbu 派兵與雷達 | Al Jazeera 2026-09-25 發布；France 與 Saudi／Turkey／Pakistan 的部署、會議安排在窗內確認。 | **續報，前次收錄 2026-09-01。** 前次是 Mecca Joint Defence Agreement 首次委員會與 Saudi secretariat；今日新增是 Houthi 攻擊下的緊急軍方會議及 France 向 Yanbu 派出人員、雷達與防禦系統。聯防條約尚未正式啟動。https://www.aljazeera.com/news/2026/9/25/saudi-arabia-allies-line-up-support-as-houthi-attacks-mount |

## 全球新聞入選時間與續報依據（研究批次二）

| 編號／事件 | 事件或首次可靠發布時間 | 去重與判定 |
|---|---|---|
| G6 Pakistan 在 PTI 聲援 Imran Khan 遊行前封鎖 Islamabad | Guardian RSS `2026-09-25T13:44:55Z`，即 9/25 21:44:55 TPE；安全部署與拘留在同日發生。 | 窄搜命中 2026-08-21 的 Khan hospital transfer，但不是本次首都封鎖與遊行，首次收錄此事件。官方部署約 22,000 名安全人員並禁止集會；PTI 遊行時間在首批報導時仍可能調整。https://www.theguardian.com/world/2026/sep/25/pakistan-lockdown-islamabad-imran-khan-party-march |
| G7 UNHCR 指 Sudan 逃往 Chad 人流增至每日約 400 人 | Al Jazeera 2026-09-25 發布；UNHCR 同日公布本年已逾 55,000 人的新數字。 | 窄搜 `Sudan.*Chad.*55,000|400.*day.*Chad|UNHCR.*Chad.*funding` 無同一新通報命中，首次收錄。400 人／日約為先前數月速度 20 倍；援助計畫僅約 20% funded，數字仍會隨登記更新。https://www.aljazeera.com/news/2026/9/25/more-than-55000-sudanese-refugees-flee-to-chad-as-un-calls-for-funding |
| G8 美國上訴法院維持 Pentagon 對 Anthropic 的 supply-chain risk designation | Reuters 2026-09-25 12:53 EDT，即 9/26 00:53 TPE；法院同日作成判決。 | **續報，前次收錄 2026-06-06。** 前次是政府與 Anthropic 緊張似有緩和、DoD 仍在訴訟中捍衛黑名單；今日新增是上訴法院維持 designation，使爭議從行政決定與訴訟進入上訴裁判。https://www.marketscreener.com/news/anthropic-s-pentagon-blacklist-upheld-in-us-appeals-court-how-the-conflict-unfolded-ce785adfd18af02c |
| G9 New Mexico 陪審團認定 Meta 就 Facebook 資料作法誤導居民 | Reuters 2026-09-25 12:50 EDT，即 9/26 00:50 TPE；CBS／AP 2026-09-25 14:50 EDT，即 9/26 02:50 TPE。 | 窄搜命中 2026-08-08 的 New Mexico 兒童安全案，但本案是 Cambridge Analytica／資料作法與 29 項陳述的不同訴訟。首次收錄此裁決節點。陪審團認定 29 項中 26 項具誤導性；罰金仍待法官決定，Meta 表示反對。https://www.marketscreener.com/news/meta-misled-users-about-facebook-data-practices-new-mexico-jury-finds-ce785adfd08cf525 ; https://www.cbsnews.com/news/facebook-liable-deceiving-users-cambridge-analytica/ |
| G10 Pope Leo 在 France 訪問中警告 AI 可能侵蝕人性 | Guardian 首發 2026-09-25 12:01 EDT，即 9/26 00:01 TPE；Euronews 亦在 9/25 16:48 CEST 發布。 | 窄搜命中其他 Pope Leo 活動，但無本次 France 訪問與 AI 倫理演說，首次收錄。這是首位教宗 18 年來對 France 的完整正式訪問；AI 內容屬倫理與政策倡議，不是新法規。https://www.theguardian.com/world/2026/sep/25/pope-leo-ai-threat-to-humanity-three-day-france-visit ; https://www.channelnewsasia.com/world/pope-leo-warns-ai-use-risks-humanity-6410816 |

## 排除、衝突與邊界判斷

- Democratic Republic of the Congo 的 Lake Tanganyika 船難，AP 首發為 2026-09-24 13:44 EDT，即 9/25 01:44 TPE，早於全球窗下界約 6 小時 17 分；Al Jazeera 9/25 再刊不改變事件／首發時間，因此排除。
- Argentina 32.3% poverty rate 的官方數據與 Reuters 首次可靠發布都在 9/24，早於全球窗下界；即使 9/25 仍有報導或社群討論，也不當成新事件。
- Netanyahu 在 UN 演說與代表退場發生於 9/24 15:28 EDT 左右，即 9/25 03:28 TPE，早於下界；排除。
- UAE 對 Iranian airline 的禁令在 Thursday 已宣布，無法確認新事件落在全球窗內；排除。
- Michigan CEO 的「Lake America」撤離消息實際在 9/23 宣布，9/25 報導只是後續重述；排除。
- Ukraine 9/24 strikes 的主要事件與首次可靠發布時間早於下界；沒有以文章更新時間重列。
- SAVE 命令不代表州政府被強制使用系統，也不是最終 merits ruling；現行聯邦法對選舉前 90 日內系統性清冊移除仍有限制。
- UN settlement database 採「合理理由」納入，Israel 批評機制政治化；本文保留這項反對意見，不把資料庫等同刑事定罪。
- Saudi Arabia 報告攔截 6 枚 ballistic missiles，France 已確認部署；但聯防 pact 是否正式觸發、後續作戰範圍及 Houthi 戰損未有一致獨立驗證。
- Anthropic 案報導指出部分關鍵政府用途仍可延續；blacklist 主要影響 defense supply chain contracts，不寫成所有聯邦使用立即停止。
- Meta 案陪審團認定的 violations 可能帶來每次最高 US$5,000 的法定處罰，但實際 penalty 尚未由法官裁定，不能以理論上限當成既成罰款。
- 全球 Top 10 排序綜合 Reuters、AP、Guardian、Al Jazeera、CBS、官方與跨區域影響；這是編輯綜合，不宣稱有精確全球社群討論量排名。
- 只有日期的官方頁保留日期層級；已知精確發布時間統一換算 Asia/Taipei，不以更新、重刊或首頁熱門時間取代事件時間。

## 後續追蹤

- Trump–Xi 峰會後是否產生可核對的 AI、tariff、rare earths 或 Taiwan 後續協議；1 月貿易休戰期限前是否落實具體措施。
- ICC 是否遭美國擴大到機構層級制裁、盟國如何維持銀行與供應鏈；SAVE 命令在 merits case 與各州實際使用上的後續。
- Saudi allies 的 military chiefs meeting、France 在 Yanbu 的部署細節，以及 Houthi 攻擊是否觸發正式共同防衛。
- Anthropic 上訴與 defense contracts 影響、Meta penalty 裁定，以及 Live Avatar 自訂形象的 allowlisting、安全與 SynthID 可驗證性。

## 發布紀錄

- pipeline 內容 commit：`5ae20940c279917031b3e71d36f6cb046c0daa90`。
- GitHub Pages 日期頁、`latest-slides.html` 與根入口均通過 HTTP 與完整位元組 SHA-256 比對。
- 唯一私人 LINE watchdog 於 `2026-09-26T08:19:27+08:00` 回報 `Sent LINE message`，exit code 0；未使用 `scripts/send_line_daily_slides.py`，也未重送。
- 公開頁：https://lucaskk.github.io/daily-news/wiki/daily/2026/09/2026-09-26/slides-2026-09-26.html?v=20260926-081842-reader
- pipeline checkpoint 為 `complete`；強制 `check --date 2026-09-26` exit 0。26 項 renderer／pipeline 測試、13 篇主文、3 張後續追蹤卡、逐項來源及 JavaScript 語法檢查通過。
