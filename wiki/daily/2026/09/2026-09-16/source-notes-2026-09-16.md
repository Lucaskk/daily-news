# 2026-09-16 來源筆記

- 研究截點：2026-09-16 08:01:48 Asia/Taipei = 2026-09-16 00:01:48 UTC；沿用既有私人 checkpoint，研究模式 `legacy`。
- 全球 24 小時：2026-09-15 08:01:48 至 2026-09-16 08:01:48 Asia/Taipei；UTC 2026-09-15 00:01:48 至 2026-09-16 00:01:48。
- 產品 168 小時：2026-09-09 08:01:48 至 2026-09-16 08:01:48 Asia/Taipei；UTC 2026-09-09 00:01:48 至 2026-09-16 00:01:48。
- 排序以 AP、Reuters、聯合國與官方產品公告的跨來源能見度和影響綜合判斷，不宣稱可量化的全球討論量排行。BBC 新聞頁受 robots 限制；Cool3c、Engadget 已作候選查詢，折扣、導購、舊評測與重刊不入選。

## 先行去重

- 選題前重建科技產品表：571 筆產品變更、90 份日報；模型未完整讀取歷史 ledger 或既有日報／來源筆記。
- 全球候選先以窄化組合 `rg -n -i` 搜尋全部 `wiki/daily/**/daily-news-*.md` 與 `source-notes-*.md`：沙烏地取消歐洲原油貨單、立陶宛實際擊落無人機、美國在軌武器、參院加密法案表決、剛果 C64 示威、美國軍援轉移、沙埃紅海外交、美伊海上無人船衝突、UN 加薩遺骸聲明及英委大使任命均無同一新節點。
- 另以較廣但仍限事件詞的 `rg` 比對既有主線：2026-09-14 已報沙烏地管線停運後燕布庫存僅約 5–7 天；本次是實際通知取消部分歐洲貨單及燕布停止裝船，屬實質續報。2026-09-14 已報立陶宛雷達誤判鳥群；本次 9/15 是另一起有實際擊落的無人機，不能把舊誤報改成真事件。2026-09-14 已報霍爾木茲商船起火；本次為美軍與伊朗兩艘小艇的另一宗海上無人船事件，且雙方說法相反。2026-09-07 已報加薩約百具遺骸集體安葬；本次是聯合國人權高專的新公開法律疑慮，不重報葬禮。

## 產品候選與判定

### T1 Cloudflare AI Crawl Control／Disallow AI Training
- 窄化 `rg` 查詢：`Cloudflare.*(Disallow AI Training|Bot Preference Sync|mixed.use crawlers)|Disallow AI Training.*Cloudflare|Cloudflare.*(Search.*Training.*Agent)|content-independence-day-ai-options|accountable-mixed-use-ai-crawlers`。命中 `product-news-ledger.md:417`、`2026-07-02/source-notes:49`、`2026-07-02/daily-news:171`；因此沒有讀最近 7 天表來比對此項。
- 前次 2026-07-02 已收錄 Search／Agent／Training 類別控制、BotBase 與預告 9/15 預設變更。本次 **2026-09-15 新官方 Product News** 明確推出 `Disallow AI Training` 設定、遷移舊 `Block AI Bots` 與 `Managed Robots.txt`，並讓 mixed-use crawlers 的 Search 與 Training 許可分離。這是新功能與實際遷移，不僅是既有預告到了日期。
- 官方具體段落：`What changes on September 15?`、`Existing domains that never used...`、`Recommendations for new domains`。
- https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/
- 先前預告：https://blog.cloudflare.com/content-independence-day-ai-options/
- Apple、Google、Microsoft 對新偏好機制的遵守狀態與期限不同；不能寫所有多用途爬蟲皆已全面履行。新網域設定也取決於是否選擇廣告營利配置。

### T2 OpenAI ChatGPT Work Data agent
- 窄化 `rg` 查詢：`ChatGPT Work.*Data agent|Data agent.*ChatGPT Work|put.data.to.work`；完整 ledger 與歷史日報／來源筆記無命中，因此完整讀取最近 7 天表 14 列，無同一產品變更。首次收錄。
- OpenAI 官方 Product 公告署期 2026-09-10，落在精確 168 小時窗內；不虛構首次發布時分。
- 官方段落：`Meet the new Data agent in ChatGPT Work`、`Connect to the company data...`、`Get started with the Data agent`。Data agent 在 Plugins 目錄可安裝，管理員決定連線與角色，查詢遵守來源帳號的 table／row／column 權限。
- https://openai.com/index/put-data-to-work/
- 官方列舉多種資料源；Alpha 客戶使用案例不代表所有機構預設可用，須看管理員啟用及來源權限。

