---
title: "2026-09-09 來源、時間與去重筆記"
type: source-notes
date: 2026-09-09
status: verified
tags: [provenance, deduplication, time-window, recovery]
---

# 來源與查核紀錄

## 研究截點與補跑

- Asia/Taipei 截點：2026-09-09 08:01:38（UTC 2026-09-09T00:01:38Z）。
- 全球 24 小時：2026-09-08 08:01:38 至 2026-09-09 08:01:38；UTC 2026-09-08T00:01:38Z 至 2026-09-09T00:01:38Z。
- 產品 168 小時：2026-09-02 08:01:38 至 2026-09-09 08:01:38；UTC 2026-09-02T00:01:38Z 至 2026-09-09T00:01:38Z。
- 早上約 08:07 已擷取 AP／官方來源與日期 metadata，排程卻在研究後誤回覆先前 Safari 訊息而結束，沒有產生今天檔案。09:52 使用者詢問後恢復；沿用原截點與原始擷取，不將補跑後才發生的事件混入。
- 保存 [原始日期證據](source-evidence-2026-09-09.json)：只存來源 URL、擷取時間、公開日期 metadata 與版本資料，不公開整篇媒體原文或私人設定。Sony 日文頁原始編碼與 UTF-8 不同，改以正常解碼的官方網頁內容確認日期、型號和上市表。

## 選題與來源覆蓋

