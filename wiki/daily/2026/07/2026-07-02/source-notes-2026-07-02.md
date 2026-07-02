---
title: "2026-07-02 每日新聞來源筆記"
type: source-notes
date: 2026-07-02
created: 2026-07-02
updated: 2026-07-02
status: published
tags: [daily-news, sources, provenance, deduplication]
---

# 2026-07-02 每日新聞來源筆記

## 研究截點與 24 小時視窗

- **Asia/Taipei 研究截點：** 2026-07-02 08:01:50（Asia/Taipei）
- **合格視窗：** 2026-07-01 08:01:50 至 2026-07-02 08:01:50（Asia/Taipei）
- **UTC 視窗：** 2026-07-01T00:01:50Z 至 2026-07-02T00:01:50Z
- **規則檔：** 已先讀取 `wiki/daily/README.md`，依其 24 小時、跨日去重、重大續報、簡報來源與發布驗證規則產製。

## 去重搜尋範圍

已搜尋 `wiki/daily/` 下所有既有 `daily-news-*.md` 與 `source-notes-*.md`。本次特別比對下列主線：

- **2026-07-01 已收錄：** U.S. Supreme Court birthright / campaign spending / transgender athlete rulings；U.S.-Iran Qatar talks over $6bn assets and Hormuz；Monaco explosion target context；UK defense investment；Spain immigration regularization；Lahore tutoring collapse；South Africa anti-migrant protests；Nigeria school raid；Ghana / Ivory Coast floods；Claude Sonnet 5 / Claude Science；Google Nano Banana 2 Lite / Gemini Omni Flash；Amazon FDE；X MCP server；Proton Lumo 2.0；Etched；OpenClaw；Acti。
- **Russia / Ukraine prior line：** 2026-06-13 Crimea fuel crisis；2026-06-26 Ufa refineries / Moscow defense；2026-06-27 660-drone wave；2026-06-29 Ukraine strikes Russian refineries and Putin fuel-shortage admission；2026-06-30 Russia strikes Ukraine。
- **Technology prior lines：** 2026-06-17 GitHub Models 停止新客戶；2026-06-10 Anthropic Fable 5 / Mythos 5 launch；2026-06-14 global export-control suspension；2026-06-15 Canada policy response；2026-05-31 Gemini Spark initial agentic direction；2026-06-04 Cloudflare Workers / Agents SDK。

本日採用標準：同一主線必須有本視窗內的新官方程序、重大統計、跨境攻擊、平台可用性、退場時程或資本／供應鏈節點。單純重述、舊事件更新、仍在首頁熱門、或只有評論分析者排除。

## 全球 Top 10 來源與時間依據

