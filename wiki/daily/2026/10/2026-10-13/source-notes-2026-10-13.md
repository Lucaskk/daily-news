# 2026-10-13 來源筆記

研究完成；發布與配送結果以私人 production checkpoint 與完成檢查為準。

- 凍結截點：2026-10-13 08:01:29 Asia/Taipei（2026-10-13T00:01:29Z）。
- 全球24小時窗：2026-10-12T08:01:29+08:00 至 2026-10-13T08:01:29+08:00；UTC 2026-10-12T00:01:29Z 至 2026-10-13T00:01:29Z。
- 科技／AI 產品 14 日視窗：2026-09-29T08:01:29+08:00 至 2026-10-13T08:01:29+08:00；UTC 2026-09-29T00:01:29Z 至 2026-10-13T00:01:29Z。
- 去重僅查2026-09-29至2026-10-12的14份日報；同窗產品表72列。未讀完整歷史表。
- legacy模式，12站scan於2026-10-13T00:01:44至00:01:47Z完成；原始快取留私人目錄，不加入Git。OpenAI及INSIDE scan失敗，已用web首頁補查；Yahoo與Bnext web失敗，待查scan內容與逐站搜尋；TechNews web為舊快取，須補查。

## 第一批候選

- Meta Muse Wonder：10/12官方產品發布線索，待官方全文與14日去重。官方 https://dev.meta.ai/models/muse-wonder 、 https://research.meta.ai/blog/muse-wonder 。Engadget與TechCrunch、WIRED及Axios均有同日報導，不將討論量當成定量排名。
- Engadget首頁同時有Fitbit Edge正式發布、Smart巴黎新車、No Man's Sky iOS產品路線；需區分前次預告與真正獨立事件，不用評測或傳聞補位。
- 全球候選：經濟學獎頒給Hall／Woodford；Saudi防空失效調查；Ukraine週一能源攻擊／暫停反擊聲明；墨西哥政府週一確認風災死亡；New Delhi週一更換抗議地點。前次主線待lookup，未選定。
- 排除暫存：Nobel舊得主清單、歷史今日、當日照片集不單獨占新聞名額；Pillay專訪若只有評論不算正式制裁新進展。

## 逐站查閱與補查

scan 是取得紀錄，不代表選題完成。以下為逐站首頁最新文章／逐站搜尋與原始文章的實際檢查；選取的是已核實項目，不聲稱其他候選均不合格。首頁時間可能晚於凍結截點，只有發布／事件本身在截點前的消息可入選。

