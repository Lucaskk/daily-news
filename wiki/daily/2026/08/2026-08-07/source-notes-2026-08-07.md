---
title: "Source Notes - Daily Global and Tech AI News - 2026-08-07"
date: 2026-08-07
type: source-notes
status: published
research_cutoff: "2026-08-07 08:02:03 Asia/Taipei"
window_taipei: "2026-08-06 08:02:03 至 2026-08-07 08:02:03 Asia/Taipei"
window_utc: "2026-08-06T00:02:03Z 至 2026-08-07T00:02:03Z"
tags: [daily-news, source-notes, provenance, deduplication]
---

# Source Notes - 2026-08-07

## Research Cutoff and Window

- Asia/Taipei 研究截點：**2026-08-07 08:02:03 Asia/Taipei**。
- 合格 24 小時窗口：**2026-08-06 08:02:03 至 2026-08-07 08:02:03 Asia/Taipei**。
- UTC 對照：**2026-08-06T00:02:03Z 至 2026-08-07T00:02:03Z**。
- 本次先讀取 `wiki/daily/README.md`，依其規則處理 24 小時窗口、跨日去重、重大續報、來源筆記與 HTML deck 驗證。
- 「Most discussed」採綜合判斷：AP / Guardian international prominence、major tech outlet coverage、official product / changelog release、company-scale materiality and credible aggregation from visible search results。未把單一社群熱度或文章更新時間當成入選依據。

## Cross-Day Deduplication

- 搜尋範圍：`wiki/daily/**/daily-news-*.md`、`wiki/daily/**/source-notes-*.md`、`wiki/daily/**/*.html`。
- 重點查詢詞包括：`Hormuz`, `Oman`, `Yemen`, `Lebanon`, `Ukraine`, `Patriot`, `Leipzig`, `Congo Ebola`, `Kinshasa`, `birthright citizenship`, `birth tourism`, `Uganda Gaza force`, `West Bank healthcare`, `Awdah Hathaleen`, `consulate closures`, `Sheikh Hasina`, `OpenAI GPT-5.6 Luna`, `Kimi K3`, `WeatherNext`, `Jony Ive`, `Pixel 11`, `Mirendil`, `Terafab`, `AI therapists`, `Naive`, `eBay live shopping`, `EA PIF`, `Google AI Studio`。
- 已捕捉但本次仍保留的續報：
  - Hormuz / Lebanon：前次 2026-08-06；今日新增 AP 2026-08-06 Mideast roundup 的 near-deal framing、Yemen flare-up and Lebanon deaths。
  - Ukraine / Patriot：前次 2026-08-06；今日新增 Ukraine strikes on Bashkortostan / Yaroslavl refineries, Black Sea boats / shadow fleet and urgent interceptor procurement。
  - Leipzig drone bomb：前次 2026-08-06；今日新增 The Guardian 報導 drone bomb near Ukrainian ammunition plane and German hybrid-attack attribution concern。
  - Congo Ebola：前次 2026-08-05；今日新增 AP quarantine near Kinshasa, cases over 4,000 / deaths over 1,800 and Guardian mutation concern / active case search。
  - Gaza disarmament / stabilization force：前次 2026-08-01 and 2026-08-03；今日新增 Uganda parliament approval for troop contribution。
- 保留的舊背景但非未標示重複：
  - Awdah Hathaleen killing occurred in 2025；本次入選基準是 2026-08-06 Israeli prosecutors' indictment, a new legal proceeding。
  - OpenAI GPT-5.6 price / Work / Codex education items were captured 2026-07-31 and 2026-08-05；本次入選基準是 Aug. 6 official ChatGPT Sol / Luna access update。
  - Kimi K3 was mentioned in 2026-07-20 subscription-pause context；本次入選基準是 GitHub Copilot GA / paused rollout incident on Aug. 6。

## Selected Global Items

