# 2026-09-14 來源筆記（9/15 補製）

本次依使用者要求補製原本未完成的 9/14 日報，不是當日已完成稿的重送。原私人 checkpoint 為 research_pending；保留原截點，不以補製時間延長選題窗口。

- 研究截點：2026-09-14 08:01:40 Asia/Taipei = 2026-09-14 00:01:40 UTC。
- 全球 24 小時：2026-09-13 08:01:40 至 2026-09-14 08:01:40 Asia/Taipei；UTC 2026-09-13 00:01:40 至 2026-09-14 00:01:40。
- 產品 168 小時：2026-09-07 08:01:40 至 2026-09-14 08:01:40 Asia/Taipei；UTC 2026-09-07 00:01:40 至 2026-09-14 00:01:40。
- 排序依 Reuters、AP、BBC、國際媒體的跨來源能見度與事件影響編輯判斷，沒有可回溯的全球討論量排行。補製時的首頁、社群票數與熱門排名不當成截點時的量化證據。
- 已檢查 Cool3c 與 Engadget；現在首頁晚於凍結截點，只用來發現候選。折扣、評論、舊消息及未查證傳聞不入選。

## 先行去重

已重建產品表（補製前 568 列、88 份報告）。模型不讀完整歷史表。以 `rg --no-ignore -n -i` 搜尋全 `wiki/daily/` 的 `daily-news-*.md`、`source-notes-*.md`、`product-news-ledger.md`，只取命中列。

| 候選與查詢 | 歷史結果 | 判定 |
| --- | --- | --- |
| `CUDA.*13\.4` | 無同版本命中；再讀最近 7 天 17 列產品表，無同項 | 首次收錄 |
| `StarCraft.*2030`、`星海.*射擊` | 9/13 來源筆記曾列候選但因官方查核不足排除；不是已收錄產品 | 補足官方來源後首次收錄；不重報同場已收錄的 Diablo V／Switch 2 |
| `Virgo`、`Matui`、`Vanuatu`、`Kyaw Moe Tun`、`瑞典.*選舉` | 無相同事件 | 保留 |
| `Yagodin`、`Dorohusk`、`波蘭.*列車`、`列車.*波蘭`、`立陶宛.*鳥`、`柴油.*卡車` | 無相同事件 | 保留 |
| Saudi East-West／沙烏地管線 | 9/12 停運，9/13 伊拉克調查與撤職 | 新增庫存緩衝及修復時程分歧，明標續報 |
| Hormuz 船舶攻擊 | 既有海峽風險背景；本次是 9/13 UKMTO 新船舶事件 | 只報新攻擊，舊管線／紅海島嶼事件不另算 |

## 入選時間與原始來源

以下以可核對的事件日或首發時間判斷，非僅採文章更新時間；來源只有日期或分钟精度時不虛構秒數。

### T1 NVIDIA CUDA Toolkit 13.4
- 官方開發者文章署期 2026-09-09，Jonathan Bentz；在產品 7 天窗中間，無需推定午夜。
- https://developer.nvidia.com/blog/?p=121255
- 官方內文確認 Windows on Arm、Rubin compute capability 107 預覽、MPS V3 等。Rubin 是 preview，不寫全面正式供應。產品版本不同，不和舊 CUDA 教學合併。

### T2 Blizzard STARCRAFT 開放世界射擊新作
- BlizzCon 9/12 開幕正式公告；官方回顧內文將 9/13 稱為明日，確認公告事件日為 9/12。二次媒體首發 2026-09-12T17:58:10Z（台北 9/13 01:58:10）核對時序。
- https://news.blizzard.com/en-gb/article/24301453/everything-announced-at-blizzcon-2026-opening-ceremony
- https://www.pcgamer.com/games/fps/new-starcraft-game-is-an-open-world-shooter-coming-in-2030/
- 官方僅確認新作類型、Koprulu Sector 與 Spring 2030 目標；預告不等於可遊玩版本，未證實售價或最終規格。

### 1 瑞典國會選舉
- 9/13 投票本身為新事件；Reuters 當日報導，Yahoo 初版 2026-09-13 00:04 UTC，後續投票報導 11:46 UTC。只採投票與組閣爭點，不把後來 AP 滾動頁的最終席次倒灌到原截點。
- https://currently.att.yahoo.com/att/swedes-vote-election-could-usher-000425104.html
- https://malaysia.news.yahoo.com/swedes-vote-election-could-usher-000425104.html
- https://kathmandupost.com/world/2026/09/13/swedes-vote-in-election-that-could-usher-far-right-into-government

### 2 印尼 Virgo Transport 8 傾覆
- 事件為 9/13；ABC 9/13 7:22 AM 初報 6 死、107 生還、130 失蹤。El País 2026-09-13T19:03:53Z（台北 9/14 03:03:53）報導更新通報 6 死、108 生還、129 失蹤。
- https://www-cdn.abcnews.com/International/6-dead-130-missing-after-indonesian-ferry-capsizes/story?id=136400801
- https://elpais.com/internacional/2026-09-13/al-menos-6-muertos-y-129-desaparecidos-tras-volcar-un-barco-de-pasajeros-indonesio.html
- 243 人為當時名冊基礎，搜救數據不同批次不混加。9/14 03:39:52Z 的 AP 擴大搜救報導已超窗，排除。

