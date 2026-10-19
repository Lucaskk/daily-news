# 2026-10-19 來源筆記

研究截點｜2026-10-19 08:00:31（Asia/Taipei）；2026-10-19T00:00:31Z。
全球 24 小時窗：2026-10-18T08:00:31+08:00 至 2026-10-19T08:00:31+08:00；UTC 2026-10-18T00:00:31Z 至 2026-10-19T00:00:31Z。
科技／AI 產品 14 日視窗：2026-10-05T08:00:31+08:00 至 2026-10-19T08:00:31+08:00；UTC 2026-10-05T00:00:31Z 至 2026-10-19T00:00:31Z。
去重範圍只限 10/05–10/18 十四份日報；已建立同窗 68 列產品表，不查更早日報、歷史來源筆記或完整 ledger。

## 啟動與來源掃描

- begin 已成功，stage research_pending。沿用既有 Homebrew Python 與 runtime Git，未接受 Xcode 授權或更動全域設定。
- status 確認 legacy 與十二個啟用來源；scan 已完成，私有證據 source-scan-20261019T000052521512.json。取得內容不等於完成編輯審閱。
- 本期仍研究中，不得宣稱發布或 LINE 成功。

## 第一批候選

- 加拿大 Wainwright 基地火災：Reuters 初報 https://www.aol.com/articles/serious-incident-canada-military-alberta-021335000.html ，10/18 02:13 UTC；軍方／政府當日說明需交叉核對，初報與稍後死亡數可能不同。
- 烏克蘭情報共享恢復：Reuters https://theprint.in/world/us-resumes-intelligence-sharing-with-ukraine-after-pause-zelenskiy-says/3075391/ ，10/18 19:30 IST；為澤倫斯基受訪說法，不直接推論美方全面恢復所有服務。
- Congo 伊波拉擴至第八省：AP https://www.ksat.com/health/2026/10/18/congos-fast-moving-ebola-outbreak-spreads-to-eighth-province/ ，10/18，需核對首發時區與官方新省份病例。
- Trudy：Reuters https://gvwire.com/2026/10/18/hurricane-trudy-lashes-mexicos-pacific-coast-but-is-set-to-weaken-tonight/ ，10/18，週日新位置及強度；不是重刊週五預報。
- 排除：Rubio 約旦河西岸表態報導 10/18 05:30 IST = 00:00 UTC，早於凍結視窗起點 31 秒，不能僅因日期相同而採用。
- 科技首輪：Glimpse、RG DDS 已於昨日收錄；Technics 新評測指向九月發布不再包裝。待補查 Tesla 官方路線、Plex 原始發布、API changelog、Ember 新杯及其他啟用站最新線索。

## 第二批研究與科技定案

- Claude：官方 https://claude.com/resources/articles/dashboards-and-motion ，日期 2026-10-08，首段及 Dashboards、Motion、Getting started 段確認測試、方案與管理員限制。查詢 `Claude.*Motion|Motion.*Claude|Claude.*Dashboard|Dashboard.*Claude`，十四份日報無匹配；再核對相同 10/05–10/18 產品表，未見本次功能。採用獨立新功能，不是既有 Cowork 雲端執行的續報。
- Plex：官方由 Plex, Inc. 發布的 https://www.prnewswire.com/news-releases/plex-and-fandango-turn-movie-discovery-into-theatrical-ticket-sales-302909719.html ，10/15 11:00 EDT = 15:00 UTC = 台北23:00。採用 Starting today／U.S.／Fandango ticketing／Kochava attribution 三段。查詢 `Plex.*Fandango|Fandango.*Plex|Plex.*電影票` 無匹配，核對同窗產品表亦無，採用。
- 上述查詢由 news_workflow lookup 只讀十四份日報。recent-14d 表包含的 RG DDS 公司欄誤推為 Google，不能盲信公司欄；本期依完整事件、原始日報及產品名稱判讀，未修改無關 parser。
- 官方第二輪另查 Tesla https://www.tesla.com/roadster （web 只取得極短內容，未以媒體極端性能宣稱當原廠實測）、OpenAI https://developers.openai.com/api/docs/changelog 的10/16 prompt-to-voice段（記為候選，不與已收錄 GPT-Live 模型或 SDK 自訂語音介面混為一談，本期未選）、Ember 原廠新聞稿轉載 https://www.streetinsider.com/PRNewswire/Ember%2BLaunches%2BMug%2B3%2C%2Bits%2BThird-Generation%2BFlagship%2BSmart%2BMug/27067259.html （九月推出，排除）。不要求補滿十則。

## 十二站逐站紀錄

第一輪逐站檢視 scan 的最新標題及下列候選；第二輪回查上述官方來源。不是用單次跨站搜尋代替十二站查閱。失敗補查保留實際限制，未核實的線索不當作已確認發布。

