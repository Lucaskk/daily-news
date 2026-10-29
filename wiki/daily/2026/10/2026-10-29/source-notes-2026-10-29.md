# 2026-10-29 來源筆記

研究截點：2026-10-29 08:01:08（Asia/Taipei），ISO 2026-10-29T08:01:08+08:00；UTC 2026-10-29T00:01:08Z。
全球24小時窗：2026-10-28T08:01:08+08:00至2026-10-29T08:01:08+08:00；UTC 2026-10-28T00:01:08Z至2026-10-29T00:01:08Z。
科技／AI 產品 14 日視窗：2026-10-15T08:01:08+08:00至2026-10-29T08:01:08+08:00；UTC 2026-10-15T00:01:08Z至2026-10-29T00:01:08Z。

- begin成功，legacy及原排程不改；只讀10/15–10/28十四份日報生成43列同窗表，不查完整歷史或舊來源筆記。
- 十二站scan證據source-scan-20261029T000128315427.json，逐站判讀另記，不把取得成功當查完。

## 第一批：逐站發現與官方補查

逐站讀取首頁最新文章連結，每站至多22筆；不是以跨站搜尋代替查閱。未入選不代表全站沒有其他合格新品。

|來源|實際文章及日期|候選與判讀|
|---|---|---|
|Engadget|https://www.engadget.com/2299925/apples-redesigned-macbook-pro-has-an-oled-touchscreen-weighs-just-three-pounds/ （10/28）|觸控Mac為候選；另見Echo Show 16、Buds On、Xreal Aura、StreamSet。Kindle評測不直接否定新品，須回查官方發布；本日優先已有完整官方證據的兩項。折扣、招聘、延遲傳聞不作產品發布。|
|The Verge|https://www.theverge.com/gadgets/1019554/apple-touchscreen-macbook-pro-and-tell （10/28）|Mac候選；Echo Time、Show16及Home View為其他線索，iPad mini手玩與最高價配置不是新的獨立事件。|
|TechCrunch|https://techcrunch.com/2026/10/28/apple-launches-its-new-touchscreen-macbook-pro/ （10/28）|Mac候選；Anthropic支出工具、Xreal Aura另有線索，融資與市值評論不作新品。|
|WIRED|https://www.wired.com/story/the-inside-story-of-why-apple-finally-brought-a-touch-display-to-the-mac/ （2026-10-28T17:15:16.524Z）|Mac候選；Echo新品與Kindle評測為其他線索，訪談、政治、促購排除。|
|Ars Technica|https://arstechnica.com/apple/2026/10/apple-announces-touchscreen-macbook-pro-with-oled-display/ （2026-10-28T17:25:04Z）|Mac候選；Gemini 4 Carbon尚不可使用不直接等於公開測試，另待官方可用性證據；M6舊事件排除。|
|Cool3c|https://www.cool3c.com/article/253526 （10/29 02:08台北）|Mac候選；253521 LYTIA720、253520 Prism控制器為其他線索，253487 Walkman同已收錄事件；螢幕與掛燈折扣不作新品。|
|Yahoo奇摩科技|https://tw.news.yahoo.com/tech-news/ ，首頁觸控Mac報導225500411.html、10/28電玩宅速配095649614.html|首頁混有政治餐飲，屬分類污染，不推定無科技新聞；Mac回查Apple官方；舊iPhone流行、銷量紀錄與未來主機價格猜測不作產品發布。|
|TechOrange|https://techorange.com/2026/10/28/google-deepmind-genie-4-world-model/ （10/28 11:20:43台北）|Genie4線索，尚須官方產品狀態核實；荷蘭裁員、主權AI訪談、產業論壇不獨立充作新品。|
|數位時代|https://www.bnext.com.tw/article/92788/ntu-ic-design-ai-engine-taiwan-7-frontier-technologies （10/24 20:52台北）|研究技術綜述，未取得對外發布／測試日期，不當新品；92783提示詞教學、92752估值評論排除。|
|TechNews|https://technews.tw/2026/10/28/anduril-will-collab-with-qualcomm-to-build-laptops-in-the-us/ （10/28）|BlueChip與10/28日報同事件排除；IBM投資、產能與財報不是新品；Oracle Rubin整合為另待查線索。|
|openai.com|https://openai.com/index/introducing-gpt-6-1-terra/ （10/26）、https://openai.com/index/securing-our-frontier-model-training-environment/ （10/23）|Terra已於10/27收錄；安全研究非新品。dot首次9/29逾窗；簡訊功能線索不冒充首次dot發布，本日未納入。|
|INSIDE|https://www.inside.com.tw/article/42757-apple-unveils-groundbreaking-macbook-pro-with-proled-xdr-display （10/29 02:01:50台北）|Mac候選；IPO估值、未確認採購與宣傳論壇不作新品；KBox F、AI TOP100是其他需核對首發日期的線索。|

