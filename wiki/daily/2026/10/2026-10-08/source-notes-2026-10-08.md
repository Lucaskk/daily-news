# 2026-10-08 來源筆記

- 凍結研究截點：2026-10-08T08:02:01+08:00；可讀截點：2026-10-08 08:02:01（Asia/Taipei）；UTC 2026-10-08T00:02:01Z。
- 全球 24 小時窗：2026-10-07 08:02:01 至 2026-10-08 08:02:01 Asia/Taipei；UTC 2026-10-07T00:02:01Z 至 2026-10-08T00:02:01Z。
- 科技／AI 產品 14 日視窗：2026-09-24 08:02:01 至 2026-10-08 08:02:01 Asia/Taipei；UTC 2026-09-24T00:02:01Z 至 2026-10-08T00:02:01Z。
- 研究模式 legacy；去重僅 2026-09-24 至 2026-10-07 的 14 份日報，當日與更早檔案、來源筆記及完整歷史表不參與比對。同窗表 65 列。
- scan 實際執行 2026-10-08T00:02:11 至 00:02:13 UTC，12 站；原始內容保存於私人快取，不加入 Git。取得時間不等於發布時間。

## 研究進度

### 第一批官方核對與去重

- T1 ChatGPT Intelligent UI：官方 2026-10-07 公告與 release notes 的當日段落；Plus／Pro／Business／Enterprise 開始推出，Free／Go 為翌日。https://openai.com/index/gpt-6-for-everyone/ 、https://help.openai.com/en/articles/6825453-chatgpt-release-notes 。僅日期，不虛構時刻。
- T2 Haiku 5.5：官方新聞索引 2026-10-07；公告頁存取失敗，使用官方產品頁及模型文件補查。https://www.anthropic.com/claude/haiku 、https://platform.claude.com/docs/en/models/haiku-5-5/overview 。產品頁舊標題仍寫 Haiku 4.5，正文為 5.5，保留此頁面不一致。
- T3 Surface：2026-10-07 新增預購，不把 Computex 預告當新品。Ultra 起價 US$2,599、10/16 出貨；Dev Box US$5,999、美國首波、11 月供貨。https://blogs.windows.com/devices/2026/10/07/pre-order-our-most-powerful-surface-devices-ever/ 。商務通路配置價格不同，不能視為全球統一定價。
- T4 Windows MXC：官方 2026-10-07 段落明載 generally available；Copilot 未來代理體驗與尚未整合工具不混作已可用。https://blogs.windows.com/windowsexperience/2026/10/07/building-windows-for-hybrid-intelligence/ 。
- T5 SynthID Detector：官方 2026-10-07 向全球開放英文網站；先前限定測試與 9/26 Live Avatar 水印是不同事件。Apple 支援仍為 soon，未檢出水印不代表真人製作。https://blog.google/innovation-and-ai/models-and-research/google-deepmind/synth-id-ai-content/ 。媒體內文星期與官方日期不一致時採官方日期。
- T6 Playground：官方 2026-10-07 實驗產品公告，美國 18 歲以上；Unity Spark 為後續測試，不是今日全面整合。https://blog.google/innovation-and-ai/technology/ai/playground-experimental-gaming-platform/ 。
- T7 XREAL AURA：公司新聞稿首次 2026-10-07 08:00 ET，即 20:00 Asia/Taipei／12:00 UTC。256GB US$1,279、512GB US$1,499，先讓付費預約者購買，首波美國／加拿大／日本／韓國；公開購買為未來數週。https://www.prnewswire.com/news-releases/xreal-aura-starts-at-1-279--bringing-wired-xr-glasses-with-android-xr-to-customers-this-year-302900445.html 。產品頁 FAQ 舊市場列表與新新聞稿不同，以有日期的首波公告為準；不宣稱已普遍出貨。
- T8 Webex Dialog：Cisco 2026-10-07 公布具體路線，beta 預計 2027 日曆年第 1 季；不是正式上市。https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2026/m10/cisco-unveils-new-agentic-collaboration-experiences.html 。
- 窄化 lookup：`OpenAI.*GPT.?6.*(Intelligent|UI)|ChatGPT.*(Intelligent UI|智慧介面)|Haiku.?5[.]5|Surface.*(Ultra|Dev Box)|Windows.*(Execution Containers|MXC)|SynthID.*Detector|Google.*Playground|XREAL.*(Aura|AURA)|Webex.*Dialog`。前 14 日報無命中，才完整核對同窗 65 列 recent-14d 表；八項均無同一產品變更，保留。未讀完整歷史表。
- 廣泛世界 lookup 命中 10/4 胡塞 Aramco 攻擊、10/6 曼德海峽戰況及紐約麻疹緊急狀態；今天機場攻擊與賓州新增統計須標續報。沖繩會面、化學獎、伊茲米爾轉黨、緬甸訪馬、斯里蘭卡拘留、教宗會議與波蘭學校攻擊查無同事件。

