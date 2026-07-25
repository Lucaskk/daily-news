---
title: "Source Notes - Daily Global and Tech AI News - 2026-07-25"
type: source-notes
created: 2026-07-25
updated: 2026-07-25
status: published
tags: [daily-news, source-notes, provenance]
research_cutoff: "2026-07-25 08:01:44 Asia/Taipei"
window: "2026-07-24 08:01:44 至 2026-07-25 08:01:44 Asia/Taipei"
utc_window: "2026-07-24T00:01:44Z 至 2026-07-25T00:01:44Z"
---

# Source Notes - 2026-07-25

研究截點｜2026-07-25 08:01:44（Asia/Taipei）  
24 小時窗口｜2026-07-24 08:01:44 至 2026-07-25 08:01:44（Asia/Taipei）  
UTC 窗口｜2026-07-24T00:01:44Z 至 2026-07-25T00:01:44Z  
主報告｜[daily-news-2026-07-25.md](daily-news-2026-07-25.md)  
投影片｜[slides-2026-07-25.html](slides-2026-07-25.html)

## Production Rule Checks

- 已在本輪開始前閱讀 `wiki/daily/README.md`，套用 24 小時窗口、Top 10 global news、科技／AI 分區、續報標示、完整來源 URL、簡報展開卡與發布驗證規則。
- 「最新」只取事件發生、官方產品釋出或首次可靠發布落在窗口內的項目；不把舊事件的文章更新、改標、轉載或仍在熱門欄視為新事件。
- 已搜尋 `wiki/daily/` 下既有 daily reports 與 source notes，排除已收錄且無重大新增的題材；續報只在有材料新進展時保留。
- 全球新聞保留 exactly 10 items；科技／AI 產品與平台新聞另列 10 items。
- 所有時間以來源 JSON-LD `datePublished`、可見 first-published time 或官方 release date 為主；僅有日期級官方公告時，以同日主要科技媒體精確發佈時間補足時間基準。

## Prior Archive Duplicate Scan

本輪在 `wiki/daily/` 中用關鍵字搜尋既有收錄，包括 `Iran`, `Hormuz`, `Hodeida`, `merchant vessel`, `Houthis`, `wildfire`, `Cap Ferret`, `Spain`, `Canada`, `Ukraine`, `Patriot`, `West Bank`, `ICC`, `Karim Khan`, `Volker Türk`, `tariffs`, `EU trade`, `UNESCO`, `Opus 5`, `Marketplace`, `Midjourney`, `Co-Star`, `Attie`, `Bitchat`, `World`, `Cognition`, `Poke`, `Anduril`, `Prentis`, `open-weight`。

### Duplicate / Out-of-Window / Lower-Priority Exclusions

- Gaza famine ended / IPC update：AP original `datePublished=2026-07-23T12:03:15Z`，即 2026-07-23 20:03:15（Asia/Taipei），早於本輪窗口起點；雖有 24 小時內轉載與更新，按規則排除。
- OpenAI ChatGPT desktop voice / GPT-Live-1：TechCrunch 2026-07-24 06:36 PDT 文章落在本輪窗口，但事件已於 2026-07-24 報告 T2 以 OpenAI release notes / 9to5Mac 收錄，今日無材料新進展，排除。
- Jack Dorsey Buzz、Light Flip、Suno 55M breach：TechCrunch 原始發布日期多為 2026-07-21，雖在 2026-07-24 TechCrunch most-popular modules 仍出現，均不視為本輪新事件。
- Canada Mark Carney tariff response：AP `datePublished=2026-07-23T22:06:11Z`，早於本輪 UTC 窗口；關稅主線今日只保留 2026-07-24 發布的多國反彈與 EU tech fines investigation。
- Poland PiS split：Guardian 2026-07-24 14:50 BST，符合窗口且重要，但本輪全球 Top 10 在 Europe 已有 wildfires 並保留更高跨區衝擊的 Canada wildfires、UNESCO / ICC / UN governance；列候補。
- Thomson Reuters / ICE data deal：Guardian 2026-07-24 23:53 AEST，符合窗口；資料監控與移民執法重要，但相較本輪戰爭、火災、UN / ICC and trade items，排入候補。
- India Cockroach hunger strike：屬已多次追蹤的 India protest 主線，今日報導較偏續報；未高於已選全球焦點。
- OpenAI shopping research：OpenAI 官方頁實際日期為 2025-11-24，搜尋結果「today」是 crawl artifact，排除。
- OpenAI GPT-5.6 / ChatGPT Work / OpenAI Presence official pages：發布日期分別是 2026-07-09 或 2026-07-22，均非本輪新發布；已在 prior reports 中收錄或排除。