第二輪針對明確產品線索回查Apple Newsroom、Apple Developer Touch公告、Samsung美國Newsroom與產品頁。Apple topics/mac直接擷取僅讀到舊推薦，改以官方10月archive與逐篇新聞稿補查；不把舊頁當無新聞。Samsung 10/1首次發表逾窗，10/28美國上市公告則為不同市場可用性變更，不能以新報導重標全球首發。

### 產品事件去重

- 執行lookup，範圍10/15–10/28十四份日報，query：`PROLED|touchscreen|觸控.*MacBook|Galaxy Buds On|Buds On|Echo Show 16|Echo Time|Genie 4|Gemini 4 Carbon|LYTIA 720|Archer 8 Ultra|KBox`。最初PATH缺rg而失敗，補回既有codex-path後成功，historical_match=false，result空白、無截斷。
- 查無命中後**完整讀取同窗43列recent-14d表**，沒有PROLED觸控機或Buds On美國供應事件。T1比對鍵Apple/MacBook Pro/PROLED/Touch/10-28；T2 Samsung/Galaxy Buds On/US availability/10-28。採用兩項，不宣稱其他線索皆不合格。
- 10/28已收錄M6基本MacBook Pro/iMac；今日14/16吋PROLED、M5 Pro/Max觸控新設計是不同SKU及獨立發布，不是M6評測續報。iPad mini、BlueChip、Walkman、Terra因同事件已收錄排除。
- T1官方段落：首段14/16吋、雙層OLED、最高2000nits、120Hz、M5 Pro/Max；Touch段、Pricing and Availability段。效能／續航為廠商宣稱，不寫成獨立實測。
- T2官方段落：U.S. availability、Comfortable Open-Ear Design、9.5/38 hours及頁尾相容性附註。美國US$229、11月初上市；確切日仍以官方頁為準，不移植媒體11/6為全球上市日。

## 第二批：入選時間、原文與矛盾

|項目|事件／首次可靠發布時間依據（UTC；台北見日報）|判讀|
|---|---|---|
|T1|Apple Newsroom官方日期2026-10-28，無精確時間，不虛構UTC午夜|10/28正式發布與預購，11/6供應；價格段US$2,899／3,399起，M5 Max為4,499／4,799起。|
|T2|Samsung US官方日期2026-10-28，無精確時間|區域供應新公告；不是10/1初次發表。9to5Google與Android Authority寫11/6，官方僅early November，採後者。|
|1|AP 2026-10-28T08:50:53Z；Euronews首次09:28:26Z|事故當日上午約08:54當地；至少68死。AP直接存取受限，以搜尋取得AP原報及Euronews逐篇全文補查；傷者統計不同，不拼湊成單一確定數字。|
|2|Fed決議2026-10-28T18:00:00Z|會議頁確認美東14:00，正式聲明維持3.75–4%，Cook與Hammack反對、主張升息。|
|3|Reuters經Quews 2026-10-28T20:36:10Z|早段披露週日方案；本版新增伊朗官員反駁。原文現標題已改Iran sees only unacceptable ideas，保留URL及前後差異，不把改標題當新事件；10/28首次可靠披露及當日伊朗回應為收錄基準。ToI原逐則頁403，不稱沒有內容或圖片。|
|4|英財政部govuk:first-published-at 2026-10-28T15:45:59Z|當日演說，非10/23預告；OBR與減費均標示預測／政策目標。MarketScreener403，改讀gov.uk逐字稿。|
|5|AP經iNFOnews article:published_time 2026-10-28T17:47:40Z|頁面可見12:30更新非首次時間；美財政部當日制裁，保留盧安達未履約反駁。|
|6|CP經CityNews article:published_time 2026-10-28T18:17:46Z|正式票決130–17、25棄權；AP另一滾動頁首次10/28 04:09:05Z包含票前辯論，不能用整頁首次時間稱票決已完成，故用CP本篇。|
|7|AP經Audacy 2026-10-28T09:00:39Z|當日雙方確認30小時無違規；未聲稱物資已抵達或全線停火。|
|8|AP經ABC 2026-10-28T22:00:00Z（18:00美東）|Hochul當日簽署，法定生效1/1；首次可靠報導為基準，不虛構法案號或全文未核對條文。|
|9|TechCrunch 2026-10-28T20:01:00Z|先前未公開資料外洩首次可靠披露；取得時間疑八月中旬，不把入侵時間寫在本窗。Okta否認自身系統遭入侵與駭客說法並存。|
|10|Microsoft正式日期2026-10-28；美東收盤後、17:30法說前已發布|日報日期-only，不補秒數。923億營收、639億Cloud、Azure年增48%；GAAP／non-GAAP分開。|

### 全球去重與續報

兩次lookup均只比對10/15–10/28十四份日報，無截斷：
`Oleshky|奧列什基|卡達|Qatar|伊朗.*草案|古巴|Cuba|盧安達|Rwanda|Healey|海利|聯準會|FOMC|紐約.*聊天|Homeland|國土安全|西班牙.*火車|微軟.*財報`；
`伊朗|卡達|Qatari|Hochul|聊天機器人|DHS|盧旺達|Rwanda|西班牙|Microsoft|預算`。

