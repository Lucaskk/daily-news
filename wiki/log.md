# Knowledge Base Log

## [2026-05-24] init | Knowledge base scaffold

- Created the initial raw/wiki/schema structure.
- Added operating rules in `AGENTS.md`.
- Added starter index, overview, principles, open questions, and templates.

## [2026-05-24] ingest | LLM Wiki

- Added a source summary for Karpathy's LLM Wiki gist.
- Linked the source to [[llm-wiki-principles]], [[overview]], and [[open-questions]].
- Updated `wiki/index.md`.

## [2026-05-24] automation | Daily global and tech AI news

- Created a recurring Codex automation to collect daily global/world news and technology/AI product news.
- Standardized daily output under `wiki/daily/YYYY/MM/YYYY-MM-DD/`.
- Added `wiki/templates/daily-news-report.md`.

## [2026-05-24] ingest | Daily global and tech AI news

- Manually ran the daily news workflow because the first scheduled run time had already passed.
- Created `wiki/daily/2026/05/2026-05-24/daily-news-2026-05-24.md`.
- Created `wiki/daily/2026/05/2026-05-24/source-notes-2026-05-24.md`.
- Updated `wiki/index.md`.

## [2026-05-24] update | Daily slide deck workflow

- Updated the recurring automation to create a web-based slide deck after each daily news run.
- Added `wiki/daily/2026/05/2026-05-24/slides-2026-05-24.html`.
- Added `wiki/daily/latest-slides.html` as the stable local entry point.
- Updated `AGENTS.md`, `README.md`, `wiki/templates/daily-news-report.md`, and `wiki/index.md`.
- Refined the automation to report a localhost slide URL after future runs.

## [2026-05-24] update | Slide source links

- Added visible bottom-left source URL hyperlinks to every slide in `slides-2026-05-24.html`.
- Updated `AGENTS.md` so future slide decks include per-slide source URL hyperlinks.

## [2026-05-24] update | Duplicate news rule

- Added a daily workflow rule to search prior `wiki/daily/` reports before selecting stories.
- Future daily runs should exclude previously captured stories unless there is a material new development.

## [2026-05-27] update | Slide source label style

- Updated existing daily slide decks so bottom-left source links display readable source/topic labels instead of raw URLs.
- Updated `AGENTS.md` and `wiki/templates/daily-news-report.md` so future slide decks use topic labels for clickable sources.

## [2026-05-25] ingest | Daily global and tech AI news

- Created `wiki/daily/2026/05/2026-05-25/daily-news-2026-05-25.md`.
- Created `wiki/daily/2026/05/2026-05-25/source-notes-2026-05-25.md`.
- Created `wiki/daily/2026/05/2026-05-25/slides-2026-05-25.html`.
- Updated `wiki/daily/latest-slides.html`, `wiki/index.md`, and `wiki/overview.md`.
- Excluded previously captured stories unless there was a material new development, and labeled continuations explicitly.

## [2026-05-26] ingest | Daily global and tech AI news

- Created `wiki/daily/2026/05/2026-05-26/daily-news-2026-05-26.md`.
- Created `wiki/daily/2026/05/2026-05-26/source-notes-2026-05-26.md`.
- Created `wiki/daily/2026/05/2026-05-26/slides-2026-05-26.html`.
- Updated `wiki/daily/latest-slides.html`, `wiki/index.md`, and `wiki/overview.md`.
- Excluded previously captured stories unless there was a material new development, and labeled continuations explicitly.

## [2026-05-28] ingest | Daily global and tech AI news

- Created `wiki/daily/2026/05/2026-05-28/daily-news-2026-05-28.md`.
- Created `wiki/daily/2026/05/2026-05-28/source-notes-2026-05-28.md`.
- Created `wiki/daily/2026/05/2026-05-28/slides-2026-05-28.html`.
- Updated `wiki/daily/latest-slides.html`, `wiki/index.md`, and `wiki/overview.md`.
- Excluded previously captured stories unless there was a material new development, and labeled continuations explicitly.

## [2026-05-29] update | LINE push setup

