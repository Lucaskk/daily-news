---
title: "2026-10-01 每日新聞來源筆記"
date: 2026-10-01
type: source-notes
status: research-complete
tags: [daily-news, sources, provenance, deduplication]
---

# 2026-10-01 每日新聞來源筆記

## 研究窗口

- Asia/Taipei 凍結截點：`2026-10-01 08:01:41 +08:00`。
- 全球新聞 24 小時窗：`2026-09-30 08:01:41` 至 `2026-10-01 08:01:41`（Asia/Taipei）；UTC 為 `2026-09-30 00:01:41Z` 至 `2026-10-01 00:01:41Z`。
- 科技／AI 產品 7 日窗：`2026-09-24 08:01:41` 至 `2026-10-01 08:01:41`（Asia/Taipei）；UTC 為 `2026-09-24 00:01:41Z` 至 `2026-10-01 00:01:41Z`。
- 研究模式：`legacy`。先執行 `build_product_news_ledger.py`，得到 627 筆產品變更／105 份日報；模型未整份讀取歷史 ledger，只按候選窄搜，無相同變更命中後才完整讀取 47 行、29 筆的最近七日表。

## 科技產品搜尋與去重

- 第一輪廣泛掃描固定來源池：Engadget、The Verge、TechCrunch、WIRED、Ars Technica、Cool3c、Yahoo 奇摩科技、TechOrange 科技報橘、數位時代，另以 OpenAI、Google DeepMind 官方頁交叉確認。表面候選 14 則；核對原始日期後，Roku Labs、Spotify Partner Program、Apple ATT、Pinterest Restyle、Instinct／Muse calls 都是 9 月 17 日舊變更，科技首頁的相對時間屬聚合頁重排，排除。評論、融資、傳聞與舊評測也不收錄。
- 第一輪保留 5 個合格且非重複產品變更，已達 5–8 則搜尋目標，因此未為湊數進行第二輪無限補查。官方查證涵蓋 OpenAI Dots／DevDay recap／API changelog、Google DeepMind Gemini 4 Argon 頁面與 Instinct 發表說明；媒體來源用於精確時間及外部限制脈絡。
- 每個候選先以公司、產品、動作與比對鍵組合窄搜 `product-news-ledger.md` 及所有歷史日報／來源筆記。查詢 `OpenAI.*Dots|Dots.*always-on|openai-dots`、`OpenAI.*ChatGPT Space|ChatGPT Space.*shared|chatgpt-space`、`OpenAI.*Codex.*cloud|Codex.*reusable development environments|codex-cloud-reusable`、`Google.*Gemini 4.*Argon|Gemini 4 Argon.*Google|gemini-4-argon`、`Instinct.*Selections|Selections.*product recommendations|instinct-selections` 均無同一產品變更命中；之後才讀最近七日表，表內亦無這五項。