| # | Item | Event / publication-time basis | Deduplication decision | Primary URLs |
|---|---|---|---|---|
| 1 | 續報｜Hormuz 協議接近定案，但 Yemen 大規模攻擊與 Lebanon 爆炸顯示中東仍多線升級 | AP JSON-LD `datePublished=2026-08-06T08:34:42Z` = 2026-08-06 16:34:42 Asia/Taipei；article modified 2026-08-06T23:31:02Z. | 續報；前次 2026-08-06 Hormuz draft pending approval and South Lebanon evacuation warning。今日新增 near-deal framing, Yemen flare-up and Lebanon deaths in same AP roundup。 | https://apnews.com/article/mideast-news-roundup-iran-lebanon-israel-aug-6-2026-07074f3374339a34bc539f56d7d6287a |
| 2 | 續報｜Ukraine 深入攻擊 Russia 煉油與 Black Sea 船隻，盟友仍急尋 Patriot 攔截彈 | AP JSON-LD `datePublished=2026-08-06T09:22:19Z` = 2026-08-06 17:22:19 Asia/Taipei；modified 2026-08-06T18:30:51Z. | 續報；前次 2026-08-06 Russia Kyiv barrage / 17 deaths / Patriot failure。今日新增 Ukrainian strikes on Bashkortostan and Yaroslavl refineries, patrol boats / shadow fleet and NATO / partner interceptor search。 | https://apnews.com/article/russia-ukraine-war-ballistic-missiles-patriots-drones-30447169b0145caa2e48ebf22b235c7a |
| 3 | 續報｜Leipzig 爆裂物無人機據稱接近載彈 Ukraine 飛機，德方把事件升高為混合攻擊疑慮 | Guardian metadata `datePublished=2026-08-06T15:06:28Z` = 2026-08-06 23:06:28 Asia/Taipei；modified 2026-08-06T20:21:02Z. | 續報；前次 2026-08-06 captured explosive drone found at Leipzig airport。今日新增 proximity to Ukrainian ammunition plane and German hybrid-attack attribution concern。 | https://www.theguardian.com/world/2026/aug/06/leipzig-drone-bomb-found-near-ukrainian-plane-carrying-ammunition |
| 4 | 續報｜Congo Ebola 確診突破 4,000，Kinshasa 附近船客隔離且 Africa CDC 憂病毒變異 | AP `datePublished=2026-08-06T08:57:26Z` = 2026-08-06 16:57:26 Asia/Taipei；Guardian `datePublished=2026-08-06T16:18:46Z` = 2026-08-07 00:18:46 Asia/Taipei. | 續報；前次 2026-08-05 captured 3,802 cases / 1,707 deaths。今日新增 near-Kinshasa quarantine, cases over 4,000, deaths over 1,800, mutation concern and active case-search plans。 | https://apnews.com/article/congo-ebola-outbreak-ituri-protest-health-workers-1de45c3ecedabb974dce0b176f0dcc3f ; https://www.theguardian.com/world/2026/aug/06/ebola-virus-drc-mutating |
| 5 | Trump 再簽出生公民權與 birth tourism 行政命令，正面挑戰 Supreme Court 近期判決 | AP JSON-LD `datePublished=2026-08-06T21:10:05Z` = 2026-08-07 05:10:05 Asia/Taipei；White House fact sheet dated 2026-08-06. | New executive-action event inside window. Prior birthright-citizenship court cases were background; this is a new pair of executive orders after the Supreme Court ruling。 | https://apnews.com/article/trump-border-immigration-birthright-citizenship-494add8239eb1c0c9f4ccb45db03f1f0 ; https://www.whitehouse.gov/news/ ; https://www.theguardian.com/us-news/2026/aug/06/trump-birthright-citizenship-executive-orders |
| 6 | 續報｜Uganda 國會批准派兵參與 Gaza international force，但穩定部隊仍未成形 | AP JSON-LD `datePublished=2026-08-06T14:27:21Z` = 2026-08-06 22:27:21 Asia/Taipei；modified 2026-08-06T15:52:34Z. | 續報；前次 2026-08-01 / 2026-08-03 captured Gaza disarmament roadmap and Israeli concerns。今日新增 Uganda domestic authorization for troop contribution。 | https://apnews.com/article/uganda-troops-gaza-international-force-2363467ec800644552f8be5a1b84f8f4 |
| 7 | Rights group 警告 Israel 政策正把 West Bank healthcare 推向崩潰 | AP JSON-LD `datePublished=2026-08-06T09:39:55Z` = 2026-08-06 17:39:55 Asia/Taipei；modified 2026-08-06T14:19:50Z. | New accountability report inside the window；no same event found in prior daily reports。 | https://apnews.com/article/west-bank-healthcare-physicians-human-rights-israel-17a6c89efefa7e3ec07b3c68705ee043 |
| 8 | Israel 起訴 West Bank settler 涉 2025 年 Palestinian activist Awdah Hathaleen 死亡案 | Guardian / Reuters metadata `datePublished=2026-08-06T14:38:40Z` = 2026-08-06 22:38:40 Asia/Taipei；modified 2026-08-06T19:42:05Z. | New legal proceeding；2025 killing is background, not the event-time basis。Prior daily search did not find the same indictment。 | https://www.theguardian.com/world/2026/aug/06/israel-charges-west-bank-settler-killing-palestinian-activist-awdah-hathaleen |
| 9 | U.S. 將關閉五個海外領事館，批評者稱 China 可能填補外交真空 | Guardian metadata `datePublished=2026-08-06T15:41:29Z` = 2026-08-06 23:41:29 Asia/Taipei. | New diplomatic-footprint decision / congressional notice inside window；no prior daily capture of these five closures。 | https://www.theguardian.com/us-news/2026/aug/05/us-state-department-consulate-closures |
| 10 | India-Bangladesh 關係因 Sheikh Hasina 在 Delhi 對媒體發聲再探低點 | Guardian metadata `datePublished=2026-08-06T14:30:43Z` = 2026-08-06 22:30:43 Asia/Taipei；modified 2026-08-06T15:34:41Z. | New diplomatic-row publication inside window；prior Hasina / Bangladesh background is older and not the event basis。 | https://www.theguardian.com/world/2026/aug/06/india-bangladesh-relations-exiled-pm-speech-delhi-sheikh-hasina |