| 來源 | 實際文章／檢查網址 | 發布日期與判斷 |
|---|---|---|
| Engadget | https://www.engadget.com/2284478/meta-says-its-caught-up-to-the-frontier-with-its-latest-wonder-ai-models/ | 10/12，Wonder 線索回查 Meta，採用。首頁另有 Smart 巴黎車展及 Fitbit；前者具體官方首發時間未充分定位，不採；後者已追蹤。 |
| The Verge | https://www.theverge.com/ai-artificial-intelligence/1009479/meta-muse-wonder-full-ai-model ; https://www.theverge.com/news/1009465/microsoft-maia-300-chip-improvements-rollout （10/12 17:00 UTC Wonder、13:00 UTC Maia 300） | 另見14:00 UTC No Man's Sky，三項回查官方並採用，不從100字額度首頁搬用規格。Apple 10/13 智慧家庭發表前傳聞不採。CMF Speaker Series 為其他新品線索，未作本次入選依據。 |
| TechCrunch | https://techcrunch.com/2026/10/12/meta-releases-its-first-frontier-model-muse-wonder/ ; https://techcrunch.com/2026/10/08/google-releases-a-new-local-first-granola-competitor/ | 10/12 Wonder、10/8 06:28 PDT Foresight。僅用後者定位首次可靠發布時間；功能依 Google 官方，不從受限25字媒體來源摘要。 |
| WIRED | https://www.wired.com/story/muse-wonder-puts-meta-back-at-the-ai-frontier | 10/12 17:00 UTC；原文工具讀取失敗，首頁與逐站搜尋取得同題，再改查 Meta 官方。Kindle／AlterMe 評測線索未直接視為新品事件。 |
| Ars Technica | https://arstechnica.com/gaming/2026/10/after-a-10-year-redemption-arc-no-mans-sky-is-coming-to-the-iphone-and-ipad/ | 10/12，採 Apple 官方新上市日公告；首頁另有 Amazon 機器人專題及 Epic AI-first 傳聞，不作產品發布。 |
| Cool3c | https://www.cool3c.com/category/product ; https://www.cool3c.com/article/252801 | scan／直接HTTP403，web首頁曾空內容，改逐站搜尋及產品分類頁取得 Alexa Tablet、Sony ECM-AX10、Sigma 50–120mm、MSI 掌機線索。Sigma 原始事件10/8、10/9已收錄；Alexa亦10/9已收錄。Sony原始公告10/8，採用；分類相對「幾天前」不作精確發布依據。 |
| Yahoo奇摩科技 | https://tw.news.yahoo.com/tech-news/ ; https://tw.news.yahoo.com/no-man-sky-%E5%8D%81%E5%B9%B4%E7%A3%A8%E5%8A%8D-%E5%A4%AA%E7%A9%BA%E6%8E%A2%E7%B4%A2%E5%B7%A8%E4%BD%9C%E7%99%BB%E9%99%B8-225704047.html | web讀取失敗，scan及直接HTML成功；首頁連結 No Man's Sky，回查10/12 Apple公告採用，不以Yahoo較晚轉載時間判斷。混入國家公園電影／政治新聞不屬科技產品。 |
| TechOrange | https://techorange.com/2026/10/12/china-s-delivery-robots-learning-tackle-night-shift/ | scan失敗，web首頁／逐站搜尋成功。10/12夜間配送文，內文深圳3月／京東4月營運，不當10月新品；同日ASML Hyper NA分析、TeamT5治理專題不採。H-JEPA研究線索未當消費產品發布。 |
| 數位時代 | https://www.bnext.com.tw/article/92466/gemini-skills-how-to-write-free ; https://www.bnext.com.tw/article/92570/furbo-tomofun-ai-subscription-pet-camera | web失敗，scan／直接HTML與fetch成功。Skills文章10/9，內文原始事件9/30，與既有Skills事件比對，不因首頁重刊再選；Furbo商業訪談沒有可定位新品發布。 |
| TechNews | https://technews.tw/2026/10/13/microsoft-maia-300-to-begin-production-deployments-in-2027/ ; https://technews.tw/2026/10/12/apple-acquires-ai-audio-startup-huxe-talent-acquisition-voice-interaction-tech/ | web首頁舊快取，直接HTML／fetch補查成功。Maia文10/13 02:14 TPE、事件10/12官方，採用。Huxe收購不等於具體新產品。首頁財報、投資、ASML預測不補位。 |
| OpenAI | https://openai.com/news/ ; https://openai.com/index/gpt-6-for-everyone/ | scan失敗，web最新列表成功，10/7 GPT-6／Intelligent UI事件10/8已收錄；10/8 false-front安全行動不是產品發布。 |
| INSIDE | https://www.inside.com.tw/article/42617-google-ai-edge-foresight-mac-offline-ai-meeting-notes | scan失敗，web首頁及fetch文章成功；10/12 15:05:28 TPE轉介10/8 TechCrunch，不誤標今日發布。另見Meetings外掛、REA與FDX Fusion線索，未以缺乏定位的摘錄入選。 |

第二輪定向官方補查：Meta research／newsroom、Apple Newsroom／App Store、Google Foresight官方內嵌頁、Sony公司發布的PRNewswire新聞稿、Microsoft Maia官方部落格、Google Fitbit官方發布與Smart媒體索引。選取5項已核實獨立變更；沒有湊滿10項。