| # | 入選項目 | 事件／發佈時間依據 | 去重與續報判斷 | 主要來源 |
|---|---|---|---|---|
| 1 | 續報｜U.S.-Iran Qatar 會談取得正面進展 | AP metadata `datePublished=2026-07-01T08:19:31Z`，即 2026-07-01 16:19:31（Asia/Taipei）；Qatar 表示 Wednesday separate talks made positive progress and parties agreed to continue. | **續報，前次 2026-07-01。** 前次收錄 $6bn assets / Hormuz 條件與間接會談；本次新增實際 separate meetings、Qatar positive progress 與同意續談。 | https://apnews.com/article/iran-us-war-strait-of-hormuz-july-1-2026-de0729197bc7b9d3ee9e543d94c18fbe |
| 2 | 續報｜Ukraine drones 造成 Russia summer fuel crisis | AP metadata `datePublished=2026-07-01T04:01:51Z`，即 2026-07-01 12:01:51（Asia/Taipei）；Ufa support article `2026-07-01T11:56:02Z`。 | **續報，前次 2026-06-29。** 前次收錄 refinery attack and Putin fuel-shortage admission；本次新增 AP quantified output collapse and offline refining capacity。 | https://apnews.com/article/russia-ukraine-war-fuel-crisis-gas-ec7e67f94ead8bf3ba064c785c2a8871；https://apnews.com/article/russia-ukraine-war-ufa-refinery-oil-8f85eea709f58365c42ec3b29e5d1d6d |
| 3 | AP 重建 Iran Minab 小學空襲 | AP metadata `datePublished=2026-07-01T04:01:22Z`，即 2026-07-01 12:01:22（Asia/Taipei）；事件本身為 2026-02-28，但本窗內首次可靠發布完整重建。 | 既有 daily 未見 Minab / Airwars / school strike capture；依規則「first reliably published」收錄，並在報告中明示不是新發生事件。 | https://apnews.com/article/iran-school-strike-baluch-trump-2a134a5c74d80db763db4c3eb6d0d847 |
| 4 | Trump 拒絕在 July 1 deadline 續簽 USMCA | Guardian metadata `datePublished=2026-07-01T20:09:01Z`，即 2026-07-02 04:09:01（Asia/Taipei）；July 1 deadline decision. | 2026-05-29 / 2026-06-14 曾有 USMCA 背景與準備，但未收錄 July 1 不續約決定；屬新制度節點。 | https://www.theguardian.com/us-news/2026/jul/01/trump-usmca-trade-treaty |
| 5 | Trump crypto financial disclosure | AP metadata `datePublished=2026-07-01T20:01:49Z`，即 2026-07-02 04:01:49（Asia/Taipei）；disclosure-based first reliable publication. | 未見既有 daily report 捕獲此 financial disclosure / crypto income estimate；屬新披露文件事件。 | https://apnews.com/article/trump-finances-real-estate-crypto-bibles-golf-8b8b54fae333d1200f4c1b509991b544 |
| 6 | 續報｜Afghanistan / Pakistan drones and airstrikes | Al Jazeera metadata `datePublished=2026-07-01T07:55:16Z`，即 2026-07-01 15:55:16（Asia/Taipei）；Xinhua timestamp 2026-07-01 14:09:15 local page time supports same-day publication. | **續報，前次 2026-06-30。** 前次收錄 Pakistan-Afghanistan civilian casualty claims；本次新增 cross-border drones and Afghan airstrike claims against ISIL centres. | https://www.aljazeera.com/news/2026/7/1/pakistan-says-it-intercepted-four-drones-fired-from-afghanistan?traffic_source=rss；https://english.news.cn/20260701/a36531a65e0c4a14a84ca973ad78f961/c.html |
| 7 | SSPX 祝聖四名主教 | AP metadata `datePublished=2026-07-01T04:02:03Z`，即 2026-07-01 12:02:03（Asia/Taipei）；Guardian backup `datePublished=2026-07-01T14:27:27Z`。 | 未見既有 daily report 捕獲 SSPX / Econe consecrations；屬宗教治理與教會法新事件。 | https://apnews.com/article/975a7dd408e151310f5e515030cd6c97；https://www.theguardian.com/world/2026/jul/01/fears-catholic-schism-sect-ordains-ultra-conservative-bishops-pope-leo |
| 8 | 全球海洋 hottest June | Al Jazeera metadata `datePublished=2026-07-01T04:38:43Z`，即 2026-07-01 12:38:43（Asia/Taipei）；引述 EU climate monitors / Copernicus 2026 first-half ocean warmth. | 既有 heatwave 主線多次收錄 Europe / France / UK；本次是 global oceans June record，指標不同且為本窗內新可靠發布。 | https://www.aljazeera.com/news/2026/7/1/worlds-oceans-experience-hottest-june-ever-scientists-say-more-heat-ahead |
| 9 | Romania storm after heatwave | AP metadata `datePublished=2026-07-01T11:43:55Z`，即 2026-07-01 19:43:55（Asia/Taipei）；event after heatwave and storms. | 未見既有 daily report 捕獲 Romania storm casualty / flooding；與一般 Europe heatwave 主線不同，屬新災害事件。 | https://apnews.com/article/storm-weather-europe-heatwave-romania-5081a17e7ba75c5c84bd183c800956c3 |
| 10 | Qatar 贈送 Air Force One 首航 | AP metadata `datePublished=2026-07-01T13:25:17Z`，即 2026-07-01 21:25:17（Asia/Taipei）；first flight to North Dakota. | 未見既有 daily report 捕獲 Qatar gifted jet first presidential flight；此前展示或討論不等於首航，故以 first use 作新事件。 | https://apnews.com/article/trump-air-force-one-plane-qatar-8eb5da68e95d583b14811f85e62cbcd1 |

## 科技／AI 產品與平台來源

