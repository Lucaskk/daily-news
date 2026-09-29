---
title: "2026-09-29 每日新聞來源與時間筆記"
date: 2026-09-29
type: source-notes
status: research-complete
tags: [daily-news, sources, provenance, deduplication]
---

# 2026-09-29 每日新聞來源與時間筆記

## 研究範圍

- Asia/Taipei 研究截點：`2026-09-29 08:00:30 +08:00`
- 全球新聞 24 小時窗：`2026-09-28 08:00:30` 至 `2026-09-29 08:00:30`（Asia/Taipei）
- 全球新聞 UTC 窗：`2026-09-28T00:00:30Z` 至 `2026-09-29T00:00:30Z`
- 科技／AI 產品 7 日窗：`2026-09-22 08:00:30` 至 `2026-09-29 08:00:30`（Asia/Taipei）
- 科技／AI 產品 UTC 窗：`2026-09-22T00:00:30Z` 至 `2026-09-29T00:00:30Z`
- 研究模式：`legacy`。AI 負責來源搜尋、查證、語意去重與摘要；Python 負責產品索引、固定結構檢查、渲染、發布與配送。
- 選題前已執行 `python3 scripts/build_product_news_ledger.py`，重建 616 列產品變更索引（103 份既有日報）；模型未讀取完整歷史表。
- 歷史去重範圍：`wiki/daily/` 下全部 `daily-news-*.md`、`source-notes-*.md` 與產品 ledger，只以候選實體、產品、更新動作與比對鍵窄搜命中列。

## 科技產品兩輪搜尋、時間與去重

- 第一輪廣泛掃描：檢查 Engadget、The Verge、TechCrunch、WIRED、Ars Technica、Cool3c、Yahoo 奇摩科技、TechOrange 科技報橘與數位時代的最新／聚合結果，共整理 10 個表面候選。逐頁核對原始日期後，Meta Seller／Facebook Verified、Sonos app、Anbernic RG SP、Lola × Miffy、Roku Labs、Huawei Ascend 960DT、Apple EU ATT 變更與 Instinct／Muse calls 等八項實為 7 月或 9 月 17 日舊文；Gemini Spark 結果也只回到 7–8 月既有更新。第一輪只有 SpaceX Starship Flight 14 的「實際首次入軌」是窗內合格新節點，初選 1 則。
- 第二輪官方定向補查：因第一輪少於 5 則，查 OpenAI release notes、GitHub Changelog、AWS What's New／News Blog、Google Products、Apple Newsroom、Microsoft／Azure、NVIDIA developer updates，涵蓋 AI 產品、開發工具、雲端服務與硬體。找到 5 個未重複且日期可定位的合格變更：ChatGPT Health 個人化摘要、Claude Sonnet 5.5 進入 GitHub Copilot、CodeQL 2.27.1、CloudWatch Omni GA、AWS End User Messaging 的 WhatsApp 雙向語音通話。第二輪 5 則，加上第一輪 1 則，共保留 6 則；未為達成 5–8 目標納入過期或弱證據候選。
- 歷史 `rg`：每個候選先以公司、產品、更新動作與比對鍵窄搜完整產品 ledger、全部日報與來源筆記。五個新變更無相同命中；Starship 命中 2026-09-20 的 Flight 14 日期／任務規劃，故本次標示續報。因有無命中候選，依規則完整讀取一次 `product-news-recent-7d.md`（26 列），沒有發現五個新變更；Starship 表列的仍是任務預告而非實際入軌結果。

