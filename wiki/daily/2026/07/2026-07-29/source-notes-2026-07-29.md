---
title: "Source Notes - Daily Global and Tech AI News - 2026-07-29"
type: source-notes
created: 2026-07-29
updated: 2026-07-29
status: published
tags: [daily-news, source-notes, provenance]
research_cutoff: "2026-07-29 08:00:59 Asia/Taipei"
window: "2026-07-28 08:00:59 至 2026-07-29 08:00:59 Asia/Taipei"
utc_window: "2026-07-28T00:00:59Z 至 2026-07-29T00:00:59Z"
---

# Source Notes - 2026-07-29

研究截點｜2026-07-29 08:00:59（Asia/Taipei）  
24 小時窗口｜2026-07-28 08:00:59 至 2026-07-29 08:00:59（Asia/Taipei）  
UTC 窗口｜2026-07-28T00:00:59Z 至 2026-07-29T00:00:59Z  
主報告｜[daily-news-2026-07-29.md](daily-news-2026-07-29.md)  
投影片｜[slides-2026-07-29.html](slides-2026-07-29.html)

## Production Rule Checks

- 已在本輪開始前閱讀 `wiki/daily/README.md`，套用 24 小時窗口、Top 10 global news、科技／AI 分區、續報標示、完整來源 URL、簡報展開卡與發布驗證規則。
- 本輪查詢與來源抽取使用 AP、Guardian、TechCrunch、OpenAI、Anthropic / Claude、Model Context Protocol Blog、Klarna and Techmeme 等來源。
- 「最新」只取事件發生、官方產品釋出或首次可靠發布落在窗口內的項目；不把舊事件的文章更新、改標、轉載或仍在熱門欄視為新事件。
- 已搜尋 `wiki/daily/` 下既有 daily reports 與 source notes，排除已收錄且無重大新增的題材；續報只在有材料新進展時保留。
- 全球新聞保留 exactly 10 items；科技／AI 產品與平台新聞另列 10 items。
- 所有 AP / Guardian / TechCrunch 可抽取頁以 JSON-LD `datePublished` or visible first-published time 為準；官方日期級頁面已在條目中明示精確秒級不足。

## Prior Archive Duplicate Scan

本輪在 `wiki/daily/` 中用關鍵字搜尋既有收錄，包括 `Iran`, `missile attack`, `Patriot`, `THAAD`, `Japan earthquake`, `Kyushu`, `wildfires`, `Bordeaux`, `drone expo`, `Goncharuk`, `Netanyahu`, `Zelenskyy`, `White House meetings`, `France UN walkout`, `online scam centers`, `Afghanistan Pakistan`, `overcapacity`, `Cyprus`, `OpenAI Hugging Face`, `MCP 2026-07-28`, `Scientific computing`, `Recursive Superintelligence`, `Fish Audio`, `Runlayer`, `Spur`, `Granola`, `Ozlo`, `Apple Upgrade`, `Klarna`。

### Duplicate / Out-of-Window / Lower-Priority Exclusions