早上已查看 [AP World](https://apnews.com/world-news)、[Guardian 9/8 世界版索引](https://www.theguardian.com/world/2026/sep/08/all)、[Engadget](https://www.engadget.com/) 與 [Cool3c](https://www.cool3c.com/)。AP 世界版對加拿大、中東油輪、沙烏地與英國屯墾區禁令給予顯著版位；Guardian 提供跨媒體議題核對，科技候選再回官方查證。沒有取得可比的全球社群聲量資料，故不宣稱客觀聲量前十。

本次國際事件的可驗證時間與正文主要取自 AP；同一篇 AP 的轉載不算第二個獨立確認。Reuters 未取得足夠可直接核對的本日原文，BBC 存取受限，不將它們列作已讀證據。安全、政策與規格優先比對 Meta、Sony、澳洲政府及中國商務部。媒體版位是重要性訊號，不是把舊聞重新當成新事件的理由。

## 每則時間依據

AP 表列首次時間取自原頁 NewsArticle 的 datePublished；更新時間只是界定本次使用的版本，從不單獨作為入選依據。表內 UTC 均可與上方窗口直接比較；日報展示值已加八小時。只有日期的 Sony 公告保留日期，不虛構午夜。

| 項目 | 首次可靠發布 UTC | 使用版本的更新 UTC | 入選事件／發表節點 | 原始來源 |
| --- | --- | --- | --- | --- |
| T1 Meta Muse | 2026-09-08T19:00:51Z | 官方未另列 | 9/8 推出獨立個人代理與 Muse Secure VM | [Meta](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) |
| T2 Sony SEL814G | 官方日期 2026-09-08，時分未知 | 不以更新判斷 | 9/8 新品公告；9/29、10/9 是未來日本預購／上市 | [Sony](https://www.sony.jp/CorporateCruise/Press/202609/26-0908B/) |
| 1 加拿大關稅 | 2026-09-08T04:07:02Z | JSON-LD 同首次；article:modified_time 11:27:30.658 | 9/8 措施開始執行；AP 記 00:01 當地，未自行猜時區 | [AP](https://apnews.com/article/canada-trump-carney-trade-war-tariffs-4620ffb5ecc029322217207fa6758431) |
| 2 伊朗油輪 | 2026-09-08T20:45:57Z | 2026-09-08T23:15:07Z | 9/8 美方五艘油輪戰果與伊朗報復聲明 | [AP](https://apnews.com/article/iran-tanker-navy-warship-dfc9a1d9c9a5b8bc7b47fcc004025e65) |
| 3 沙烏地遇襲 | 2026-09-08T04:02:15Z | 2026-09-08T13:05:00Z | 9/8 清晨多城市新攻擊與 73 傷通報 | [AP](https://apnews.com/article/4ad9446f0bb8c096750c84b6e1ba86b8) |
| 4 英國禁令 | 2026-09-08T09:09:24Z | 2026-09-08T18:18:21Z | 9/8 正式宣布；非當日已全面生效 | [AP](https://apnews.com/article/uk-west-bank-israel-settlement-sanctions-b4d7354221bfe0c48e4bfce7a3b7624b) |
| 5 基輔空襲 | 2026-09-08T06:17:35Z | 2026-09-08T16:58:48Z | 暫停攻擊首都後 9/8 恢復空襲；當日通話為附帶進展 | [AP](https://apnews.com/article/russia-ukraine-war-kyiv-missiles-drones-attacks-fd634a6786462bc95b7dfefc97d2331e) |
| 6 日本 DCS | 2026-09-08T09:45:06Z | 同首次 | 9/8 保證金開始及日本抗議；9/7 初裁為背景 | [AP](https://apnews.com/article/china-japan-chips-chemical-dumping-ea58c95c47481c5c822a3a544e6b68cc) |
| 7 澳洲草案 | 2026-09-08T09:01:41Z | 2026-09-08T09:17:06Z | 9/8 公布 My Feed, My Way／照護義務草案 | [AP](https://apnews.com/article/australia-social-media-algorithms-digital-duty-care-1eee351b39f22b340ef289c792f7993b)；[官方](https://minister.infrastructure.gov.au/wells/media-release/my-feed-my-way) |
| 8 巴西裁定 | 2026-09-08T16:13:49Z | 2026-09-08T22:44:07Z | 9/8 撤職與政府上訴 | [AP](https://apnews.com/article/30cd3bab96065b3a076f4756294b09b4) |
| 9 匈牙利驅逐 | 2026-09-08T09:33:52Z | 2026-09-08T15:22:12Z | 9/8 公布十名外交人員驅逐決定 | [AP](https://apnews.com/article/hungary-russia-diplomats-magyar-security-orban-leave-5e8d90957d8b990a8cb3dbd7185a4794) |
| 10 英國航管 | 2026-09-08T15:14:54Z | 2026-09-08T21:48:57Z | 9/8 故障、取消航班與當日晚間修復通報 | [AP](https://apnews.com/article/uk-airports-traffic-control-disruptions-408a8997d9fb39508e922e09d2523884) |

AP 搜尋索引有時比 JSON-LD 少一秒，例如巴西、Muse、胡塞；本文統一採來源頁機器可讀的精確日期，不混合不同索引。

## 跨日去重

選題前執行 `python3 scripts/build_product_news_ledger.py`：83 份日報、557 列歷史產品、27 列最近七天表。程式可掃全部檔案，但模型只按候選讀 `rg` 命中；沒有載入完整歷史表。搜尋範圍為 `wiki/daily/` 全部 `daily-news-*.md`、`source-notes-*.md`，產品另含 `product-news-ledger.md`。

| 候選 | 窄式查詢與命中 | 七天表備援 | 判定 |
| --- | --- | --- | --- |
| Meta Muse 個人代理 | `Meta.*Muse\|Muse.*Meta` 命中歷史表第 185 列 Glimmer（比對鍵 277a4fd7869e）及第 216 列 Code beta（8335f4529fd5）；`Muse.*(personal\|個人\|Secure VM)\|introducing-muse-personal-ai-agent` 只有 8/11 Spark 願景相關文字，無本次產品變更 | 不因有相關命中而全讀；只讀必要前後文。先前 Sony 無命中時讀過七天表，也未見 Muse 獨立代理 | 保留；新獨立產品，不把較早 Spark 模型或 7/24 Meta AI 任務功能冒充新消息 |
| Sony FE 8–14mm | `Sony.*8.?14mm\|8.?14mm.*Sony\|FE.8.?14mm\|SEL814G\|SEL0814G` 無命中；官方確認型號為 SEL814G | 歷史無命中後完整讀 9/2–9/8 的 27 列表，無同變更 | 保留新品公告；不宣稱已在台灣供貨 |
| AMD Ryzen AI Max PRO 400 | `Ryzen AI Max.*(400\|192)` 未見相同歷史變更，但官方相關發布早於七天窗 | 因無命中讀過最近七天表；仍不能取代時間查核 | 排除，近期重述未提供窗內新發布證據 |

全球候選按事件詞搜尋：加拿大反制關稅、five tankers／五艘油輪、Houthi Saudi／胡塞沙烏地、英國屯墾區禁令、基輔特使停攻、dichlorosilane／二氯二氫矽／硅、日本反傾銷、My Feed My Way、Mendonça／Mendonca、匈牙利驅逐外交官、NATS／英國航管。另以本次全部 AP 文章 ID 及 Sony `26-0908B` 搜全歷史，均無同一來源頁命中。網址不重複不能單獨代表事件不重複，因此另保留下列主線判讀。

| 本次續報 | 前次收錄 | 前次內容 | 本次重大新進展 |
| --- | --- | --- | --- |
| 1 加拿大 | [2026-09-02](../2026-09-02/daily-news-2026-09-02.md) | 加拿大補選報導附記反制將於 9/8 開始 | 正式開始徵稅 |
| 2 伊朗油輪 | [2026-09-06](../2026-09-06/daily-news-2026-09-06.md)、[2026-09-08](../2026-09-08/daily-news-2026-09-08.md) | 三艘油輪遇襲；之後伊朗先發準則 | 另一次五艘油輪打擊與約旦報復聲明 |
| 3 胡塞 | [2026-09-07](../2026-09-07/daily-news-2026-09-07.md) | 葉門 Hays 地面戰推進 | 沙烏地城市與設施跨境遇襲 |
| 4 英國 | [2026-06-09](../../06/2026-06-09/daily-news-2026-06-09.md) | 議員推動屯墾區貿易禁令 | 政府正式宣布政策與以方反制 |
| 5 基輔 | [2026-09-06](../2026-09-06/daily-news-2026-09-06.md)、[2026-09-07](../2026-09-07/daily-news-2026-09-07.md) | 首都暫停攻擊、美方特使會談 | 首都恢復空襲與新的傷亡 |

其餘五則未找到相同事件的既有收錄，亦不將廣泛國別或長期政治背景視為同一事件。

## 官方查核與排除

- Meta：使用 [9/8 官方公告](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) 的 How It Works、Built to be Private, Safe, and Secure、Looking Ahead 段。Muse Secure VM 是本次產品；Confidential VM、眼鏡與其他 coming soon 功能不能混成已發布。Engadget 的 [Muse 報導](https://www.engadget.com/2253133/meta-reveals-its-ai-agent-that-can-shop-send-emails-and-plan-trips-on-your-behalf/) 僅用來發現候選與判斷科技版位，不擴張官網未證實的市場或安全保證。
- Sony：Cool3c 首頁新品訊息提供候選，規格、型號、發表日、日本預購／上市表及價格均回查 [日本官方](https://www.sony.jp/CorporateCruise/Press/202609/26-0908B/)。歐美價格不能換算成台灣價格；日本供貨時間以當地公告為準。
- AMD：相關 [AAI 官方新聞稿](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era) 早於本次七天窗；不因九月文章再提記憶體或本機模型用途而收錄。
- 澳洲：以 [官方草案公告](https://minister.infrastructure.gov.au/wells/media-release/my-feed-my-way) 校正 proposed／targeted consultation 狀態，不把既有年齡限制當成今天新法。
- 中國 DCS：以 [商務部說明](https://cacs.mofcom.gov.cn/article/gnwjmdt/sb/zo/202609/189170.html) 核對 9/7 初裁、80.8%–99.2% 與尚待終裁；今日新節點是 AP 明確記錄的 9/8 保證金生效及日方回應。AP 標題容易讓讀者誤解進出口方向，正文與官方明確是中國對日本原產進口品施加措施。
- 排除 Cool3c 折扣、導購與未有新產品狀態的問卷報導；排除 Engadget 舊評測、預測與無可靠新節點的 Chrome 重述。Apple 未發表產品的預測不當作正式發布。
- 排除昨日已收錄的 Sony 耳機、伊朗先發準則與敘利亞核案重述；也不以仍在熱門榜的舊事件補足十則。

## 歧異與限制

- 英國航管：AP title／JSON-LD headline 尚為逾六百班、影音近三百班，但 21:48:57Z 版本正文為逾一千班。採截點前正文，保留差異，不稱其他版本是假消息。
- 基輔：七死二十八傷含基輔及周邊；早期市區局部通報是不同統計範圍。軍事情勢與普丁通話均保留消息方。
- 油輪：五艘是美方聲明；伊朗也報告油輪遇襲，但不足以獨立核實每艘損害。約旦攻擊缺少美方確認；不將地理稱呼不精確的船位描述畫成精確地圖。
- 沙烏地：73 傷來自聯軍，設施停運來自能源部；胡塞稱報復與沙方稱挑釁並存。不能把所在區域煉油能力當成確認停產量。
- 英國禁令：宣布時間與 6–9 個月落實期分開；以色列反制亦保留「表示將」。巴西撤職與監控指控不是定罪，上訴未決。
- Meta 安全、效能及主動任務能力屬官方產品主張；獨立測試、台灣可用性與訂閱細節仍需後續確認。

## 圖片與呈現

圖片來源和原始網址見 [presentation JSON](presentation-2026-09-09.json)。Meta 使用本次公告宣傳圖，Sony 使用 SEL814G 真實產品圖，全球分節使用明標非事件照片的地球主題圖。保留各權利人資訊，不宣稱官方圖片為自由授權。固定 renderer 產生原頁展開與單篇 ChatGPT 提問介面；沒有對使用者 iPhone 的 App 接管或預填文字作實機驗證。
