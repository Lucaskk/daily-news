# 2026-10-11 來源筆記

狀態：選題與報告完成；發布／配送以pipeline實際結果為準。

## 時間與範圍
研究截點｜2026-10-11 08:02:18（Asia/Taipei）

- 凍結截點：2026-10-11T08:02:18+08:00；UTC 2026-10-11T00:02:18Z。
- 全球24小時：2026-10-10T08:02:18+08:00 至截點；UTC 2026-10-10T00:02:18Z 至截點。
- 科技／AI 產品 14 日視窗：2026-09-27T08:02:18+08:00 至截點；UTC 2026-09-27T00:02:18Z 至截點。
- 去重只用2026-09-27至2026-10-10的14份日報；不讀較早日報、歷史來源筆記或完整歷史表。
- legacy模式；已執行status、begin、14日產品表建立及scan。scan於UTC00:02:32–00:02:35取得12站紀錄，原始內容與雜湊保存在私人research-cache，不提交私人路徑或設定。

## 第一批事件查證
- Isaias：NHC 2026-10-10 01:30 UTC公告在Destin附近以105mph登陸，落在24小時窗；前次10/10日報只收錄三級預測，實際登陸屬重大續報。https://www.nhc.noaa.gov/text/refresh/MIATCUAT4%2Bshtml/100130.shtml 。AP首次發布2026-10-10T07:37:43Z，傷亡仍可能變動。https://apnews.com/article/65ac97bf16477d89ec6f847b09ccb6fc
- 利雅德機場：AP首次發布2026-10-10T09:40:39Z，沙國航空機關稱12死；與10/8日報的較早機場攻擊區分，待逐項核對新一輪攻擊時間。https://apnews.com/article/a5f40b5e0ab08ae8128db5ed749114d8
- 周先旺：AP首次發布2026-10-10T11:50:33Z，當日法院受賄判決14年；不是疫情責任判決。https://apnews.com/article/466b71bdbe194fac65575e236d122794
- 教宗死刑聲明：AP首次發布2026-10-10T13:45:52Z；世界反死刑日新聲明，不把美國先前決策重新當成今日消息。https://apnews.com/article/74cd030e0e877b5aa2ea5812426f7a57
- Erie：AP轉載頁2026-10-10 15:23 EDT，明確更正九名死者包含嫌疑人。Yahoo影片標題曾稱九人另加槍手，採AP更正，不相加。https://ny1.com/nyc/all-boroughs/ap-top-news/2026/10/10/9-dead-after-shooting-in-northern-pennsylvania
- 巴拿馬：AP西文2026-10-10 16:48 EDT，政府緊急狀態、至少27傷；7.7與6.6地震，與較早7.5初報有差異，採AP所引USGS但保留修訂可能。https://www.local10.com/espanol/2026/10/10/sismos-en-panama-dejaron-al-menos-27-heridos-mientras-el-gobierno-intenta-asistir-a-los-afectados/

## 候選去重第一批
lookup截止時間使用凍結值，組合查詢含Microsoft.*Decision.?1、Forza.*Horizon.?6及各世界事件名。命中Isaias（10/9、10/10）、沙國機場（10/8）、波蘭校園攻擊（10/8）；其餘Sudan僅命中衣索比亞鄰國背景，非本次無人機攻擊。科技項目尚待獨立窄查與無命中表格備援核對。

## 不採用的線索
- AI生成聚合站apnews.ai、預測站Next Edition不作新聞證據。
- Trump責怪Zelenskyy及戰爭選舉分析：不以措辭、評論填補新事件。
- Erie不同標題傷亡數不一致：不能把嫌疑人重複計入。
- Forza官方10/8文章與10/9影片目錄不同日期：以預購文章10/8作事件日期，不以影片新增日期改寫。

## 逐站查閱紀錄
以下為實際檢視首頁最新文章、私人scan原始HTML連結及失敗後web補查結果；不是以status當作查閱。未選的候選不宣稱不存在其他合格新聞。