### T3 OpenAI Agents API
- 窄化 `rg` 查詢：`Introducing.the.Agents.API|Agents API.*Codex|Codex.*Agents API`；完整 ledger 與歷史檔案無同一變更命中，因此對照最近 7 天表 14 列，無同項。首次收錄。
- OpenAI 官方 Product API 公告署期 2026-09-10，明示 `public beta`；屬開發者新產品入口，非先前 Codex 一般功能公告。
- 官方段落：`introducing the Agents API in public beta`、`Build and run cloud agents with the Codex harness`。具體供應、限制及定價仍應以官方文件查核，本文不填未核實數字。
- https://openai.com/index/introducing-the-agents-api/

### 排除候選
- OpenAI GPT-Live-1 在 ChatGPT Voice 的使用已於 2026-07-24 收錄；後續 9/10 宣傳不能重列同一 rollout。
- OpenAI ChatGPT for Financial Services 9/10 可成獨立候選，但在今日產品排序中低於上述三項；未用產品數量補位。
- Blizzard Diablo IV Switch 2 的 9/15 預定上市已於 2026-09-13 收錄，沒有本窗內新增規格或重大可用性變更證據，不重報預定日期。
- Engadget 7 月文章預告 Cloudflare 9/15 設定，僅作發現；採 9/15 官方新設定與遷移公告作時間依據。Cool3c HTC VIVE Eagle 擴區及圓框內容缺本次可核對的精確新節點／官方交叉證據，未選。

## 全球入選事件／發布時間依據

### 1 續報｜沙烏地取消部分歐洲原油貨單
- Reuters 轉載首發 2026-09-16 02:46 AEST = 2026-09-15 16:46 UTC = 台北 2026-09-16 00:46，落窗；9/15 業界知情來源披露已通知部分歐洲客戶取消 9 月裝船，燕布暫停裝船。
- https://au.marketscreener.com/news/saudi-cancels-some-oil-cargoes-after-pipeline-hit-top-buyer-chasing-alternatives-ce785bddde8bfe24
- 前次 [[daily-news-2026-09-14]] 是庫存 5–7 天與修復時間估計；本次是實際訂單與裝船狀態。Saudi Aramco 拒絕評論，確切取消量及停裝期間未確認。期貨近 108 美元、歐洲現貨基準近 122 美元，口徑不同。

### 2 立陶宛擊落無人機
- AP 2026-09-15 08:17:24 UTC = 台北 16:17:24；當日官方確認北約戰機在立陶宛空域擊落無人機。另有俄船對丹麥直升機施放干擾火光，本文只聚焦擊落事件。
- https://apnews.com/article/russia-ukraine-war-lithuania-drone-downed-nato-9671662649ebed2eca41879982f366ad
- 9/14 所報鳥群誤報與本次不是同一雷達目標；本次無人機來源、目的及是否載炸藥仍待調查，不以官員推測判定俄方責任。

### 3 美國首次承認部署在軌武器
- AP 2026-09-15 12:16:26 UTC = 台北 20:16:26；空軍部長 Troy Meink 週一在會議提出新官方公開說法，AP 於本窗內首次可靠發布。
- https://apnews.com/article/space-weapons-air-force-5a2a0ada771daaf4fbef0991d8c09259
- 未公布武器類型、數量、用途或目標，不把 Golden Dome 未來計畫混作已部署系統。1967 年條約對核與大規模毀滅武器等限制與所有常規武器是否被禁止，需區分。

### 4 美國參院加密法案未過程序表決
- AP 2026-09-15 13:00:30 UTC = 台北 21:00:30；當日 49–50 表決未能推進法案。
- https://apnews.com/article/senate-crypto-bill-midterms-trump-ethics-e3caf262dc138147941787299e5f0a66
- 這是程序阻擋，不是對所有加密資產規範的終局否決；民主黨要求更強的總統及家屬利益衝突限制。

### 5 剛果反修憲示威遭驅散
- AP 2026-09-15 20:21:57 UTC = 台北 2026-09-16 04:21:57；9/15 Kinshasa 與其他城市 C64 示威及警方催淚瓦斯。
- https://apnews.com/article/722684d7da7ffe1d49c44dd03db82904
- 反對派稱修憲可能讓 Tshisekedi 爭取第三任；政府指抗議擾亂活動。修憲尚在討論，未通過、未舉行公投；暴力與傷亡說法待核。

