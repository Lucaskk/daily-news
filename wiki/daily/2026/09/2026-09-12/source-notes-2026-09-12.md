---
title: "2026-09-12 新聞來源與時間依據"
date: 2026-09-12
type: source-notes
status: verified
---

# 研究視窗

- 研究截點：2026-09-12 08:01:29（Asia/Taipei）／2026-09-12T00:01:29Z。
- 全球 24 小時：2026-09-11 08:01:29 至 2026-09-12 08:01:29（Asia/Taipei）；UTC 2026-09-11T00:01:29Z 至 2026-09-12T00:01:29Z。
- 科技產品 168 小時：2026-09-05 08:01:29 至 2026-09-12 08:01:29（Asia/Taipei）；UTC 2026-09-05T00:01:29Z 至 2026-09-12T00:01:29Z。
- 已讀中央 README，建立私人 production checkpoint，重建 86 份日報／564 筆產品變更索引。
- 09:54 恢復：checkpoint 仍為 research_pending，當日僅此草稿；09:44 watchdog 是 waiting_for_publish，並非 LINE API 拒收。補完沿用原截點，不改成恢復時間。內容查證完成不等於發布或配送成功，後者以 pipeline check／wiki log 為準。

## 選題與來源範圍

以 Reuters、AP 跨國重大事件與官方發布為主，搭配國際科技媒體、官方產品博客及聚合結果發現候選；沒有可驗證的全球總討論量，因此不宣稱客觀熱度前十。全球恰好十則，產品兩則；能源、公衛、司法、外交與新資料發布分開處理。