| 項目 | 事件／發布時間依據與來源 | 去重、決定與不確定性 |
|---|---|---|
| T1 OpenAI Dots／always-on agent／`openai-dots` | OpenAI 官方頁標示 2026-09-29；AP 於 `2026-09-29T18:51:35Z` 首次完整報導，換算 `2026-09-30 02:51:35` TPE。https://openai.com/index/introducing-dots/ ; https://apnews.com/article/77b6b8888145869206996d7509d24256 | 歷史窄搜無命中，最近七日表無同項，首次收錄。可用於 Pro、Business Premium 的合格市場；Enterprise／Edu／Healthcare 為管理員預設關閉的 beta。自主工作能力與安全聲明主要來自公司，實務可靠性仍待驗證。 |
| T2 OpenAI ChatGPT Space／shared AI workspace／`chatgpt-space` | OpenAI DevDay recap 官方發布日期 2026-09-29，未提供獨立時分。https://openai.com/index/devday-2026-recap/ | 歷史窄搜只見一般 workspace 背景，沒有 ChatGPT Space 這次上市；最近七日表無同項。桌面與 web 已向 Pro、Business、Enterprise 提供，mobile 只先支援尋找、閱讀與分享，建立／編輯仍未上線。 |
| T3 OpenAI Codex in the cloud／reusable environments／`codex-cloud-reusable` | OpenAI DevDay recap 官方發布日期 2026-09-29，未提供獨立時分。https://openai.com/index/devday-2026-recap/ ; https://help.openai.com/en/articles/6825453-chatgpt-release-notes | 歷史窄搜無本次跨裝置與 reusable environments 變更，最近七日表無同項。官方稱 Plus、Pro、Business、Healthcare、Education、Enterprise 可用；環境權限與 repo 設定仍由使用者／團隊控制。 |
| T4 Google Gemini 4 Argon／trusted cyber rollout／`gemini-4-argon` | Google DeepMind 於 2026-09-30 公布；Axios `2026-09-30T20:00:05Z`，即 `2026-10-01 04:00:05` TPE。https://deepmind.google/models/gemini/ ; https://www.axios.com/2026/09/30/google-gemini-4 | 歷史窄搜無命中，最近七日表無同項。先提供 Fairwind Program 的少量 cyber defenders，尚無一般 API／消費者日期與正式價格；benchmark 與 1M output claim 主要來自 Google。 |
| T5 Instinct Selections／curated recommendations／`instinct-selections` | 創辦人於 9/29 晚間宣布功能；TechCrunch 於 2026-09-30 08:56 PDT 發布，即 `2026-09-30 23:56:00` TPE。https://techcrunch.com/2026/09/30/instincts-new-product-recommendations-are-giving-some-users-the-ick/ | 歷史窄搜無命中，最近七日表無同項。首次收錄。公司未說明合作策展者名單、是否收 affiliate／廣告費，也未公布 rollout 範圍；部分使用者回報未主動要求就收到推薦。 |

## 全球 Top 10 時間、去重與歧異

