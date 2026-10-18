# 2026-10-18 來源筆記

研究截點｜2026-10-18 08:01:26（Asia/Taipei）

研究截點：2026-10-18T08:01:26+08:00（2026-10-18T00:01:26Z）。
全球 24 小時：2026-10-17T08:01:26+08:00 至截點；UTC 2026-10-17T00:01:26Z 至截點。
科技／AI 產品 14 日視窗：2026-10-04T08:01:26+08:00 至截點；UTC 2026-10-04T00:01:26Z 至截點。
去重僅查 10/04–10/17 十四份日報，不查歷史來源筆記或完整歷史表。

## 啟動與來源掃描

- 系統 Python／Git 因 Xcode 未接受授權退出 69；改用既有 /opt/homebrew/bin/python3 與 Codex runtime fallback Git，不接受授權、不修改系統設定。
- begin 成功，狀態 research_pending。已依凍結截點建立 recent-14d 表，讀取十四份日報、70 列。
- scan 已實際讀取全部十二個啟用來源；證據保存於私有 research-cache/source-scan-20261018T000155362724.json。成功取得不代表編輯審閱完成。
- 目前仍在研究，未完成報告、發布或配送，不得宣稱成功。

## 初步取捨

- Engadget：Roadster、Technics EAH-A1000 評測、Anbernic RG DDS 為新品線索；需回查官方日期與近十四日收錄。操作教學、購物及舊硬體介紹不是新品發布。
- The Verge：Steam Achievement Sets、Surface Laptop Ultra 已有近期日報；Roadster 尚須官方查證。專欄與訪談不當作產品事件。
- TechCrunch：10/16 Elorian Glimpse 為模型研究預覽候選；10/17 Replit 預設模型供應商變動亦待官方確認。Ember 評測需回查新品發布，不以評測日期代替。
- WIRED：HTC VIVE Eagle 與 Technics 評測需回查原始發布；Razer Barracuda V2 Pro 已於 10/17 收錄。加密、微塑膠及選舉報導不屬新品。
- Ars：Plex 電影票功能為候選；KDE Plasma 6.8、Surface Ultra 已收錄；評論及研究不直接算產品發布。
- OpenAI 首頁最新焦點停於 10/07，必須另查 release notes／逐站搜尋，不可當作沒有新消息。
- INSIDE：10/17 Zeabur 停止營運公告為候選；XR 論壇心得不是產品發布，已有 Muse Wonder 不重刊。

## 世界候選

- 法國 10/17 全國示威，AP 原文 https://apnews.com/article/44b9d3ba91ffad4029f975dced7e31cb （首發 09:18:36Z），需與近十四日示威條目比較並標記新發展。
- 米蘭 10/17 生活成本示威衝突，AP https://apnews.com/article/aada57790a8d2d3c02ab55911b9ecead （20:42:26Z）。
- ICRC 10/17 證實協助葉門釋放 159 人 https://www.icrc.org/en/news-release/yemen-icrc-supports-release-154-detainees-sanaa 。URL 尾碼 154 與正文 159 不同，採正文並保留原網址，不自行修正 URL。官方為日期來源，不虛構時分。
- Pope Leo 出院、新一輪對俄制裁暫停、印度宗教節慶踩踏待查原始報導。
- 排除：10/16 俄國九地區襲擊已收錄；10/16 Warsh 報導在全球時間窗外；搜尋命中舊報導不可利用更新時間翻新。

## 逐站審閱與補查

以下在十二站 scan 後逐站檢視首頁最新清單，並讀取所列單篇；不是用跨站搜尋取代掃描。部分 web 工具回傳 Internal Error，改用現有 Python urllib／fetch_source 取得單篇正文。