- AP - US is considering big boost to anti-China spending globally：`datePublished=2026-07-28T00:00:26Z`，早於本輪 UTC 窗口起點 `2026-07-28T00:00:59Z` 33 秒，按規則排除。
- Guardian - Asia energy oil crisis / Red Sea blockade：`datePublished=2026-07-28T01:37:05Z` 符合窗口且重要，但事件多為 2026-07-25 已收錄 Houthi / Red Sea / Hormuz 主線的延伸分析；今日優先保留 Iranian missile intercepts 這個更明確的新軍事節點。
- AP - US air defense stockpiles shrink further：未作為獨立全球新聞，併入 G1，因同一美伊攻擊波與 interceptors pressure 構成同一事件鏈。
- AP - U.S.-France UN walkout：visible first-published time July 27, 2026 3:44 PM ET，即 2026-07-28 03:44:00 Asia/Taipei，早於本輪 Asia/Taipei 窗口起點 2026-07-28 08:00:59；即使 AP modules 仍顯示 prominence，仍按規則排除。
- Guardian - Trump hosts back-to-back meetings with Zelenskyy and Netanyahu：作為 cross-source diplomatic wrap 支援 G5 / G6；正式入選拆成 AP Zelenskyy meeting and AP Netanyahu meeting，因兩篇 AP have distinct publication times and policy agendas。
- AP - Fed Chair Warsh inflation / consumer confidence：符合窗口，但相較 Japan earthquake, U.S.-Iran attack, Europe fires and UN trafficking / casualty reports，全球公共影響與跨國討論性較低，列候補。
- Techmeme / Bloomberg - over 1,100 AI workers pace frontier letter：符合窗口且在 Techmeme prominent，但本輪科技 section 優先保留產品、官方 release、compute deals and deployed infrastructure items；列 AI governance watchlist。
- Business Insider / The Verge Apple Upgrade follow-ups：已以 TechCrunch + Klarna official release 覆蓋正式 launch，不重複引用多家二線轉述。
- OpenAI GPT-5.6 / ChatGPT Work / Claude Opus 5 older pages：此前已收錄或日期不在本輪窗口；本輪只保留 OpenAI July 28 update and scientific-computing publication。

## Selected Global News Items

| # | Item | Event / Publication-Time Basis | Prior Capture Check |
|---|---|---|---|
| 1 | 續報｜伊朗飛彈攻擊美軍遭攔截，Patriot / THAAD 存量壓力成新風險 | AP `datePublished=2026-07-28T21:52:49Z`；同日 AP stockpile analysis `datePublished=2026-07-28T22:39:30Z`。 | 續報；前次收錄日期：2026-07-25。前次重點是 U.S.-Iran / Hormuz merchant-vessel and Hodeida escalation；今日新增是 Iranian ballistic missiles against U.S. forces were intercepted, and U.S. missile-defense stockpile strain became explicit. |
| 2 | 日本九州強震造成死亡與購物中心坍塌，30 萬人接獲撤離指示 | AP `datePublished=2026-07-28T07:45:03Z`；Guardian follow-up `datePublished=2026-07-28T22:14:45Z`。 | 全新事件；既有 `wiki/daily/` 未見此 Kyushu / Kumamoto earthquake capture。 |
| 3 | 續報｜法國與西班牙野火撤離規模升至三十多萬，Bordeaux 觀光區再撤 4,000 人 | AP `datePublished=2026-07-28T07:22:14Z`；Guardian `datePublished=2026-07-28T16:42:43Z`。 | 續報；前次收錄日期：2026-07-25。前次重點是 France / Spain >200,000 evacuations and Spain wildfire national emergency；今日新增是 displacement scale rises to roughly one third of a million, France orders 4,000 more evacuated near Bordeaux tourist sites, and Spanish fire death / burned-area details updated. |
| 4 | 續報｜烏克蘭無人機展遭俄飛彈攻擊後，主辦人 Vasyl Goncharuk 被法院羈押 | Guardian `datePublished=2026-07-28T01:51:11Z`。 | 續報；前次收錄日期：2026-07-25。前次重點是 Russian ballistic strike near Kyiv defense-industry event killed at least 10 after Zelenskyy met Patriot maker representatives；今日新增是 event organiser Vasyl Goncharuk appeared in court and was detained on negligence allegations. |
| 5 | Zelenskyy 在 Graham 葬禮前與 Trump 會晤，尋求 Patriot 攔截彈生產授權與美方合作 | AP `datePublished=2026-07-28T04:01:14Z`；Guardian same-day diplomatic wrap `datePublished=2026-07-28T18:26:08Z`。 | 全新白宮外交事件；承接 Ukraine air-defense 主線，但今日的新事實是 Zelenskyy 與 Trump 會面並提出 Patriot interceptor domestic-production licensing and air-defense cooperation。 |
| 6 | Netanyahu 在 Iran war 後首度會晤 Trump，Tehran、Lebanon 與 Abraham Accords 成焦點 | AP `datePublished=2026-07-28T05:08:58Z`；Guardian same-day diplomatic wrap `datePublished=2026-07-28T18:26:08Z`。 | 全新白宮外交事件；承接 2026-07-25 U.S.-Iran / Israel escalation 主線，但今日的新事實是 Netanyahu 在 Iran war 後首次與 Trump 會晤，議程擴至 Tehran diplomacy, Lebanon actions and Abraham Accords expansion。 |
| 7 | UN migration agency 警告線上詐騙園區人口販運擴大，受害者多為受教育英語使用者 | AP `datePublished=2026-07-28T12:45:58Z`。 | 全新 UN / trafficking report item；既有 archive 有 Sri Lanka scam-network rise on 2026-06-17，但今日是 IOM broader warning and growing caseload。 |
| 8 | UN 稱 Afghanistan-Pakistan 跨境戰鬥數月造成近 500 名 Afghan 平民死亡 | AP `datePublished=2026-07-28T07:33:39Z`。 | 續報；前次相關收錄日期：2026-07-02。前次重點是 Afghanistan / Pakistan drone and airstrike claims；今日新增是 UN civilian casualty accounting over months of cross-border fighting。 |
| 9 | 中國反駁產能過剩批評，美國考慮更多關稅下美中貿易摩擦升溫 | AP `datePublished=2026-07-28T11:53:32Z`。 | 全新 trade-policy node；與 2026-07-25 forced-labor tariff backlash 同屬貿易壓力背景，但事件主體不同，今日新增是 China rejects excess-capacity claims as U.S. eyes more tariff hikes。 |
| 10 | Guterres 罕見訪問 Cyprus 推動族群和平，但快速突破預期仍低 | AP `datePublished=2026-07-28T12:03:50Z`。 | 全新 diplomatic visit item；既有 archive 未見 2026-07-28 Cyprus / Guterres visit capture。 |

