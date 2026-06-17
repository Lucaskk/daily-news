# 2026-06-17 來源與去重筆記

## 研究時間窗

- Asia/Taipei 研究截點：`2026-06-17 08:00:52 +08:00`
- UTC 研究截點：`2026-06-17T00:00:52Z`
- 24 小時窗起點：`2026-06-16 08:00:52 +08:00`（`2026-06-16T00:00:52Z`）
- 24 小時窗終點：`2026-06-17 08:00:52 +08:00`（`2026-06-17T00:00:52Z`）
- 收錄原則：事件、官方發布或重大新進展必須在上述 24 小時窗內發生或首次可靠發布；文章更新、首頁延續曝光或重寫標題不單獨構成新事件。
- 跨日去重範圍：搜尋 `wiki/daily/` 下全部 `daily-news-*.md` 與 `source-notes-*.md`，特別比對 2026-06-11 至 2026-06-16 的 Iran / G7 / Ukraine / UK-Russia / GitHub / OpenAI / SpaceX / Cursor / Android 主線。

## 全球新聞來源帳本

| # | 項目 | 事件／發布時間依據 | 去重與續報判定 | 原始來源 |
|---|---|---|---|---|
| 1 | Iran 要求 Israel 撤出 Lebanon 作為和平條件 | AP JSON-LD `datePublished=2026-06-16T07:43:20Z`；Guardian `datePublished=2026-06-16T17:22:13Z`。 | **續報，前次 2026-06-15、2026-06-16。** 前次收錄美伊協議與以色列反彈；今日新增 Iran top diplomat 將 Israel withdrawal 作為條件，且 Trump 批評 Israel。 | https://apnews.com/article/iran-us-war-israel-lebanon-oil-june-16-2026-d79458506c46e3f4a78aef0f9d8b9250；https://www.theguardian.com/world/2026/jun/16/irans-top-envoy-says-peace-deal-with-the-us-dependent-on-israels-withdrawal-from-lebanon |
| 2 | G7 / Ukraine / Russian oil sanctions | AP JSON-LD `datePublished=2026-06-16T04:05:32Z`；Guardian live metadata `2026-06-16T15:00:45Z`。 | **續報，前次 2026-06-16。** 前次是 G7 開幕與美伊協議議程；今日新增 full-day Ukraine focus、Trump 對俄油制裁訊號、Zelenskyy 防空與 Patriot 要求。 | https://apnews.com/article/g7-iran-ukraine-trump-macron-zelenskyy-e7fad4eabaae8181f70fa5a0b9e499b2；https://www.theguardian.com/world/live/2026/jun/16/g7-world-leaders-ukraine-russia-war-iran-trump-zelenskyy-putin-eu-france-eu-europe-latest-news-updates |
| 3 | European Parliament 批准 Trump tariff deal | Guardian JSON-LD `datePublished=2026-06-16T16:00:27Z`。 | 未在既有日報找到 European Parliament 正式批准此 tariff deal；2026-06-13 的 worldwide tariffs court story 是不同法律節點。 | https://www.theguardian.com/world/2026/jun/16/european-parliament-finally-approves-trump-tariff-deal |
| 4 | Russian frigate 對 British yacht 開警告火 | Guardian 頁面顯示 first published `Tue 16 Jun 2026 16.34 BST`（`2026-06-16T15:34:00Z`）；JSON-LD `datePublished=2026-06-16T21:13:40Z`。 | **續報，前次 2026-06-15。** 前次是 UK / France 扣押 Russian shadow-fleet tanker Smyrtos；今日是 Russian warship 對 civilian yacht warning shots，屬新海上安全事件。 | https://www.theguardian.com/uk-news/2026/jun/16/russian-frigate-fires-warning-shots-at-british-yacht-in-channel-reports |
| 5 | B-52 crash kills 8 | Al Jazeera JSON-LD `datePublished=2026-06-16T08:32:45Z`；AP JSON-LD `datePublished=2026-06-16T18:56:48Z`。 | 未在既有 daily 找到同一 B-52 crash；屬新軍機事故。 | https://www.aljazeera.com/news/2026/6/16/us-b-52-bomber-crashes-in-california-what-we-know；https://apnews.com/article/b52-stratofortress-crash-california-2cf849e75640a2e0b98ab94cc4a14430 |
| 6 | FBI disrupts White House UFC attack plan | AP JSON-LD `datePublished=2026-06-16T12:00:47Z`。 | 未在既有 daily 找到同一 White House UFC attack plot；屬新執法與公共安全事件。 | https://apnews.com/article/fbi-trump-ufc-white-house-b6a41e2e8fc7feb84440581c2535b000 |
| 7 | Eduardo Bolsonaro sentenced | Guardian JSON-LD `datePublished=2026-06-16T21:44:54Z`。 | 既有 daily 曾收錄 Jair Bolsonaro / Brazil coup trial 主線背景，但未收錄 Eduardo Bolsonaro 此次判刑；屬新司法節點。 | https://www.theguardian.com/world/2026/jun/16/brazilian-court-convicts-eduardo-bolsonaro-us-help-father-jair |
| 8 | Sweden immigration crackdown laws | Guardian JSON-LD `datePublished=2026-06-16T04:00:44Z`。 | 未在既有 daily 找到 Sweden good-behaviour / snitch law vote；屬新政策節點。 | https://www.theguardian.com/world/2026/jun/16/sweden-votes-to-back-laws-reinforcing-its-immigration-crackdown |
| 9 | Sri Lanka cybercrime relocation | Guardian JSON-LD `datePublished=2026-06-16T00:27:46Z`，在本窗起點後約 27 分鐘。 | 未在既有 daily 找到 Sri Lanka scam-network relocation；屬新調查／趨勢發布。 | https://www.theguardian.com/world/2026/jun/16/sri-lanka-alarming-rise-cybercrime-scam-networks-south-east-asia-cambodia-myanmar-china |
| 10 | EU-UK post-Brexit reset summit | Guardian JSON-LD `datePublished=2026-06-16T17:02:33Z`。 | 既有 daily 有 UK / EU 個別政策事件，但未收錄 7 月 Brussels reset summit announcement；屬新外交程序節點。 | https://www.theguardian.com/world/2026/jun/16/eu-uk-announce-summit-reset-post-brexit-relations |