## 科技候選時間、去重與官方段落

所有 lookup 使用 `--cutoff 2026-10-13T08:01:29+08:00`，僅9/29–10/12十四份日報。最後窄查 `Maia.*300|Sony.*ECM-AX10|ECM-AX10|Google.*Foresight|No.Man.*Sky|Muse.*Wonder` 無命中，隨後核對同窗 recent-14d 表；表內 EmbeddingGemma 2 是模型發布，不是 Foresight 應用推出。沒有讀舊來源筆記或完整歷史表。

| 項目／比對鍵 | 首次發布／事件基準 | 官方段落、判斷與歧異 |
|---|---|---|
| T1 Meta／Muse Wonder／2026-10-12-release | 官方10/12日期；頁面00:00Z屬日期佔位，不渲染午夜 | https://research.meta.ai/blog/muse-wonder ; https://about.fb.com/news/2026/10/introducing-muse-wonder-models/ 。Takeaways明確分開Wonder今日API／Muse Code，Full今日限Muse Code訂戶，Muse消費端soon。Active Memory／Active Focus段落；安全完整報告soon，不宣稱已獨立驗證。 |
| T2 Microsoft／Maia 300／2026-10-12-announcement | 官方10/12日期；TechNews10/13 02:14 TPE在截點前 | https://blogs.microsoft.com/blog/2026/10/12/microsoft-to-expand-azure-maia-system-to-multi-gigawatt-deployments/ 。開頭及末段明訂2027 production deployments；Key capabilities列N2P、8組HBM4、18TB/s、950W。效能40%為預期且比較基線不完整，不寫已量產或實測勝NVIDIA。 |
| T3 Apple／App Store Indie Games Week／2026-10-12-mobile-availability | 官方10/12日期 | https://www.apple.com/newsroom/2026/10/app-store-indie-games-week-kicks-off-today/ 。首段7款download或pre-order；No Man's Sky段落明訂10/28 iPhone／iPad，包含Cosmos；最後段四款available now。整體作1項新手機平台供應事件，不拆7則，不把未來上市當今日已上市。 |
| T4 Google／AI Edge Foresight／2026-10-08-release | TechCrunch頁首10/8 06:28 PDT＝13:28Z＝21:28 TPE；官方頁有下載但無日期 | https://developers.google.com/edge/foresight 。官方外框只有iframe，fetch內嵌頁後確認Automated Synthesis、Local Knowledge、Meeting Intelligence、FAQ：on-device Gemma、Apple Silicon、離線、檔案與逐字稿本機。日期以TechCrunch首次報導，功能以官方；INSIDE10/12非首發。沒有將既有EmbeddingGemma2再次收錄成模型新聞。 |
| T5 Sony／ECM-AX10／2026-10-08-announcement | Sony新聞稿10/8 12:00 ET＝16:00Z＝10/9 00:00 TPE，這是真實精確時間非日期佔位 | https://www.prnewswire.com/news-releases/sony-electronics-announces-the-worlds-first-eclipsa-audio-certified-spatial-audio-microphone-for-smartphones-302902696.html 。首段4全向麥克風；註3 iOS18／Android14 USB-C，註6部分錄影編輯需專用App／相容清單，註8 4K錄製預計12月後，不寫現在所有手機全功能。 |

排除：`Sigma.*50-120|Alexa.*Tablet`命中10/9同發布；`Fitbit.*Edge`命中10/10預告，10/12正式介紹雖有新規格／預購，但本次優先獨立新產品而不以已追蹤主線補位。Smart新車官方首發定位不足，保留待查，不稱其無新品。Gemini Skills窄查及表格顯示9/30已收錄，導覽文不是再發布。

## 全球十則的時間與去重依據

