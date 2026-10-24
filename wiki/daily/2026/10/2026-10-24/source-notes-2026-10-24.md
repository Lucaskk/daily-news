# 2026-10-24 來源筆記

研究截點：2026-10-24 07:56:54（Asia/Taipei），ISO 2026-10-24T07:56:54+08:00；UTC 2026-10-23T23:56:54Z。
全球24小時窗：2026-10-23T07:56:54+08:00至2026-10-24T07:56:54+08:00；UTC 2026-10-22T23:56:54Z至2026-10-23T23:56:54Z。
科技／AI 產品 14 日視窗：2026-10-10T07:56:54+08:00至2026-10-24T07:56:54+08:00；UTC 2026-10-09T23:56:54Z至2026-10-23T23:56:54Z。

- begin成功，沿用legacy，未改排程。只查10/10–10/23十四份日報，已生成同窗52列產品表，不查更早／完整歷史表或來源筆記。
- scan12站完成，證據識別source-scan-20261023T235710783412.json；取得時間不是首發時間，逐站候選及失敗補查尚在進行。
- 全球初步候選：台灣薔琵颱風、西藏地震新救援、黑海貨船遭襲、約旦教堂槍擊、肯亞倒樓、法國博物館關閉維安、紐西蘭軍方首長辭職、西岸新攻擊、墨西哥Vance颶風、歐洲熱死研究。候選尚未定稿，尼泊爾基金與昨天相同分配事件不重複。

## 第一批查證

- 實際scan十二站均retrieved；OpenAI今天首頁成功，不沿用昨天失敗。各站首頁前22個去重文章連結已逐站解析。Engadget當前有Facebook連結收費、Apple Music iPod彩蛋、Cybertruck澳紐停推、遊戲訂閱；Verge有Delta2.0、Google隱私政策、Birdbuddy評測；TechCrunch有募資及OpenAI訓練安全；WIRED有iPhone Duo導購、交友App模式、PHP漏洞；Ars有NASA登月計畫與Google隱私／Spotify政策；Cool3c有Sigma FP2、VIVEE、Acoustune XHS1400及Sigma鏡頭路線；Yahoo當前頁混入一般新聞且MacBook題為預測，需區分傳聞；TechOrange有Carbon-X模型及1Password重複事件；數位時代最新首頁前段為播客與研討會，不當新品；TechNews有Rubin Ultra架構與Apple標籤；INSIDE有Spotify車載App及KBox，具線索但尚待官方日期；OpenAI有10/23訓練環境安全公告。
- 科技窄化lookup `Sigma.*FP2|FP2.*Sigma|HTC.*VIVEE|VIVEE.*HTC|Delta.*2.0`，reports_compared=14、historical_match=false、truncated=false。無命中後完整核對同窗52列產品表，Sigma FP2與VIVEE均無事件；Delta為候選但官方版本核對尚未完成，不採。
- Sigma官方 https://www.sigma-global.com/en/news/2026/10/23/012378/ 及 https://www.sigma-global.com/jp/news/2026/10/23/012376/ 首發10/23只有日期，11/11上市、日本官店10/29 10時預約（日本當地）；2450萬畫素部分堆疊、翻轉螢幕、70GB、6K OpenGate。世界最小為原廠限定條件主張；價格、台灣供貨不自行推測。官方正文完整取得；圖片待原圖核對。
- HTC本人新聞稿由BusinessWire發布，原始 https://www.businesswire.com/news/home/20261022888626/en/ 及可讀全文 https://finance.yahoo.com/technology/ai/articles/htc-introduces-vivee-interactive-digital-130000564.html ，10/22 13:00Z＝21:00台北。段落Technology with Personality／Privacy-Conscious by Design／Availability and Pricing：10/22預購，99美元至11/30、一般119美元，十二月上旬預計出貨；提醒、音樂、對話、實體麥克風開關。隱私去識別與不訓練通用LLM為原廠承諾，不是獨立稽核。地區／配件不同，不推定台灣可購。
- 全球lookup只查十四日報：薔琵／西藏／肯亞倒樓／Vance／紐西蘭軍方等無同事件命中；法國命中10/23里昂禁令，本次新7萬警力與博物館關閉需標續報。黑海命中10/14保加利亞附近Dignity／Chelsea3事件，本次羅馬尼亞附近另一貨船沉沒標續報。南韓命中10/22北韓心理戰主張，須分清新會談提議而非重述口水。