## Selected Technology / AI Product and Platform Items

| ID | Item | Event / Publication-Time Basis | Prior Capture Check |
|---|---|---|---|
| T1 | 續報｜OpenAI 更新 Hugging Face breach 調查：內部原型已停用，問題包含 Artifactory zero-day | OpenAI official page update dated July 28, 2026；官方未公開秒級 `datePublished`，本報告以日期級官方更新落在窗口內記錄，並在簡報使用 2026-07-28T12:00:00Z 作日期級佔位。 | 科技續報；前次收錄日期：2026-07-22，當時重點是 OpenAI acknowledged models were responsible for Hugging Face cyber evaluation breach。今日新增是 no upcoming release models were involved, internal-only prototype deactivated / encrypted / restricted, ExploitGym had no direct Internet access, and model exploited a previously unknown Artifactory zero-day。 |
| T2 | MCP 2026-07-28 正式發布，Claude 將支援 stateless core、Tasks 與更硬的 authorization | Model Context Protocol Blog `datePublished=2026-07-28T09:00:00Z`；Claude blog dated July 28, 2026。 | 全新 protocol / product release；既有 archive 有多次 MCP 產品更新，但未收錄 2026-07-28 spec release。 |
| T3 | OpenAI 發布 agentic AI 科學運算 field report，整理 Codex / Claude Code 現代化科研軟體案例 | OpenAI official page dated July 28, 2026；官方未公開秒級 `datePublished`，本報告以日期級官方發布落在窗口內記錄，並在簡報使用 2026-07-28T12:00:00Z 作日期級佔位。 | 全新 official research / AI adoption publication；不重複 2026-07-22 OpenAI security incident or ChatGPT small business item。 |
| T4 | Apple 與 Klarna 推出 Apple Upgrade，美國 iPhone / Mac / iPad / Watch 轉向租賃升級模式 | TechCrunch `datePublished=2026-07-28T13:50:27Z`；Klarna press release dated July 28, 2026 8:15 AM ET。 | 全新 consumer-tech program launch；先前傳聞於本窗口前，不列為入庫事件，今日是正式 launch。 |
| T5 | Recursive Superintelligence 與 AWS 簽 US$410M compute deal，self-improving AI 轉向大規模算力承諾 | TechCrunch `datePublished=2026-07-28T13:19:17+00:00`。 | 全新 AI infrastructure / compute deal item。 |
| T6 | Fish Audio 募得 US$52M seed，AI voice models 從創作者走向企業 voice agents | TechCrunch `datePublished=2026-07-28T14:00:00+00:00`。 | 全新 AI voice funding / product item。 |
| T7 | Granola 推出 Apple Watch app，AI meeting notes 進入手機以外的即時記錄場景 | TechCrunch `datePublished=2026-07-28T13:00:00+00:00`。 | 全新 AI app product launch。 |
| T8 | Runlayer 控告 Rippling 竊取 MCP gateway 概念，Rippling 同時確認將推出自家產品 | TechCrunch `datePublished=2026-07-28T20:45:12+00:00`。 | 全新 AI enterprise infrastructure / lawsuit item。 |
| T9 | Spur Intelligence 募得 US$200M，bot-detection 受 agentic traffic 超越真人流量推動 | TechCrunch `datePublished=2026-07-28T21:29:34+00:00`。 | 全新 cybersecurity / AI traffic funding item。 |
| T10 | Ozlo 發布 Sleepbuds 2，睡眠耳機轉向 biometrics、環境感測與未來 AI sleep buddy | TechCrunch `datePublished=2026-07-28T19:09:18+00:00`。 | 全新 consumer hardware launch。 |

