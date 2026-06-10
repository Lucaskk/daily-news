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