| 項目 | 事件／發佈時間依據 | 窄化查詢、命中與判定 |
|---|---|---|
| T1 SpaceX／Starship Flight 14／首次進入地球軌道並部署 26 顆 Starlink V3／`starship-flight14-orbit` | SpaceX 官方任務頁列 2026-09-28 12:15–13:30 UTC 發射窗；AP 於 12:50 UTC（2026-09-28 20:50 TPE）首次完整發布已進入軌道。飛船因上升段引擎提早停機，把原訂約十小時／六圈縮短為約三小時，仍完成衛星部署與受控濺落。https://www.spacex.com/launches/sl-17-50%3A1008 ; https://tech.yahoo.com/science/articles/spacexs-supersized-starship-launches-toward-125036831.html ; https://www.washingtonpost.com/health/2026/09/28/spacex-starship-orbit/5033407a-bb3b-11f1-81fc-9b76f8343b6c_story.html | 查詢 `SpaceX.*Starship.*orbit|Starship.*first.*orbit|starship-orbit` 命中 2026-09-20：當時只收錄 9/28 時程、監管待定與 V3 部署計畫。本次是計畫變成已完成的首次入軌與實際衛星部署，屬重大新階段，標示「續報｜」並引用前次日期。 |
| T2 GitHub／GitHub Copilot／Claude Sonnet 5.5 GA／`copilot-claude-sonnet-5-5` | GitHub Changelog 官方標示 2026-09-28 Release；Sonnet 5.5 對 Copilot Pro、Pro+、Max、Business、Enterprise 逐步 GA，可在 IDE、CLI、coding agent、app、網站與 mobile 選用。https://github.blog/changelog/2026-09-28-claude-sonnet-5-5-in-github-copilot/ | 查詢 `GitHub.*Claude Sonnet 5.5|Claude Sonnet 5.5.*Copilot|copilot-sonnet-5-5` 無命中；近七日表只有 Claude Opus 5.5 與 GitHub Copilot 其他模型，模型／可用性變更不同，首次收錄。 |
| T3 OpenAI／Health in ChatGPT／個人化健康摘要／`chatgpt-health-personalized-summaries` | OpenAI ChatGPT release notes 精確段落日期為 2026-09-28：Health tab 現可選擇 chart、metric 或 record，依已連接健康資訊取得個人化說明與洞察。https://help.openai.com/en/articles/6825453-chatgpt-release-notes | 查詢 `OpenAI.*Health.*personalized summaries|Health.*chart.*metric.*record|chatgpt-health-summaries` 無相同新功能命中；2026-07-24 已收錄 Health in ChatGPT 向美國使用者開放，這次是其後新增的資料導向摘要功能，標示「續報｜」並寫明前次內容。 |
| T4 AWS／Amazon CloudWatch Omni／正式 GA／`aws-cloudwatch-omni-ga` | AWS What's New 標示 2026-09-23 GA；Omni 以 OpenTelemetry 整合 application／agent telemetry，提供自然語言調查、DevOps Agent、跨 AWS accounts／Regions／Azure 的服務圖與 IDE extension。https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-cloudwatch-omni-ai/ ; https://aws.amazon.com/blogs/aws/introducing-amazon-cloudwatch-omni-ai-powered-observability-for-generative-ai-and-agentic-workloads/ | 查詢 `AWS.*CloudWatch Omni|CloudWatch Omni.*AWS|cloudwatch-omni` 無命中；近七日表無同產品，首次收錄。官方列出的 GA 區域為 N. Virginia、Oregon 與 Ireland，不能概括為全球所有 region。 |
| T5 AWS／End User Messaging Social／WhatsApp 雙向語音通話／`aws-whatsapp-voice-calling` | AWS What's New 標示 2026-09-25：企業可用既有 verified WhatsApp business identity 接聽客戶通話，也能在取得同意後外撥；console 與 API 均可管理。https://aws.amazon.com/about-aws/whats-new/2026/09/aws-end-user-messaging-voice-calling-whatsapp/ | 查詢 `AWS End User Messaging.*WhatsApp.*voice|WhatsApp voice.*AWS|aws-whatsapp-voice` 無命中；近七日表無同變更，首次收錄。3 月官方教學僅是非同步 voice notes，本次是即時雙向 voice calling，並非同一功能。 |
| T6 GitHub／CodeQL 2.27.1／安全查詢與語言支援更新／`github-codeql-2-27-1` | GitHub Changelog 標示 2026-09-25 Improvement；新增 C／C++ 與 C# queries、Kotlin 2.4.20 支援，更新 Go、JavaScript／TypeScript、Rust 與 Actions data-flow／accuracy。github.com code scanning 自動部署，GHES 3.24 將內含此版。https://github.blog/changelog/2026-09-25-codeql-2-27-1-adds-c-and-c-query-and-kotlin-2-4-20-support/ | 查詢 `GitHub.*CodeQL 2.27.1|CodeQL 2.27.1|codeql-2-27-1` 無命中；近七日表無同版本，首次收錄。這是可辨識版本發布，不是一般教學文章。 |

### 產品候選排除

- 固定來源池首頁把多篇舊文重新列為近期內容；核對頁面原始日期後，Meta Seller／Facebook Verified（7 月）、Sonos app／Anbernic／Lola（7 月）、Roku Labs／Huawei 960DT／Apple EU ATT／Instinct 與 Muse calls（9 月 17 日）均早於七日下限，排除，不以 crawl／更新時間冒充新品。
- Gemini Spark「expanded access」搜尋只命中 7 月 Mac／Chrome 與 8 月全球化、模型更新；完整歷史亦已有多次收錄，本輪沒有可定位的新發布段落。
- Google Health、Google Photos、Meta Connect、WiCi、Logitech G、Copilot Home／Code／Autopilot 等均已在 9 月 25–28 日收錄，沒有新的獨立變更，不重複。
- Google Vids 的 Gemini Omni HD 影片更新雖在 9 月 23 日官方發布，但 2026-07-17 已收錄 Gemini Omni 與 Vids 的核心生成／avatar 能力；本輪差異不足以優先於全新項目，列為小幅續更而不占一則。