### 3 沙烏地管線續報
- Reuters 9/13 首次披露買家與業界消息人士的庫存／修復估计；Business Recorder 標示 Published September 13，18:29 為更新時間，不能單獨當事件依據。
- https://www.brecorder.com/news/amp/40439290
- 新增燕布約 5–7 天緩衝；約 400 萬桶／日、全球 4% 為可能受影響流量，並非證實已消失。5–6 周與更快部分復輸是不同來源估計，官方尚未確認。
- 前次：[[daily-news-2026-09-13]] 的伊拉克撤職；再前次 9/12 停運。

### 4 霍爾木茲新船舶攻擊
- Reuters 電台頁刊於 Fargo 當地 9/12 21:22 CDT = 9/13 02:22 UTC = 台北 10:22；內文 UKMTO 明確稱週日（9/13）船舶中彈、起火與撤離。
- https://740thefan.com/2026/09/12/new-report-of-attack-on-strait-of-hormuz-shipping-fans-fears-of-threats-to-oil-supplies/
- 精確襲擊與撤離分鐘未提供；不把另艘伊朗船死傷視為同一船，也不重列先前管線停運作新事件。

### 5 俄軍擊中波烏邊界附近列車
- BBC 首發 2026-09-13 16:07 UTC = 台北 9/14 00:07；報導當日列車機車頭受襲，無傷亡通報。
- https://currently.att.yahoo.com/att/russia-struck-train-near-poland-160713485.html
- Johnson 等人先前已經通過同一路線，不是其座車被擊中；俄方承認打擊西烏鐵路設施，但個別目標意圖未獨立證實。

### 6 萬那杜 MV Matui 最新搜救通報
- Reuters 9/13 首次報導總理辦公室週日新聲明，電台 9/12 22:03 EDT = 9/13 02:03 UTC；Yahoo 9/13 03:53 UTC 為另一版本。
- https://theduke.fm/2026/09/12/one-dead-more-than-30-missing-after-vanuatu-ferry-sinks-pms-office-says/
- https://currently.att.yahoo.com/att/one-dead-more-30-missing-020309926.html
- 沉船發生週五 9/11，不能寫成週日新海難。入選的是週日政府首度可靠披露至少 1 死、逾 30 失蹤、15 生還與搜救方向；無先前收錄。超載／警告問題是待查主張。

### 7 科索沃國會通過庫爾蒂新政府
- AP／ABC 9/13 11:20 AM 報導週日國會表決；事件在歐洲當日，明確落窗。頁面時區未標，不擅自補成精確台北秒數。
- https://abcnews.com/International/wireStory/kosovo-gets-new-government-political-impasse-persists-136404108
- 120 席中 62 人支持；反對派質疑先選副議長的程序。組閣通過並非所有政治危機解除。

### 8 緬甸政府尋求針對駐聯合國代表的跨國法律行動
- Reuters／MarketScreener 9/13 13:48 AEST = 03:48 UTC = 台北 11:48，報導週日官方媒體新聲明。
- https://au.marketscreener.com/news/myanmar-government-revokes-status-and-seeks-action-against-un-envoy-kyaw-moe-tun-ce785bdcd98bf022
- 2021 年解職為舊背景，不以再說撤職當新品；新項為當局尋求法律／外交協助的聲明。沒有證實 Interpol 接案、發布通緝或 UN 撤銷席位。

### 9 俄方公布核電廠燃料車遭襲指控
- Reuters／MarketScreener 9/13 10:01 沙烏地時間 = 07:01 UTC = 台北 15:01，記錄 Likhachev 週日首次公開說法。
- https://sa.marketscreener.com/news/russian-nuclear-head-says-ukraine-attacked-fuel-trucks-endangered-zaporizhzhia-plant-ce785bdcd98af020
- 所稱襲擊為週五 9/11，不假稱週日襲擊。新公開指控涉及備援柴油運送與核安；尚無獨立核對、烏方回應或 IAEA 證實，不把兩名士兵死亡寫成查證定論。

### 10 立陶宛疑似無人機警報解除
- 事件為 9/13 日間，國家危機管理中心澄清目標為鳥群；Reuters 更正版本於當日已有彙整紀錄（13:01 UTC）。不沿用早版的確認無人機入侵說法。
- https://www.byteseu.com/2362188/
- https://www.newsminimalist.com/articles/nato-jets-scramble-over-lithuania-but-suspected-drone-was-flock-of-birds-1b68ed79
- 上述為 Reuters 轉載／索引，仍須以通訊社可讀版本核對；LRT 網站讀取受 robots 限制。此條為日間短暫警報與當日澄清，不是戰爭新攻擊。

## 補發與呈現

- 沿用現有單欄閱讀器：產品在前、標題時間出處、摘要、原頁展開與 ChatGPT 後續問題。
- 補發只公開此日期目錄，LINE 使用帶版本的日期網址；不拿舊頁替換今天入口或修改今天成功紀錄。
- 圖像權利與原圖網址記錄於 presentation-2026-09-14.json；主題圖明標非事件照片。
- 公開日期頁2026-09-15驗證HTTP200、完整位元組及文章結構一致；commit 5ffd5b4。唯一私人watchdog於01:42:53 Asia/Taipei回報Sent LINE message、exit0，使用獨立補發receipt，未變更正常每日成功日期。
- 版本網址：https://lucaskk.github.io/daily-news/wiki/daily/2026/09/2026-09-14/slides-2026-09-14.html?v=28b5f8c351f4d138
- 立陶宛原始Reuters連結另核對：https://www.reuters.com/business/aerospace-defense/lithuania-closes-vilnius-airport-nato-summons-jets-response-possible-drone-2026-09-13/ ，直接讀取受限，事實採可讀Reuters轉載，不使用社群留言作證據。