## 科技／AI 來源帳本

| # | 項目 | 事件／發布時間依據 | 去重與續報判定 | 原始來源 |
|---|---|---|---|---|
| 1 | SpaceX acquires Cursor | TechCrunch JSON-LD `datePublished=2026-06-16T11:21:41Z`；多家商業／科技 outlet 同日追蹤。 | 2026-06-13 曾收錄 SpaceX IPO，不含 Cursor acquisition；屬 IPO 後新 M&A 節點。 | https://techcrunch.com/2026/06/16/spacex-to-acquire-cursor-for-60b-in-stock-days-after-blockbuster-ipo/ |
| 2 | Android 17 rollout and Gemini features | Google official page `datePublished=2026-06-16T18:00:00+00:00`；TechCrunch 同日 `2026-06-16T18:00:00+00:00`。 | 未在既有 daily 找到 Android 17 final rollout；I/O preview 與此正式 rollout 不同。 | https://blog.google/products-and-platforms/platforms/android/android-17-features/；https://techcrunch.com/2026/06/16/android-17-launches-with-new-multitasking-tools-as-google-expands-gemini-features/ |
| 3 | GitHub Code Quality GA and billing | GitHub Changelog official date `2026-06-16`，頁面未公開精確首發時間；日報採 `2026-06-16 12:00:00 +08` 作日期錨點並明確標註限制。 | 未在既有 daily 找到 Code Quality GA / pricing item；與 2026-06-14 Copilot code review controls 不同。 | https://github.blog/changelog/2026-06-16-github-code-quality-generally-available-july-20-2026 |
| 4 | GitHub Models unavailable to new customers | GitHub Changelog official date `2026-06-16`，頁面未公開精確首發時間；日報採 `2026-06-16 12:00:00 +08` 作日期錨點並明確標註限制。 | 未在既有 daily 找到 GitHub Models retirement path；屬 AI platform access 退場節點。 | https://github.blog/changelog/2026-06-16-github-models-is-no-longer-available-to-new-customers/ |
| 5 | Mobileye US robotaxi operator launch | TechCrunch JSON-LD `datePublished=2026-06-16T17:50:23Z`。 | 未在既有 daily 找到 Mobileye 自營 robotaxi service；屬 autonomous vehicle product / business-model shift。 | https://techcrunch.com/2026/06/16/mobileye-us-robotaxi-launch-will-put-it-on-both-sides-of-the-av-business/ |