|來源|文章、可核實日期與結果|
|---|---|
|Engadget|https://www.engadget.com/2282487/bose-lifestyle-ultra-soundbar-review/ 首次2026-10-09T18:00:00Z。新品線索回查Bose官方https://www.bose.com/pressroom/bose-lifestyle-collection ，首次5/5、上市5/15，逾窗排除。https://www.engadget.com/2282389/pebble-flow-ev-rv-review/ 為本次首頁評測線索；官方https://pebblelife.com/post/production-intent-pebble-flow 為2025/1/6，不能以評測當新品。|
|The Verge|https://www.theverge.com/ 頁面10/10最新列表實讀：14:48 UTC Goodreads分數評級、14:41 UTC Anthropic離線評估、10/9 Microsoft-Decision-1。後者回查官方採用；前二者未選，研究安全事件不是產品推出。Google Streamer、HomeView商標線索屬未確認產品傳聞，不補位。|
|TechCrunch|https://techcrunch.com/2026/10/10/cloudflare-acquires-deno-to-improve-its-workers-programming-model/ 10/10收購線索，未據此宣稱Workers新版本上市；https://techcrunch.com/2026/10/10/apple-discloses-deal-to-hire-team-and-license-tech-from-personalized-podcast-startup-huxe/ 10/10人才與技術交易，非具體產品可用性變更。https://techcrunch.com/2026/10/09/anthropic-cant-reliably-control-its-ai-agents-its-cutting-off-its-internal-evals-from-the-live-internet-instead/ 10/9，內部評估安全處置，不列產品。|
|WIRED|https://www.wired.com/story/how-this-tiny-startup-pikio-built-the-worlds-safest-bike-helmet/ 首次10/10T09:00Z。回查https://pikiolabs.com/products/model-si-preorder?view=preorder-si 僅能確認預購與October 2026出貨，未取得14日內首次預購／實際出貨日期，不採。Tesla更名線索保留，未作此次精選。|
|Ars Technica|https://arstechnica.com/science/2026/10/the-psychedelic-brain-looks-like-chaos-underneath-theres-order/ 首頁10/10，研究非產品；https://arstechnica.com/gadgets/2026/10/your-artwork-could-be-featured-in-the-next-debian-release/ 10/9徵稿非軟體版本發布；https://arstechnica.com/cars/2026/10/volkswagens-replacement-for-the-id-4-crossover-is-here/ 首頁10/9新車線索未列本次精選，不以首頁日期直接當官方上市日。|
|Cool3c|scan及urllib403，改用web首頁、最新消息與個別文章。https://www.cool3c.com/article/252836 首次2026-10-09 15:35，Freckl線索回查官方https://freckle.tech/ ，尚未核實首次預購日期，不採；首頁小米4.5L氣炸鍋、山水SSB-Z2、Watch2Pro均明列特價；SynthID Detector已於10/8日報收錄，不重複。|
|Yahoo奇摩科技|web入口失敗後改用scan原始HTML及urllib取得https://tw.news.yahoo.com/tech-news/ 。可核實連結https://tw.news.yahoo.com/iphone-duo%E5%82%B3%E5%8A%A0%E5%96%AE30-%E5%8F%B0%E7%A9%8D%E9%9B%BB-%E9%B4%BB%E6%B5%B7%E7%AD%89%E4%BE%9B%E6%87%89%E9%8F%88%E5%90%9E%E8%A3%9C%E4%B8%B8-222435151.html 為訂單傳聞，首頁另有華為配對Apple Watch線索，但未核實獨立發布日，因此不採，不從網址尾碼虛構日期。|
|TechOrange|scan失敗，web首頁成功補查。https://techorange.com/2026/10/08/honda-electrification-2027-releases-e20/ 10/8，回查Honda10/6新技術公告採用；首頁10/10貝萊德Token Economy報告是產業分析，10/8CloudMile活動及高通生態系介紹不作單獨產品發布。|
|數位時代|web失敗，scan與urllib成功。https://www.bnext.com.tw/article/92578/kirin-health-science-third-pillar metadata2026-10-09T14:07+08:00，企業策略分析；https://www.bnext.com.tw/article/92539/micron-fy2026-q4-earnings-memory-outlook 為財報線索，不作產品。|
|TechNews|web曾回舊頁，改用即時urllib首頁及scan原始HTML；https://technews.tw/2026/10/09/asml-next-gen-hyper-na-euv-stronger-high-na-expected-10-years/ 10/9為十年展望，未列本次具體產品精選；首頁10/10Claude虐待政策與Megapack採購為線索，未以新文章日期當首次功能推出。|
|openai.com|scan失敗，官網導覽不足，改查https://help.openai.com/en/articles/6825453-chatgpt-release-notes 最新10/9段落。Composer predictions已於10/10收錄；10/8跟進指令已於10/9收錄；不以release notes整頁更新時間重收。|
|INSIDE|scan及urllib403，web首頁與https://www.inside.com.tw/category/headline 補查成功。10/10Claude警方假線報為安全事件非產品；10/9Gemini同事代理與10/8EmbeddingGemma2及Haiku5.5已收錄。10/10OLED MacBook月底亮相是傳聞；10/9Apple10/13活動線索未據此推論HomePad已發布。|