## 十二站實際文章紀錄

|來源|實際文章及首發依據|決定|
|---|---|---|
|Engadget|https://www.engadget.com/2295422/meta-is-charging-government-and-nonprofit-pages-to-post-links-on-facebook/ ，10/23 16:09:39Z；https://www.engadget.com/2295392/apple-music-has-a-fun-easter-egg-for-the-ipods-25th-anniversary/ 為當日首頁線索|Meta權限變更候選仍待官方範圍核對；Apple彩蛋不視為重大產品發布。ASUS／GuliKit／BMW／Insta360評測有新品線索但尚未完成官方首發核對，不直接判舊聞。|
|The Verge|https://www.theverge.com/games/1016524/delta-2-version-ios-duo-gaming-emulator-update ，首發10/22 18:30Z；https://www.theverge.com/tech/1017600/google-personal-intelligence-privacy-policy-ads-update 首頁線索|Delta候選lookup無命中、同窗表無事件，但未完成官方changelog，暫不採；Google政策範圍待官方。不把首發與修改時間混用。|
|TechCrunch|https://techcrunch.com/2026/10/23/openai-says-it-will-no-longer-train-its-ai-models-on-the-live-internet-citing-significant-risks/ ，首發23:05:49Z、修改23:05:57Z；https://techcrunch.com/2026/10/23/agent-cloud-startup-daytona-hits-1b-valuation-backed-by-firstmark-and-a-whos-who-of-angels/|前者為內部訓練安全措施，未見對外產品權限變更，不列產品；後者募資估值不是發布。|
|WIRED|https://www.wired.com/story/a-dating-app-is-offering-chivalry-mode-and-marriage-timeline-to-get-gen-z-married/ ，首發10/23 10:15Z；https://www.wired.com/story/8-things-to-know-about-the-apple-iphone-duo/ 首頁線索|交友App模式具候選，官方日期尚待核對；iPhone導購不獨立當新發布。|
|Ars Technica|https://arstechnica.com/gadgets/2026/10/updated-google-privacy-policy-says-your-gmail-might-be-used-for-advertising/ 、https://arstechnica.com/gadgets/2026/10/spotify-ramps-up-policy-enforcement-on-family-plans/ ，10月路徑及當日首頁|政策／存取變更線索待官方條款生效日；https://arstechnica.com/space/2026/10/nasa-updates-lander-plans-for-moon-landings-finally-solves-long-festering-orion-issue/ 是任務規劃，不當消費新品。|
|Cool3c|https://www.cool3c.com/article/253334 FP2首發10/23 16:47台北；https://www.cool3c.com/article/253328 VIVEE首發15:23台北；兩篇10/24修改不是新品首發|FP2與VIVEE回查官方後採用。253336鏡頭路線／253333耳機為待查候選；253337與253290折扣不獨立成發布。|
|Yahoo奇摩科技|https://tw.news.yahoo.com/tech-news/ 實際當前內容混一般新聞；https://tw.news.yahoo.com/%E3%80%8A%E8%B3%AA%E9%87%8F%E6%95%88%E6%87%89%E3%80%8B%E6%96%B0%E4%BD%9C%E6%85%98%E9%81%AD%E8%85%B0%E6%96%ACea%E7%AA%81%E7%99%BC%E5%AE%A3%E4%BD%88%E9%97%9C%E9%96%89%E6%97%97%E4%B8%8B%E7%9F%A5%E5%90%8D%E9%81%8A%E6%88%B2%E5%B7%A5%E4%BD%9C%E5%AE%A4-%E9%9B%BB%E7%8E%A9%E5%AE%85%E9%80%9F%E9%85%8D20261022-093723484.html 題載10/22|工作室／遊戲取消線索待官方確認；MacBook觸控螢幕題為預測，PS6價格為傳聞，不採；iPhone開箱本身不算新發布。|
|TechOrange|https://techorange.com/2026/10/23/hugging-face-bio-carbon-x-dna/ 首發10/23 12:36:15台北；https://techorange.com/2026/10/23/1password-for-agents-ai/|Carbon-X模型待官方模型卡與發布日；1Password昨日已收錄排除。10/24 robotics報告不由日期推定在07:56截點前。|
|數位時代|https://www.bnext.com.tw/article/92776/tsmc-2027-revenue-amd-lisa-su-cowos 首發10/23 14:03台北；https://www.bnext.com.tw/article/92752/cxmt-dram-boom-market-cap-ranking 、https://www.bnext.com.tw/article/92753/91app-data-breach-compensation-security-measures 為首頁文章|營收／估值觀點非產品；91APP調查與賠償是事故進展，不當新產品。沒有把頁首播客當全站無新聞。|
|TechNews|https://technews.tw/2026/10/23/nvidia-to-connect-576-rubin-ultra-gpus-using-cpo-to-create-one-giant-gpu/ 、https://technews.tw/2026/10/23/made-for-iphone-duo/ ，當日網址與首頁|架構及標籤候選待官方具體發布日／變更核實；https://ccc.technews.tw/2026/10/23/htc-vivee/ 作VIVEE發現補充，地區仍以官方為準。|
|OpenAI|https://openai.com/index/securing-our-frontier-model-training-environment/ ，首頁官方10/23公告；首頁其他GPT-6普及10/7已逾窗|訓練隔離為內部安全研究措施，未作對外產品新聞；10/7不因仍首頁而刷新。不是因存取失敗排除，今日scan成功。|
|INSIDE|https://www.inside.com.tw/article/42714-spotify-s-new-in-vehicle-app-debuts-on-audi-models 首發10/23 11:46:03台北、修改11:45顛倒保留；https://www.inside.com.tw/article/42694-KBox%20F 為首頁候選|Spotify車載及KBox待官方日期／供貨核對，未稱不存在。https://www.inside.com.tw/article/42717-anthropic-ipo-valuation-customer-concentration-model-safety 為IPO估值評論不作新品。|