## Selected Technology / AI Product and Platform Items

| # | Item | Event / publication-time basis | Deduplication decision | Primary URLs |
|---|---|---|---|---|
| T1 | OpenAI 更新 GPT-5.6 Sol，並將 GPT-5.6 Luna 與 unlimited text chats 擴到 Free / Go 使用者 | OpenAI official page dated 2026-08-06; no exact seconds exposed. TechCrunch exact `datePublished=2026-08-06T17:34:42Z` = 2026-08-07 01:34:42 Asia/Taipei. | New ChatGPT availability / model-routing update；not a repeat of 2026-07-31 GPT-5.6 price or 2026-08-05 education plugin item。 | https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/ ; https://techcrunch.com/2026/08/06/openai-brings-unlimited-chatgpt-text-chats-to-free-users/ |
| T2 | GitHub Copilot 上架 Kimi K3 後暫停 rollout，open-weight coding model 發布治理受測 | GitHub changelog `datePublished=2026-08-06T10:27:25-07:00` / `2026-08-06T17:27:25Z` = 2026-08-07 01:27:25 Asia/Taipei；modified 2026-08-06T21:09:30Z. | New Copilot distribution / rollout-pause event；distinct from 2026-07-20 Kimi K3 subscription pause。 | https://github.blog/changelog/2026-08-06-kimi-k3-is-now-available-in-github-copilot/ |
| T3 | Google DeepMind 開源 WeatherNext 2，宣稱 cyclone forecast 可多爭取約一天預警 | Google Blog and DeepMind official pages show `Aug 06, 2026` / `article:published_time=2026-08-06`; represented as date-level marker `2026-08-06T04:00:00Z` = 2026-08-06 12:00:00 Asia/Taipei, not a claimed exact second。 | New official model / research release and open-source announcement inside date-level window。 | https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/ ; https://blog.google/innovation-and-ai/models-and-research/google-deepmind/weathernext-2-cyclones/ |
| T4 | OpenAI 與 Jony Ive 首款裝置據報像 hockey puck smart speaker，2027 年才可能上市 | The Verge metadata `datePublished=2026-08-06T20:55:39Z` = 2026-08-07 04:55:39 Asia/Taipei. | New product-reporting / hardware roadmap item；rumor status explicitly labeled。 | https://www.theverge.com/ai-artificial-intelligence/976431/openai-chatgpt-battery-smart-speaker-rumor |
| T5 | Google 宣布 Pixel 11 發表會將由 Trevor Noah 主持，Made by Google 走向娛樂化硬體發布 | The Verge metadata `datePublished=2026-08-06T21:15:47Z` = 2026-08-07 05:15:47 Asia/Taipei. | New launch-event item inside window；not treated as device launch / availability。 | https://www.theverge.com/tech/976454/made-by-google-2026-event-pixel-11-trevor-noah |
| T6 | Mirendil 與 Google Cloud 簽 US$100m+ compute deal，self-improving AI lab 擴充算力 | TechCrunch metadata `datePublished=2026-08-06T13:00:00Z` = 2026-08-06 21:00:00 Asia/Taipei. | New compute partnership / AI lab infrastructure item inside window。 | https://techcrunch.com/2026/08/06/exclusive-mirendil-inks-100m-google-cloud-deal-to-scale-self-improving-ai/ |
| T7 | Tesla 與 SpaceX 將投資 US$16.8bn 建 Terafab advanced chip factory | TechCrunch metadata `datePublished=2026-08-06T15:21:51Z` = 2026-08-06 23:21:51 Asia/Taipei. | New AI chip / semiconductor infrastructure announcement inside window。 | https://techcrunch.com/2026/08/06/tesla-and-spacex-will-invest-16-8b-to-start-building-terafab-chip-factory-in-texas/ |
| T8 | California lawmakers 推 SB 903，限制 AI "therapists" 與心理健康 triage 自動化 | AP JSON-LD `datePublished=2026-08-06T17:56:30Z` = 2026-08-07 01:56:30 Asia/Taipei. | New AI health-governance / product-boundary item；selected because it directly affects AI therapy chatbot deployment。 | https://apnews.com/article/california-chatbots-therapy-ai-health-regulations-438eaaa4afc617153aa83acc150b9bda |
| T9 | Naive 募得 US$28.5m，要自動化公司設立與營運雜務 | TechCrunch metadata `datePublished=2026-08-06T17:00:37Z` = 2026-08-07 01:00:37 Asia/Taipei. | New startup funding / enterprise-agent product direction item。 | https://techcrunch.com/2026/08/06/naive-raises-28-5m-to-automate-the-grunt-work-of-setting-up-and-running-a-company/ |
| T10 | eBay 在 record quarter 後加碼 live shopping，追趕 Whatnot 與 TikTok Shop | TechCrunch metadata `datePublished=2026-08-06T14:17:46Z` = 2026-08-06 22:17:46 Asia/Taipei. | New marketplace-product strategy item inside window。 | https://techcrunch.com/2026/08/06/ebay-continues-to-bet-on-live-shopping-after-record-quarter/ |