## 官方定向補查與科技決策
- 硬體：Apple newsroom https://www.apple.com/newsroom/ 最新可讀日期9/29；Mac mini／Studio9/22上市逾窗。Bose5/5及Pebble2025首次發布逾窗。Pikio月度供貨資訊不足以確認14日內變更。
- 消費軟體：Forza https://forza.net/news/forza-horizon-6-pre-order-ps5 ，精確定位10/8「Starting today」PS5預購及1/26、1/21版本段落，採用。
- 開發工具與AI：Microsoft https://commandline.microsoft.com/microsoft-decision-1-model-foundry/ 10/9「available in Microsoft Foundry」「coming soon through OpenRouter」；Foundry官方https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-microsoft-decision-1-in-microsoft-foundry-for-decision-and-classific/4562742 明列public preview。與第三方稱GA不同，採官方公開預覽。
- 公開測試／交通：Honda官方10/6共同研發成果與2027會計年度實證段落，屬具體技術／產品路線更新；150kW為後續驗證，不採媒體可能讓人誤解已公路實現的表述。
- Google官方補查https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026 （10/8），已收錄不重複；2025回顧頁不採。
- T1查詢`Microsoft.*Decision.?1|Decision.?1.*Microsoft`、T2查詢`Forza.*Horizon.?6|Horizon.?6.*PS5`，獨立科技組合lookup無命中；才完整讀同窗70列產品表，均無相同事件。
- T3查詢`Honda.*(無線|充電|DWPT)|本田.*(無線|充電)|DWPT|Honda.*Taisei`無命中，再核對已載入同窗表，無相同事件。
- 不需要湊10則，採3則有官方時間基礎且未重複的獨立事件。

## 全球時間與去重補充
|項目|首次發布／事件依據（UTC）|24小時判斷與去重|
|---|---|---|
|1 Isaias|10/10 01:30官方登陸；AP07:37:43|在窗內；10/10預測→實際登陸重大續報。|
|2利雅德|AP／KSAT首次10/10 09:40:39；當日新12死通報|在窗內首次可靠通報；10/8較早攻擊→新一輪航廈攻擊。|
|3巴拿馬|Local10首次metadata10/10 23:47:55；頁面顯示16:48 EDT與modified20:48:10Z有矛盾|兩時間均在窗內；採保守較晚metadata，不虛構震源發生時間；新政府緊急措施。|
|4 Simon|NHC第13號10/10 15:00|在窗內150mph觀測；14日Simon無命中；不是已登陸。|
|5蘇丹|AP／KSAT首次10/10 09:40:39，原始標題即包含40死|採首次可靠傷亡通報，不採23:19:53修改時間；星期五攻擊無精確時分，不宣稱攻擊剛發生。14日Sudan僅他國背景。|
|6國慶演說|ABC／AP10/10 00:49 EDT=04:49Z；台灣10/10上午演說|在窗內；無本次演說舊收錄。|
|7波蘭|CityNews首次10/10 09:49:57，週六警方公布數字|在窗內；10/8校園攻擊→全國拘留／預防行動重大續報。|
|8 Erie|AP／NY1週六10/10 15:23 EDT=19:23Z|只採週六官方確認及澄清；不將週五17時槍擊本身作新事件。14日Erie無命中。|
|9周先旺|AP10/10 11:50:33；週六法院判決|在窗內；窄查周先旺／Zhou.Xianwang無命中。|
|10教宗|AP10/10 13:45:52；世界反死刑日新聲明|在窗內；不重收美國舊安排。|

