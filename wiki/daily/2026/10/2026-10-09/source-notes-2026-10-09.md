# 2026-10-09 來源筆記

- 凍結截點：2026-10-09T08:00:37+08:00／2026-10-09T00:00:37Z。
- 全球24小時窗：2026-10-08 08:00:37 至2026-10-09 08:00:37 Asia/Taipei；UTC 10/8 00:00:37Z至10/9 00:00:37Z。
- 科技／AI 產品 14 日視窗：2026-09-25 08:00:37 至2026-10-09 08:00:37 Asia/Taipei；UTC 9/25 00:00:37Z至10/9 00:00:37Z。
- 模式legacy；status讀CSV12來源。scan於00:00:44–46 UTC執行，逐站原始取得與完整雜湊保存在私人快取，不加入Git。成功不等於完成查閱。
- 去重只比對9/25–10/8前14份日報；已重建同窗70列產品表，不讀完整歷史。

## 第一批候選與排除

- Amazon 10/8正式推出Alexa Tablet新系列，非Surface或舊Fire評測；官方 https://www.aboutamazon.com/news/devices/new-amazon-alexa-tablets-alexa-plus 。美加墨10/14出貨，預購與到貨分開。
- Google Gemini agent 10/8官方新通用企業代理公告 https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/gemini-at-work/ ，深入核對 https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026 。不重刊2025 Enterprise或2026/4 Agent Platform。
- INSIDE 10/8 Markdown文章 https://www.inside.com.tw/article/42582-google-drive-docs-native-markdown-files-preview-edit-collaborate ，指向Google10/5原生.md編輯推出，非2024匯入／匯出。官方web讀取失敗待urllib補查。
- Engadget 10/8 Safety Signal停用 https://www.engadget.com/2281591/google-is-doing-away-with-safety-signal-on-pixel-watch/ ，官方支援頁 https://support.google.com/googlepixelwatch/thread/471984501/end-of-support-for-safety-signal-on-google-pixel-watch-is-going-away?hl=en ，只取得殼頁，公告日期未確認，未採。修正先前暫記的錯誤文章編號。
- Razer Basilisk V4媒體10/8說新推出，但官方newsroom索引出現9/24線索，日期有疑問；先不採，不能以評測日期替代推出。
- lookup `Amazon.*Alexa Tablet|Gemini.*(universal agent|通用代理)|Drive.*Markdown|Markdown.*Docs|Safety Signal|Basilisk.*V4` 前14報無命中；下一步核對同窗表，未查更早資料。
- 全球候選：10/8烏克蘭巴士攻擊、Microsoft綠卡程序暫停、Isaias升級、文學獎、伊斯坦堡倒塌、緬甸正式會談、英國領事館降級、Crew12實際濺落。
- 排除：Serbia海外投票規則AP原始10/6、10/8 spotlight重刊不算新；WWF全球報告官方10/7已發布，10/8日本版不能冒充首次；西班牙Maricarmen死亡10/7 19:18Z在全球窗外，不採死亡舊聞。
- 初查世界命中9/28、10/4西班牙示威，10/8敏昂萊抵達；緬甸若採10/8會談需標續報。

## 逐站查閱與補查

scan成功8站、HTTPError4站；失敗不代表沒有新聞。成功站完整SHA256及原始HTML保存私人scan證據，未將私人路徑入庫。以下是實際本輪檢視範圍，不宣稱已窮盡所有文章。