| 排名／項目 | 事件／首次可靠發布時間依據 | 歷史去重與判定 |
|---|---|---|
| G1 Russia 大規模攻擊 Ukraine 電網 | AP `2026-09-30T09:06:31Z`，即 `2026-09-30 17:06:31` TPE；攻擊發生於星期三凌晨，造成至少 7 死。https://apnews.com/article/b837b4ee58f0aa8b4e5a5a872906d91e | **續報，前次 2026-09-30。** 前次為前一輪 Kyiv ballistic／jet-drone attack 與攔截困難；本次新節點是更大規模合成攻擊、至少 7 死及 hydro／thermal power plant、substation、storage 與 data center 等電網目標，顯示冬季能源戰升級。雙方目標與攔截數仍不可完全獨立核實。 |
| G2 U.S. 完成 Iraq 撤軍 | AP `2026-09-30T05:02:35Z`，即 `2026-09-30 13:02:35` TPE；U.S. military 星期三正式宣布完成撤離。https://apnews.com/article/a097a39f3d1a3515adc2ba3298a6816f | 先前只收錄撤軍時程與基地移交，本次是 12 年 anti-ISIS mission 正式完成的新執行節點，收錄為重大續報，前次相關節點 2026-08-13。 |
| G3 U.S. 將 Syria 移出武器出口禁令 | AP `2026-09-30T15:41:39Z`，即 `2026-09-30 23:41:39` TPE；State Department 星期三公告。https://apnews.com/article/b76e32ef38891a20cf191018bdcdd424 | 窄搜 `Syria.*arms export ban|arms export ban.*Syria` 無相同政策命中，首次收錄。這是可執行的出口管制變更，不等於任何個別軍售已獲批准。 |
| G4 Iran 稱收到 U.S. 對停戰方案的正式回覆 | AP `2026-09-30T10:59:39Z`，即 `2026-09-30 18:59:39` TPE。https://apnews.com/article/2c42d71d8a4be3443147cd65a6ee9193 | **續報，前次 2026-09-29。** 前次為調停人仍斡旋且主要障礙未解；9/30 日報因無新正式節點而排除。今日新增是 Iran 政府確認收到正式 U.S. response 並提交內閣，但內容與是否拒絕仍未公開。 |
| G5 MI5 公開警告 UK 大學停止與 CGTRI 合作 | Guardian 2026-09-30 09:00 EDT，即 `2026-09-30 21:00:00` TPE。https://www.theguardian.com/uk-news/2026/sep/30/mi5-issues-spy-alert-over-body-linked-chinese-state-stealing-vital-uk-research-universities | 窄搜 MI5、CGTRI、CAGT 無相同警報命中，首次收錄。MI5 指其是 China MSS front company；Chinese embassy 尚未回應，公開材料未披露完整證據鏈。 |
| G6 Grenfell 調查檔案移交 CPS | Guardian 2026-09-30 09:02 EDT，即 `2026-09-30 21:02:00` TPE。https://www.theguardian.com/uk-news/2026/sep/30/grenfell-fire-police-investigators-files-prosecutors | 2026-05-19 曾有警方將尋求起訴的預告；今日是 20 家公司與 54 人證據檔案正式交給 CPS 的程序新階段，標示續報。最終是否起訴與罪名仍由 CPS 決定。 |
| G7 South Korea 要求 North Korea 為地雷爆炸道歉 | Guardian 2026-09-30 03:53 EDT，即 `2026-09-30 15:53:00` TPE。https://www.theguardian.com/world/2026/sep/30/south-korea-apology-north-korea-mine-injures-soldiers | **續報，前次 2026-09-29。** 前次是 South Korea 初步判定北韓地雷造成三名軍人受傷；今日新增 UNC 認定 armistice violation、Seoul 正式要求道歉，North Korea 則否認並稱為自導事件。 |
| G8 Malaysia 啟動 Myanmar 公民遣返 | Guardian／AFP 2026-09-30 02:05 EDT，即 `2026-09-30 14:05:00` TPE；第一批約 1,500 人開始返國。https://www.theguardian.com/world/2026/sep/30/malaysia-begins-myanmar-repatriations-despite-warnings-from-un-and-rights-groups | 窄搜 Malaysia、Myanmar、5,000、repatriation 無同一執行節點命中，首次收錄。政府稱自願，UN rights chief 與 NGO 質疑在戰亂與迫害風險下能否真正自願；Rohingya 人數未公開。 |
| G9 Indonesia 停職五名監獄官員 | Guardian／AP 2026-09-30 01:27 EDT，即 `2026-09-30 13:27:00` TPE。https://www.theguardian.com/world/2026/sep/30/indonesia-prison-officials-suspended-luxury-apartments-prisoners | 窄搜 Cibinong、luxury prison、five officials 無命中，首次收錄。Ombudsman 發現逾 10 個住宅式單位；住用囚犯與是否付賄尚未正式確認。 |
| G10 Gaza 新一輪 strikes 造成 5 死 19 傷 | AP `2026-09-30T10:10:13Z`，即 `2026-09-30 18:10:13` TPE。https://apnews.com/article/449f9e378b8c9bc66fe36712efdfa6b5 | **續報，前次相關收錄 2026-08-03。** 本次是近一年的 ceasefire 下新的 hospital-confirmed casualty event；Israel 未就 AP 所列每次 strike 提供完整目標說明，死傷數來自兩家 Gaza hospitals。 |

## 排除與邊界

- Antarctica sea-ice 報導首次發布為 `2026-09-30 08:00:00` TPE，比窗口起點早 1 分 41 秒；即使只差很短仍排除，未用更新時間補進窗口。
- Brazil Tapajós de Fato 停止報導選舉屬重要 press-freedom story，但威脅事件跨越數年，窗內文章是綜合報導，沒有明確新決定時間；不占 Top 10。
- 9/29 UN Yemen envoy 會談、Hurricane Polo 登陸、RBA 升息、Estonia attribution、Vietnam detentions、Tu-95 crash 與 U.S. election cyber support 已在 9/30 日報收錄，不重複。
- 全球候選均先以事件實體與動作窄搜歷史。相同戰爭或政策主線只有在窗內出現新的死亡、正式回覆、實施、移交或法律程序時才標示續報。

