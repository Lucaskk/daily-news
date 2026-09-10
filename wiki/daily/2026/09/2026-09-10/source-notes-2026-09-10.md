# 2026-09-10 來源與去重筆記

## 研究視窗

- 截點：2026-09-10 08:01:18 Asia/Taipei／2026-09-10T00:01:18Z。
- 全球：2026-09-09 08:01:18 至 2026-09-10 08:01:18 Asia/Taipei；UTC 2026-09-09T00:01:18Z 至 2026-09-10T00:01:18Z。
- 產品：2026-09-03 08:01:18 至 2026-09-10 08:01:18 Asia/Taipei；UTC 2026-09-03T00:01:18Z 至 2026-09-10T00:01:18Z。
- 時間窗固定，不因寫作或 Pages 部署時間移動。日期來源不補造午夜；首次發布與後續修改分開。

## 發現與重要性

查閱 AP 世界版、Reuters 當日索引與授權轉載、Apple 官方新品公告，並按規則開啟 [Engadget](https://www.engadget.com/) 與 [Cool3c](https://www.cool3c.com/)。兩家科技站版面均由 Apple 秋季新品主導，因此本次以兩款手機與 Siri AI 具體推出時程為產品重點。全球主線在 AP、Reuters 均出現核案、能源及海運升級，另納入不同地區的實際司法、勞動、救援與外交事件。這是編輯綜合，不宣稱取得完整社群聲量或客觀全球排名。

Reuters 授權轉載頁明列原通訊社與報導日期。Reuters Connect 的第三方圖片／影片目錄只作發現線索，不冒稱為 Reuters 自行驗證。AP 直接 HTTP 讀取遭 403 的頁面，保留可讀網頁研究結果與 UTC 發布資料；不虛構已下載原始頁。來源只保留必要 metadata 與摘要，未複製全文。

## 產品去重

選題前執行 `python3 scripts/build_product_news_ledger.py`：84 份日報、559 筆產品變更。範圍是 `wiki/daily/product-news-ledger.md` 及全部歷史 `daily-news-*.md`、`source-notes-*.md`，只用 `rg` 讀命中列。完整歷史表沒有載入模型。

| 候選／變更 | 窄式查詢與命中 | 近 7 天完整表備援 | 判定 |
|---|---|---|---|
| Apple iPhone Duo 正式發布 | `Apple.*iPhone Duo|蘋果.*iPhone Duo|iphone-duo`；無命中 | 有，僅因歷史無命中；當時表為 9/3–9/9 共 21 列，無同一變更 | 首次收錄 T1 |
| Apple iPhone 18 Pro／Max 正式發布 | `Apple.*iPhone 18 Pro|蘋果.*iPhone 18 Pro|iphone-18-pro`；無命中 | 有，同一份 21 列備援表，無同一變更 | 首次收錄 T2 |
| Apple Siri AI／iOS 27 具體推出時程 | `Apple.*Siri AI|Siri AI.*Apple`；命中 6/10 Siri／DMA、7/14 公開 beta 及 8 月排除筆記。ledger 命中鍵 `5c15320abc14`、`9fe1fc29953f` | 不因本候選讀取，歷史已有命中 | T3 續報；7/14 是 beta 擴大測試，本次是 9/14 系統更新與 Siri 英文 beta、10 月五種語言時程 |

實際執行合併式 pattern `Apple.*(iPhone Duo|iPhone 18 Pro|Siri AI)|蘋果.*(iPhone Duo|iPhone 18 Pro)|iphone-duo|iphone-18-pro`，再單獨重查兩款手機以確認無命中。沒有以 Apple 單獨 OR 掃出全部公司歷史。

## 逐項時間、原始網址與狀態

| ID | 首次發布／事件依據 | 去重與新增事實 | 原始來源 |
|---|---|---|---|
| T1 | Apple `datePublished=2026-09-09Z`；`dateModified=2026-09-09T19:09:28Z`，修改時刻不冒充首刊。美國正式新品公告日完全落在產品窗 | 首次摺疊手機正式發布，未來 10/16 預購、10/23 供應不是已完成 | https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/ ; https://www.apple.com/iphone-duo/ |
| T2 | Apple `datePublished=2026-09-09Z`；`dateModified=2026-09-09T19:09:03Z` | 首次硬體公告；引用開頭、Advanced Camera System、A20 Pro、供應條目。美國公告 9/12 預購、9/18 供應 | https://www.apple.com/newsroom/2026/09/apple-debuts-iphone-18-pro-and-iphone-18-pro-max/ ; https://www.apple.com/iphone-18-pro/specs/ |
| T3 | 同一 9/9 官方公告的 Availability 條目：iOS 27 will be available、Siri AI is rolling out；不是拿整頁修改時間當新功能 | 續報 2026-07-14 公開 beta／2026-06-10 WWDC。新增明定 9/14 系統更新、英文 Siri beta，10 月法日韓葡西語；繁中 Siri 未列 | https://www.apple.com/newsroom/2026/09/apple-debuts-iphone-18-pro-and-iphone-18-pro-max/ |
| 1 | AP 首刊 2026-09-09T16:30:00Z＝台北 9/10 00:30；Reuters 9/9 表決報導交叉確認 | 續報 2026-09-05 草案，新增正式通過。23／3／8 票合計 34，不猜缺席原因 | https://apnews.com/article/607ecdffcd8ef88ddf8f33041e86b720 ; https://currently.att.yahoo.com/att/iaea-board-passes-resolution-reporting-162954509.html |
| 2 | AP 首刊 2026-09-09T09:08:51Z＝台北 17:08:51；採同日交易突破及美國收盤，均早於截點。Reuters 9/9 13:53 EDT 盤中數據另存為比較 | 續報 2026-07-24 油價曾破百；這是新一日重新突破，不重用 7 月或昨日戰果 | https://apnews.com/article/7538e6386a819bcdc2547d530ec3472e ; https://www.marketscreener.com/news/oil-treasury-yields-turn-higher-as-stocks-falter-ce785bd9d088f321 |
| 3 | 事件為 2026-09-09 約 03:00 UTC＝台北約 11:00；Reuters 9/9 報導 | 續報 2026-09-09 油輪戰線，但新增 New Andros 伊拉克水域攻擊；不累加伊朗宣稱船數 | https://www.ajot.com/news/oil-tanker-hit-in-iraqi-waters-as-vessels-get-caught-in-us-iran-attacks |
| 4 | Reuters 9/9 首次報導具體 30 天與七天執行期限；公開來源只按日期呈現，未以更新時分補造首刊 UTC | 續報 2026-09-09 英國禁令與以方表態，新增外交認證和期限 | https://www.investing.com/news/world-news/israel-tells-britain-to-close-east-jerusalem-consulate-within-30-days-sources-say-4892986 ; https://today.lorientlejour.com/article/1546965/israel-tells-british-consulate-in-east-jerusalem-to-close-within-30-days-sources-say.html |
| 5 | Reuters／MarketScreener 9/9 00:36 EDT＝04:36 UTC＝台北 12:36，修改至 08:30 EDT 仍在截點前 | 續報 2026-09-09 基輔主線，新增 Starokozache 口岸襲擊／交通暫停 | https://www.marketscreener.com/news/russian-drones-kill-injure-people-at-ukraine-moldova-border-crossing-ce785bd9db8bf023 ; https://theprint.in/world/russian-drones-kill-two-at-ukraine-moldova-border-crossing-authorities-say/3037835/ |
| 6 | Reuters／MarketScreener 首刊 9/9 03:52 EDT＝07:52 UTC＝台北 15:52；當日裁定 | 無同一案裁定命中；不把無管轄權寫成實體合法性判決 | https://www.marketscreener.com/news/hungary-loses-court-fight-over-frozen-russian-asset-profits-for-ukraine-ce785bd9da8ffe20 |
| 7 | AOL JSON-LD `datePublished=2026-09-09T06:04:41+00:00`；`dateModified=2026-09-09T06:09:12+00:00`，首刊台北 14:04:41 | 無歷史同一統計報導。本窗新發布採訪與具體統計；疫情自 3 月起，不宣稱今日才爆發。999 包含疑似與確診，不全為確診死亡 | https://www.aol.com/articles/bangladesh-fights-worlds-worst-measles-060441000.html |
| 8 | AOL JSON-LD `datePublished=2026-09-09T14:07:27+00:00`；`dateModified=2026-09-09T14:10:26+00:00`，首刊台北 22:07:27 | 續報 2026-09-06 隧道救援，新增軍方貨運無人機配送作業；沒有宣称 8 月洪災發生在本窗 | https://www.aol.com/articles/nepal-turns-drones-deliver-flood-140727000.html |
| 9 | Reuters 9/9 當地日間罷工現場報導，Te Ao 9/9 交叉確認。NZST 比台北快四小時，日間停工落在本窗；日期保留、不虛構時分 | 首次收錄實際停工，不重刊早先預告 | https://www.internazionale.it/ultime-notizie-reuters/2026/09/09/new-zealand-public-servants-walk-off-job-over-pay-offer ; https://www.teaonews.co.nz/2026/09/09/maori-public-servants-feeling-weight-of-cuts-as-thousands-strike-nationwide/ |
| 10 | Reuters／StreetInsider 9/9 15:50 EDT＝19:50 UTC＝台北 9/10 03:50；當日 Quito 訪問 | 首次收錄本次資金要求與 Los Tiguerones 指定，不當成已完成撥款 | https://www.streetinsider.com/Reuters/Rubio%2Bsays%2Bhe%2Bwill%2Bseek%2B%2445%2Bmillion%2Bin%2Bsecurity%2Bfunding%2Bfor%2BEcuador/27042434.html |

## 全球歷史搜尋與排除

歷史 `rg` 詞含 `IAEA.*Security Council|伊朗.*安理會`、`New Andros`、`Brent.*100|布蘭特.*100|101\.21`、`Israel.*30 days|以色列.*30`、`Starokozache|Darnyts`、`Hungary.*(frozen|profits|court)|匈牙利.*(收益|管轄)`、`Bangladesh.*measles|孟加拉.*麻疹`、`Nepal.*(flood|drone)|尼泊爾.*(洪|無人)`、`New Zealand.*(strike|servants)|紐西蘭.*罷工`、`Los Tiguerones|厄瓜多.*4,500`。只讀命中列，並針對 9/6 尼泊爾及 9/9 既有選題查看必要內容。

- IAEA：命中 9/5 草案與待追蹤問題，故本次標續報。
- 油價：命中 7/24 三位數與繞航管線，故標續報且限定新交易日。
- 尼泊爾：8/27、8/30、8/31、9/1、9/5、9/6 災情報導皆是舊背景；以最近 9/6 生還者節點為前次收錄，本次只選配送作業。
- 9/8 美國打擊五艘伊朗油輪、9/8 加拿大反制關稅，以及前一日沙烏地遇襲：已收錄，不重列。
- 美國擬禁止加拿大商品：初次消息在本窗開始前，未以 9/9 轉載時間當新事件，排除。
- 北韓 Yongbyon 新設施報導引用 8/28 IAEA 報告；無法確認原報告首次公開是否在 24 小時窗內，排除。
- 英國首相為屯墾區禁令辯護：僅政治說明，不另占名額；只保留新增外交期限。
- Engadget 的 Muse 社群帳號爭议不是 Muse 新產品變更；9/9 已收錄的 Meta Muse、Sony SEL814G 不再收錄。
- Cool3c 的購機贈演唱會購票資格屬促銷；Razer 鍵盤摘要價格出現 1,980／1,890 差異，未另取得官方查證，本次不採用。AirPods、Watch 為其他新品候選，本次聚焦最高價值的手機與 AI 推出時程，未聲稱已全面盤點所有新品。

## 圖像與驗證

圖像原始 URL、權利及說明記於 `presentation-2026-09-10.json`。Apple 圖為相應型號官方發布素材；全球區的地球圖明標非事件照。使用固定 renderer，來源分別放在每則原頁展開內容末端，ChatGPT 功能僅組合所選文章，不自動提交。

發布與 LINE 結果另記 [知識庫日誌](../../../../log.md)，不以研究完成冒稱配送成功。