### scan 結果

- 成功：Engadget `90b9cabb`、The Verge `278f5677`、TechCrunch `29cd7814`、WIRED `aec15cb3`、Ars `3e9cb61c`、Yahoo `11cd3172`、Bnext `736182d8`、TechNews `5ba812bb`（SHA-256 前八碼，完整雜湊保存在私人證據）。
- scan 失敗：Cool3c、TechOrange、OpenAI、INSIDE；已改用 web 首頁／逐站文章與官方更新頁補查。Bnext／Yahoo／TechNews 的 web 讀取另有失敗，不能以此否定 scan 取得內容。
- Bnext scan 最新包括 Claude Code Mods 教學、Cowork 雲端改制、Muse 評測、YouTube 商務消息；Cowork 10/6 改制已收錄 10/7，評測需回查官方發布，不直接認定新品。CDN TechNews 年份頁實際是 7/29 舊頁，不能作今日最新證據，改用 scan 最新文章及逐站搜尋。

- 已逐站開啟 Engadget、The Verge、TechCrunch、WIRED、Ars Technica、Cool3c、TechOrange、INSIDE；Yahoo／Bnext／TechNews web 存取失敗，正在逐站搜尋補查。
- 官方回查：Microsoft 10/7 開放 Surface Laptop Ultra 與 Dev Box 預購；Windows MXC 一般可用，其他代理功能須區分未來推出。Google 10/7 向全球開放 SynthID 英文網站，Apple 支援仍標示 soon；Playground 首波僅美國 18+，Unity Spark 尚在測試。
- 全球候選：10/7 烏克蘭新空襲、化學獎、斯里蘭卡前第一夫人拘留、胡塞新攻擊；昨天黑海油輪及肯亞首例不因重刊再次收錄。

## 逐站文章補查與選題結果

日期只記來源能確認的精度；首頁相對時間不轉成虛構的發布時刻。下列為實際檢查的候選，不宣稱全站僅有這些合格新聞。