- Added local `.env` values for LINE push delivery; `.env` is ignored by git.
- Sent a successful LINE push test using `scripts/send_line_daily_slides.py`.
- Updated the recurring automation to push the public GitHub Pages latest-slides URL to LINE after daily publishing succeeds.
- Refined the automation to publish via GitHub connector when local git push credentials are unavailable.
- Updated the LINE push script to include the date and a concise subject in the message body.

## [2026-05-29] ingest | Daily global and tech AI news

- Created `wiki/daily/2026/05/2026-05-29/daily-news-2026-05-29.md`.
- Created `wiki/daily/2026/05/2026-05-29/source-notes-2026-05-29.md`.
- Created `wiki/daily/2026/05/2026-05-29/slides-2026-05-29.html`.
- Updated `wiki/daily/latest-slides.html`, `wiki/index.md`, and `wiki/overview.md`.
- Excluded previously captured stories unless there was a material new development, and labeled continuations explicitly.

## [2026-05-30] ingest | Daily global and tech AI news

- Created `wiki/daily/2026/05/2026-05-30/daily-news-2026-05-30.md`.
- Created `wiki/daily/2026/05/2026-05-30/source-notes-2026-05-30.md`.
- Created `wiki/daily/2026/05/2026-05-30/slides-2026-05-30.html`.
- Updated `wiki/daily/latest-slides.html`, `wiki/index.md`, and `wiki/overview.md`.
- Excluded previously captured stories unless there was a material new development, and labeled continuations explicitly.

## [2026-05-31] ingest | Daily global and tech AI news

- Created `wiki/daily/2026/05/2026-05-31/daily-news-2026-05-31.md`.
- Created `wiki/daily/2026/05/2026-05-31/source-notes-2026-05-31.md`.
- Created `wiki/daily/2026/05/2026-05-31/slides-2026-05-31.html`.
- Updated `wiki/daily/latest-slides.html`, `wiki/index.md`, and `wiki/overview.md`.
- Excluded previously captured stories unless there was a material new development, and labeled continuations explicitly.

## [2026-06-01] ingest | Daily global and tech AI news

- Created `wiki/daily/2026/06/2026-06-01/daily-news-2026-06-01.md`.
- Created `wiki/daily/2026/06/2026-06-01/source-notes-2026-06-01.md`.
- Created `wiki/daily/2026/06/2026-06-01/slides-2026-06-01.html`.
- Updated `wiki/daily/latest-slides.html`, `wiki/index.md`, and `wiki/overview.md`.
- Excluded previously captured stories unless there was a material new development, and labeled continuations explicitly.

## [2026-06-01] update | Daily global and tech AI news refresh

- Re-ranked the 2026-06-01 daily report using current web research later in the day.
- Replaced weaker continuation items with tariff-refund appeal, Shangri-La alliance signaling, Philippines-Vietnam strategic upgrade, and China patrols east of Taiwan.
- Refreshed `wiki/daily/2026/06/2026-06-01/daily-news-2026-06-01.md`, `source-notes-2026-06-01.md`, and `slides-2026-06-01.html`.
- Updated `wiki/index.md` and `wiki/overview.md` to match the refreshed synthesis.

## [2026-06-02] ingest | Daily global and tech AI news

- Created `wiki/daily/2026/06/2026-06-02/daily-news-2026-06-02.md`.
- Created `wiki/daily/2026/06/2026-06-02/source-notes-2026-06-02.md`.
- Created `wiki/daily/2026/06/2026-06-02/slides-2026-06-02.html`.
- Updated `wiki/daily/latest-slides.html`, `wiki/index.md`, and `wiki/overview.md`.
- Excluded previous daily-news duplicates unless there was a material new development, and labeled continuations explicitly.

## [2026-06-03] ingest | Daily global and tech AI news

- Created `wiki/daily/2026/06/2026-06-03/daily-news-2026-06-03.md`.
- Created `wiki/daily/2026/06/2026-06-03/source-notes-2026-06-03.md`.
- Created `wiki/daily/2026/06/2026-06-03/slides-2026-06-03.html`.
- Updated `wiki/daily/latest-slides.html`, `wiki/index.md`, and `wiki/overview.md`.
- Excluded previous daily-news duplicates unless there was a material new development, and labeled continuations explicitly.