## Selected Global News Items

| # | Item | Event / Publication-Time Basis | Prior Capture Check |
|---|---|---|---|
| 1 | U.S.-Iran / Hormuz merchant vessel and Hodeida escalation | AP `datePublished=2026-07-24T04:39:16Z` | 續報；前次收錄 2026-07-24 U.S.-Iran 第 13 夜 / Houthis tanker attack / Brent and pipeline risk。今日新增 M/T Lavine、Saudi Hodeida strikes、Gulf base claims and stranded mariners。 |
| 2 | France / Spain wildfires >200,000 evacuations | AP `datePublished=2026-07-24T07:34:07Z`; Guardian first published 2026-07-24 09:54 BST | 續報；前次收錄 2026-07-24 Saumos wildfire。今日新增 Cap Ferret / Spain merged fires / national wildfire emergency and much larger evacuation scale。 |
| 3 | Russian ballistic strike kills 10 in Ukraine after Patriot meeting | AP `datePublished=2026-07-24T09:33:31Z` | Fresh battlefield event; not a repeat of prior Ukraine command / diplomacy items。 |
| 4 | Israeli military kills 4 Palestinians in West Bank | AP `datePublished=2026-07-24T07:08:29Z`; Guardian first published 2026-07-24 19:23 AEST | Fresh West Bank violence event; prior archive has broader West Bank sanctions / settlement items but not this Tell incident。 |
| 5 | Forced-labor tariff backlash | AP `datePublished=2026-07-24T07:03:22Z`; Guardian business live 2026-07-24 | 續報；前次 2026-07-24 captured tariff announcement。今日新增 trading-partner reactions, legal criticisms and export-market shifts。 |
| 6 | ICC removes Karim Khan | AP `datePublished=2026-07-24T11:07:01Z`; Guardian same-day report | Fresh institutional outcome; prior archive had ICC pressure but not removal vote。 |
| 7 | Volker Türk reappointed UN human-rights chief | AP `datePublished=2026-07-24T18:21:16Z` | Fresh UN General Assembly vote; not previously captured。 |
| 8 | Trump launches EU trade-practices investigation over tech fines | AP `datePublished=2026-07-24T17:31:34Z` | 續報；前次 2026-07-24 T8 captured EU Google fine。今日新增 U.S. formal trade-investigation threat。 |
| 9 | UNESCO / UN committee adds West Bank and Lebanon sites | AP `datePublished=2026-07-24T09:38:36Z` | Fresh heritage / diplomacy event; not previously captured。 |
| 10 | Western Canada lightning-triggered wildfires | Guardian / Reuters first published 2026-07-24 18:58 BST (`2026-07-24T17:58:00Z`) | Fresh Canada fire escalation; distinct from prior North America smoke or Europe wildfire items。 |

## Selected Technology / AI Product and Platform Items

| ID | Item | Event / Publication-Time Basis | Prior Capture Check |
|---|---|---|---|
| T1 | Anthropic Claude Opus 5 | Anthropic official date `Jul 24, 2026`; TechCrunch `datePublished=2026-07-24T17:00:00Z` | Fresh official model release; no prior Opus 5 capture。 |
| T2 | Facebook Marketplace seller app | TechCrunch `datePublished=2026-07-24T12:47:15Z`; IBD same-day product-market summary | Fresh Meta commerce product update。 |
| T3 | Midjourney acquires Co-Star | TechCrunch `datePublished=2026-07-24T15:09:55Z`, citing Bloomberg | Fresh AI consumer-app acquisition。 |
| T4 | Bluesky Attie Quests | TechCrunch `datePublished=2026-07-24T15:13:57Z` | Fresh AI assistant feature expansion; not prior Buzz / social AI item。 |
| T5 | World US$52.5M token sale | TechCrunch `datePublished=2026-07-24T16:11:56Z` | Fresh financing / proof-of-human infrastructure signal。 |
| T6 | India / Bitchat GitHub notice | TechCrunch `datePublished=2026-07-24T16:54:58Z` | Fresh open-source product availability / legal event; Buzz from 2026-07-21 excluded。 |
| T7 | Cognition acquires Poke | TechCrunch `datePublished=2026-07-24T18:07:32Z` | Fresh AI assistant acquisition and agent-personality strategy。 |
| T8 | Anduril US$100B valuation talks | TechCrunch `datePublished=2026-07-24T17:33:19Z`, citing Reuters | Fresh defense-AI financing signal; not a product release but platform / autonomous defense market news。 |
| T9 | Prentis computer-use AI lab | TechCrunch `datePublished=2026-07-24T22:25:58Z` | Fresh AI lab / enterprise workflow-agent financing talks。 |
| T10 | Open-weight restrictions debate | TechCrunch `datePublished=2026-07-24T15:51:49Z` | Fresh AI policy / model-distribution ecosystem item; linked to prior OpenAI / Hugging Face breach but today's item is a new industry letter / policy push。 |