排序是國際媒體／官方重要性綜合，不是經計算的全球社群討論排行。AP與Reuters、EFE、官方英國／歐盟／AEA互補；Techmeme river可見Wonder多媒體聚集訊號，不把聚合站當原始規格來源。

| 排名 | 新事件／首次可靠發布基準 | 去重與新增內容 |
|---|---|---|
| 1 經濟學獎 | AEA官方10/12公告：https://www.aeaweb.org/news/nobel-prize-economic-sciences-oct-12-2026 | `Hall.*Woodford`無同獎項命中；Stanford／Columbia原頁403，改AEA全文核對。AP早於慣例頒獎時間的metadata不採，保留官方日期。 |
| 2 歐盟1569制裁 | EFE first-published 10/12 11:45:56Z＝19:45:56 TPE；正式批准當天 | https://efe.com/mundo/2026-10-12/ue-mayor-paquete-sanciones-selectivas-rusia/ 。窄查1569／俄軍工制裁無同批名單；826企業+743個人，不與另批77人混算。官方Council長網址間歇失敗，EFE全文引用Council與正式公報。 |
| 3 沙烏地防空調查 | AP first 10/12 12:47:35Z＝20:47:35 TPE | https://apnews.com/article/saudi-yemen-houthis-riyadh-airport-40c6ab822df376688ce1a0955a044488 。續報10/12利雅德機場遭襲；新為週一防空失效調查報導，不把週日死者重算。調查由2匿名官員提供，官方未答覆。 |
| 4 烏克蘭能源戰 | AP first 10/12 08:03:58Z＝16:03:58 TPE；正文週一新攻擊與當日訪談 | https://apnews.com/article/russia-ukraine-energy-strikes-trump-ceasefire-6fdef6ff4d033b379c74e1d62183d078 。續報10/12川普週日停攻說法；新為週一基礎設施再遭襲、烏方表示已暫停能源目標攻擊；不是重刊停火宣稱。 |
| 5 法國冷藏駭攻 | Reuters／Internazionale first 10/12 20:35:06+02:00＝18:35:06Z＝10/13 02:35:06 TPE；事發10/11–12夜間 | https://www.internazionale.it/ultime-notizie-reuters/2026/10/12/hackers-heat-french-supermarket-fridges-sparking-fires-and-food-losses 。`冷藏.*攻擊|fridge.*attack`無命中。Reuters稱150家Intermarche；Verge轉AFP稱300家，分母／時間未釐清，保留歧異，不擅自合併。 |
| 6 跨國對伊朗聲明 | GOV.UK first-published 10/12 16:06 BST＝15:06Z＝23:06 TPE；更新17:58不作基準 | https://www.gov.uk/government/news/joint-statement-on-iran-12-october 。續報9/29 Fairford嫌犯保釋／國家關聯線索、10/5轟炸機撤回；新為10/12多國外長聯合承認英國對Iran責任歸屬。簽署清單共32國，早期候選29國已更正；非司法定罪，沒有新增制裁已生效的依據。 |
| 7 墨西哥災情 | AP first 10/12 18:00:56Z＝10/13 02:00:56 TPE；2州長週一確認 | https://apnews.com/article/tropical-storm-flooding-rain-hurricane-cc01ec735f4ff7c11798bc9066dc1879 。續報10/12 Simon風險警告；新為Guerrero老人死亡及Baja California女童死亡、10人失蹤的官方確認；不同風暴Simon與Rachel，非全歸Simon。 |
| 8 歐盟暴利稅評估 | Reuters10/12 Hoekstra訪談，AOL僅顯示17:49 UTC更新，不用URL17:48推測精確首發 | https://www.aol.com/articles/eu-looking-oil-gas-windfall-174810000.html 。`windfall|暴利稅`無同工作組命中；新為Commission組工作組評估；未通過稅法，2022稅率是背景非新方案。 |
| 9 中國車市新數據 | Reuters10/12 CPCA週一公布9月數據；AOL僅顯示05:09UTC更新，保留事件日期 | https://www.aol.com/articles/china-home-car-sales-downturn-050706000.html 。`汽車.*銷售|car.*sales`無同月數據命中；1.63m內銷乘用車-28.1%、923k出口+73.2%，不與全車種混用。 |
| 10 德里抗議地點限制 | AP first10/12 12:36:56Z＝20:36:56 TPE，正文Monday警察行政變更 | https://apnews.com/photo-gallery/india-cockroach-protest-jantar-mantar-9858403e4a62b7e580f84fcd19a4c5e1 。`Jantar|New.Delhi`無同限制命中；雖URL是photo-gallery，選的是週一不再允許Jantar Mantar集會並指定3替代點的新措施，不是照片集本身。 |