- [Cool3c](https://www.cool3c.com/) 已查看新品、導購、AI 區塊；iPhone 18 系列已收錄，促銷與未核實新品時點不補位。
- [Engadget](https://www.engadget.com/) 已檢查，發現 Gemini 桌面版後回查 Google 官方發布日。評論及舊產品不作新發布依據。
- 聚合站僅供找線索，不採其轉述的產品日期。GPT-Live 舊公告是七月發布，沒有核實新 API 節點前不加入。

## 產品按需去重

搜尋涵蓋完整 `wiki/daily/` 的 `daily-news-*.md`、`source-notes-*.md` 與 `product-news-ledger.md`，只讀 rg 命中列；没有讀入完整歷史表。索引由程式掃描 86 份日報，564 筆變更。

| 候選／變更鍵 | rg 組合詞 | 命中判讀與二次核對 | 結果 |
|---|---|---|---|
| Cursor／Projects／beta-launch／2026-09-10 | `Cursor.{0,35}Projects`、反向組合、`cursor.com/blog/projects` | 無同產品命中；完整讀最近七天表的 17 列，沒有 Projects | 保留；一列一變更 |
| Google／Gemini Windows／desktop-launch／2026-09-10 | `Gemini.{0,35}Windows`、反向組合、`gemini-app-now-on-windows` | 6/2 與 7/14–16 只出現其他產品或跨詞共現，非同一變更；二次核對 17 列無此發布 | 保留，不重收媒體隔日報導 |

兩產品首次官方發布均僅提供 2026-09-10 日期，位於 168 小時窗中間；不虛构 00:00 或時區。新表的比對鍵由既有程式依報告生成，候選變更鍵供人工查詢，不冒充既有 hash。

## 全球歷史搜尋

窄化搜尋：`\bPerim\b`、Dhubab、支聯會、Chow Hang、Lee Cheuk、鄒幸彤、李卓人、協助死亡、assisted dying、Africell、Savanta、Knighton、CIA/PDB 解密組合、各原文 URL；CPI 依八月＋數據發布組合搜尋。`Modi` 最初誤命中 modified、`Perim` 誤命中 experimental，已改用字界及標題匹配，不將雜訊當去重證據。

- Houthi／Mokha：命中 9/11 日報第 1 則；新項是 Perim／Dhubab 與管線遇襲，標續報。
- Ebola：標題命中 9/6（180 天計畫）、9/4（村落策略）、9/3（三千死）及更早報導；新增第七省與 9/11 政府新通報，標續報並引用最近 9/6。
- Modi：命中 9/1 日報第 6 則，是比什凱克 SCO 開幕。新德里 9/11 雙邊會談是另一場活動，非該峰會重刊。
- 其餘未找到相同事件／同次官方發布，判為首次收錄；英方戰損與昨日設施空襲不同，不重列空襲內容。

## 逐則時間與證據

各來源完整連結同時保留於 [日報](daily-news-2026-09-12.md) 的逐則來源區，HTML 由同一份報告產生。

| 項目 | 首發／事件依據及 UTC | 入窗判定與限制 | 原始來源 |
|---|---|---|---|
| T1 Projects | 官方 Sep 10, 2026；無時分 | 七日窗內 beta rollout，不是九月十二日新品 | https://cursor.com/blog/projects |
| T2 Gemini Windows | 官方 article:published_time=2026-09-10 | 七日窗內；產品公告稱當日可下載，進階功能有條件 | https://blog.google/innovation-and-ai/products/gemini-app/gemini-app-now-on-windows/ |
| G1 Perim／管線 | Reuters dateline ADEN/DUBAI Sept 11，正文事件 Friday；轉載頁 Published 20:03、Updated 23:33，但頁面未明示時區 | 當日新事件；不把不明時區的時鐘直接當 UTC。9/11 已可靠報導到達 Perim；停運為同日官方聲明 | https://za.investing.com/news/commodities-news/yemens-houthis-reach-strategic-island-at-mouth-of-vital-shipping-lane-4462290 |
| G2 CPI | 官方排程 Sep 11 08:30 EDT=12:30 UTC，台北20:30；Reuters 結果稿確認实际公布 | 用正式數據發布時間；資料期間八月不影響首次公開日。BLS 搜尋快取仍顯示七月，未拿快取充當八月表格 | https://www.bls.gov/cpi/ ; https://au.marketscreener.com/news/us-consumer-inflation-picks-up-in-august-ce785bdfdc8bf620 |
| G3 英國表決 | AP 原頁首發10:37:26 UTC為預告，Local10正文已載四小時辯論後286比270；Reuters Sep11結果稿15:35頁面時間 | 採週五表決日，不把 AP 預告首發當成結果時間；Reuters及AFP結果同向 | https://www.local10.com/news/world/2026/09/11/uk-lawmakers-vote-down-bill-to-allow-assisted-dying-in-england-and-wales/ ; https://www.lse.co.uk/news/uk-lawmakers-reject-bid-to-legalise-assisted-dying-lebqws1le54aly6.html |
| G4 香港量刑 | AP 首建 Sep10 23:01:50 UTC 為預告；判刑為香港 Sep11週五法院事件，Reuters／EFE同日確認 | 入选基準為香港法院日間判刑，不用窗外預告時刻；保留事件日期 | https://apnews.com/article/1e91bf6d80c11ae3802481e0ac6b324a ; https://www.investing.com/news/economy-news/hong-kong-court-jails-two-tiananmen-vigil-group-leaders-for-7-years-4897191 |
| G5 剛果通報 | Reuters Sep12 07:12 AEST=Sep11 21:12 UTC；更新08:55 AEST=22:55 UTC | 政府 Friday新增數據；兩次均早於截止00:01:29 UTC。南烏班吉較早聲明為背景，不誤稱患者當日死亡 | https://au.marketscreener.com/news/ebola-infections-top-7-000-in-congo-as-virus-spreads-to-new-province-ce785bdfd18bf227 |
| G6 雙邊會談 | AP Sep11 13:02:10 UTC，台北21:02:10；WBOC正文引印度外交部兩份會談聲明 | 已發生的週五會談，非週末峰會結果 | https://apnews.com/article/f7735ac233c7e8db8ac021c53a3eef8a |
| G7 英方戰損 | AP Sep11 09:44:34 UTC，台北17:44:34；Knighton Friday向記者說明 | 新公開估計而非重新報導戰爭起點；不混入原頁其他空襲內容 | https://apnews.com/article/090b61e66dbde88598a1b1bfe42ad85d ; https://www.local10.com/news/world/2026/09/11/more-than-500000-russian-troops-killed-in-ukraine-uk-defense-chief-says/ |
| G8 Africell | AP Sep11 13:04:35 UTC，台北21:04:35；公司 Friday宣布 | EXIM新貸款，不是2018/2019 DFC舊案；Reuters先前以草稿報導，AP後續確認宣布 | https://apnews.com/article/a755a634563876d52c9738dce4e5d7f4 |
| G9 解密 | AP Sep11 18:51:28 UTC，台北Sep12 02:51:28；ISCAP官方9/11公告today releasing | 新釋出文件為事件，不以25週年紀念重收2001襲擊 | https://apnews.com/article/2444830d317967cb64b9eb8d509fa0c7 ; https://isoo-overview.blogs.archives.gov/2026/09/11/iscap-declassification-of-records-relating-to-9-11-including-a-ruling-on-iscap-appeals-2022-008-and-2023-001/ |
| G10 BoE | 官方 Published on 11 September 2026；Reuters Sep11 09:45 UTC報導 | 官方八月調查首次公開日；不是把八月訪問重當今日事件 | https://www.bankofengland.co.uk/inflation-attitudes-survey/2026/august-2026 |

## 矛盾及排除

- 英國協助死亡：Guardian 搜尋標題「in favour」與 AP／Reuters／AFP 的否決結果相反。使用已讀 AP 286–270及 Reuters結果，不採該標題，也不假定已知矛盾成因。對照 https://www.theguardian.com/society/2026/sep/11/mps-vote-legalise-assisted-dying-england-wales 。
- 香港：早期 Reuters 概稱兩人七年；AP／EFE列鄒幸彤七年三個月，保留差異，不加總成另一刑期。
- 剛果：WHO 9/10報告截至9/7為六省，Reuters 9/11新通報為七省；不同截止不是直接矛盾。
- 英方俄軍死亡估計不是獨立清點；沒有俄方即時確認。BoE調查的跨廠商差異不可當真實民意全幅變化。
- 美國聯邦職缺忠誠問題禁令 Reuters 首發 Sep12 10:09 AEST=00:09 UTC，晚於截點，排除：https://au.marketscreener.com/news/us-judge-blocks-trump-administration-s-loyalty-question-for-job-applicants-ce785bdfd181f320 。
- Pemex漏油 Reuters首發 Sep12 11:13 AEST亦晚於截點，排除。伊拉克Shalamcheh口岸23:45 UTC消息雖入窗，選題上未優先於已入選議題；沒有假稱其窗外。
- CPI預測稿、9/10 PPI、舊尼泊爾救援、旧地震頁面的新站頭日期均不補位。近期Apple手機已收錄，不因導購更新重列。

## 圖像與生成

三張本機圖片來源及完整原圖 URL 見 `presentation-2026-09-12.json`。已目視確認 Cursor 為官方 Projects 示意，Gemini 為公告標誌配圖，全球分節為地球主題圖，均不冒充當日現場。圖片權利屬原作者；不在研究證據中保存媒體全文。