## [2026-06-04] ingest | Daily global and tech AI news

- Created `wiki/daily/2026/06/2026-06-04/daily-news-2026-06-04.md`.
- Created `wiki/daily/2026/06/2026-06-04/source-notes-2026-06-04.md`.
- Created `wiki/daily/2026/06/2026-06-04/slides-2026-06-04.html`.
- Updated `wiki/daily/latest-slides.html`, `wiki/index.md`, and `wiki/overview.md`.
- Excluded previous daily-news duplicates unless there was a material new development, and labeled continuations explicitly.

## [2026-06-05] ingest | Daily global and tech AI news

- Created `wiki/daily/2026/06/2026-06-05/daily-news-2026-06-05.md`.
- Created `wiki/daily/2026/06/2026-06-05/source-notes-2026-06-05.md`.
- Created `wiki/daily/2026/06/2026-06-05/slides-2026-06-05.html`.
- Updated `wiki/daily/latest-slides.html`, `wiki/index.md`, and `wiki/overview.md`.
- Excluded previous daily-news duplicates unless there was a material new development, and labeled continuations explicitly.

## [2026-06-06] ingest | Daily global and tech AI news

- Created `wiki/daily/2026/06/2026-06-06/daily-news-2026-06-06.md`.
- Created `wiki/daily/2026/06/2026-06-06/source-notes-2026-06-06.md`.
- Created `wiki/daily/2026/06/2026-06-06/slides-2026-06-06.html`.
- Updated `wiki/daily/latest-slides.html`, `wiki/index.md`, and `wiki/overview.md`.
- Excluded previous daily-news duplicates unless there was a material new development, and labeled continuations explicitly.

## [2026-06-07] ingest | Daily global and tech AI news

- Created `wiki/daily/2026/06/2026-06-07/daily-news-2026-06-07.md`.
- Created `wiki/daily/2026/06/2026-06-07/source-notes-2026-06-07.md`.
- Created `wiki/daily/2026/06/2026-06-07/slides-2026-06-07.html`.
- Updated `wiki/daily/latest-slides.html`, `wiki/index.md`, and `wiki/overview.md`.
- Excluded previous daily-news duplicates unless there was a material new development, and labeled continuations explicitly.

## [2026-06-08] ingest | Daily global and tech AI news

- Created `wiki/daily/2026/06/2026-06-08/daily-news-2026-06-08.md`.
- Created `wiki/daily/2026/06/2026-06-08/source-notes-2026-06-08.md`.
- Created `wiki/daily/2026/06/2026-06-08/slides-2026-06-08.html`.
- Updated `wiki/daily/latest-slides.html`, `wiki/index.md`, and `wiki/overview.md`.
- Excluded previous daily-news duplicates unless there was a material new development, and labeled continuations explicitly.

## [2026-06-09] ingest | Daily global and tech AI news

- Created `wiki/daily/2026/06/2026-06-09/daily-news-2026-06-09.md`.
- Created `wiki/daily/2026/06/2026-06-09/source-notes-2026-06-09.md`.
- Created `wiki/daily/2026/06/2026-06-09/slides-2026-06-09.html`.
- Updated `wiki/daily/latest-slides.html`, `wiki/index.md`, and `wiki/overview.md`.
- Excluded previous daily-news duplicates unless there was a material new development, and labeled continuations explicitly.

## [2026-06-10] ingest | Daily global and tech AI news

- Created `wiki/daily/2026/06/2026-06-10/daily-news-2026-06-10.md`.
- Created `wiki/daily/2026/06/2026-06-10/source-notes-2026-06-10.md`.
- Created `wiki/daily/2026/06/2026-06-10/slides-2026-06-10.html`.
- Updated `wiki/daily/latest-slides.html`, `wiki/index.md`, and `wiki/overview.md`.
- Excluded previous daily-news duplicates unless there was a material new development, and labeled continuations explicitly.

## [2026-06-10] ingest | Daily global and tech AI news refresh