## 逐項圖片查證
圖片存在與能否再利用分開判斷；沒有採用不表示原文沒有圖。
- T1 Microsoft：Command Line urllib403，web可讀文字；Foundry文章可見模型及Playground圖，但未取得穩定原圖及明確可用權利，本次省略，不稱無圖。
- T2 Forza：HTTP200，原文及og有本次PS5官方遊戲影像；採本次官方圖，權利歸Xbox／Playground，不宣稱自由授權。
- T3 Honda：HTTP200，原文有系統圖、GA樣品與VA；og為官方技術圖https://wieck-honda-production.s3.amazonaws.com/photos/098d3a21ce18b3a3d1f3e0da11b75443f88d183b/thumbnail-364x204.jpg 。高解析下載連結經web轉到首頁，本次省略，未用低解析預覽冒充公路照片。
- 1 Isaias：AP原頁403；NHC文字登陸快報無事件圖，僅機構標誌，不以標誌冒充現場。
- 2利雅德：AP403；KSAT原文可讀，og為10/6加薩資料照，另有海灣定位圖，非本次機場現場，不套用。
- 3巴拿馬：Local10 HTTP200，有og原圖https://www.local10.com/resizer/v2/CFCHCF2HYQF6SUXEJKEUZTARTQ.jpg?auth=29b512643b565a2c14c0d4649a7f24944b15e8dc1852b1b1c3c816729b033677&width=700 ，屬AP版權圖；本次不下載再利用。
- 4 Simon：AP403；NHC公告索引無og僅機構標誌；不以別的颶風舊照片替代。
- 5蘇丹：KSAT HTTP200，og與原圖是10/6加薩照片及海灣定位圖，不是Abu Shandi，省略避免誤導。
- 6台灣：ABC HTTP200，原文及og有AP／Chiang Ying-ying國慶照片https://i.abcnewsfe.com/a/9cbc2ad0-4a3f-4922-9b0f-32c01399b8c5/wirestory_acef4d9b8c0e988d8db93e89d84b0e9d_16x9.jpg?w=1600 ，未取得重用授權，保留來源不下載。
- 7波蘭：CityNews HTTP200，原文與og有AP／Rafal Niedzielski10/7現場照片https://vancouver.citynews.ca/wp-content/blogs.dir/sites/9/2026/10/94c22829cb040f6ea427e3b84cdbe675f0f6c27218e4d097fd505e5910e164d3.jpg ，是較早事件資料照，未取得重用授權，省略。
- 8 Erie：NY1 HTTP200，og與正文僅Spectrum通用新聞圖https://s7d2.scene7.com/is/image/TWCNews/Spectrum-News-National-News-Slate ，不作事件圖。
- 9周先旺：AP原頁403，無法完成原頁圖片取得，不稱原文無圖。
- 10教宗：AP原頁403；AP目錄顯示10/8宗教活動資料照，不當10/10聲明現場圖，亦未取得再利用授權。

## 排序與限制
Simon已由官方索引取得固定存檔https://www.nhc.noaa.gov/archive/2026/ep20/ep202026.public.013.shtml ，HTTP200，確認15:00 UTC、150mph及墨西哥警報範圍；替換容易變動的mobile URL。Forza原圖下載成功94,349 bytes，記於presentation JSON並隨日報提交。Freckle官方可讀，確認預購及December 2026首批，但無首次變更日期，仍排除。

以跨媒體曝光、官方新進展、公共安全及制度影響綜合排序，沒有聲稱取得全球點閱榜。搜尋命中、可讀metadata與來源原文比標題優先；不採AI生成聚合頁，不以未取得圖片或403當作全站無新聞。