## Excluded or Lower-Priority Candidates

- **Oath Keepers Jan. 6 sedition case dismissed:** AP `datePublished=2026-08-05T14:18:40Z`, which is before this run's UTC window start. `dateModified=2026-08-06T00:00:36Z` was also just before window start and not used to treat the older event as new.
- **CDC director Erica Schwartz confirmed:** AP `datePublished=2026-08-05T19:05:14Z`, before the UTC window. Excluded despite homepage prominence.
- **Michigan / Ohio cyclospora deaths and CDC outbreak update:** deaths first reported 2026-08-03 and CDC multi-state update 2026-08-05T21:09:16Z, outside current window.
- **FIFA / Infantino governance analysis:** AP article `datePublished=2026-08-06T18:28:08Z` is in-window, but material event nodes were already captured 2026-08-01 and 2026-08-03; current item is mainly analysis / election outlook, so not reselected.
- **Ceuta / Morocco analysis:** Guardian items are in-window, but the concrete Ceuta migration crisis, death toll, rumor mechanism and minors were already captured repeatedly from 2026-08-01 to 2026-08-05; no sufficiently new event node was found.
- **AP solar / climate-fund court ruling:** AP report was first published 2026-08-04, outside the window; later related prominence was not a new event.
- **Sun telescope images:** AP `datePublished=2026-08-05T15:03:41Z`, before the window；modified time was in-window but image release itself was older。
- **EA US$55bn Saudi PIF buyout completion:** event completed 2026-08-04 and primary AP / Verge / Guardian coverage fell before the exact window; excluded despite discussion.
- **Google AI Studio standalone Android app cancellation:** The Verge metadata `datePublished=2026-08-01T13:57:46Z`; outside this run's window.
- **Google AI leadership shakeup / Discovery Loop analysis:** the departure / startup launch was captured 2026-08-06 as Discovery Loop；The Verge Aug. 6 analysis did not add a distinct product event.
- **UK not intervening in Paramount / Warner Bros. Discovery deal:** in-window AP item, but lower priority than direct AI / developer / hardware / marketplace product items.