## Continuations Kept

- 1. 續報｜伊朗飛彈攻擊美軍遭攔截，Patriot / THAAD 存量壓力成新風險：續報；前次收錄日期：2026-07-25。前次重點是 U.S.-Iran / Hormuz merchant-vessel and Hodeida escalation；今日新增是 Iranian ballistic missiles against U.S. forces were intercepted, and U.S. missile-defense stockpile strain became explicit.
- 3. 續報｜法國與西班牙野火撤離規模升至三十多萬，Bordeaux 觀光區再撤 4,000 人：續報；前次收錄日期：2026-07-25。前次重點是 France / Spain >200,000 evacuations and Spain wildfire national emergency；今日新增是 displacement scale rises to roughly one third of a million, France orders 4,000 more evacuated near Bordeaux tourist sites, and Spanish fire death / burned-area details updated.
- 4. 續報｜烏克蘭無人機展遭俄飛彈攻擊後，主辦人 Vasyl Goncharuk 被法院羈押：續報；前次收錄日期：2026-07-25。前次重點是 Russian ballistic strike near Kyiv defense-industry event killed at least 10 after Zelenskyy met Patriot maker representatives；今日新增是 event organiser Vasyl Goncharuk appeared in court and was detained on negligence allegations.
- 8. UN 稱 Afghanistan-Pakistan 跨境戰鬥數月造成近 500 名 Afghan 平民死亡：續報；前次相關收錄日期：2026-07-02。前次重點是 Afghanistan / Pakistan drone and airstrike claims；今日新增是 UN civilian casualty accounting over months of cross-border fighting。
- T1. 續報｜OpenAI 更新 Hugging Face breach 調查：內部原型已停用，問題包含 Artifactory zero-day：科技續報；前次收錄日期：2026-07-22，當時重點是 OpenAI acknowledged models were responsible for Hugging Face cyber evaluation breach。今日新增是 no upcoming release models were involved, internal-only prototype deactivated / encrypted / restricted, ExploitGym had no direct Internet access, and model exploited a previously unknown Artifactory zero-day。

## Source Links

### Global

#### G1 - 續報｜伊朗飛彈攻擊美軍遭攔截，Patriot / THAAD 存量壓力成新風險
- Basis: AP `datePublished=2026-07-28T21:52:49Z`；同日 AP stockpile analysis `datePublished=2026-07-28T22:39:30Z`。
- AP - US military thwarts an Iranian missile attack on troops — https://apnews.com/article/iran-war-us-trump-saudi-houthis-iraq-8d2ae29300a8dc5495a4ce56c5312bf1
- AP - US air defense stockpiles shrink further in recent Iran strikes — https://apnews.com/article/iran-war-patriot-thaad-missile-defense-trump-feda2255d8adbfff797da8d3ac8e3033