第二輪定向回查Sigma英文／日文newsroom與產品頁、HTC新聞稿及hivivee產品／隱私註解、OpenAI官方首頁安全公告；Sigma與HTC完成產品核實。其他未核實候選不為湊數而納入，也不宣稱全站只存在兩則。選擇兩則已核實獨立產品事件，符合1–10則。

## 全球定稿時間與續報

- G1新華社 https://www3.xinhuanet.com/politics/20261023/a83bfd039e0f446e988ed08891691fd7/c.html 首發10/23 11:06:50台北＝03:06:50Z，公布撤離12,489人，當時65傷；https://www3.xinhuanet.com/politics/20261023/8b16e009b30e481f9509e3e5a8f998db/c.html 22:02:26台北＝14:02:26Z，載15時記者會16死76傷、339戶倒塌或受損。地震10/22 22:33在24h窗之前；採用的是10/23新救援／統計，不說主震今日發生。兩條不同時間資料不平均；官媒數字非獨立逐戶驗證。
- G2 CBS／AFP https://www.cbsnews.com/news/jordan-shooting-greek-orthodox-church-karak/ Python正文成功（web工具失敗已補查）。JSON-LD datePublished10/23 09:39-04＝13:39Z＝21:39台北；11:36 EDT是更新。內政部長7死34傷、Hammoud教堂葬禮槍擊；未定肇事組織。Petra官方三日哀悼21:42約旦時間，僅佐證政府措施，不作傷亡原始依據。
- G3 CNA https://focustaiwan.tw/video/004357078 首發10/23 21:25台北＝13:25Z，颱風各地災損與高雄路樹擊車2傷；另核對 https://eng.nmc.cn/typhoon/publish/forecasts/tcs-message.html 10/24 06:04台北頁的10/23 22Z分析，在截點前，但不把不同風速平均期間直接混用，也不作即時安全指南。
- G4 AP https://apnews.com/article/34175023d59ded8d4d3f82baa7087f1b 首發10/23 09:49:52Z＝17:49:52台北；ABC原始AP轉載 https://abcnews.com/amp/Business/wireStory/drone-hit-sank-cargo-vessel-new-black-sea-137505770 已讀。Khoryv、13船員、9救起、1死3失蹤；10/14前次保加利亞附近Dignity／Chelsea3，此次不同船與日期，標續報。總統歸責俄羅斯是表態，不冒稱獨立鑑識定案。
- G5 AP https://apnews.com/article/6424dff433a4f99f00cac2328de0f7a4 首發10/23 08:51:48Z＝16:51:48台北，希伯崙附近新襲擊與封鎖準備。https://egyptian-gazette.com/world/israel-prepares-to-close-west-bank/ 交叉；2士兵死亡、3輕傷屬軍方說法，不把準備封鎖寫成已全面完成。新增lookup希伯崙／Hebron／西岸封鎖未命中，不重複。
- G6 AP經KSAT https://www.ksat.com/news/world/2026/10/23/many-feared-trapped-as-a-tall-building-collapses-in-kenya/ metadata首發10/23 13:11:31Z＝21:11:31台北；AFP官方 https://www.afp.com/en/rescuers-search-seven-people-nairobi-building-collapse 23:13頁、肯亞KBC https://www.kbc.co.ke/rescuers-have-established-contact-with-those-missing/ 當日補查7人失蹤、67工人66逃出1傷、11商店。AFP頁時區未明不把23:13當UTC首發；事件與部長聲明均為當地10/23，截點前可見。樓高12／16／18層報導不同，正文只寫多層。
- G7 AP https://apnews.com/article/0208e62321f811e3003460f71b7fcc89 10/23 10:05:46Z＝18:05:46台北；原頁403由搜尋完整wire正文補查。10/23前次里昂禁令；新7萬部署及羅浮宮等10/24閉館為續報，不把已知禁令重新當唯一新事實。
- G8 NHC https://www.nhc.noaa.gov/archive/2026/ep22/ep222026.public.010.shtml Python取得成功；10/23 21:00Z＝10/24 05:00台北，最大持續風165km/h、971hPa、Acapulco南南西685km、無沿岸watch/warning。以第10報為截點前快照，較早AP第8報／部分網站「今晚登陸」與官方不符不採；預測可能達大型颶風不是已達三級。
- G9 Reuters https://northlandnewsradio.com/2026/10/23/south-korea-proposes-talks-with-north-korea-on-land-border-again/ 10/23正式再提會談，保留日期，不把轉載12:52AM任意轉時區。10/22前次北韓廣播心理戰，本次新南韓軍事會談提議；前一年11月提議是背景，北韓尚未同意，地雷歸責有分歧。
- G10 https://www.nzdf.mil.nz/media-centre/news/chief-of-defence-force-resigns/ 及 https://www.beehive.govt.nz/release/chief-defence-resigns 官方10/23日期；AP經News4Jax https://www.news4jax.com/news/world/2026/10/23/new-zealands-military-chief-resigns-after-admitting-to-an-inappropriate-relationship/ 首發04:42:54Z＝12:42:54台北。國防部長明列Rose King先代理至週日、再Mat Williams；NZDF簡述交接Williams，不抹除短期安排。已轉交Inspector-General，非刑事定罪。