命中10/28日報93、101行Oleshky停火開始，10/23日報234、242行古巴客運評估及96、104行伊朗油輪通報；分別在第7、6、3則加續報，清楚寫新進展。另命中10/27微軟離職、10/20西班牙豪雨、10/15州政府訴訟／DHS難民規則及CPI背景，均不是本日財報／列車相撞／紐約簽法／資料外洩／FOMC正式決議事件。未把同一公司或國家視為全部重複。

排除：以色列選後地區反應評論缺額外獨立實質動作，不補世界篇數；蘇丹Nyala週一攻擊與週三相互矛盾數字雖值得追蹤，本日未優先選取；不採未驗證的「零違規代表全線和平」或「美伊達協議」。

## 第三批：逐篇圖片與原文稽核

逐篇取得原文meta／圖片標籤；存在不等於已有轉載授權。未下載的新聞社照片不是「原文沒有圖片」。

|項目|原文圖片或og:image結果／原圖網址|採用決定|
|---|---|---|
|T1|官方正文產品圖 https://www.apple.com/newsroom/images/2026/10/apple-unveils-groundbreaking-macbook-pro-with-proled-xdr-display/article/Apple-MacBook-Pro-with-PROLED-XDR-Display-QuickTime-261028_big.jpg.large.jpg ；另有Touch社群圖|已下載與目視確認為此次PROLED新機，非舊M6機；採官方產品圖，不聲稱本站實測。|
|T2|Newsroom https://img.us.news.samsung.com/us/wp-content/uploads/2026/10/28101617/Buds-On-1200x630.png ；產品頁og僅Samsung標誌|採Newsroom產品／佩戴示意，目視確認耳夾造型；原PNG轉JPEG僅格式壓縮，完整主體不裁切。|
|1|AP直連存取失敗，Euronews正文及og有救援照 https://images.euronews.com/articles/stories/09/97/01/65/1200x675_cmsv2_460f38d5-46e5-5063-b7df-c35e0d4f645f-9970165.jpg|署名Juanma Jimenez／Europa Press via AP；未取得再發布授權，不複製。|
|2|Fed og https://www.federalreserve.gov/images/social-media/social-default-image-opengraph.jpg ，為機構預設圖|非本次會議現場，不作事件圖。|
|3|ToI403；Reuters經Quews og https://quews.news/wp-content/uploads/Reuters_Direct_Media/USOnlineReportWorldNews/tagreuters.com2026binary_LYNXNPEM9R0NZ-VIEWIMAGE.jpg|有Reuters圖，未取得再發布授權，不複製，不稱無圖。|
|4|gov.uk有演說預覽 https://assets.publishing.service.gov.uk/media/6ae219dea5c2f99e3a7b8258/thumbnail_gov_CX_speech.png ，另有GOV.UK標誌|預覽存在；本日未下載／逐張確認權利及人物日期，故省略，不稱原文無圖。|
|5|AP經iNFOnews https://infonews.ca/wp-content/uploads/fe453fef331a51d38ee06039414d07c882330c9267e691cddd2738fcf67871d1.jpg|圖說為Kagame 10/13 F1公告資料照，非制裁現場；未授權不複製。|
|6|CP經CityNews https://montreal.citynews.ca/wp-content/blogs.dir/sites/19/2026/10/46e2aa9704658245fe18fc05401eca02ece4beaa5615436437fd3113b9dc4dda.jpg|有AP／Seth Wenig當日聯大照片，未取得再發布授權不複製。|
|7|AP經Audacy https://www.audacy.com/media-library/a-ceasefire-in-a-ukrainian-city-is-holding-officials-say-as-moscow-and-kyiv-await-us-led-talks.jpg?id=68543636&width=1200&height=600&coordinates=0%2C250%2C0%2C250|AP／Evgeniy Maloletka 10/27街景，非10/28物資抵達證據；未授權不複製。|
|8|ABC og https://i.abcnewsfe.com/a/edde4de8-3754-4ee0-9914-8820c3faaad6/wirestory_03a4e090a7df1532838a5cb6f93a23ba_16x9.jpg?w=1600|AP／Yuki Iwamura 10/2州長資料照，非簽署現場；未授權不複製。|
|9|TechCrunch og https://techcrunch.com/wp-content/uploads/2026/10/dhs-2255143488.jpg?resize=1200,800|有DHS主題照片，不是外洩名單；未取得再發布授權不複製。|
|10|Microsoft原文圖片標籤為商標、分享icon及年報封面 https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/Annual_Report_2026|未查得可確認本次季報事件照，不用年報封面冒充季度事件。|

## 產製交接

兩則產品、全球十則；正文來源連結各自置底。已建立presentation及兩張官方本地圖。依規則使用固定renderer，由finish先發布與驗證再唯一私人LINE watchdog，不用預覽阻擋配送。尚未通過check前不宣稱完成。