|來源|實際文章、發布依據|決定|
|---|---|---|
|Engadget|https://www.engadget.com/2279565/google-synth-id-detector-ai-detection-website-is-now-available/ 、https://www.engadget.com/2279750/googles-experimental-playground-platform-uses-ai-to-create-games-for-you/ 、https://www.engadget.com/2279737/xreals-aura-android-xr-smartglasses-will-cost-you-at-least-1279/ ：10/7 最新文章|官方回查後採 T5、T6、T7；Cisco https://www.engadget.com/2278872/cisco-is-bringing-a-new-agentic-framework-to-its-webex-enterprise-platform/ 回查 T8。其他裝置線索未全數驗證，不稱不合格。|
|The Verge|https://www.theverge.com/news/1006378/microsoft-surface-laptop-ultra-pricing-release-date ：10/7 17:48 UTC|回查官方預購變更，採 T3；June 預告不作今日事件。|
|TechCrunch|https://techcrunch.com/2026/10/07/microsoft-releases-new-nvidia-chip-ai-pcs-with-revamped-windows-11/ ：10/7 13:22 PDT；https://techcrunch.com/2026/10/07/googles-new-synthid-website-can-identify-ai-generated-media/ ：07:00 PDT；https://techcrunch.com/2026/10/07/google-experiments-with-an-ai-powered-gaming-platform/ ：07:36 PDT|核對 Microsoft／Google 公告，採 T3–T6。資金交易不單獨作產品變更；內文星期錯誤不覆蓋官方日期。|
|WIRED|https://www.wired.com/story/openai-chatgpt-intelligent-ui-is-more-show-than-tell/ ：10/7 2:00 PM，顯示時區未確認|採官方 10/7 日期 T1；XR 評測回查 AURA 新定價，不因評測形式直接排除新品；Prime Day 特價不採。|
|Ars Technica|https://arstechnica.com/health/2026/10/pa-measles-outbreak-tops-1000-cases-largest-since-disease-was-eliminated/ ：10/7 20:01:14 UTC|採全球10。首頁 SynthID 線索回查 T5；Jaguar 新車與 Adobe 線索未列本次優先十則，不宣稱皆不合格。|
|Cool3c|https://www.cool3c.com/article/252767 ：BOOX 導購頁；https://www.cool3c.com/article/249189 ：六月初 RTX Spark 預告；最新首頁另有 ASUS 預購線索|scan 失敗後 web 補查。BOOX 首次六月、折扣非新事件；ASUS 回查 https://press.asus.com/news/press-releases/asus-proart-rtx-spark-p16-p14-ai-pcs/ 10/8 公告描述 10/7 預購，是有效候選但十則上限下未選。首頁相對時間不視為精確日期。|
|Yahoo 奇摩科技|https://tw.news.yahoo.com/gta-vi-%E8%83%BD%E7%94%A8pc%E7%8E%A9%E9%A6%96%E7%99%BC-%E5%8E%9F%E4%BE%86%E9%82%84%E6%9C%89%E9%80%99-%E6%8B%9B-120000250.html ：10/7 節目；scan 另見 LINE 偷看訊息與 iPhone 充電教學|web 首頁失敗，以成功 scan 與逐站搜尋補查。GTA 首發說法缺官方確認、教學無新變更，不採；LINE 測試首次日期未核實，不以轉載日期入選。|
|TechOrange|https://techorange.com/2026/10/07/perplexity-portable-computer-windows/ 、https://techorange.com/2026/10/07/personal-agent-protocol-pap-ai-agent/ ：均10/7文章|scan 失敗後 web 補查。Windows Portable 官方 https://blogs.nvidia.com/blog/local-ai-perplexity-windows-pcs/ 是9/14，逾窗；PAP 官方 https://sierra.ai/uk/blog/introducing-personal-agent-protocol 是10/6路線，v0.1未發布，有效路線候選但優先十則未選。|
|數位時代|https://www.bnext.com.tw/article/92505/muse-tutorial-hands-on ：頁面 payload 10/6 08:48+08；https://www.bnext.com.tw/article/92539/micron-fy2026-q4-earnings-memory-outlook ：財報展望|web 失敗改 urllib 讀取。Muse 首次9/8逾窗，10/4 gadgets 已收錄；Cowork 10/6已收錄10/7。Mods 教學缺首次變更日期，不補位；財報非獨立產品發布。|
|TechNews|https://technews.tw/2026/10/07/google-nano-banana-2-1/ ：10/7；https://technews.tw/2026/10/07/mistral-large-4-le-chonk/ ：10/7；https://cdninfosecu.technews.tw/2026/10/0/ ：索引 EmbeddingGemma 10/7 15:50|scan 與逐站搜尋補查；年度 CDN 舊7/29頁不用。官方回查採 T9、T10；Mistral 已收錄10/7排除。|
|OpenAI|https://openai.com/index/gpt-6-for-everyone/ 、https://help.openai.com/en/articles/6825453-chatgpt-release-notes ：10/7新段落|scan／直接 HTTP 403，web 官方文章與支援更新補查；採 T1，保留分批推出限制。|
|INSIDE|https://www.inside.com.tw/article/42585-youtube-shorts-shopping-creator-monetization-2026 ：10/7|scan 失敗後 web 首頁與文章補查。商務案例不等於今日新功能；Shorts 既有變更10/3已收錄。投資／傳聞不採；記憶體線索未確認官方首次時點。|

## 第二輪官方補查、去重與矛盾

- T2 官方支援 https://support.claude.com/en/articles/12138966-release-notes 的 October 7 Haiku 5.5 launch 段落確認日期；產品頁分 ≤100K 與 >100K input 價格，不混用級距。模型文件的 tokenizer／context 限制仍保留。
- T9 https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/ 、https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2 、https://developers.googleblog.com/embeddinggemma-2-the-developer-guide/ 的10/6發布、downloadable weights、740M／270M與Apache2段落。lookup `EmbeddingGemma.*2|Embedding.?Gemma.?2` 無命中，再核對同窗65列表無同事件，採用。
- T10 https://ai.google.dev/gemini-api/docs/changelog 的 October 6 段落明載 GA `gemini-nano-banana-2.1`、1K／2K／4K及1:8／8:1；deprecated 段落明載尚無 shutdown date。https://deepmind.google/models/model-cards/nano-banana-2-1/ 為October2026模型卡。第三方10/29停用說法與官方不同，未採。lookup `Personal Agent Protocol|Meta.*PAP|Sierra.*PAP|Portable.*Computer|Claude.*Mods|Nano Banana.*2[.]1|ProArt.*RTX Spark|RTX Spark.*ProArt|Home Leo` 無命中，僅同窗表 fallback；T10無同事件採用，其餘依日期與重要性處理。
- 全球窄查 `Pryluky|普里盧基|Kyiv.*(25|birthday)|基輔.*(25|生日)|Kagan|Soai|Tugay|Shiranthi|Ostroleka|Koja|古謝|Min Aung|敏昂|Amoris|1066|1,066`，只見9/24 Kyiv URL背景命中；不把網址數字的偶然命中當事件重複。另查胡塞與麻疹主線如前述。

## 全球十則時間依據

原始網址逐則完整保留於日報來源欄；以下發布時點均在24小時窗內，更新時刻只用來判讀截至截點的事實，不充作新事件。