| 來源 | 單篇與日期／取捨 |
|---|---|
| Engadget | https://www.engadget.com/2289293/double-fine-first-post-xbox-title-first-person-soulslikes-and-other-new-indie-games/ ，10/17 11:30 UTC，遊戲展示彙整；本期未核實其中獨立遊戲官方發布時間，不採彙整文日期。首頁 Technics／Alexa Tablet 評測不當新發布，RG DDS 已收錄。|
| The Verge | https://www.theverge.com/transportation/1013220/robotaxi-self-driving-car-laws ，10/18 12:00 UTC，地方治理與車輛法規議題，不是產品新供應。首頁奶泡機推薦、人物訪談及電影評論不採為新品。|
| TechCrunch | https://techcrunch.com/2026/10/18/disney-agrees-to-hire-the-majority-of-character-ais-workforce/ ，10/18 16:30 UTC，人員聘僱交易不等同產品發布；Ember評測 https://techcrunch.com/2026/10/17/embers-new-temperature-controlled-mug-makes-my-nightly-tea-ritual-even-better/ 回查九月發布排除。Replit 預設供應商訪談尚未獨立核實各方案部署，未採。|
| WIRED | https://www.wired.com/story/data-center-industry-is-trying-to-woo-kids/ ，10/18 10:30 UTC，資料中心教育公關活動，不是新品。HTC評測指向既有眼鏡，禮品與配件導購不以文章新日期補位。|
| Ars Technica | https://arstechnica.com/ai/2026/10/anthropic-gives-outside-ai-watchdog-employee-like-access/ ，10/18 16:25:19 UTC，外部監督制度，不直接當一般產品供應；Plex候選另回查10/15原始新聞稿後採用。|
| Cool3c | https://www.cool3c.com/article/253119 ，當日首頁約19小時前（非精確首發），單篇HTTP403；以 https://www.cool3c.com/category/product 與逐站搜尋補查，確認Xbox Nano線索，已於10/15日報收錄，排除。另有加熱抱枕與隔熱片，未核實14日內正式上市，不採。|
| Yahoo奇摩科技 | 掃描入口混合一般新聞，另檢視科技／遊戲標題與逐站搜尋；《GTA6》宣傳片 https://tw.news.yahoo.com/%E3%80%8Agta6%E3%80%8B%E4%B8%8A%E5%B8%82%E5%AE%A3%E5%82%B3%E5%BD%B1%E7%89%87%E5%85%AC%E9%96%8B-%E6%B5%81%E9%87%8F%E5%8F%88%E8%A6%81%E7%A0%B4%E5%84%84%E5%95%A6%EF%BC%81-090918364.html 未獨立核實新產品狀態日期，iPhone14日評測及通路優惠非新發布。未把混合入口視為沒有科技新聞。|
| TechOrange | https://techorange.com/2026/10/19/fedex-dhl-ai/ ，URL日期10/19但HTTP403、逐站搜尋未取得精確首發，可能在截點後，未採。https://techorange.com/2026/10/17/control-your-ai-costs/ 為成本分析，非特定產品更新。|
| 數位時代 | https://fc.bnext.com.tw/articles/view/4985 ，Claude Motion教學頁發生302循環；逐站搜尋找到同媒體教學 https://1day1ai.bnextmedia.com.tw/articles/claude-motion-slides-to-video-voiceover ，約10/14，回查官方10/08公告後採用，不以教學日期當事件。友達10/17周年路線盤點未進一步取得原廠具體商用日期，不採。|
| TechNews | https://technews.tw/2026/10/18/ai-emotional-counseling-hot-girl-hotline/ ，10/18，情感App線索，但未取得官方新上架／版本日期，本期未採。10/18 AI付費率、Warsh評論與台股名單非產品事件。|
| openai.com | 首頁仍以10/07焦點為主，補查官方API changelog 10/16 prompt-to-voice與release notes；Slides、GPT-Live新模型已收錄，不重刊。官方新功能留為候選，本期優先兩項已完成查核事件。|
| INSIDE | https://www.inside.com.tw/article/42654-google-ai-news-program-cnn-financial-times-axios-400-publishers-licensing ，10/17 09:12:23台北，授權計畫線索；未定位官方實際消費產品部署時點，不採為新品。XR論壇、台南鐵路及品牌新聞不以科技文章標籤直接補入產品區。|

## 世界時間與續報核對

