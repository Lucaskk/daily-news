---
title: "Source Notes - 2026-07-30 Daily News"
date: 2026-07-30
type: source-notes
status: published
research_cutoff: "2026-07-30 08:02:44 Asia/Taipei"
window_taipei: "2026-07-29 08:02:44 至 2026-07-30 08:02:44 Asia/Taipei"
window_utc: "2026-07-29T00:02:44Z 至 2026-07-30T00:02:44Z"
---

# Source Notes - 2026-07-30 Daily News

## Research Cutoff and Window

- Asia/Taipei 研究截點：**2026-07-30 08:02:44（Asia/Taipei）**。
- 合格 24 小時窗：**2026-07-29 08:02:44 至 2026-07-30 08:02:44（Asia/Taipei）**。
- UTC 對照：**2026-07-29T00:02:44Z 至 2026-07-30T00:02:44Z**。
- 本次使用 current web research from AP, Al Jazeera, The Guardian, Google official blog, OpenAI official pages, The Verge, TechCrunch, Axios and Reuters-distributed reporting where available。
- OpenAI official pages selected on 2026-07-29 did not expose reliable second-level `datePublished` metadata through `curl`; these are recorded as **date-level official publications** and represented in report / slides as `2026-07-29T12:00:00Z` with an explicit note that the timestamp is a placeholder, not a precise publish second。

## Cross-Day Deduplication

- Searched all prior `wiki/daily/**/daily-news-*.md` and `wiki/daily/**/source-notes-*.md` before final selection.
- High-risk duplicate terms checked included `美伊`, `伊朗`, `Hormuz`, `Japan`, `九州`, `wildfire`, `野火`, `Ebola`, `煉油`, `refinery`, `OpenAI`, `Gemini`, `Copilot`, `Meta`, `FIFA`, `Myanmar`, `Kenya`, `Al-Shabab`, `人形機器人`, `humanoid`。
- Continuations retained only where the new event within this window materially changed the story:
  - U.S.-Iran / Hormuz: previous capture 2026-07-29; new U.S.-Saudi Iraq strikes, Jordan missile interceptions and Damietta vessel fires.
  - Ukraine energy strikes: previous captures 2026-07-02 and 2026-07-05; new two-major-refinery strike after Zelenskyy / Trump meeting.
  - Japan Kyushu quake: previous capture 2026-07-29; new death toll, named casualty sites, utilities and rescue figures.
  - Europe wildfires: previous capture 2026-07-29; new firefighter deaths and 2026-07-29 AP / Guardian cross-Europe updates.
  - Congo Ebola: previous capture 2026-07-07; new WFP warning connecting the fastest-growing outbreak to Ituri acute hunger and funding cuts.

## Selected Global Items

