# 2026-11-01 來源筆記

研究截點：2026-11-01 07:58:14（Asia/Taipei）；ISO 2026-11-01T07:58:14+08:00；UTC 2026-10-31T23:58:14Z。
全球24小時窗：2026-10-31T07:58:14+08:00至2026-11-01T07:58:14+08:00；UTC 2026-10-30T23:58:14Z至2026-10-31T23:58:14Z。
科技／AI 產品 14 日視窗：2026-10-18T07:58:14+08:00至2026-11-01T07:58:14+08:00；UTC 2026-10-17T23:58:14Z至2026-10-31T23:58:14Z。

- begin成功，legacy及原同對話08:00排程不變。只讀10/18–10/31十四份日報建立32列同窗表，未查完整歷史或舊來源筆記。
- 十二站scan完成；實際讀取證據source-scan-20261031T235826957431.json留私人快取，The Verge截斷，須補查。scan不等於選題完成。
- 第一輪官方線索：Mistral newsroom列10/29 https://mistral.ai/news/mistral-large-4-oss/ ，與10/6預覽不同頁；Apple Developer10/29 https://developer.apple.com/news/?id=w9mxlhek 及 https://developer.apple.com/tw/support/adjustments-to-the-taiwan-storefront/ 明列10/31台灣佣金30%降26%。待完成逐站發現及十四報去重才決定。

## 第一批官方核對與去重

- lookup初次PATH缺rg失敗，不當作無命中；補回既有codex-path後成功，查詢 `Mistral.*Large.*4|Le Chonk|mistral-large-4|App Store.*26|佣金.*26|w9mxlhek|台灣.*抽成` ，10/18–10/31十四報0命中。無命中後完整讀32列同窗表，兩事件仍無重複，保留。未讀歷史來源筆記；待查線索不等於已收錄事件。
- Mistral https://mistral.ai/news/mistral-large-4-oss/ 本次明寫釋出改進版權重，官方newsroom列10/29；不是把10/6預覽改時間。已讀Built for Builders（low/medium/high，high預設）及Defenders（一般權重與嚴格審核專用資安版本分開）。https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B/raw/main/README.md ：約1T總參數，49B每token啟用，含embeddings/output約52B；1M上下文，文字與圖片輸入。https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B/raw/main/LICENSE 實際讀取：Mistral Ecosystem Open-Weight License是修改MIT，MaaS業者商用須另簽商業授權，內部使用例外；不寫成無限制MIT或所有人可免費代管API。模型卡39語言標籤與正文160+不同層次，不額外宣稱所有語言品質。
- Apple Developer10/29原始公告及繁中支援頁皆確認10/31生效，iOS/iPadOS台灣店面標準IAP與付費App佣金由30%至26%；不用先簽新版條款才享調降。https://developer.apple.com/support/terms/apple-developer-program-license-agreement/ Attachment15可核對。官方公平會公告由行政院原樣轉載 https://www.ey.gov.tw/Page/88F151FFCE5C741E/21914069-70cc-4efe-919a-e7f0057ecfd0 （10/30），接受承諾並保留不履行時恢復調查，不是全面免抽成。入選基準為10/29正式政策公告；不是折扣導購或把生效日假裝首發。

## 第一輪逐站最新文章檢視

十二站均已實際讀首頁連結；每站的候選與排除如下，截斷與舊／雜訊頁仍續做補查，不聲稱全部線索已查清。