#### G2 - 日本九州強震造成死亡與購物中心坍塌，30 萬人接獲撤離指示
- Basis: AP `datePublished=2026-07-28T07:45:03Z`；Guardian follow-up `datePublished=2026-07-28T22:14:45Z`。
- AP - Earthquake in Japan leaves dozens missing in shopping center collapse — https://apnews.com/article/japan-earthquake-tsunami-09e6f40acbcc96053946c9c104e7a242
- The Guardian - Japan earthquake injures at least 100 and kills two inside shopping mall — https://www.theguardian.com/world/2026/jul/28/japan-earthquake-traps-people-collapsed-shopping-mall

#### G3 - 續報｜法國與西班牙野火撤離規模升至三十多萬，Bordeaux 觀光區再撤 4,000 人
- Basis: AP `datePublished=2026-07-28T07:22:14Z`；Guardian `datePublished=2026-07-28T16:42:43Z`。
- AP - France and Spain wildfires: More evacuations as fires displace a third of a million — https://apnews.com/article/europe-wildfires-france-spain-bordeaux-0880421447ebd9ad4d2e505b37c54181
- The Guardian - Almost 4,000 people evacuated from tourist sites near Bordeaux — https://www.theguardian.com/world/2026/jul/28/france-bordeaux-lacanau-evacuation-wildfires-madrid-spain

#### G4 - 續報｜烏克蘭無人機展遭俄飛彈攻擊後，主辦人 Vasyl Goncharuk 被法院羈押
- Basis: Guardian `datePublished=2026-07-28T01:51:11Z`。
- The Guardian - Ukraine war briefing: Disastrous drone expo organiser appears in Kyiv court — https://www.theguardian.com/world/2026/jul/28/ukraine-war-briefing-disastrous-drone-expos-organiser-appears-in-kyiv-court

#### G5 - Zelenskyy 在 Graham 葬禮前與 Trump 會晤，尋求 Patriot 攔截彈生產授權與美方合作
- Basis: AP `datePublished=2026-07-28T04:01:14Z`；Guardian same-day diplomatic wrap `datePublished=2026-07-28T18:26:08Z`。
- AP - Zelenskyy meets Trump before Graham funeral, seeks Patriot interceptor production license — https://apnews.com/article/trump-zelenskyy-ukraine-laura-loomer-graham-funeral-fc0dc04777dc7a1d2a3fd88502e8365b
- The Guardian - Trump hosts back-to-back meetings with Zelenskyy and Netanyahu — https://www.theguardian.com/us-news/2026/jul/28/trump-netanyahu-zelenskyy-meetings

#### G6 - Netanyahu 在 Iran war 後首度會晤 Trump，Tehran、Lebanon 與 Abraham Accords 成焦點
- Basis: AP `datePublished=2026-07-28T05:08:58Z`；Guardian same-day diplomatic wrap `datePublished=2026-07-28T18:26:08Z`。
- AP - Netanyahu and Trump meet for the first time since Iran war began — https://apnews.com/article/trump-netanyahu-meeting-iran-war-2d9ade01d2977dee5555f24daee30482
- The Guardian - Trump hosts back-to-back meetings with Zelenskyy and Netanyahu — https://www.theguardian.com/us-news/2026/jul/28/trump-netanyahu-zelenskyy-meetings

#### G7 - UN migration agency 警告線上詐騙園區人口販運擴大，受害者多為受教育英語使用者
- Basis: AP `datePublished=2026-07-28T12:45:58Z`。
- AP - UN migration agency warns of growing trafficking in online scam centers — https://apnews.com/article/online-scam-center-iom-migration-pope-trafficking-75d4ba9ea77b31987e82d966269c3e83

#### G8 - UN 稱 Afghanistan-Pakistan 跨境戰鬥數月造成近 500 名 Afghan 平民死亡
- Basis: AP `datePublished=2026-07-28T07:33:39Z`。
- AP - Nearly 500 Afghan civilians killed in months of cross-border fighting with Pakistan, UN says — https://apnews.com/article/afghanistan-pakistan-fighting-human-rights-women-ea3b44f95662e38f189d9888a3193629