| # | 入選項目 | 事件／發佈時間依據 | 去重與選題判斷 | 主要來源 |
|---|---|---|---|---|
| T1 | Cloudflare Content Independence Day | TechCrunch metadata `datePublished=2026-07-01T17:48:37Z`，即 2026-07-02 01:48:37（Asia/Taipei）；Cloudflare official blog dated July 01, 2026. | 2026-06-04 曾收錄 Cloudflare Workers / Agents SDK；本次是 AI crawler access / compensation policy and monetization gateway，事件不同。 | https://techcrunch.com/2026/07/01/cloudflares-new-policy-pushes-ai-companies-to-pay-for-publishers-content/；https://blog.cloudflare.com/content-independence-day-ai-options/；https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/ |
| T2 | 續報｜Anthropic redeploys Fable 5 / Mythos 5 | Anthropic official page updated Jul 1, 2026；官方未曝精確時間，報告以 2026-07-01 12:00:00（Asia/Taipei）作日期錨定。 | **續報，前次 2026-06-14。** 前次收錄 export-control suspension；本次新增 access restored / redeployment across products and cloud partners. | https://www.anthropic.com/news/redeploying-fable-5；https://www.anthropic.com/news/claude-fable-5-mythos-5 |
| T3 | 續報｜Google Gemini Spark macOS / local files / MCP | TechCrunch metadata `datePublished=2026-07-01T14:20:19Z`，即 2026-07-01 22:20:19（Asia/Taipei）；Google official product update supports details. | **續報，前次 2026-05-31。** 前次收錄 Gemini Spark 初始 agentic direction；本次新增 Mac availability, local files, custom MCP and app integrations. | https://techcrunch.com/2026/07/01/gemini-spark-googles-agentic-assistant-is-now-available-on-mac/；https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-june-2026/ |
| T4 | GitHub Copilot vision GA | GitHub official changelog Release July 1, 2026；官方未曝精確時間，報告以 2026-07-01 12:00:00（Asia/Taipei）作日期錨定。 | 未見既有 daily report 捕獲 Copilot vision GA；屬 Copilot Chat multimodal availability change. | https://github.blog/changelog/2026-07-01-copilot-vision-is-generally-available/ |
| T5 | GitHub Copilot adds Kimi K2.7 Code | GitHub official changelog Release July 1, 2026；官方未曝精確時間，報告以 2026-07-01 12:00:00（Asia/Taipei）作日期錨定。 | 未見既有 daily report 捕獲 Kimi K2.7 in Copilot；屬 model picker / open-weight model availability. | https://github.blog/changelog/2026-07-01-kimi-k2-7-is-now-available-in-github-copilot/ |
| T6 | 續報｜GitHub Models full retirement | GitHub official changelog dated July 1, 2026；官方未曝精確時間，報告以 2026-07-01 12:00:00（Asia/Taipei）作日期錨定。 | **續報，前次 2026-06-17。** 前次收錄 no new customers；本次新增 July 30 shutdown and July 16 / 23 brownouts. | https://github.blog/changelog/2026-07-01-github-models-is-being-fully-retired-on-july-30-2026/ |
| T7 | GitHub Copilot governance controls | GitHub official changelog entries dated July 1, 2026；官方未曝精確時間，報告以 2026-07-01 12:00:00（Asia/Taipei）作日期錨定。 | 與 T4/T5/T6 不同，重點是 enterprise governance / cost controls，而非 model availability or retirement. | https://github.blog/changelog/2026-07-01-set-ai-credit-session-limits-in-copilot-cli-and-sdk/；https://github.blog/changelog/2026-07-01-enterprise-managed-settings-json-is-generally-available/；https://github.blog/changelog/2026-07-01-enterprises-can-default-to-auto-model-selection |
| T8 | Together AI Series C | TechCrunch metadata `datePublished=2026-07-01T18:29:14Z`，即 2026-07-02 02:29:14（Asia/Taipei）；HPCwire / AIwire same-day announcement. | 未見既有 daily report 捕獲 Together AI $800M round；屬 AI infrastructure capital milestone. | https://techcrunch.com/2026/07/01/neocloud-together-ai-raises-800m-leaps-to-8-3b-valuation/；https://www.hpcwire.com/aiwire/2026/07/01/together-ai-raises-800m-at-8-3b-valuation-to-make-frontier-ai-accessible-to-all/ |
| T9 | Venice AI Series A | TechCrunch metadata `datePublished=2026-07-01T14:25:23Z`，即 2026-07-01 22:25:23（Asia/Taipei）。 | 未見既有 daily report 捕獲 Venice AI Series A / unicorn；屬 privacy-first AI platform capital and product growth item. | https://techcrunch.com/2026/07/01/venice-ai-becomes-a-unicorn-with-65m-series-a-as-its-privacy-first-ai-platform-takes-off/ |
| T10 | NVIDIA Build in America | NVIDIA official blog dated July 1, 2026；官方未曝精確時間，報告以 2026-07-01 12:00:00（Asia/Taipei）作日期錨定。 | 未見既有 daily report 捕獲 NVIDIA July 1 U.S. build / Blackwell / supercomputer manufacturing package；屬 AI infrastructure supply-chain announcement. | https://blogs.nvidia.com/blog/nvidia-and-partners-build-in-america-for-america/ |