| 來源 | 文章、日期與取捨 |
|---|---|
| Engadget | https://www.engadget.com/2289602/anbernics-rg-dds-is-almost-double-the-price-of-the-original-nintendo-3ds/ ，10/17 12:15 EST；回查官方 RG DDS 預購頁及 10/16 可靠報導後採用。https://www.engadget.com/2288638/technics-eah-a1000-review/ ，10/16 評測；官方 https://us.technics.com/blogs/news/technics-introduces-eah-a1000-flagship-wireless-headphones-a-new-standard-in-premium-listening 明載 9/29，排除以評測刷新。|
| The Verge | https://www.theverge.com/transportation/1012552/tesla-roadster-next-gen-reveal-elon-musk ，10/15 發表事件，當日頁面已逐篇讀取；屬候選，但本期不採用未進一步完成原廠路線及監管限制查核的規格。Steam 成就集與 Surface 評測已在近期表出現，不重複。|
| TechCrunch | https://techcrunch.com/2026/10/17/replit-is-no-longer-working-with-anthropic-ceo-says/ ，10/17，取得單篇但不以 CEO 訪談直接推定所有工作區均切換；未採用。10/16 Elorian 線索另回查官方 Introducing Glimpse。|
| WIRED | https://www.wired.com/story/htc-wants-its-vive-eagle-smart-glasses-to-be-the-anti-meta/ ，10/17 評測／訪談，正文說九月已在美國開賣，非本次新發布，排除。Razer 評測指向已於 10/17 收錄的新機，不重刊。|
| Ars Technica | https://arstechnica.com/gadgets/2026/10/plex-now-helps-sell-movie-theater-tickets/ ，10/15 17:22，Plex／Fandango 新功能線索；官方定向搜尋尚未取得獨立原始發布全文，本期不採。Plasma 6.8、Surface 已收錄。|
| Cool3c | https://www.cool3c.com/article/253110 ，10/17 15:09，正文為 Wuben G5 評測及導購，未提供十四日內發布證據，不把折扣當新事件。Walkman 正式發布已收錄 10/16。|
| Yahoo奇摩科技 | scan 頁混合一般新聞，另以逐站搜尋補查 https://tw.news.yahoo.com/ipad-%E5%AF%A6%E7%8F%BE%E5%8E%9F%E7%94%9F-linux-%E7%92%B0%E5%A2%83-linpad-112317309.html ，10/17，LinPad 線索；未取得可核實的原始版本及發布時點，本期排除，不將入口混合新聞判作沒有科技消息。|
| TechOrange | https://techorange.com/2026/10/17/control-your-ai-costs/ ，10/17，企業 AI 成本分析而非特定新品或公開測試，不採。10/16 身分治理論壇、美銀修補人力屬活動／組織措施。|
| 數位時代 | https://www.bnext.com.tw/article/92686/auo-semiconductor-glass-core-micro-led-20261017 ，10/17 14:39，友達周年活動揭露技術與送樣進度，尚未回查原廠精確路線公告，不採作本期正式產品發布。|
| TechNews | https://technews.tw/2026/10/17/chinese-startup-develops-euv-light-source/ ，10/17，研發與預計商用線索，不把文章日期當正式商品可用日期；未完成官方時點查證，本期不採。首頁 Lightmatter／CPO 等線索亦不以產業評論湊數。|
| openai.com | 首頁最新焦點停於 10/07，另逐站搜尋 https://developers.openai.com/api/docs/changelog 與 https://help.openai.com/en/articles/6825453-chatgpt-release-notes 。10/16 prompt-to-voice 為新功能線索，10/15 GPT-Live 與 10/16 Slides 已見近期表；本期不將滾動頁整體更新算新產品。|
| INSIDE | https://www.inside.com.tw/article/42662-zeabur-shutdown-dec-31-dedicated-servers-stop-renewal-dec-1 ，10/17，取得完整正文；明示截至查核官方部落格／狀態頁尚無停止營運公開公告，為使用者信件報導，未採作已核實的正式平台公告。10/17 XR 論壇非產品發布。|

## 官方定向補查與科技去重