## Continuations Kept

- 2026-07-24 -> 2026-07-25: U.S.-Iran / Hormuz moved from 13th-night strikes and Houthi tanker attacks to U.S. disabling another merchant vessel, Saudi Hodeida strikes, Gulf base claims and stranded mariners.
- 2026-07-24 -> 2026-07-25: France Saumos wildfire escalated into France / Spain >200,000 evacuation / lockdown scale and Spain national wildfire emergency.
- 2026-07-24 -> 2026-07-25: Trump forced-labor tariff announcement moved into formal backlash from trading partners and legal-policy critique.
- 2026-07-24 -> 2026-07-25: EU Google fine moved into a U.S. trade-practices investigation threat.

## Source Links

### Global

- AP - US military fires on merchant vessel trying to breach blockade of Iranian ports — https://apnews.com/article/iran-us-hormuz-strait-war-24-july-2026-78c2dbf538f6e61ab816479a4d9bdd85
- The Guardian - US expands Iran attacks as Trump warns Tehran and Houthis over Red Sea strikes — https://www.theguardian.com/world/2026/jul/24/us-expands-iran-attacks-as-trump-warns-tehran-and-houthis-over-red-sea-strikes
- AP - Wildfires in southwestern France and near Madrid force over 200,000 to evacuate — https://apnews.com/article/54c3d375fa1cca8399ea2645a8e119b0
- The Guardian - More than 200,000 people flee or lock down as wildfires sweep France and Spain — https://www.theguardian.com/world/2026/jul/24/france-evacuation-cap-ferret-peninsula-wildfire
- AP - Russian ballistic strike kills 10 in Ukraine after Zelenskyy hosts Patriot missile systems meeting — https://apnews.com/article/russiak-ukraine-war-patriots-trump-loomer-raytheon-a2f06208baa0759215d973f01758e30f
- AP - Israeli military kills 4 Palestinians after settler killed in West Bank — https://apnews.com/article/israel-palestinians-west-bank-violence-settlers-c9394defe87c7529655d9b23cab58cdc
- The Guardian - Israel planning extensive military operation in West Bank after settler attack — https://www.theguardian.com/world/2026/jul/24/palestinians-israeli-killed-west-bank-shooting
- AP - New US tariffs linked to foreign forced labor claims anger trading partners — https://apnews.com/article/us-tariffs-trump-labor-reaction-china-asia-b178ead12f022009817c60010ac07eb3
- The Guardian - Business live: European stocks rise as oil falls back below $100; tariffs — https://www.theguardian.com/business/live/2026/jul/24/asian-stocks-slide-trump-countries-trade-tariffs-latest-economy-news
- AP - ICC chief prosecutor removed over sexual misconduct allegations — https://apnews.com/article/icc-court-prosecutor-karim-khan-united-nations-5a9490e98b74f3bf13f5eae26fb3c3d7
- The Guardian - Karim Khan ousted from role as prosecutor of international criminal court — https://www.theguardian.com/law/2026/jul/24/karim-khan-ousted-from-role-as-prosecutor-of-international-criminal-court
- AP - UN human rights chief wins reappointment — https://apnews.com/article/turk-human-rights-chief-united-nations-61dc91622d141da0aba689e6436ea47c
- AP - Trump says US will investigate EU trade practices — https://apnews.com/article/trump-eu-trade-tech-fine-google-2e125ac0d3c1ac7a96c9194a372ba47e
- AP - UN committee adds West Bank site and Lebanese castles to World Heritage list — https://apnews.com/article/12c558a4b6aa03fa40ad33ffb6e54b89
- The Guardian / Reuters - Thousands of lightning strikes trigger fresh wildfires in western Canada — https://www.theguardian.com/world/2026/jul/24/thousands-of-lightning-strikes-trigger-fresh-wildfires-in-western-canada

### Technology / AI