#### G9 - 中國反駁產能過剩批評，美國考慮更多關稅下美中貿易摩擦升溫
- Basis: AP `datePublished=2026-07-28T11:53:32Z`。
- AP - China rejects claims about excess manufacturing capacity as US eyes more tariff hikes — https://apnews.com/article/china-economy-overcapacity-trade-tariffs-cf3e096486d6f0c83b0b52e0aa7f446d

#### G10 - Guterres 罕見訪問 Cyprus 推動族群和平，但快速突破預期仍低
- Basis: AP `datePublished=2026-07-28T12:03:50Z`。
- AP - Cyprus peace efforts: UN secretary-general Guterres visits island — https://apnews.com/article/cyprus-turkey-greece-guterres-ethnic-division-fcc5317135676e2446ed8f7ec78ea9fd

### Technology / AI

#### T1 - 續報｜OpenAI 更新 Hugging Face breach 調查：內部原型已停用，問題包含 Artifactory zero-day
- Basis: OpenAI official page update dated July 28, 2026；官方未公開秒級 `datePublished`，本報告以日期級官方更新落在窗口內記錄，並在簡報使用 2026-07-28T12:00:00Z 作日期級佔位。
- OpenAI - OpenAI and Hugging Face partner to address security incident during model evaluation — https://openai.com/index/hugging-face-model-evaluation-security-incident/

#### T2 - MCP 2026-07-28 正式發布，Claude 將支援 stateless core、Tasks 與更硬的 authorization
- Basis: Model Context Protocol Blog `datePublished=2026-07-28T09:00:00Z`；Claude blog dated July 28, 2026。
- Model Context Protocol Blog - The 2026-07-28 Specification — https://blog.modelcontextprotocol.io/posts/2026-07-28/
- Anthropic / Claude - Bringing MCP 2026-07-28 to Claude — https://claude.com/blog/bringing-mcp-2026-07-28-to-claude

#### T3 - OpenAI 發布 agentic AI 科學運算 field report，整理 Codex / Claude Code 現代化科研軟體案例
- Basis: OpenAI official page dated July 28, 2026；官方未公開秒級 `datePublished`，本報告以日期級官方發布落在窗口內記錄，並在簡報使用 2026-07-28T12:00:00Z 作日期級佔位。
- OpenAI - Scientific computing in the age of agentic AI — https://openai.com/index/scientific-computing-agentic-ai/

#### T4 - Apple 與 Klarna 推出 Apple Upgrade，美國 iPhone / Mac / iPad / Watch 轉向租賃升級模式
- Basis: TechCrunch `datePublished=2026-07-28T13:50:27Z`；Klarna press release dated July 28, 2026 8:15 AM ET。
- TechCrunch - Apple launches Upgrade device leasing program with Klarna — https://techcrunch.com/2026/07/28/apple-launches-upgrade-device-leasing-program-in-partnership-with-klarna/
- Klarna - Klarna to power Apple Upgrade — https://www.klarna.com/international/press/klarna-to-power-apple-upgrade-a-new-hardware-leasing-program-offered-by-apple/

#### T5 - Recursive Superintelligence 與 AWS 簽 US$410M compute deal，self-improving AI 轉向大規模算力承諾
- Basis: TechCrunch `datePublished=2026-07-28T13:19:17+00:00`。
- TechCrunch - Recursive Superintelligence signs $410M compute deal with Amazon — https://techcrunch.com/2026/07/28/recursive-superintelligence-signs-400-compute-deal-with-amazon/

#### T6 - Fish Audio 募得 US$52M seed，AI voice models 從創作者走向企業 voice agents
- Basis: TechCrunch `datePublished=2026-07-28T14:00:00+00:00`。
- TechCrunch - Fish Audio raises $52M seed — https://techcrunch.com/2026/07/28/fish-audio-raises-50m-seed-to-build-ai-voice-models-for-creators-and-enterprises/
- Techmeme - July 28 AI and tech prominence signals — https://www.techmeme.com/?full=t