- 補查涵蓋硬體預購／官方商品頁（Anbernic）、AI 公開研究預覽／API（Elorian）、官方 newsroom（Technics）、開發工具／release notes（OpenAI）及消費軟體（Plex／Fandango）。合格兩則即可，不補滿十則。
- T1：查詢 `Elorian.*Glimpse|Glimpse.*Elorian`，十四份日報無匹配；完整讀取僅 10/04–10/17 的 recent-14d 表，仍無本次事件。採用。官方 10/16 Introducing Glimpse 的「Research preview」「Glimpse is available through API and our chat UI today」及末尾研究方向段落確認發布與限制。性能數字不直接當獨立實證；精確重建及控制機器人仍為未來工作。
- T2：查詢 `Anbernic.*RG.?DDS|RG.?DDS.*Anbernic|RG DDS`，十四份日報無匹配；同窗 recent-14d 表無匹配。採用。官方商品頁的 Pre-Order、Ships gradually starting December 10, 2026、About the RG DDS 與記憶體／螢幕規格段落為依據。
- T2 時間交叉核對：https://www.notebookcheck.net/Anbernic-RG-DDS-pre-order-is-live-but-there-s-a-long-wait-before-it-ships.1425957.0.html 可見 Published 10/16/2026，10/17 是更新。保留日期，不虛構預購首秒。
- 同窗產品表已完整讀取，70 列；未查任何更早日報、歷史來源筆記或完整 ledger。

## 世界新聞時間與去重定案

| 排名 | 新事件時間依據 | 去重／差異 |
|---|---|---|
| 1 | Reuters 10/17 23:30 IST = 18:00 UTC = 10/18 02:00 台北；週五晚行政命令及週六烏方回應 | 前次 10/10 柴油安排，本次新增正式制裁暫緩，標續報。|
| 2 | AP 首發 10/17 09:18:36 UTC = 17:18:36 台北；週六新遊行、截點前最新版人數 | 命中 10/06、10/09、10/14 法國學生抗議；以前次 10/14 為續報起點，新增跨群體動員及週六衝突。|
| 3 | NDTV 首發 10/17 22:47 IST = 17:17 UTC = 10/18 01:17 台北；事故約 19:40 IST | 新的加爾各答事故，未命中十四份日報；排除 2025 Kumbh 踩踏搜尋命中。|
| 4 | Reuters 10/17 17:00 IST = 11:30 UTC = 19:30 台北；突尼斯週六現場 | 未見本次示威；八月舊示威搜尋命中不採。|
| 5 | ICRC 正文 17-10-2026、Today 確認當日實際釋放 | 日期來源不補午夜。metadata 建檔 10/16、修改 10/17、time 欄 10/17 07:00+02:00互異，採當日正文事件，不用修改時間翻新；官方當地上午在窗內。159 與 URL 154 差異明記。|
| 6 | Vatican News 可見 10/17 15:44 CEST = 13:44 UTC = 21:44 台北；metadata 15:57:55+02:00 為另一欄，保留可見時間 | 命中 10/12 手術決定、10/14 手術及診斷，本次出院與翌日活動為續報。|
| 7 | Reuters 10/17 15:30 IST = 10:00 UTC = 18:00 台北；週六會議與記者會 | 當日主席聲明及離席，不以昨日官員說法刷新。|
| 8 | AP 首發 10/17 17:18:57 UTC = 10/18 01:18:57 台北 | 命中 10/16 第三日，本次第五日、七警停職調查為新進展；167／132 是累計不是單日。|
| 9 | AP 10/17 23:03:49 UTC = 10/18 07:03:49 台北；週六控制率及撤離狀態 | Norte 起火在週五、未見十四日報收錄；今天使用週六更新。州長 10/16 公告僅背景。|
| 10 | dpa／AFP 同日初始搜尋報導 10/17 13:01 UTC = 21:01 台北；單篇稍後更新到 18:31:17 UTC | 當日探索協商完成，不稱新政府已成立；九月選舉僅背景。|