- Anthropic - Introducing Claude Opus 5 — https://www.anthropic.com/news/claude-opus-5
- TechCrunch - Anthropic launches Opus 5 — https://techcrunch.com/2026/07/24/anthropic-launches-opus-5/
- TechCrunch - Facebook launches a dedicated Marketplace app for sellers, adds a free verification system — https://techcrunch.com/2026/07/24/facebook-launches-a-dedicated-marketplace-app-for-sellers-adds-a-free-verification-system/
- Investor's Business Daily - Meta Launches Seller App To Boost Facebook Marketplace — https://www.investors.com/news/technology/meta-stock-ebay-stock-facebook-marketplace-seller-app/
- TechCrunch - Midjourney acquired the astrology app Co-Star — https://techcrunch.com/2026/07/24/midjourney-acquired-the-astrology-app-co-star/
- TechCrunch - Bluesky's AI assistant Attie expands into an open social research tool — https://techcrunch.com/2026/07/24/blueskys-ai-assistant-attie-expands-into-an-open-social-research-tool/
- TechCrunch - Sam Altman's biometric startup World raises $52.5M via crypto sale — https://techcrunch.com/2026/07/24/sam-altmans-biometric-startup-world-raises-52-5-million-via-crypto-sale/
- TechCrunch - India's move against Jack Dorsey's Bitchat sparks legal debate — https://techcrunch.com/2026/07/24/indias-move-against-jack-dorseys-bitchat-sparks-legal-debate/
- TechCrunch - Why Cognition bought Poke: AI personality is becoming a competitive advantage — https://techcrunch.com/2026/07/24/why-cognition-bought-poke-ai-personality-is-becoming-a-competitive-advantage/
- TechCrunch - Anduril reportedly in talks to raise funding at $100B valuation — https://techcrunch.com/2026/07/24/anduril-reportedly-in-talks-to-raise-funding-at-100b-valuation-more-than-3x-last-years-mark/
- TechCrunch - Prentis, new AI lab co-founded by Reid Hoffman, Mark Pincus in talks to raise $100M — https://techcrunch.com/2026/07/24/prentis-new-ai-lab-co-founded-by-reid-hoffman-marc-pincus-in-talks-to-raise-100m/
- TechCrunch - As US weighs response to Chinese AI, industry urges against broad open-weight restrictions — https://techcrunch.com/2026/07/24/as-us-weighs-response-to-chinese-ai-industry-urges-against-broad-open-weight-restrictions/

## Reliability Notes

- AP, Guardian / Reuters, official Anthropic pages and TechCrunch were used as primary source classes. AP and official product pages were preferred where available.
- AP pages were checked for JSON-LD `datePublished` via direct metadata extraction where the browser view rendered generic timestamp placeholders.
- Guardian visible first-published times were converted manually to UTC / Asia/Taipei when JSON-LD was not required for selection.
- Market / funding items from TechCrunch that cite Reuters or unnamed sources are treated as reported talks, not confirmed transactions.
- EU / U.S. trade and tariff items preserve source framing differences: EU competition enforcement vs Trump trade-abuse framing; affected country / economy counts vary by outlet and should not be collapsed.
- Bitchat item is explicitly conditional because GitHub did not confirm receiving the notice and repos remained available at publication time.

## Follow-Up Watchlist

- U.S.-Iran / Hormuz: M/T Lavine crew status, Hodeida damage assessment, Gulf base damage confirmation, trapped mariner relief and Oman / Pakistan mediation.
- Europe and Canada wildfires: evacuation orders, burned area, injury / fatality updates, EU / Mexico / cross-border firefighting support and smoke forecasts.
- Ukraine: final casualty count, investigation into defense-event security and further Patriot / Raytheon cooperation.
- West Bank: Israeli military investigation, settler attacks, Palestinian casualty verification and whether Nablus lockdown expands.
- Tariffs and EU tech fines: legal challenges, retaliatory measures, Section 301 scope and U.S. trade investigation timeline.
- ICC / OHCHR: Karim Khan legal challenge, interim prosecutor arrangements, Türk's funding / cooperation constraints.
- Anthropic Opus 5: third-party benchmarks, API availability across AWS / Google Cloud / Microsoft Foundry, refusal and fallback behavior.
- Meta Marketplace seller app: rollout geography, AI listing accuracy, fraud / verification effects and eBay competitive response.
- Midjourney / Co-Star, Bluesky Attie and Cognition / Poke: product integration roadmaps, privacy handling and paid-tier plans.
- India / Bitchat: GitHub transparency-log entry, Indian government confirmation or denial and any court challenge.
- World, Prentis, Anduril and open-weight restrictions: financing close, investor terms, policy drafts and signatory / opposition updates.