## Contradictions and Uncertainty Notes

- **Hormuz:** near-deal reporting is not a signed text; Iran, Oman and U.S. terms remain partly opaque. Yemen / Lebanon escalation may reduce trust even if maritime terms progress.
- **Ukraine:** strike claims, drone-intercept numbers and target descriptions come from opposing governments and can be inflated or incomplete. Civilian casualty statistics rely on U.N. monitoring but can lag.
- **Leipzig:** Russia attribution is not final; German investigation may later classify the incident differently.
- **Congo Ebola:** mutation concern is under study, not confirmed. Quarantine near Kinshasa is precautionary pending test results.
- **Birthright citizenship:** White House framing and civil-liberties interpretation sharply conflict; the legal effect depends on litigation and agency guidance.
- **Uganda / Gaza force:** parliamentary approval is a preparatory step; no final international mandate or deployment schedule is confirmed.
- **West Bank healthcare:** Israeli authorities may dispute responsibility or emphasize security needs; patient-access data may vary by district.
- **OpenAI hardware rumor:** The Verge item relies on Bloomberg reporting; OpenAI has not formally launched the device.
- **GitHub Kimi K3:** rollout pause means the availability headline was materially qualified within the same day; users should wait for GitHub's incident update.
- **AI therapy regulation:** SB 903 is not yet law and its exact scope remains contested by health groups and tech trade groups.

## Image Sources Used in HTML Deck

- Unsplash newsroom / media desk background：https://images.unsplash.com/photo-1495020689067-958852a7765e?auto=format&fit=crop&w=1800&q=80
- Unsplash earth from space background：https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1800&q=80
- Unsplash shipping lane / containers background：https://images.unsplash.com/photo-1566576721346-d4a3b4eaeb55?auto=format&fit=crop&w=1800&q=80
- Unsplash city at night / security background：https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=1800&q=80
- Unsplash medical / lab background：https://images.unsplash.com/photo-1582719471384-894fbb16e074?auto=format&fit=crop&w=1800&q=80
- Unsplash civic building background：https://images.unsplash.com/photo-1529107386315-e1a2ed48a620?auto=format&fit=crop&w=1800&q=80
- Unsplash map background：https://images.unsplash.com/photo-1524661135-423995f22d0b?auto=format&fit=crop&w=1800&q=80
- Unsplash circuit board background：https://images.unsplash.com/photo-1518779578993-ec3579fee39f?auto=format&fit=crop&w=1800&q=80
- Unsplash cloud / data center style background：https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=1800&q=80
- Unsplash mobile devices background：https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=1800&q=80
- Unsplash semiconductor / electronics background：https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?auto=format&fit=crop&w=1800&q=80
- Unsplash documents background：https://images.unsplash.com/photo-1492724441997-5dc865305da7?auto=format&fit=crop&w=1800&q=80

## Publication / Verification Notes

- Created `wiki/daily/2026/08/2026-08-07/daily-news-2026-08-07.md`, `source-notes-2026-08-07.md` and `slides-2026-08-07.html`.
- Updated `wiki/daily/latest-slides.html`, root `index.html`, `.nojekyll`, `wiki/index.md`, `wiki/overview.md` and `wiki/log.md` with cache-busting version `20260807-080203-ai-news-r1`.
- Local verification passed at `http://localhost:4173/wiki/daily/latest-slides.html`.
- GitHub Pages verification passed for the dated deck, latest redirect, daily report and source notes：
  - https://lucaskk.github.io/daily-news/wiki/daily/2026/08/2026-08-07/slides-2026-08-07.html?v=20260807-080203-ai-news-r1
  - https://lucaskk.github.io/daily-news/wiki/daily/latest-slides.html?v=20260807-080203-ai-news-r1
- LINE delivery was skipped because `.env` contains `LINE_CHANNEL_ACCESS_TOKEN` and `PUBLIC_SLIDES_BASE_URL`, but `LINE_TO_ID` is missing or empty.