|來源|scan／補查|文章、發布日期與決定|
|---|---|---|
|Engadget|取得，86b932c7；首頁及原文|https://www.engadget.com/2280917/amazon-alexa-tablets-october-2026/ ，10/8，新平板線索回查Amazon採T1；https://www.engadget.com/2280787/amazon-alexa-tablet-12-pro-hands-on/ 同事件評測不另列；Safety Signal如上待確認，不採|
|The Verge|取得，1f8e4665，快取截斷；web首頁補足|https://www.theverge.com/tech/1008422/apple-macbook-pro-touchscreen-ipad-mini-rumor ，10/8傳聞，不是正式發布；首頁Alexa Tablet評測回查Amazon，與T1同事件不另列|
|TechCrunch|取得，19cdeacc；首頁與原文|https://techcrunch.com/2026/10/08/amazon-unveils-new-alexa-tablets-with-alexa-and-google-play-store-access/ ，10/8 06:00 PDT，採官方為主；https://techcrunch.com/2026/10/08/popular-ai-leaderboard-arena-nearly-doubles-valuation-to-3-1b-valuation-in-10-months/ ，10/8融資估值而非产品變更，不採|
|WIRED|取得，c560636b；首頁與原文|https://www.wired.com/story/amazon-alexa-tablets-2026/ ，10/8，新品線索回查官方，與T1合併；Prime Day導購不獨立列新聞|
|Ars Technica|取得，a354a0d9；首頁與原文|https://arstechnica.com/gadgets/2026/10/amazons-new-alexa-tablets-drop-the-fire-branding-but-are-more-android-than-ever/ ，10/8，同T1；首頁科學研究與遊說政治不是產品發布|
|Cool3c|scan HTTPError，web首頁與逐站搜尋補查|https://www.cool3c.com/article/252801 ，10/8 15:51，Sigma新品回查10/8官方公告採T4；https://www.cool3c.com/article/252754 ，10/6 Wolverine V4，未列本日優先清單；首頁Claw CG3M新型號線索需官方首次日期，未採；Osmo Action 6首頁明載去年11月推出，今日折扣排除|
|Yahoo奇摩科技|取得6de8ed04但科技頁混入政治；web分類／RSS失敗，逐站搜尋補查|https://tw.news.yahoo.com/gemini%E8%A6%81%E7%B8%AE%E6%B0%B4%E4%BA%86-%E5%8A%9F%E8%83%BD%E5%A4%A7%E7%A0%8D-%E4%BB%98%E8%B2%BB-%E5%85%8D%E8%B2%BB%E9%83%BD%E5%8F%97%E5%BD%B1%E9%9F%BF-231300033.html/ ，10/5 19:13，Gemini模型權限，lookup命中10/7，排除重複；搜尋索引亦返回春季舊頁，不能当今日新聞|
|TechOrange|scan HTTPError，web首頁／逐站原文補查，原文後續urllib403|https://techorange.com/2026/10/08/artcraft-software-ai-developer-adobe/ ，10/8，回查 https://github.com/storytold/artcraft/releases 最新v0.41.0為9/26，發布說明只寫下載，無法證明媒體所述七套替代工具是這次獨立重大更新，不採該主張；不是因403宣稱沒有新品|
|數位時代|取得a6d65611，web錯誤，以快取及逐站搜尋補查|https://fc.bnext.com.tw/articles/view/4622 ，10/8，Haiku方案比較，模型推出已10/8日報收錄，排除；Meetings 10/8教學線索回查官方release notes，實際首次為9/29，不能當10/8新品，本輪不採；媒體原文完整URL未取得，保留限制|
|TechNews|取得1f7fffcb，web首頁錯誤，以逐站原文補查|https://technews.tw/2026/10/09/google-introduces-the-gemini-agent/ ，10/9 01:59，回查Google採T2；不由媒體時間推論所有功能全面可用|
|openai.com|scan HTTPError，官方help release notes補查成功|https://help.openai.com/en/articles/6825453-chatgpt-release-notes October 8 Faster steering in Codex採T5；October 7 Intelligent UI已10/8收錄，不重列；September29 Meetings是舊發布，不因教學文章重新發布|
|INSIDE|scan HTTPError，以逐站原文／官方補查|https://www.inside.com.tw/article/42582-google-drive-docs-native-markdown-files-preview-edit-collaborate ，10/8，官方10/5原生Markdown採T3；首頁Haiku新介紹為10/7推出且10/8已收錄，不重列|

## 官方定向補查與科技去重結果

完成一輪硬體Amazon／Sigma、企業AI Google、消費文件Workspace、開發工具OpenAI release notes定向查詢。採5則，不為湊10則加入未確認上市日期、新聞評論或重複功能。

- T1–T3窄查：`Amazon.*Alexa Tablet|Gemini.*(universal agent|通用代理)|Drive.*Markdown|Markdown.*Docs`，前14報無命中，讀取同窗70列表第二次確認，無同事件。T1官方首次12:55:12.507Z；T2Google Blog10/8日期、Cloud metadata10/9 03:00:11+0800（首次追蹤欄03:10），都在科技窗；T3官方10/5及Rollout pace原文列兩軌自10/5漸進最多15天、Workspace與個人皆適用。
- T4、T5窄查：`Codex.*(steer|引導|干預|跟進)|Meetings|Sigma.*50.?120`，前14報無命中，核對同窗產品表；採Sigma 10/8發布及10/22上市段，Codex October8 Faster steering段。Meetings不採作10/8新品。
- Yahoo候選查`Gemini.*(Flash.Lite|權限|縮水)`命中10/7 T7，排除。ArtCraft查名無命中，但發布說明不足支撐七工具變更，仍排除。無命中不是自動通過查證。
- Basilisk V4：媒體10/8與官方newsroom搜尋結果9/4等日期不一致，原始公告時間未釐清，暫不採，撤回第一批9/24暫定線索作確定日期的可能誤解。

## 全球時間與去重依據

所有來源URL與標題見日報逐項來源。AP搜尋/原頁當日報導先前已讀，後續urllib原文及og圖片檢查403；不是將存取失敗誤判無新聞。