- Refreshed `wiki/daily/2026/06/2026-06-10/daily-news-2026-06-10.md` and `source-notes-2026-06-10.md` after later web research.
- Promoted Iran retaliatory attacks on U.S. bases / U.S.-linked regional facilities from unresolved risk to the top story.
- Added Somali World Cup referee Omar Artan's U.S. entry denial as a fresh World Cup governance story.
- Replaced weaker standalone Ukraine / fuel-price items with Xi-Kim nuclear-silence signaling and folded energy risk into the Iran escalation.
- Updated `slides-2026-06-10.html`, `wiki/index.md`, and `wiki/overview.md` to match the refreshed synthesis.

## [2026-06-10] maintenance | Stock analysis workflow

- Installed `chengwesley/taiwan-stock-analysis` as local Codex skill `taiwan-stock-analysis`.
- Added `scripts/generate_stock_analysis.py` to create Taiwan stock analysis HTML, JSON, and Markdown artifacts from public quote and financial-statement sources.
- Added `scripts/line_stock_webhook.py` so LINE stock requests can reply with one short analysis link instead of a long message body.
- Added `wiki/stocks/` index and latest-analysis entry point.
- Updated `README.md`, `DEPLOYMENT.md`, `.env.example`, `AGENTS.md`, and `wiki/index.md` for the stock analysis workflow.

## [2026-06-11] maintenance | Stock analysis workflow

- Moved Goodinfo financial-statement fetching out of Vercel and into the local Mac Python workflow.
- Added a GitHub-backed stock request queue, a 15-minute Mac scheduler, daily de-duplication, and GitHub API publishing.
- Added `wiki/stocks/pending.html` and per-stock stable redirects under `wiki/stocks/by-code/`.
- Kept the existing Vercel LINE webhook as the only public webhook; the Mac remains private and does not expose a local server.

## [2026-06-11] ingest | Daily global and tech AI news

- Created `wiki/daily/2026/06/2026-06-11/daily-news-2026-06-11.md`.
- Created `wiki/daily/2026/06/2026-06-11/source-notes-2026-06-11.md`.
- Selected exactly 10 global items after searching prior daily reports and source notes for duplicates.
- Labeled U.S.-Iran strikes and the U.S. immigration law as continuations with explicit material changes.
- Added official OpenAI, GitHub and Anthropic product changelog updates without repeating yesterday's model / Siri stories.
- Created `wiki/daily/2026/06/2026-06-11/slides-2026-06-11.html` and updated `wiki/daily/latest-slides.html`.
- Updated `wiki/index.md` and `wiki/overview.md`, then published the complete daily package to GitHub Pages.
- Served the deck locally on port 4175; LINE delivery was skipped because `.env` did not contain `LINE_TO_ID`.

## [2026-06-12] ingest | Daily global and tech AI news

- Created `wiki/daily/2026/06/2026-06-12/daily-news-2026-06-12.md` and `source-notes-2026-06-12.md` after current web research and archive deduplication.
- Selected exactly 10 global items; labeled the U.S.-Iran settlement claim as a continuation and documented the material change from active strikes to a declared pause.
- Added distinct technology / AI product coverage for Visa agentic payments, GitHub Agentic Workflows, Copilot CLI configuration, Claude Corps and IBM-ServiceNow enterprise AI.
- Created `wiki/daily/2026/06/2026-06-12/slides-2026-06-12.html` with 12 slides, readable source labels, keyboard controls and touch navigation.
- Updated `wiki/daily/latest-slides.html`, `wiki/index.md`, `wiki/overview.md` and the root GitHub Pages redirect.
- Published the daily package to GitHub Pages through the GitHub connector after local HTTPS push authentication failed.
- Served the deck locally on port 4174; LINE delivery was skipped because `.env` did not contain `LINE_TO_ID`.

## [2026-06-14] update | Clear Chinese headline summaries

- Rewrote the 2026-06-14 report and slide headlines as complete Traditional Chinese summary sentences rather than mixed-language keyword fragments.
- Translated country names, policy terms and explanatory card text while retaining official product and company names where needed.
- Moved slide content into a dedicated scroll area above the mobile source and navigation bars so fixed controls no longer cover news cards.

## [2026-06-14] update | Sources inside every expandable item