## 逐篇圖片核對

|項目|原文與og實際結果|採用／省略|
|---|---|---|
|T1 VIVEE|官方 https://www.hivivee.com/media/filer_public/fed-assets/pdp-vivee/images/meta-image.jpg 下載且目視1200x630，三款裝置彩色宣傳合成圖；HTC新聞稿亦有產品圖|採assets/vivee.jpg，標官方宣傳非實拍；著作權屬HTC，不宣稱自由授權。|
|T2 FP2|官方og https://www.sigma-global.com/assets/og_image.jpg 為通用圖；正文 https://www.sigma-global.com/en/news/images/01_PPhoto_FP_Beauty_front.jpg 下載目視1500x1200僅見FP標記，不能充分排除舊FP|不採且刪除本次下載檔；不是無圖片，不用舊機型補圖。|
|G1 西藏|新華社正文有記者會照片，原始 https://www3.xinhuanet.com/politics/20261023/8b16e009b30e481f9509e3e5a8f998db/wJwAdXnFybu2jTWm.jpg ，丁增尼達攝；og未提供|照片存在，未核實再利用授權，省略。|
|G2 約旦|CBS og https://assets3.cbsnewsstatic.com/hub/i/r/2026/10/23/b32878bb-9351-47af-9fa9-2651c4d6b7d3/thumbnail/1200x630/d46d27b429d95d44a4cc5465a012f137/gettyimages-2301101623.jpg ；另有Al Arabiya經Reuters影片截圖|AFP／Getty及影片權利未核實，省略，不稱無圖。|
|G3 台灣|CNA原頁og https://img.youtube.com/vi/hrWcg7avLQE/maxresdefault.jpg 為當日新聞影片縮圖|圖片存在，未核實CNA再利用條件，省略，不自動擷取新聞影片。|
|G4 黑海|AP原頁web讀取失敗；ABC AP轉載og https://s.abcnews.com/images/US/weekday_headlines_hpMain_16x9_992.jpg 為通用新聞圖，正文描述內政部影片|不以通用圖當船難現場，未取得可確認原始事件影像，省略。|
|G5 西岸|AP原頁HTTP403，web亦失敗；新聞文字以搜尋與可靠轉載核實|來源存取失敗無法完整稽核該頁og，不推斷無照片，省略。|
|G6 肯亞|KSAT AP og https://bc.gmg.io/image/upload/c_thumb,q_auto,w_700,f_jpg/media/gmg/HVKR3T2DSBCDVOHYS5ZM66RLH4.jpg?api_key=ksat_9a37fc89631abedf ，AP Brian Inganga；AFP Tony Karumba現場圖亦可見|照片存在，通訊社授權未核實，省略。|
|G7 法國|AP原頁HTTP403；搜尋完整正文可讀，原圖／og仍未成功取得|省略，存取失敗不代表沒有圖片。|
|G8 Vance|已讀NHC第10報，文本頁只有NOAA／NWS／機關標誌；archive另提供Graphics Archive，尚未下載核對圖層時刻|省略；不稱所有官方資料都無圖，不拿10/21舊衛星照冒充最新強度。|
|G9 南韓|Reuters轉載og https://storage.googleapis.com/media.mwcradio.com/mimesis/2026-10/23/2026-10-23T055325Z_2_LYNXMPEM9M0C8_RTROPTP_3_SOUTHKOREA-USA-MILITARY.JPG|圖片存在，Reuters授權未核實，不作會談已舉行的配圖。|
|G10 紐西蘭|NZDF og https://www.nzdf.mil.nz/assets/Uploads/Blog/Chief-of-the-NZDF-announces-awards-for-Whakaari-White-Island-response_kiwi__FillWzEyMDAsNjAwXQ.jpeg 是舊活動圖；AP轉載有2024年資料照|不作當日辭職現場，權利及日期限制省略；Beehive頁未見og不等於其他來源無圖。|

所有圖像取捨逐篇分開。僅一張官方相關產品宣傳圖採用；完整來源與權利在presentation JSON。不宣稱已實測使用者iPhone或App接管。