|站點|檢視文章／日期線索|處理|
|---|---|---|
|Engadget|https://www.engadget.com/2302896/what-happens-when-ai-starts-self-replicating/ ；https://www.engadget.com/2301962/bolt-graphics-powers-on-first-zeus-gpu/ ；https://www.engadget.com/2294413/easysmx-s10-lite-review/|AI風險解說非產品釋出；Zeus首次上電為具體路線候選、EasySMX評測須先查官方發布日期，不直接判舊聞；Googlebook／MacBook則回官方及同窗歷史核查|
|The Verge|https://www.theverge.com/gadgets/1013375/muse-charm-gadgets-preview-waveshare-esp32-claude-vibe-code ；https://www.theverge.com/tech/1022592/apple-homeview-amazon-echo-show-16-smart-display-family-computer|自製AI裝置與智慧螢幕評述，實際供應狀態未核，不當作一般新品；首頁截斷須逐篇補讀|
|TechCrunch|https://techcrunch.com/2026/10/31/judge-allows-naacp-lawsuit-over-xai-data-center-pollution-to-move-forward/ ；https://techcrunch.com/2026/10/30/ollie-a-privacy-focused-ai-assistant-is-shutting-down/|訴訟非產品功能；Ollie停用待官方時程，不直接排除；募資與股價亦非新品|
|WIRED|https://www.wired.com/review/backup-by-biolite/ ；https://www.wired.com/review/keurig-alta-brewer/ ；https://www.wired.com/story/kernel-panic-volta-autodoxer-ai-infostealer-malware/|兩評測帶新品線索須回查官方首次發布；惡意程式報導為資安研究不是產品可用性更新；特價不補數|
|Ars|https://arstechnica.com/space/2026/10/think-you-can-save-the-hubble-space-telescope-nasa-wants-to-know/ ；https://arstechnica.com/gadgets/2026/10/fujifilm-to-boost-tape-production-5x-as-ai-fuels-archiving-demand/|十月路徑但精確事件待核；NASA徵案與磁帶增產投資不直接當新產品，評論／亡故回顧不入科技|
|Cool3c|https://www.cool3c.com/article/253633 、https://www.cool3c.com/article/253632 、https://www.cool3c.com/article/253600 、https://www.cool3c.com/article/253599|DJI及Zikko標題為特價，vivo台灣上市待官方；不因促銷刷新首次上市日，折疊機品質傳聞排除|
|Yahoo科技|首頁實際被政治與地方新聞混入，僅部分10/30遊戲影片；https://tw.news.yahoo.com/tech-news/|不是沒有科技新聞，將逐站搜尋補查。AppStore降佣已有明確官方線索|
|TechOrange|https://techorange.com/2026/10/30/mistral-large-4-open-weights-cybersecurity/ ；https://techorange.com/2026/10/31/private-cloud-outlook/|前者核官方OSS頁與LICENSE後保留；後者市場調查非獨立產品；10/28Genie4仍待官方公開測試狀態|
|數位時代|https://www.bnext.com.tw/article/92783/ai-reasoning-prompt-six-frameworks-chain-of-thought-self-consistency ；92788台大引擎文章|首頁舊稿／教學，不據此認定無新品，待本站RSS或逐站搜尋補查|
|TechNews|https://technews.tw/2026/10/30/vivo-x500-series-taiwan/ ；https://technews.tw/2026/10/31/openai-ceo-sam-altman-talk-about-dram/|前者台灣供貨候選；後者談話非新功能，股價財報與投資不當產品|
|openai.com|https://openai.com/index/introducing-gpt-6-1-terra/ 10/26；https://openai.com/index/updated-model-spec/ 10/29|前者同窗已收錄，後者政策與安全研究未指明功能發布，不重列|
|INSIDE|https://www.inside.com.tw/article/42787-google-project-suncatcher-satellite-tpu-gemma-4-first-response 10/31；https://www.inside.com.tw/article/42758-google-gemini-4-carbon-cybersecurity-long-horizon-fairwind 10/29|太空TPU里程碑與Carbon待官方；Rune併購、Naver持股不屬新品，未核線索保持待查|

## 補查與選題結論

- Verge原篇補查 metadata：Muse Charm 10/31 16:05Z，自製裝置線索不直接當商業上市；HomeView評論仍未核供貨。Engadget Zeus 10/31 17:30Z首次上電仍待官方，EasySMX評測也未當成已確認新品。未完成線索不計為不合格總數。
- WIRED BioLite評測回查 https://www.bioliteenergy.com/blogs/gear-guides/backup-progress-report-an-update-for-our-reservation-holders 與 https://www.bioliteenergy.com/pages/backup ：官方說明9月初起出貨、預約預計10月中以前完成，不能以10/31評測刷新事件。Keurig評測回查 https://www.keurigdrpepper.com/category/brand-news/ 及 https://www.keurigdrpepper.com/behind-the-scenes-of-our-keurig-alta-brewer-and-k-rounds-pods/ ：後者僅秋季規畫，最新發布仍待精確日期核對，不判舊、不補數。
- Yahoo雜訊首頁另讀 https://tw.news.yahoo.com/technology/archive/ 並逐站搜尋，找到10/30 App Store消息；以Apple官方日期為準，不用聚合頁顯示時鐘推算首次發布時間。
- 數位時代補查 https://www.bnext.com.tw/rss 為404；本站限定日期搜尋無結果，不能推論無新聞。另讀 https://bnext.transistor.fm/ 最新10/30無人機創業／入股節目，並非獨立產品發布；10/29 Terra與同窗已收錄事件重複。覆蓋有限如實保留。
- 官方定向補查涵蓋Mistral newsroom／模型卡／LICENSE、Apple Developer newsroom／支援條款、BioLite硬體出貨、Keurig產品發布索引、OpenAI發布與Model Spec。科技採兩則已完成官方與去重者，非宣稱所有待查線索都不合格。
- 科技比較鍵：T1 `Mistral.*Large.*4|Le Chonk|mistral-large-4`（公司、模型、權重釋出）；T2 `App Store.*26|佣金.*26|w9mxlhek|台灣.*抽成`（平台、台灣店面、費率條款）。合併lookup零命中後，實際完整讀取同窗32列表，fallback=true（人工讀表）；兩項採用，不以10/6預覽或其他費率制度代換。