|項目|事件／首次可靠時間基準（UTC及台灣）|去重決定與限制|
|---|---|---|
|1 烏克蘭巴士|10/8新攻擊；AP07:49:30Z＝15:49:30台灣|10/8日報為10/7基輔空襲，標續報，新增地點與攻擊。AP30人；其他Reuters引述出現33，數字時點未完全對齊，不覆蓋|
|2 美國綠卡|10/8政府措施；AP14:34:35Z＝22:34:35|前14報查綠卡／green card無命中；PERM不是所有H-1B取消；行政指控不是定罪|
|3 文學獎|瑞典學院10/8結果及加拿大官方10/8祝賀|Carson无命中；AP06:47:28Z頁面早於頒獎常規時刻，不拿它作結果宣布時刻；保留日期，官方頁無秒數|
|4 Isaias|10/8升級／撤離；AP05:37:27Z＝13:37:27|無命中；滾動首刊不是升級精確時刻，仍為10/8事件，登陸預報不寫已發生|
|5 英領事機構|AP10/8滾動頁07:57Z＝15:57；定位英國機構降級段|前14報無命中；保留英方仍運作與以方終止領事館的差異|
|6 緬甸會談|10/8正式會談；AP06:27:15Z＝14:27:15|命中10/8抵達；標續報，新增會談，先前遣返批次只作背景|
|7 法國學生|10/8封校／警方處置；AP09:16:51Z＝17:16:51|命中10/2學生抗議及危機會議；標續報，新增學校處置及集會；累計逮捕不作當日數字|
|8 英德會談|Euronews首次10:22:46+02＝08:22:46Z＝16:22:46台灣|Burnham／柏林資安無命中；條約預期程序不写已批准|
|9 伊斯坦堡|10/8黎明前倒塌；AP07:05:50Z＝15:05:50|Maltepe無命中；原因未定，不歸因地震|
|10 Crew-12|事件10/8 15:34Z＝23:34；NASA即時博客15:36Z＝23:36|Crew12無命中；新聞稿17:02:28Z較晚，不取代即時博客首次發布；237在軌天數與ISS235不同範圍|

世界查詢：`Burnham|柏林.*資安|Isaias|Carson|Maltepe|Crew.?12|綠卡|green card|東耶路撒冷.*(降級|關閉)|Jerusalem.*consulate`無命中；`敏昂|緬甸.*馬來|法國.*學生|克拉馬托|Kramatorsk|烏克蘭.*(電力|空襲)`命中上述三則續報。範圍固定9/25–10/8日報，未查歷史來源筆記。

## 逐項原文／og:image稽核

本輪使用原頁HTML parser檢查meta及img。已下載圖逐張視覺核對；素材不是產品實測或第三方效能驗證。原圖完整網址與權利記於presentation JSON；未取得授權與原文沒有圖分開。

|項目|實際查證|使用決定|
|---|---|---|
|T1|Amazon200，og為平板正面，正文三尺寸圖|採正文原圖 https://assets.aboutamazon.com/ad/13/d5df01dc4dc7916815e964d079f1/amazonalexatablets-inline-amazonnews-ck10726.png ，Amazon官方新聞素材，權利歸Amazon，不宣稱自由授權|
|T2|Cloud200，og https://storage.googleapis.com/gweb-cloudblog-publish/images/image_3.max-2100x2100_0CYZWqn.jpg ，正文有標誌、影片縮圖|未採圖；存在官方社群預覽但未確認它代表新代理操作介面，不冒充實際介面|
|T3|Workspace200，正文與og有Markdown功能PNG示意，非無圖|本輪未下載，保留官方原文連結；非存取失敗，非原文無圖|
|T4|Sigma200，og僅通用品牌 https://www.sigma-global.com/assets/og_image.jpg ；正文當款產品照|採正文 https://www.sigma-global.com/jp/news/images/01_PPhoto_50_120_28_dc_os_026_Emt_representative.jpg ，Sigma官方新聞素材，附出處|
|T5|help原頁urllib403，web取得當日文字但無可確認當項配圖|來源圖片存取受限，不以其他Codex舊UI替代|
|1|AP原文圖片/og擷取403；先前web有救援事件圖線索|未取得可用原圖及再利用授權，不使用，非原文無圖|
|2|AP原文/og403；web原文有當日記者會及Nadella資料照|未取得再利用授權，不以資料照冒充當日事件|
|3|瑞典學院200，有Niklas Elmehed插畫及肖像；og https://www.svenskaakademien.se/og/896852bb-5479-40ba-8996-b19cf0bbc7a0.jpg|圖存在，未确认當次再利用條件，本輪不下載；不是原文無圖|
|4|AP原文/og403；web有衛星圖線索|無原圖可核對其拍攝時點及權利，本輪不使用|
|5|AP原文/og403；web原文有領事館標誌拆除事件圖|AP圖片權利未取得，不使用|
|6|AP原文/og403；web有10/8歡迎活動照片|未取得可用原圖及授權，不使用，非沒有配圖|
|7|AP原文/og403；web有巴黎抗議圖|授權未取得不使用，非原文無圖|
|8|Euronews200，正文及og https://images.euronews.com/articles/stories/09/94/39/14/1200x675_cmsv2_a17f5f2c-c642-5a7b-b73c-7cd9fbb425d4-9943914.jpg |有訪問圖，第三方新聞照片權利未取得，不使用|
|9|AP原文/og403；web有Abdullah Tepeli／DIA via AP救援圖|未取得原始圖網址及權利，不使用|
|10|NASA200，正文及og https://www.nasa.gov/wp-content/uploads/2026/10/crew12splashdown1.jpg ，NASA/Keegan Barber|採10/8當日濺落圖，NASA媒體使用指引 https://www.nasa.gov/nasa-brand-center/images-and-media/ ，非替NASA代言|