- 加拿大：採週日正式確認傷亡而非僅週六起火。Reuters https://www.aol.com/articles/major-fire-canada-military-leaves-230616000.html ，10/18 23:06 UTC；加拿大國防部當日頁取得逾時，已以 Canadian Press／CityNews及Reuters補查。初期CBC匿名消息稱七人死亡，後續官方確認四人，保留差異，不把七人當定案。
- 烏克蘭攻擊：AP／AOL https://www.aol.com/articles/ukraine-launches-more-1-000-215241000.html 最新10/18 21:52 UTC；選取10/18聖彼得堡新攻擊，原文更新時刻不當首發。前次10/16為恢復攻擊的決定，本次新地點／火災／官方統計，標續報。1,015是俄國防部聲稱攔截量，非獨立驗證的烏方發射量。
- 情報恢復：Reuters 10/18 19:30 IST = 14:00 UTC = 台北22:00，與當日攻擊不同的美烏政策／能力事件；澤倫斯基受訪確認，不能外推全部衛星及武器限制解除。
- Congo：AP／KSAT metadata首發10/18 16:43:09Z = 台北10/19 00:43:09，北烏班吉兩病例含一死亡、新增第八省；前次10/14七省統計，標續報。週五WHO訪談僅背景。
- 法國：AP／ABC 首發10/18 06:10 EDT = 10:10UTC = 台北18:10；截點前正文更新至馬克宏晚間講話及2,400逮捕。前次10/18日報為週六遊行／約400，新增正式維安指示、調查與新統計，標續報。不得沿用標題1,800當最新數字。
- Trudy：Reuters週日新位置及強度，保留10/18事件日，不猜發布時分；不是10/16預報。官方NHC相關資訊由Reuters明確引述，未假稱直接取得bulletin。
- 川普背書：Reuters／AOL首發10/18 15:12UTC = 台北23:12；17:40:33Z為較晚更新欄，不替代首發。只報告實際背書，不將民調當選舉結果。
- MMX：官方10/18 JST新聞稿全文已用Python取得，確認10/20 04:41:03JST、保留期10/21–11/9；換算台北10/20 03:41:03。部分二手文章的11/7截止與原廠不同，採JAXA。不是已升空。官方日期無時分，採當日正式公告；AFP10/18新報導交叉確認。
- Wichita：KMUW首發10/18 14:45CDT = 19:45UTC = 台北10/19 03:45，週日釋放駕駛、尚未起訴為新增程序；事故週六發生，不靠舊事故補位。全文確認10名創傷傷者，加1名非創傷醫療問題，合計11送醫；不是互相矛盾的總數。
- 教宗：官方Vatican News可見10/18 12:27CEST = 10:27UTC = 台北18:27；metadata12:30:37+02:00為另一欄，保留可見發布。前次10/18出院及祈禱預告，本次實際主持與漸進恢復職務，標續報。

全球查詢 `Wainwright|韋恩賴特|Trudy|特魯迪|Wichita|威奇托|MMX|Phobos|情報.*中斷|情報.*共享|情報.*恢復|聖彼得堡|川普.*納坦|川普.*內塔|教宗.*出院|法國.*生活成本|剛果.*七省` 命中10/18法國／教宗、10/14剛果；另 `烏克蘭.*煉油` 命中10/16恢復攻擊。僅查十四份日報，未讀歷史來源筆記。其餘候選沒見同事件收錄；續報所指前次內容及今日新增分開。

## 逐篇圖片查核

| 項目 | 實際查核及處置 |
|---|---|
| Claude | 官方公告實際介面 https://assets.claude.com/7688d4d3b888c17cf4b3553f537f291882a92656.png 已下載並目視確認為 Claude 單車資料儀表板，非動畫成果；存 assets/claude-dashboard.png，以 Anthropic 官方產品示意署名，不宣稱自由授權。|
| Plex | 新聞稿未提供 og:image；另開官方 Dropbox press kit 連結但未取得可逐檔確認內容。屬素材讀取限制，不是沒有圖片；不用不相干商標補位。|
| 加拿大基地 | Reuters/AOL metadata 確有新聞照片，未完成照片日期及轉載權核實；國防部原頁逾時。保留無圖，不宣稱原始報導無照片。|
| 聖彼得堡 | AOL/AP 照片圖說為10/17札波羅熱車輛火災，攝影 Kateryna Klochko，並非10/18聖彼得堡現場，排除。|
| 剛果 | KSAT/AP 照片為10/7 Beni，攝影 Sebastien Kitsa Musayi；不是新增省份現場，且未核實轉載權，未使用。|
| 法國 | ABC/AP 有10/18燒毀車輛照片，攝影 Emma Da Silva；照片存在但轉載權未確認，未使用。|
| 情報共享 | ThePrint 原頁 HTTP403，搜尋內容有 Reuters 照片線索但未取得原檔；記為存取限制，不記為沒有圖片。|
| Trudy | GVWire 原頁 HTTP403，搜尋內容圖說為10/17 Boca Apiza 雲層，Reuters/Gustavo Vilchis；照片存在但非本日現場、權利未確認，未使用。|
| 背書 | AOL metadata 有 Reuters 圖片，拍攝日期與轉載權未核實，不使用。|
| MMX | JAXA 新聞稿 og:image 是機構標誌，任務頁另有示意圖但本期未完成原檔查核；不以標誌或未升空的圖片暗示發射成功。|
| Wichita | KMUW 有 Roger Nomer 拍攝的事故場景照片，素材存在但轉載權未確認；不使用。|
| 教宗 | Vatican News 有10/18 AFP 照片，不等同可自由轉載的 Vatican Media 素材；權利未確認，不使用。|