| # | Item | Event / publication-time basis | Deduplication decision | Primary URLs |
|---|---|---|---|---|
| 1 | 續報｜美伊戰事擴大：Iran missiles, U.S.-Saudi strikes in Iraq | AP `datePublished=2026-07-29T05:09:02Z` → `2026-07-29 13:09:02 Asia/Taipei`; Al Jazeera `datePublished=2026-07-29T11:34:58Z` → `2026-07-29 19:34:58`。 | **Continuation, previous 2026-07-29.** Previous item was Iranian missiles intercepted and Patriot / THAAD stockpile pressure；new item adds U.S.-Saudi strikes in Iraq, Jordan missile interceptions, Damietta vessel fires and Oman Hormuz proposal rejection. | https://apnews.com/article/iran-war-us-hormuz-strait-july-29-2026-e31d249ba6443decdd3e63cd00f0fb84 ; https://www.aljazeera.com/news/2026/7/29/iran-hits-us-in-jordan-us-saudi-strikes-on-iraq-is-war-spreading |
| 2 | 續報｜Ukraine hits two major Russian refineries | AP `datePublished=2026-07-29T10:10:51Z` → `2026-07-29 18:10:51`; Al Jazeera / Reuters `datePublished=2026-07-29T07:57:04Z` → `2026-07-29 15:57:04` for related industrial-fire reports. | **Continuation, previous 2026-07-02 / 2026-07-05.** Prior captures covered refinery attacks and fuel crisis；today adds two named major refineries and timing after Zelenskyy / Trump meeting. | https://apnews.com/article/russia-ukraine-war-oil-refinery-trump-zelenskyy-4275c2280107aedba37df8704f226ce6 ; https://www.aljazeera.com/news/2026/7/29/russian-industrial-sites-on-fire-after-ukrainian-drone-attacks |
| 3 | Fed holds rates; oil and AI stocks drag markets | AP Fed URL had pre-decision `datePublished=2026-07-29T04:01:06Z`; final decision version `dateModified=2026-07-29T21:18:27Z` → `2026-07-30 05:18:27`. AP market URL had `datePublished=2026-07-29T03:43:06Z`; market close version `dateModified=2026-07-29T20:47:06Z` → `2026-07-30 04:47:06`. | New decision / market reaction within window. To avoid treating a pre-decision article as the selected event, the report uses final-result update times as the basis. | https://apnews.com/article/federal-reserve-inflation-interest-rates-iran-war-ad10c177cb8d96f9e3ed122e12352a74 ; https://apnews.com/article/stocks-markets-ai-oil-trump-rates-b8bfaf782877957bbaa7196b70a4d725 |
| 4 | U.S. FCC bans new foreign-made humanoid robots and inverters | AP `datePublished=2026-07-29T05:50:20Z` → `2026-07-29 13:50:20`; TechCrunch `datePublished=2026-07-29T17:41:09+00:00` → `2026-07-30 01:41:09`. | New policy action. Prior robotics items in the wiki were product / summit / physical AI items, not this FCC import ban. | https://apnews.com/article/china-us-humanoid-robots-ban-tech-c9f5e3c94d91d00eff3b61b141fab366 ; https://techcrunch.com/2026/07/29/us-government-bans-new-foreign-made-humanoids-robot-dogs-and-solar-inverters-citing-risks-to-national-security/ |
| 5 | 續報｜Japan Kyushu quake death toll rises to 18 | AP `datePublished=2026-07-29T01:17:53Z` → `2026-07-29 09:17:53`; `dateModified=2026-07-29T13:14:52Z`. | **Continuation, previous 2026-07-29.** Previous capture had initial deaths, mall collapse and broad evacuation；today adds 18 deaths, 62 injuries, distinct casualty sites, utilities and shelter counts. | https://apnews.com/article/japan-earthquake-kumamoto-kagoshima-mall-factory-6b0fe69d44fa5c82ac4765a8ad82ebf6 ; https://www.aljazeera.com/news/2026/7/28/magnitude-7-1-earthquake-shakes-southern-japan-tsunami-warning-issued |
| 6 | 續報｜Southern Europe wildfires and firefighter deaths | AP `datePublished=2026-07-29T07:49:09Z` → `2026-07-29 15:49:09`; Guardian feature `datePublished=2026-07-29T18:30:27Z` → `2026-07-30 02:30:27`; Guardian live `datePublished=2026-07-29T16:04:42Z` → `2026-07-30 00:04:42`. | **Continuation, previous 2026-07-29.** Prior capture was evacuation-scale and Bordeaux / Spain fires；today adds Greek firefighter deaths, new AP cross-Europe assessment, return / renewed-risk updates. | https://apnews.com/article/c3d9c45cdbf57d19bbec46d49e5237de ; https://www.theguardian.com/world/2026/jul/29/pedro-sanchez-next-12-hours-decisive-extreme-heat-wildfires-madrid-europe ; https://www.theguardian.com/world/live/2026/jul/29/france-spain-wildfires-heatwave-extreme-heat-europe-latest-news-updates |
| 7 | FIFA World Cup investor plan deadline | AP `datePublished=2026-07-29T10:59:51Z` → `2026-07-29 18:59:51`. | New governance event. Prior World Cup items involved opening, tickets, migration / visa, Argentina / Falklands and platform content; not this member deadline / investor stake plan. | https://apnews.com/article/world-cup-fifa-investors-kushner-infantino-uefa-e66dc5d5f9907f9ea5323716b7e49ca2 |
| 8 | Myanmar activists sentenced up to 37 years | AP `datePublished=2026-07-29T15:53:39Z` → `2026-07-29 23:53:39`; Al Jazeera `datePublished=2026-07-29T21:29:33Z` → `2026-07-30 05:29:33`. | New election-repression event. Prior Myanmar references involved other security / diplomacy topics, not these Mandalay election-boycott sentences. | https://apnews.com/article/60690dd13d28b35f955506c9f14b2eab ; https://www.aljazeera.com/news/2026/7/29/myanmar-court-sentences-activists-to-37-years-over-election-protest |
| 9 | 續報｜Congo Ebola outbreak worsens hunger | AP `datePublished=2026-07-29T15:57:27Z` → `2026-07-29 23:57:27`; `dateModified=2026-07-29T20:50:56Z`. | **Continuation, previous 2026-07-07.** Previous item captured outbreak scale / deaths；today adds WFP warning that outbreak controls, conflict and funding cuts are worsening acute hunger in Ituri. | https://apnews.com/article/288100564a7155ef6afffee6f2025b37 |
| 10 | Al-Shabab kills five Kenyan security personnel | Al Jazeera `datePublished=2026-07-29T19:06:38Z` → `2026-07-30 03:06:38`; Reuters-distributed account posted within window via AOL on July 28 21:57 PDT → `2026-07-29 12:57 Asia/Taipei`. | New security event. Prior Kenya items were protest / anniversary topics; this is a distinct Mandera border ambush. | https://www.aljazeera.com/news/2026/7/29/al-shabab-kills-five-kenyan-security-personnel-in-ambush ; https://www.aol.com/articles/five-kenyan-security-officers-killed-045736000.html |