## 全球查證、去重與時間依據

lookup範圍僅10/18–10/31十四報，查詢 `Oleshky|奧列什基|卡達|Qatar|G20|波蘭|Poland|索馬利亞|UNTMIS|PMI|同志遊行|Dakar|達卡|Fairfield|FSB|莫斯科.*攻擊` 。命中10/31卡達赴德黑蘭、10/29奧列什基停火、10/31 G20開幕取消合照。三項以續報列出不同狀態；其餘未命中。沒有讀舊來源筆記或完整歷史表。

|項目|事件／時間依據（UTC及台北）|採用與界線|
|---|---|---|
|1 伊朗杜哈會談|Reuters 10/31 14:57Z（台北22:57）報導、更新19:22Z；ToI同日更早確認，故顯示日期而不冒稱Reuters是全世界首發|新增實際赴杜哈，不是10/31已收錄德黑蘭接觸；非直接美伊談判、非協議|
|2 中國PMI|國家統計局10/31 09:30+08，01:30Z；只保留日期顯示，正文記原分鐘精度|49.3對9月50.1；非GDP增幅。官方生產49.8、新訂單49.4、非製造49.7、綜合49.7、高技術51.3|
|3 奧列什基|AP 10/31現場記錄邊境抵達與家屬重逢，ABC顯示05:39AM、更新17:00:19Z；首發時區不強猜，事件日足以落窗|10/29停火後的實際撤離；750是規畫容量，不是實際人數|
|4 波蘭|Polskie Radio 10/31 10:20 CET=09:20Z=17:20+08|採週六召集緊急會談，而非把週五較早衝突改日。各方法律指控並列|
|5 G20|10/31結束；CNA metadata 11/1 07:32+08=10/31 23:32Z，更新07:58+08仍早於07:58:14截點|AP首發可能預寫，改用CNA會後全文確認；主席聲明不等於聯合承諾|
|6 UNTMIS|UN News10/31發布，metadata 05:00Z=13:00+08；任務10/31結束|10/30儀式為背景，不以儀式日期混淆生效日；約25個UN實體仍在|
|7 莫斯科|Reuters／WSAU10/31 11:36AM美中時間=16:36Z=11/1 00:36+08|新威脅與園區限制；非已發生攻擊，舊案傷亡不挪用|
|8 Fairfield|事件10/30約20:30PDT=10/31 03:30Z=11:30+08；FOX10/31 07:18PDT首發、14:58PDT更新|1死6傷；懷孕家屬說法尚待確認，嫌犯未確認，不重複錯誤城市方位|
|9 Dakar|ANOC10/31官方資訊；AFP／Channels10/31 17:21:40Z=11/1 01:21:40+08發布|確認10/31開賽，不用開幕預告冒稱儀式結束；2655是官方規畫不是最終統計|
|10 台灣同志遊行|CNA10/31 17:45+08=09:45Z首發，19:22+08更新；當日約14:30出發|17萬是主辦估計，活動前15萬預測不是矛盾實測|

來源完整URL逐則保留於日報。G20補讀 https://www.cna.com.tw/news/aopl/202611010009.aspx 全文，與AP一致但記錄外交官稱主席聲明原即預計；不寫為臨時決定。AP直接403及web open錯誤，改搜索可讀正文、ABC／FOX／CNA可靠轉載；SeattlePI槍擊頁回challenge空內容，不稱沒有照片。Reuters StreetInsider403，改讀WSAU原線稿。