- Converted all remaining static news cards into expandable items, including overview, statistics, technology summary and follow-up cards.
- Removed every slide-level source footer and placed readable source labels plus full original URLs inside each item's expanded content.
- Added a single source mapping for all 49 expandable items and validated exact per-slide item/source alignment with no empty source groups.

## [2026-06-14] update | Expanded slide summaries

- Audited all 49 expandable items after a mobile screenshot showed that several summaries were too compressed.
- Added source-supported background, impact, key figures or uncertainty to every item instead of repeating the original sentence.
- Set a minimum of 80 non-whitespace characters for each news item's body before source links; the reported enriched-uranium item now explains the conflicting U.S. and Iranian proposals and sanction sequencing.

## [2026-06-14] maintenance | Daily-news deduplication rules

- Added `wiki/daily/README.md` as the central production rule file, including full-archive event-level deduplication and material-continuation criteria.
- Audited 16 daily reports from 2026-05-29 through 2026-06-14; recent reports had no unlabeled same-event repeats.
- Removed two legacy 2026-06-06 technology-list entries that had no new event, while preserving their sources and exclusion reasons in source notes.

## [2026-06-14] maintenance | 24-hour news window

- Required every selected event, official product release or material continuation update to fall within the 24 hours before the Asia/Taipei research cutoff.
- Required source notes to record the exact window and each item's event or publication-time basis.
- Prohibited using republished, retitled or still-trending older stories to fill the daily list.

## [2026-06-13] ingest | Daily global and tech AI news

- Created wiki/daily/2026/06/2026-06-13/daily-news-2026-06-13.md and source-notes-2026-06-13.md after current web research and archive deduplication.
- Selected exactly 10 global items; labeled the U.S.-Iran final-text claim as a continuation and preserved the conflicting U.S., Iranian and Israeli descriptions.
- Added distinct technology / AI coverage for ChatGPT memory controls, Codex Browser developer mode, Anthropic Public Record, TCS regulated-industry deployment and YouTube messaging.
- Created wiki/daily/2026/06/2026-06-13/slides-2026-06-13.html with 12 slides, readable source labels, keyboard controls and touch navigation.
- Updated wiki/daily/latest-slides.html, wiki/index.md, wiki/overview.md and the root GitHub Pages redirect.
- Published the daily package to GitHub Pages through the GitHub connector after local HTTPS push authentication failed.
- Served the deck locally on port 4174; LINE delivery was skipped because `.env` did not contain `LINE_TO_ID`.

## [2026-06-13] update | Mobile slide layout and expandable details

- Reworked the 2026-06-13 deck to detect narrow/coarse-pointer devices and apply a mobile-first layout with `100dvh`, safe-area spacing, larger typography, vertical content scrolling and centered navigation controls.
- Removed the floating source-link footer that covered mobile content.
- Converted all 52 news cards and ranked items into tap-to-expand details with fuller Traditional Chinese context and the original source URLs inside each expanded item.
- Updated keyboard and touch handling so interactive elements do not trigger slide navigation and vertical scrolling is not mistaken for a horizontal swipe.

## [2026-06-14] ingest | Daily global and tech AI news

- Created `wiki/daily/2026/06/2026-06-14/daily-news-2026-06-14.md` and `source-notes-2026-06-14.md` after current web research and archive deduplication.
- Selected exactly 10 global items; labeled the U.S.-Iran signing timeline as a continuation and preserved the conflict between U.S. / Pakistan and Iranian statements.
- Added technology / AI coverage for the Anthropic model shutdown, ChatGPT GPT-5.2 retirement, Copilot code review controls, Smartsheet MCP connectors and New York synthetic-performer disclosure law.
- Created `wiki/daily/2026/06/2026-06-14/slides-2026-06-14.html` with 13 responsive slides, expandable details, keyboard / touch navigation and a visible bottom-left source bar on every slide.
- Updated `wiki/daily/latest-slides.html`, `wiki/index.md`, `wiki/overview.md` and the root GitHub Pages redirect.
- Published the complete daily package to GitHub Pages through the GitHub connector after local HTTPS push authentication failed.
- Served the deck locally on port 4174; LINE delivery was skipped because `.env` did not contain `LINE_TO_ID`.