## Selected Technology / AI Product and Platform Items

| # | Item | Event / publication-time basis | Deduplication decision | Primary URLs |
|---|---|---|---|---|
| T1 | Google Gemini for macOS natural language capabilities | Google official `datePublished=2026-07-29T15:00:00+00:00` → `2026-07-29 23:00:00 Asia/Taipei`; `dateModified=2026-07-29T15:09:30.429396+00:00`. | New macOS voice / natural language workflow update. It is related to prior Gemini Mac coverage, but this is a new product capability from July 29. | https://blog.google/innovation-and-ai/products/gemini-app/speak-naturally-gemini-app-mac-os/ |
| T2 | Microsoft Copilot super app confirmed | The Verge `datePublished=2026-07-29T22:17:38+00:00` → `2026-07-30 06:17:38`. | New confirmation in Microsoft earnings-call context. Earlier rumors / Build mentions were not treated as this confirmation. | https://www.theverge.com/tech/972927/microsoft-copilot-super-app-confirmed |
| T3 | Meta personal AI agents and business agents | The Verge `datePublished=2026-07-29T21:48:07+00:00` → `2026-07-30 05:48:07`; AP Meta earnings coverage also in-window. | New Q2 earnings / product-roadmap disclosure. Distinct from prior Meta Genesis Mission and glasses / AI optimism items. | https://www.theverge.com/tech/972294/meta-q2-2026-earnings-mark-zuckerberg-personal-ai-agents ; https://apnews.com/article/bcbc62dde6d2cac724e3b3385fcabeab |
| T4 | OpenAI ChatGPT for Academic Researchers | OpenAI official page dated July 29, 2026; no precise metadata found, represented as `2026-07-29T12:00:00Z` → `2026-07-29 20:00:00` date-level marker. Axios coverage in-window corroborates. | New official access program. Distinct from 2026-07-29 OpenAI scientific-computing field report and 2026-07-29 OpenAI / Hugging Face security update. | https://openai.com/index/chatgpt-for-academic-researchers/ ; https://www.axios.com/2026/07/29/openai-academics-research-chatgpt-sol |
| T5 | OpenAI GPT-5.6 efficiency disclosure | OpenAI official page dated July 29, 2026; no precise metadata found, represented as `2026-07-29T12:00:00Z` → `2026-07-29 20:00:00` date-level marker. | New efficiency / cost engineering disclosure. Does not duplicate the initial GPT-5.6 preview / launch captures because the new event is the July 29 efficiency post. | https://openai.com/index/gpt-5-6-frontier-intelligence-efficiency/ |
| T6 | OpenAI ARC-AGI-3 settings | OpenAI official page dated July 29, 2026; no precise metadata found, represented as `2026-07-29T12:00:00Z` → `2026-07-29 20:00:00` date-level marker. | New research / product-configuration guidance. Included because it affects API harness settings, retained reasoning and compaction, not just benchmark commentary. | https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/ |
| T7 | OpenAI hardware family roadmap | The Verge `datePublished=2026-07-29T18:15:02+00:00` → `2026-07-30 02:15:02`. | New product-roadmap interview. Lower certainty than official release, but prominent because it clarifies OpenAI device-surface direction. | https://www.theverge.com/ai-artificial-intelligence/972709/openai-hardware-greg-brockman-interview |