排除：黑海船舶10/31報導實為10/28攻擊、10/29沉沒；印度氣旋死亡與尋獲遺體主要週四週五，未能確認新增事件落窗；南極會議10/30結束無精確時間，不能用10/31評論補位。未把盤後重刊、評論、聚合頁或舊PDF當新事件。

## 逐篇圖片與權利稽核

已逐篇檢視原文img及og:image。未刊不等於原文無圖；授權及資料照日期另判。

|項目|原圖／檢查結果|使用決定|
|---|---|---|
|T1|https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B/resolve/main/images/coding_index.png|下載並目視核對模型卡比較圖，採用、contain、明標非本報實測。另取官方封面webp留作來源素材但不採用，避免泛化行銷#1字樣|
|T2|https://developer.apple.com/news/images/og/apple-developer-og.png|只有通用Developer社群圖，未當新操作介面|
|1|https://hermes.media.transform.aol.com/a529d4281b2fea656fd44be943929b7ba5738bb7/w_1200,c_scale,f_auto,q_auto/https://hermes.media.static.aol.com/media/2026/10/31/afd18c39-8041-3674-ae18-4f9314e78992/dede4cb3-c54c-4249-a57d-13f9a84704a9.jpg|Reuters伊朗街景資料照，非杜哈會談現場；未另取得轉載授權，不刊|
|2|https://hermes.media.transform.aol.com/8f590bb12fe2bd03a0638d4b35356a8154b44d02/w_1200,c_scale,f_auto,q_auto/https://hermes.media.static.aol.com/media/2026/10/31/ffed22de-8027-3653-a35a-83880fa50c69/97c6cb91-141b-4241-9fe8-71745b8e6b43.jpg|官方頁為標誌，Reuters有工廠資料照；未另取得轉載授權，不刊|
|3|https://i.abcnewsfe.com/a/9e79d727-77d5-4d54-9d9c-10d860364b61/wirestory_5cbc7d2a5b8ac34b15c914338fd5a9f3_16x9.jpg?w=1600|AP／Efrem Lukatsky重逢現場照存在，未另取得授權不刊|
|4|https://static.prsa.pl/images/68649aab-4972-4aae-97ed-93bdf1711bc4.jpg|PAP／Radek Pietruszka警察場景照存在，未另取得授權不刊|
|5|https://imgcdn.cna.com.tw/www/webphotos/WebCover/800/20261101/1778x1332_14896955310.jpg|CNA引用美國國務院flickr會議圖；原flickr特定圖權利未續查，不擅認公共領域，不刊。AP403不是無圖|
|6|https://global.unitednations.entermediadb.net/assets/mediadb/services/module/asset/downloads/preset/Collections/Embargoed/2026/10/30-10-2026-UN-Photo-Raisedon-Zenenga.jpg/image1170x530cropped.jpg|已下載目視，UN Somalia／Adihamiid Mohamed；採用，caption明標10/30結束任務儀式資料照|
|7|https://media-cdn.socastsrm.com/uploads/station/1946/fbShare.png?r=67880|WSAU社群圖為電台標誌，非園區事件圖，不刊|
|8|https://images.foxtv.com/static.livenowfox.com/www.livenowfox.com/content/uploads/2026/10/1200/630/large-police-presence-at-solano-town-center-in-fairfield.jpg?ve=1&tl=1|FOX警方現場影像存在，未另取得轉載授權，不刊；SeattlePI空內容不算無圖|
|9|https://www.anocolympic.org/wp-content/uploads/2026/10/2773399-scaled.jpg ；https://www.channelstv.com/wp-content/uploads/2026/10/Youth-Olympic-Games.jpg|前者OIS／Jon Buckle，後者AFP／Patrick Meinhardt的10/29場館資料照；不冒充開幕現場，未另取得授權不刊|
|10|https://imgcdn.cna.com.tw/www/webphotos/WebCover/800/20261031/1778x1334_054836645893.jpg|CNA鄭清元／徐肇昌當日圖輯存在，未另取得轉載授權，不刊|

採用圖只作署名新聞說明，未宣稱公共領域或獲得超出原來源的授權。日報2科技＋10全球，各一次，三則全球續報具前次日期及新增事實。Safari/iOS接管與實體iPhone未測，後續以既有renderer、發布驗證及唯一watchdog完成。