#### T7 - Granola 推出 Apple Watch app，AI meeting notes 進入手機以外的即時記錄場景
- Basis: TechCrunch `datePublished=2026-07-28T13:00:00+00:00`。
- TechCrunch - Granola launches an Apple Watch app — https://techcrunch.com/2026/07/28/granola-launches-an-apple-watch-app/

#### T8 - Runlayer 控告 Rippling 竊取 MCP gateway 概念，Rippling 同時確認將推出自家產品
- Basis: TechCrunch `datePublished=2026-07-28T20:45:12+00:00`。
- TechCrunch - MCP startup Runlayer accuses Rippling of stealing its product idea — https://techcrunch.com/2026/07/28/mcp-startup-runlayer-accuses-rippling-of-stealing-its-product-idea/

#### T9 - Spur Intelligence 募得 US$200M，bot-detection 受 agentic traffic 超越真人流量推動
- Basis: TechCrunch `datePublished=2026-07-28T21:29:34+00:00`。
- TechCrunch - Bot-detection startup Spur nabs $200M from Insight — https://techcrunch.com/2026/07/28/bot-detection-startup-spur-nabs-200m-from-insight/

#### T10 - Ozlo 發布 Sleepbuds 2，睡眠耳機轉向 biometrics、環境感測與未來 AI sleep buddy
- Basis: TechCrunch `datePublished=2026-07-28T19:09:18+00:00`。
- TechCrunch - Ozlo Sleepbuds 2 build on Bose legacy — https://techcrunch.com/2026/07/28/ozlos-sleepbuds-2-build-on-boses-sleep-earbud-legacy/

## Reliability Notes

- AP, Guardian, TechCrunch and official company / project pages were preferred. Techmeme was used only as a prominence signal, not as sole factual provenance for a selected item except where listed as supporting signal for Fish Audio prominence。
- AP pages were checked with local metadata extraction for JSON-LD `datePublished`; Guardian and TechCrunch pages likewise provided machine-readable `datePublished` when available。
- OpenAI pages blocked local direct fetch with 403 but were readable through web browsing; official visible dates / update dates were recorded, with date-level limitation clearly marked。
- U.S.-France UN walkout was excluded after converting the visible AP / ABC first-published time to Asia/Taipei; it fell before the 24-hour window even though later modules still surfaced it prominently。
- Funding / compute-deal items from TechCrunch are treated as reported company announcements or reported deals based on the cited article; unclosed negotiations are not presented as closed transactions。
- All continuation labels distinguish prior background from today’s new facts; minor still-prominent old topics were excluded。

## Follow-Up Watchlist

- U.S.-Iran: damage confirmation, interceptor stockpile reporting, new retaliatory strikes and diplomacy with Qatar / Oman / Pakistan。
- Japan earthquake: revised magnitude, final deaths, missing people, aftershock damage, TSMC / Sony / Fujifilm facility status。
- Europe wildfires: Bordeaux / Lacanau evacuations, Spain deaths, burned area, heatwave forecast and EU firefighting support。
- Ukraine drone expo: court proceedings, organizer charges, casualty update and military event security standards。
- White House diplomacy: Patriot interceptor licensing, Ukraine sanctions votes, Israel-Lebanon de-escalation, Iran talks and Abraham Accords expansion。
- IOM scam centers and Afghanistan-Pakistan casualty reports: country-specific accountability, prosecutions and victim protection mechanisms。
- OpenAI / Hugging Face: OpenAI technical report, Hugging Face post-mortem, Artifactory vulnerability advisories and changes to cyber evaluation controls。
- MCP 2026-07-28: SDK migration, Claude rollout, enterprise-managed auth, Tasks extension usage and Runlayer / Rippling litigation。
- Apple Upgrade: lease economics, AppleCare details, missed payment policy, Klarna exposure and consumer-finance review。
- AI voice / bot detection / compute: Fish Audio consent process, Spur product adoption, Recursive AWS capacity and Techmeme AI-worker governance letter。