## 官方產品頁稽核與排除

- OpenAI to acquire Ona：OpenAI official page / search result顯示已於約 5 天前發布，落在本窗外；不納入。https://openai.com/index/openai-to-acquire-ona/
- ChatGPT Go worldwide：官方與媒體資料顯示為 2026-01-16 附近發布，非本窗新事件；不納入。https://openai.com/index/introducing-chatgpt-go/
- OpenAI Deployment Simulation：官方為 `Research Jun 16, 2026`，屬研究方法發布而非主要產品／平台 release；本日科技欄優先收錄 Android 17、GitHub platform changes、SpaceX-Cursor 與 Mobileye。
- Probably raises $9M：TechCrunch 發布 `2026-06-16T13:15:09Z`，符合時間窗，但影響範圍與全球討論度低於 SpaceX-Cursor、Android、GitHub 與 Mobileye；列為候補。
- India temporary Telegram ban：TechCrunch 發布 `2026-06-16T15:49:00Z`，符合時間窗但屬平台監管／政策事件，未高於本日 5 則科技產品與平台變更。
- xAI gas-turbine lawsuit / DOJ position：TechCrunch 發布 `2026-06-16T15:05:03Z`，屬 AI infrastructure 法律／環境爭議，非產品 release；列為追蹤背景。

## 排除與避免重複

- 美伊協議本身、G7 開幕、油價重定價、以色列國內反彈已於 2026-06-15 或 2026-06-16 收錄；本日只保留 Iran withdrawal condition 與 G7 / Russian oil sanctions 等新節點。
- UK / France 扣押 Smyrtos 已於 2026-06-15 收錄；本日 Russian frigate warning shots 是不同事件，已標明續報與新事實。
- Delhi strong protest / Indian seafarers deaths、Global Witness DRC coltan investigation、US diplomat found dead in Myanmar、US lawmakers Afghan-to-DRC letter均為本窗外首發或已在前日主線中處理，未納入。
- Fox-Roku、Facebook AI Mode、Sarvam、NewCore、GitHub Copilot usage metrics 已於 2026-06-16 收錄；本日不重複。
- OpenAI Ona、ChatGPT Go、ChatGPT release notes 舊條目、Google I/O 2026 preview均因本窗外或非正式新發布排除。

## 交叉來源與顯著度訊號

- AP World top stories 在研究時段列出 Iran deal / G7 / Russian oil sanctions 為主要 world stories。https://apnews.com/world-news
- AP homepage most-read 在研究時段列出 initial Iran deal、B-52 crash 等為高讀取項。https://apnews.com/
- The Guardian World page 在研究時段列出 Russian frigate、Bolsonaro、Sweden immigration、EU-UK summit、Sri Lanka cybercrime 等同日重點。https://www.theguardian.com/world
- TechCrunch 同日 AI / transport / developer-platform headlines 顯示 SpaceX-Cursor、Android 17、Mobileye、GitHub / AI platform changes 為科技討論主線。https://techcrunch.com/

## 主要不確定性

- 美伊 MOU 未公開，Iran / Israel / White House 對 Lebanon 條款的版本仍可能衝突。
- G7 對 Ukraine 的承諾仍需 summit statement、sanctions orders 與 defense production commitments 驗證。
- Russian frigate warning-shot incident 的距離、通訊與碰撞風險存在 Russian account 與 yacht passengers account 的矛盾。
- B-52 crash 原因、機組與任務細節仍待官方調查。
- SpaceX-Cursor、Mobileye robotaxi 與 GitHub Code Quality billing 將分別面臨監管、營運與企業成本實測。