## 逐項影像稽核

| 項目 | 原文／og:image查證結果與使用決定 |
|---|---|
| T1 | Meta og https://research.meta.ai/articles/introducing-muse-wonder/social/muse-wonder-social-v1.webp 是文字社群圖，不冒充操作介面；省略。 |
| T2 | Microsoft原頁直接HTTP403，web官方全文有Maia 300 system／at a glance圖；TechNews也有微軟圖。未取得可驗證本機圖檔，不寫無圖，省略。 |
| T3 | Apple有7款遊戲拼圖，原圖 https://www.apple.com/newsroom/images/2026/10/app-store-indie-games-week-kicks-off-today/tile/Apple-App-Store-Indie-Games-Week-01-lp.jpg.og.jpg?202610121817 。使用官方新聞稿配圖，非自由授權，署名Apple／遊戲開發者。 |
| T4 | Google外框og為通用Edge分享圖 https://developers.google.com/static/edge/images/share.png ，TC有Google提供的介面圖但非直接官方圖檔；省略，不稱無圖。 |
| T5 | Sony新聞稿有實物搭手機圖 https://mmx.prnewswire.com/media/MS2004873/Sony-Electronics-ECM-AX10_WithSmartphone_Windscreen.jpg?id=OA2994099&p=facebook ，使用公司提供新聞配圖並標Sony，非自由授權。 |
| 1 | AEA有og https://www.aeaweb.org/content/file?id=2454 ，未確定可重用權利；AP原頁HTTP403，省略。 |
| 2 | EFE原圖 https://efe.com/wp-content/uploads/2026/10/ue-sanciones-rusia.webp 為Kallas／EPA照片，未取得授權，省略。 |
| 3 | AP web有現場照片與圖片授權入口，直接HTTP403導致無法讀og，未取得授權；省略。 |
| 4 | AP web有戰爭影像，直接HTTP403無法讀og；未取得授權，省略。 |
| 5 | Reuters／Internazionale有超市照片 https://media.internazionale.it/images/2026/10/12/361085-hd.jpeg ，未取得授權，省略。 |
| 6 | GOV.UK有外交部建築資料照 https://assets.publishing.service.gov.uk/media/621e4de4e90e0710be0354d7/s960_fcdo-main-building.jpg ，不是Fairford現場；本次不使用。 |
| 7 | AP有風災影像，直接HTTP403無法讀og；未取得授權，省略。 |
| 8 | AOL有Reuters og照片（hermes.media.static.aol.com/media/2026/10/12/aff4710f-d160-3b21-b007-28c3c92dc948/96376148-5faf-460f-8681-fc0256b80e60.jpg），未取得授權；省略。 |
| 9 | AOL有Reuters og照片（hermes.media.static.aol.com/media/2026/10/12/17374afc-11c3-31a4-b1fc-5f025d264cf7/fdf107d5-1460-480a-bdaa-42078055e896.jpg），未取得授權；省略。 |
| 10 | AP原文照片集有抗議照片／授權入口，直接HTTP403無法讀og；未取得授權，省略。 |