### 6 美國調整 5,200 萬美元外國軍援
- AP 2026-09-15 16:02:25 UTC = 台北 2026-09-16 00:02:25；國務院週二通知國會擬將 FMF 從斯洛伐克、北馬其頓、突尼西亞及伊拉克轉往巴拿馬、秘魯、厄瓜多爾及哥倫比亞。
- https://apnews.com/article/foreign-military-financing-trump-rubio-c92157ab38b809a9faef9fa19be50cf7
- 是資金重新編列通知，不等於所有武器已交付；原受援兩國為北約成員。

### 7 沙烏地王儲赴埃及協調紅海航運
- AP 2026-09-15 18:09:31 UTC = 台北 2026-09-16 02:09:31；9/15 Mohammed bin Salman 與 Abdel-Fattah el-Sissi 新會談。埃及總統府稱雙方強調曼德海峽與紅海航行自由安全。
- https://apnews.com/article/5696629010c86b8cc83f69cbd093e3f1
- https://www.internazionale.it/ultime-notizie-reuters/2026/09/15/egypt-s-sisi-and-saudi-crown-prince-stress-need-security-red-sea-navigation
- 與已報胡塞占島、管線停運不同，今日新節點是雙邊外交；埃及軍事介入並未公布，不能推定。

### 8 美國與伊朗小艇在海上無人船事件說法相反
- AP 2026-09-15 16:34:35 UTC = 台北 2026-09-16 00:34:35；美軍週二首次公開稱擊毀兩艘企圖奪取 Saildrone 的伊朗小艇。伊朗官媒週一較早稱兩艘漁船遭擊及漁民失蹤。
- https://apnews.com/article/iran-war-military-drone-boats-98b49e9a5e10452ae8da42191205ab53
- 小艇性質、死傷及兩方通報是否指同一確切船隻尚未獨立確認。不同於 9/14 商船起火事件。

### 9 聯合國高專對加薩遺骸提出戰爭罪疑慮
- 聯合國新聞稿署期 2026-09-15，日內在 Geneva 公開；Reuters／Times of Israel 9/15 13:08 +03 = 10:08 UTC = 台北 18:08，交叉核對落窗。
- https://www.un.org/unispal/document/un-human-rights-chief-says-recovery-of-remains-in-gaza-three-years-later-adds-to-palestinian-trauma/
- https://www.timesofisrael.com/liveblog_entry/un-rights-chief-says-uncovered-remains-in-gaza-raise-concerns-of-war-crimes/
- UN 頁面直接讀取遭 403，但搜尋索引保留聲明全文摘要；本文只採可核對的公開主張。發現遺骸及高專疑慮不等於戰爭罪已被法院裁判。與 9/7 葬禮是不同公告。

### 10 英國任命駐委內瑞拉大使
- Reuters／MarketScreener 初版 2026-09-15 16:14 +03 = 13:14 UTC = 台北 21:14；英國政府 9/15 通知議會提高外交關係層級。
- https://sa.marketscreener.com/news/britain-upgrades-diplomatic-relations-with-venezuela-ce785bdddc89ff24
- 英國明稱此舉不承認 2024 年爭議選舉或支持任何派系；外交接觸與政治背書須分開。

## 圖像與呈現

- Cloudflare 官方 9/15 文章 OG 圖下載為 `assets/cloudflare.png`，權利歸 Cloudflare；圖說為官方文章配圖，非實際儀表板截圖。原圖：https://blog.cloudflare.com/_emdash/api/media/file/01M2JFGHWHDDM5TY9NKS0TY8B3.01M2JFGJS6SBSH4SX8FC56CVPD.png
- `assets/world.jpg` 為 NASA／Unsplash 全球新聞主題配圖，非立陶宛、沙烏地或其他事件照片；來源：https://unsplash.com/photos/Q1p7bh3SHj8 ，原圖：https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1200&q=85
- 使用固定手機閱讀器；每篇原頁展開、完整來源 URL 及單篇 ChatGPT 可選擇提問。
- 內容發布 commit `85f5cd9aa00077b525f27b1a3b71927b3bc0b38b`；GitHub Pages 日期頁、最新入口及根入口均通過 HTTP 與完整位元組雜湊驗證。唯一私人 watchdog 於 2026-09-16 08:08:48 Asia/Taipei 回報 `Sent LINE message`、exit 0；pipeline check 隨後 exit 0。
- 公開網址：https://lucaskk.github.io/daily-news/wiki/daily/2026/09/2026-09-16/slides-2026-09-16.html?v=20260916-080801-reader