去重查詢分兩批：`法國.*示威|教宗.*手術|IMFC|柏林.*組閣|突尼西亞.*示威|阿爾巴尼亞|Norte|葉門.*釋放|米蘭.*示威|加爾各答|No Kings`；`川普.*制裁|法國.*學生|法國.*抗議|柏林.*聯盟|IMF.*年會|加州.*野火|葉門.*159|突尼西亞.*賽義德`。只查最近十四份日報，已人工判讀上述匹配。米蘭及 No Kings 為合格候選但不採入本期，以保留地區及主題分布；未將跨國示威合併為同一事件。

## 逐篇圖片稽核

| 文章 | 原文／og:image 實際查核 | 使用決定 |
|---|---|---|
| T1 Glimpse | 官方 og:image https://elorian.ai/assets/blog/glimpse/og-introducing-glimpse.jpg ，已下載並目視為發布圖及視覺追蹤示意 | 使用，明標官方示意、非實測。|
| T2 RG DDS | 官方 secure og:image https://anbernic.com/cdn/shop/files/eg.jpg?v=1792131877&width=1200 ，已下載目視確為白色雙螢幕 RG DDS | 使用，非舊型號照片。|
| 1 制裁 | ThePrint 單篇 urllib HTTP 403，搜尋可見 Reuters 著作權照片，未取得原圖 metadata | 不下載，屬存取／權利限制，不宣稱無圖。|
| 2 法國 | AP 單篇 urllib HTTP 403；AP 另有當日圖輯 https://apnews.com/article/73243bcc44f5423ba8efbc1496e56c5d | 有活動照片線索，但未取得可用原圖及授權，不嵌入。|
| 3 加爾各答 | NDTV 單篇 urllib HTTP 403，文字由網路檢索取得，原圖未取回 | 存取失敗，不宣稱原文無圖。|
| 4 突尼西亞 | ThePrint HTTP 403；Reuters Connect 可見 Zoubeir Souissi 現場照片及商業授權標示 | 未取得轉載授權，省略而非稱無圖。|
| 5 葉門 | 官方 og:image 為 https://www.icrc.org/sites/default/files/styles/meta_image/public/2026-10/Yemen-release-op_Oct-2026_Photo-2.png?h=01028b68&itok=7R7qB1G6 ；頁面另有不符葉門的泰柬 alt | 圖片存在，但 alt／脈絡矛盾，未視覺確認，暫不嵌入。|
| 6 教宗 | 官方原圖 https://www.vaticannews.va/content/dam/vaticannews/agenzie/images/srv/2026/10/17/15/1792244706811.JPG/_jcr_content/renditions/cq5dam.thumbnail.cropped.1500.844.jpeg ；署名 VATICAN MEDIA | 當日照片存在，未取得轉載權利確認，不嵌入。|
| 7 IMFC | ThePrint HTTP 403，搜尋可見 Reuters 圖片及版權標示 | 未取得可用原圖／授權，不嵌入。|
| 8 阿爾巴尼亞 | AP HTTP 403；Reuters https://www.internazionale.it/ultime-notizie-reuters/2026/10/17/albanian-anti-government-protesters-clash-with-police-in-tirana 可見 Florion Goga 當日現場圖說 | 未取得授權，省略，不稱無圖。|
| 9 Norte | AP HTTP 403；另有當日圖輯 https://apnews.com/article/0d916c61b8894b5e8b478183b5abb613 | 照片存在，未取回可用原圖與轉載權利，不嵌入。|
| 10 柏林 | AOL og:image https://hermes.media.transform.aol.com/adcc2cb055c05f5ef8c6f675eb0f335859b51016/w_1200,c_scale,f_auto,q_auto/https://hermes.media.static.aol.com/media/2026/10/17/e90e7625-b19f-3c79-a97d-927528164ca6/ba3308ef-884d-4457-ba56-b2c95d9c0009.jpg ，署名 Annette Riedl/dpa，標為資料照 | 不是今日談判現場且未有轉載授權，不嵌入。|

兩張採用圖的出處、原圖、權利、caption 已寫入 presentation JSON；不使用生成圖或無關舊產品補圖。權利保留的官方發布素材不宣稱自由授權。