|項目|UTC首次發布／事件依據|新增與限制|
|---|---|---|
|1 烏克蘭|AP／News4Jax metadata 10/7 06:18:14Z；最新彙整18:07Z|10/7新空襲；25死含5兒童為烏方通報。俄方聲稱軍事工業目標，保留分歧；9/24背景續報。|
|2 化學獎|AP 10/7 06:43:29Z；皇家科學院同日公告|Kagan／Soai正式獲獎，非把舊研究當新實驗。|
|3 沙烏地機場|KSAT metadata 10/7 08:28:11Z；更新19:23Z|民航主管機關通報阿卜哈兩死28傷、利雅德一死8傷；沙方未指認攻擊者，胡塞自行聲稱。10/4 Aramco主線的重大新事件。|
|4 沖繩|AP 10/7 04:59:50Z|當日東京會面；10/3逮捕與10/6限制僅背景。|
|5 伊茲米爾|AP 10/7 10:45:24Z|入AKP儀式；六月離CHP不是新事實。|
|6 緬甸訪馬|Bay News9 10/7 11:54 EDT，即15:54Z|當日抵達；週四會談尚未發生，10/4遣返僅背景。|
|7 斯里蘭卡|AP 10/7 15:35:15Z；PTI／ThePrint https://theprint.in/world/sri-lankas-former-first-lady-rajapaksa-arrested-for-fraud/3064036/ 較早12:47 IST報導|日報精確時刻標所引用AP發布，不宣稱AP是全球最早報導；當日拘留一週，非定罪。|
|8 教宗|AP 10/7 15:19:17Z|開始一週會議，非已重寫教義或形成結論。|
|9 波蘭|AP 10/7 10:32:01Z|當地上午攻擊；九人傷，嫌疑人被捕，動機未定。|
|10 賓州|Ars 10/7 20:01:14Z；PA DOH同日新公告|全年1078與本次疫情1066口徑不同。74新增登錄逾40為兩週前發病；5死為累計，10/6公衛主線續報。|

## 逐篇圖片與權利檢查

已檢查原文圖片標籤及 og:image；直接 HTTP 403 與沒有圖片嚴格分開。只採三張已下載並目視核對的對應圖，其餘不是宣稱原文無圖。

|項目|實際結果與採用決定|
|---|---|
|T1|OpenAI直接403；web／WIRED可見官方介面示意，原圖權利及可穩定下載未完成，省略。|
|T2|Anthropic有社群預覽與多個alt為Haiku4.5的舊SVG，未拿舊4.5圖冒充5.5。|
|T3|Microsoft直接403；Verge有Tom Warren產品照片，未取得再製授權，省略而非無图。|
|T4|Microsoft直接403；不把存取失敗或未確認的新介面圖寫成無圖。|
|T5|原文與og均有SynthID查驗介面；採 assets/synthid-detector.webp，官方介面示意非獨立效能測試。|
|T6|有THUMBNAIL_BLOG社群圖與影片；未採其他舊產品相關配圖。|
|T7|XREAL AURA產品頁有當代實物圖；採 assets/xreal-aura.webp，完整眼鏡contain不裁切。|
|T8|Cisco og 為 `/assets/a/y2023/m09/Wx126.jpg` 舊通用配圖，不冒充Dialog新介面，省略。|
|T9|Google有embeddinggemma2-banner_169圖與圖表，是模型主題圖而非實物；本次省略。|
|T10|官方模型卡為模型資料而非新硬體照片；未取得已核對的對應原圖，省略，不宣稱頁面無圖。|
|全球1|News4Jax有AP當日救援照與og；AP保留權利，未取得授權，省略。|
|全球2|KVA有手性鏡像示意圖及新聞使用條款；採 assets/nobel-chemistry.jpg，© Johan Jarnestad／The Royal Swedish Academy of Sciences；非實驗現場，維持原圖。|
|全球3|KSAT有AP胡塞集會／周年照及og，不是機場現場；AP保留權利，省略。|
|全球4|AP直接403，web顯示活動照線索，原圖未成功取得；存取失敗，非無圖。|
|全球5|AP直接403；Reuters Connect有儀式照片但須授權，省略。|
|全球6|Bay News9 og https://s7d2.scene7.com/is/image/TWCNews/Myanmar_Malaysia_32464 有遣返背景圖，不冒充10/7到達，省略。|
|全球7|AP直接403，原圖下載與授權未取得，省略。|
|全球8|AP直接403，web有當日一般接見照，不是會議現場，省略。|
|全球9|AP直接403，web有救援照片線索，原圖與再製授權未取得，省略。|
|全球10|Ars og是2020年misinfoTOP資料圖，不冒充今日疫情；PA為官方統計頁，省略配圖。|

三張實際原始網址、來源、用途與權利逐張保留於 presentation-2026-10-08.json；不宣稱Google／XREAL圖片採自由授權。研究原始快取與私人配送設定不發布。