## 續報清單

- **2026-07-01 → 2026-07-02：U.S.-Iran / Qatar talks。** 前次收錄 talks over $6bn assets and Hormuz implementation；本次新增 separate meetings、Qatar positive progress and agreement to continue discussions。
- **2026-06-29 → 2026-07-02：Russia fuel crisis from Ukraine refinery strikes。** 前次收錄 Ukraine refinery strike and Putin fuel-shortage admission；本次新增 AP quantified crude processing / gasoline output collapse and offline refining capacity estimate。
- **2026-06-30 → 2026-07-02：Afghanistan / Pakistan border conflict。** 前次收錄 civilian casualty claims；本次新增 Pakistan intercepted drones claim and Afghanistan airstrikes against ISIL centres claim。
- **2026-06-14 → 2026-07-02：Anthropic Fable 5 / Mythos 5。** 前次收錄 export-control shutdown；本次新增 official redeployment after controls lifted。
- **2026-05-31 → 2026-07-02：Gemini Spark。** 前次收錄 initial agentic assistant direction；本次新增 Mac app, local file actions, custom MCP and third-party app integrations。
- **2026-06-17 → 2026-07-02：GitHub Models。** 前次收錄 stopped accepting new customers；本次新增 July 30 full retirement and July 16 / 23 brownouts。

## 排除與降級候選

- **U.S. Supreme Court July 1 cases：** 2026-07-01 已收錄 birthright citizenship、campaign spending 與 transgender athlete rulings；今日不以延伸評論重列。
- **Cloudflare Workers / Agents SDK main line：** 2026-06-04 已收錄 Cloudflare agent infrastructure；今日僅保留 AI crawler compensation / traffic controls，避免重複舊平台更新。
- **Russia Ufa refinery second strike：** 具本窗時間戳，但因 2026-06-26 / 2026-06-29 已有 Ufa / refinery 主線，僅作 #2 fuel crisis 支撐來源，不另列。
- **Gaza ceasefire drone strike casualties：** Al Jazeera 本窗有 fresh casualty item，但 Gaza daily casualty updates 近期多次收錄；本日優先全新 Minab investigation、USMCA、SSPX、Romania 與 climate/ocean record。
- **SpaceX AI phone prototype：** TechCrunch / WSJ report 在窗內，但 The Verge 同日報導 Elon Musk 否認；非官方產品發布且說法衝突，列排除。
- **Apple Hide My Email bug：** TechCrunch 本窗報導，但 bug 可能已存在一年以上且非產品發布；不放入科技／AI product section。
- **OpenAI GPT-5.6 Sol：** 官方日期為 2026-06-26，超出本次 24 小時窗，排除。
- **Google Nano Banana 2 Lite、Claude Sonnet 5、Claude Science、Amazon FDE、X MCP、Proton Lumo、Etched、OpenClaw、Acti：** 均已於 2026-07-01 收錄，不重列。

## 簡報與發布驗證記錄

- 全球新聞 Top 10：恰好 10 則。
- 科技／AI 產品與平台：10 則，另列於全球 Top 10 之外。
- 每則全球與科技項目均保留 Asia/Taipei 發佈時間與原始 UTC 或來源日期依據。
- 簡報 DOM 與閱讀順序中的全球 Top 10 應為 1、2、3、4、5、6、7、8、9、10。
- 每張投影片使用背景圖；每個 news/stat/tech card 使用 `<details>` 展開，展開內容底部各自包含 readable source label 與完整 URL。