## Excluded or Lower-Priority Candidates

- **China Chongqing landslide death toll 41:** AP / ABC first reliable reporting identified as July 28 U.S. time, outside this exact window; not included even though some outlets republished or crawled it on July 29.
- **Uganda declares Ebola outbreak over:** AP / Al Jazeera reporting centered on July 28, outside the current window; not used to satisfy today's Ebola slot. Congo WFP warning was selected because AP published the warning inside the window and it materially changed the outbreak / hunger analysis.
- **Libya electricity blackout protests:** July 29 analytical reporting was reviewed, but core protest / storming events first appeared around July 28 and time basis was weaker than the selected Africa security / health items.
- **U.S. Senate / Fauci contempt live item:** AP live page contained a current political update, but it ranked lower than global war, market, disaster and governance developments selected today.
- **China overcapacity / tariffs:** Already captured 2026-07-29; no new enforcement action inside this window was strong enough to re-include.
- **Japan initial earthquake and France / Spain initial evacuation scale:** Not repeated as old events. Only the July 29 death toll, casualty-site detail, firefighter deaths and new AP / Guardian wildfire updates were used as continuation bases.
- **OpenAI Presence, prior GPT-5.6 preview and prior ChatGPT release-note items:** Excluded unless July 29 official pages introduced a new program, engineering disclosure or benchmark-setting note.
- **OpenAI Study Mode / other search-visible AI items without verifiable current official time:** Excluded where precise or date-level source basis could not be confirmed reliably within the 24-hour window.
- **Separate market selloff item:** Market reaction was folded into the Fed item to avoid overcounting one economic chain; AP market data is still preserved in both the report and source notes.

## Contradictions and Uncertainty Notes

- **U.S.-Iran / Iraq:** Sources differ on exact sequence, militia responsibility and some casualty details; AP and Al Jazeera were both retained rather than flattening the dispute.
- **Damietta vessel fires:** AP records the fires and uncertainty; attribution should not be treated as confirmed.
- **Fed / markets:** The Fed AP URL's `datePublished` was earlier than the final decision result, so the report uses the final-result `dateModified` and explicitly labels that choice.
- **Japan quake:** Mall explosion cause, missing-person count and final casualty totals remain provisional.
- **Europe wildfires:** Firefighter death count changed through live updates; AP / Guardian summaries point to three Greek firefighters across Crete and mainland, while some live snippets emphasized two deaths on Crete.
- **Congo Ebola:** Case counts in conflict areas may lag; WFP funding and access constraints can change quickly.
- **OpenAI official pages:** T4-T6 use date-level placeholders because second-level official metadata was not retrievable; source notes prevent treating these placeholders as exact publish times.