## 全球 Top 10 時間、去重與歧異

| 排名／項目 | 事件／首次可靠發佈時間依據 | 歷史去重與判定 |
|---|---|---|
| G1 Myanmar Rakhine 市場空襲 | AP／Washington Post 於 2026-09-28 11:58 EDT 發布，即 2026-09-28 23:58 TPE；當日約中午兩枚炸彈落在 Kyauktaw 市場，Arakan Army 與救援人員通報 33 死、36 傷。https://www.washingtonpost.com/world/2026/09/28/myanmar-market-airstrike-deaths/6961ba26-bb55-11f1-81fc-9b76f8343b6c_story.html | 窄搜 `Kyauktaw|Rakhine.*market.*airstrike|market.*airstrike.*33` 無相同事件命中，首次收錄。Myanmar 軍方尚未回應，死傷主要來自 Arakan Army 與現場救援者，保留來源限制。 |
| G2 Russia 大規模無人機攻擊 Ukraine | AP／The Journal 於 2026-09-28 08:09 MT 發布，即 2026-09-28 22:09 TPE；彙整當日 Kyiv、Dnipro、Kharkiv、Zaporizhzhia、Odesa 等地新攻擊，官方合計至少 7 死、80 餘傷。https://www.the-journal.com/articles/associated-press/russian-drones-hammer-apartments-offices-and-a-cultural-landmark-in-ukraine-killing-7/ | 窄搜 `National Academy.*Kyiv|Dnipro.*80 wounded|Russian drones.*cultural landmark` 無同一輪攻擊命中；9/28 日報收錄的是前一日另一波九死攻擊，本次為不同日期、地點與傷亡節點，首次收錄。早期 AP 版本曾列 3 死／41 傷，數字隨地方通報上修。 |
| G3 RAF Fairford 調查進展 | AP／Hindustan Times 於 2026-09-29 00:09:05 IST 發布，即 2026-09-29 02:39:05 TPE；五名 23–25 歲 British nationals 被附嚴格條件保釋，警方列 Iran、Russia 與非國家武裝為調查方向。https://www.hindustantimes.com/world-news/us-news/5-men-arrested-near-a-us-run-air-base-are-bailed-as-uk-police-probe-whether-there-s-a-link-to-iran-101790620746257.html ; https://www.washingtonpost.com/world/2026/09/28/fairford-raf-base-suspects-arrested-plot/141b290c-bb51-11f1-81fc-9b76f8343b6c_story.html | **續報，前次 2026-09-28。** 前次僅知五人被捕、車輛受檢且國籍、動機與爆裂物均未公開；本次新增國籍、年齡、保釋、調查方向與 Iran 否認。PA 無具名來源稱未發現可用爆裂物，Washington Post／AP 則稱正檢查疑似爆裂物，兩說並列、不下結論。 |
| G4 Congo Ebola 突破 8,000 例 | AP／ABC News 於 2026-09-28 05:45 EDT 發布，即 2026-09-28 17:45 TPE；剛果衛生部截至 9/26 統計 8,067 例、3,901 死、63 個 health zones／7 省，致死率逾 48%。https://abcnews.com/International/wireStory/congo-ebola-outbreak-tops-8000-confirmed-cases-disease-136816027 ; https://ny1.com/nyc/all-boroughs/ap-top-news/2026/09/28/congo-ebola-outbreak-tops-8000-confirmed-cases-as-disease-remains-out-of-control | **續報，前次 2026-09-20。** 前次是兩萬名一線人員接種計畫；更早 9/12 為 7,022 例／3,398 死。本次新增跨過 8,000 例、3,901 死、63 health zones 與 50 名醫護死亡，屬改變規模判讀的新官方數字。監測不足可能低估實際傳播。 |
| G5 US–Iran 斡旋仍繼續 | AP／Washington Post 於 2026-09-28 08:26 EDT 發布，即 2026-09-28 20:26 TPE；三名官員稱 Qatar 等中介仍與雙方接觸，間接談判預計星期一恢復。https://www.washingtonpost.com/world/2026/09/28/iran-trump-negotiations-war-strait-nuclear/d2f05fa6-bb37-11f1-81fc-9b76f8343b6c_story.html | **續報，前次 2026-09-27。** 前次為 Trump 公開拒絕 Tehran 提案；本次新增是兩名官員稱 Washington 尚未正式拒絕現行草案、斡旋仍進行，並揭露先開 Strait／撤 blockade、再處理 sanctions 的順序。官員均匿名，White House 未確認。 |
| G6 Ethiopia 指控三鄰國支援 Tigray | AP／Washington Post 於 2026-09-28 12:10 EDT 發布，即 2026-09-29 00:10 TPE；軍方首長指控 Eritrea、Sudan、Egypt 支援 TPLF，TPLF 週末奪取 Afar 的 Erebti，MSF 稱北部多所醫院傷患激增。https://www.washingtonpost.com/world/2026/09/28/ethiopia-tigray-war-eritrea-sudan-egypt/0ee0b578-bb57-11f1-81fc-9b76f8343b6c_story.html | **續報，前次 2026-09-27。** 前次只有軍方承諾克制並點名 Eritrea；本次新增 Sudan／Egypt 指控、Erebti 易手與 MSF 的傷患數字。Eritrea、Sudan 否認，Egypt 未於首輪報導回應，無獨立證據可證實國家支援。 |
| G7 South Korea 判定 DMZ 爆炸來自 North Korean mines | AP／Washington Post 於 2026-09-28 07:49 EDT 發布，即 2026-09-28 19:49 TPE；South Korea Joint Chiefs of Staff 與 UN Command 現場勘查後公布初步判定。https://www.washingtonpost.com/world/2026/09/28/south-korea-border-mines-injured/488eeb02-bb32-11f1-81fc-9b76f8343b6c_story.html | 窄搜 `North Korean mines|DMZ.*blasts|mines.*three officers` 無相同官方判定命中，首次收錄。爆炸發生於 9/21，當時只推測是地雷且未歸責；本次以窗內首次可靠公布的初步調查結果收錄。 |
| G8 France National Rally Senate 選舉突破 | Guardian／AFP 於 2026-09-27 21:31 EDT 發布，即 2026-09-28 09:31 TPE；RN 與盟友取得創紀錄 14 席，首次跨過 10 席門檻可組 Senate caucus。https://www.theguardian.com/world/2026/sep/28/french-election-2026-far-right-senate-elections | 窄搜 `National Rally.*Senate|Senate.*National Rally.*14` 無相同選舉結果命中，首次收錄。Guardian 早期標題日期顯示 9/28，但原頁精確時間為 9/27 21:31 EDT，仍落在 TPE 24 小時窗。 |
| G9 Hurricane Polo 逼近 Baja California Sur | AP／Washington Post 於 2026-09-28 03:21 EDT 發布，即 2026-09-28 15:21 TPE；Polo 當時為 Category 3，預計帶來 storm surge、強風、豪雨、致命洪水與土石流，Puerto San Carlos 約 90% 區域被評估易淹。https://www.washingtonpost.com/world/2026/09/28/hurricane-polo-nolo-mexico-hawaii-baja-california/42c1287c-bb0d-11f1-81fc-9b76f8343b6c_story.html | **續報，前次 2026-09-23。** 前次是 Polo 升 Category 5 並沿墨西哥西南外海移動；本次新增是風暴逼近 Baja、撤離／加固與明確登陸洪水風險，屬災害進入受影響地區應變的新階段。 |
| G10 Germany 外長到訪 ICC | AP／Washington Post 於 2026-09-28 12:42 EDT 發布，即 2026-09-29 00:42 TPE；Johann Wadephul 到 The Hague 會見 ICC，德國官方同日聲明支持 ICC 屬歷史責任。https://www.washingtonpost.com/world/2026/09/28/icc-court-sanctions-europe-germany/a749d5b6-bb5b-11f1-81fc-9b76f8343b6c_story.html ; https://www.auswaertiges-amt.de/en/newsroom/news/2804132-2804132 | 窄搜 `Wadephul.*ICC|Germany.*ICC.*support` 無同一訪問命中；9/27 收錄的是 Wadephul 與 Lavrov 會談，事件不同，首次收錄。美方已制裁 13 名 ICC 人員，是否擴大到整個法院仍未確定。 |

## 未入選候選與原因

- South Korea 要求 Ukraine 就公開北韓戰俘移交道歉：事件新且窗內，但相較 DMZ 地雷初步調查對即時邊境安全的影響較低，列備選不占 Top 10。
- France 學生抗議與總統大選口水戰：有新政治衝突，但缺少如 Senate 選舉結果般可驗證的制度節點，未列入。
- Colombia 法院缺席判決 ELN 指揮官、英吉利海峽踩踏死亡與 Pope Leo 法國行程：均有新聞價值，但在十則限額下，優先保留跨境衝突、重大災害、公共衛生與制度性選舉／法院議題。
- Ukraine 傷亡數在 AP 不同時間快照由 3 死／41 傷、7 死／50 餘傷上修至 7 死／80 餘傷；日報採窗內較晚且具體列出 Dnipro、Kharkiv、Zaporizhzhia 等地的版本，並標示數字可能續調。

## 發布紀錄

- 日報與來源筆記已完成；固定 renderer 產生 `slides-2026-09-29.html`，版本 `20260929-081327-reader`。GitHub Pages、LINE watchdog 與最終 pipeline check 待發布階段補記。
