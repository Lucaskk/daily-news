---
title: "2026-10-05 來源筆記"
date: 2026-10-05
type: source-notes
status: research
---

# 2026-10-05 來源筆記

- 凍結截點：2026-10-05 08:00:15 Asia/Taipei，ISO 2026-10-05T08:00:15+08:00，即 2026-10-05T00:00:15Z。
- 全球窗：2026-10-04 08:00:15 至 2026-10-05 08:00:15 Asia/Taipei；UTC 2026-10-04 00:00:15 至 2026-10-05 00:00:15。
- 科技窗：2026-09-21 08:00:15 至 2026-10-05 08:00:15 Asia/Taipei；UTC 2026-09-21 00:00:15 至 2026-10-05 00:00:15。
- 去重只查 2026-09-21 至 2026-10-04 的 14 份日報；ledger 產生 61 列同窗表。未查完整歷史或歷史來源筆記。

## 來源掃描與科技候選

- 第一輪批次掃描 CSV 的 Engadget、The Verge、TechCrunch、WIRED、Ars Technica、Cool3c、Yahoo奇摩科技、TechOrange、數位時代、TechNews、openai.com，以首頁與 site 搜尋發現候選。Engadget 的 One UI 9 自訂教學沒有獨立新版本發布依據；Cool3c 的 Astrotoo 與露營燈為介紹／導購，未以重刊補位；TechNews 的 Terafab 洽談為產業消息；WIRED 的折扣與舊 Shield 漲價不作發布。
- 第二輪官方定向補查 OpenAI API changelog、Enterprise release notes、GitHub SDK releases 與 Samsung newsroom。已收錄的 GPT-6.1 Sol、DevDay、購物試穿等排除；Rosalind September 11 一般可用早於科技下界，10/5 收費尚無截點前生效依據，不收。
- T1：OpenAI Node SDK v7.28.0。官方 release 標記 2026-10-02，GitHub release 實際發布欄 10/4 18:22；保留版本日期，不猜時區。Features 段落新增 custom voice creation、agent session events；SDK 有型別／介面不代表每個帳戶自動取得語音建立權限。來源：https://github.com/openai/openai-node/releases/tag/v7.28.0
- T1 lookup：`openai-node.*7.28|custom voice.*creation|voice creation.*SDK`，14 份日報無命中、未截斷；才讀同窗 61 列表，無相同事件，首次收錄。
- T2：ChatGPT Enterprise Admin console 的 Plugins／Marketplaces 管理，官方 2026-10-01 段落。workspace owners/admins 可在 Admin console 管理，Apps 仍保留既有權限與入口。來源：https://help-lb.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes
- T2 lookup：`plugins.*Admin console|Admin console.*marketplace|Enterprise.*marketplace.*manage`，14 份日報無命中、未截斷；同窗表無此管理功能，首次收錄。不是 9/29 Codex Cloud 或 ChatGPT Space 的重述。

## 全球候選與去重初查

- Brazil 與 Bosnia 10/4 投票／初步計票；Germany Merz 10/4 到 Kyiv 宣布新援助；Norway Halden 狩獵隊槍擊；Latvia 10/4 計票；Ethiopia 10/4 確认 Mekelle 易手；Yemen 10/4 全線行動宣布；RAF Fairford 10/4 轟炸機返美；Myanmar 10/4 遣返者抵達；Nolo 10/4 跨換日線。
- lookup `Latvia|Mekelle|Fairford|FlyDubai|Bosnia|Nolo|Myanmar|Yemen` 僅查上述 14 份日報，未截斷。命中 Latvia 10/4 投票、Mekelle 10/3 進逼、Fairford 9/29 保釋、Myanmar 10/1 啟動遣返、Yemen 10/4 Aramco 攻擊宣稱，以及 Nolo/Polo 9/29 同頁背景。這些須明標續報、新事件節點；Bosnia 與 Norway 未命中。
- FlyDubai 安全審查新報導作排除候選，避免較弱匿名背景占用名額；沒有把 10/3 舊攻擊照片當 10/4 新聞。

## 入選全球時間與来源依據

- G1 Brazil：10/4當地投票／關閉投票所，首次收錄；來源 AP／ClickOrlando 與 DW。DW 已後續更新到10/5，因此僅使用已確認投票階段，不取無截點標記的最新票數。
- G2 Germany：10/4 Kyiv 記者會宣布約10億歐元軍援、3.5億能源援助，AP／News4Jax；日報保留事件日，未把3:42 EDT頁面建立時刻當援助宣布時刻。
- G3 Ethiopia：AP／News4Jax 10/4 07:08 EDT首次發布；Reuters／AOL 08:18 UTC另確認政府軍控制。前次10/3進逼，新節點是控制權與撤離確認。現場通訊受限。
- G4 Yemen：10/4 al-Alimi宣布收復胡塞控制區行動，AP／ABC專題確切段落與CTP／ISW交叉核對；前次10/4 Aramco攻擊聲明，新為政府正式決策。CTP未觀察到全線攻勢，保留差異。
- G5 Fairford：AP／Live5News 10/4 17:07 EDT＝10/5 05:07 TPE；前次9/29保釋，今日新為全部轟炸機返美，Sky引用軍方確認。調動細節與因果不全。
- G6 Latvia：AP 10/4 10:25:01 UTC＝18:25:01 TPE；前次10/4投票，今日計票與組閣。AP對35%聯盟／黨的敘述有簡化，未推算多數席次。
- G7 Bosnia：10/4投票與電子驗票故障，AP現場觀察。AP後續標題已改勝選宣稱，本文只用可確認的投票日事件，不以最初04:07:55 UTC作晚間結果時間。
- G8 Myanmar：AP／NY1 10/4 07:19 ET＝19:19 TPE；前次10/1啟動遣返，今日新為實際抵達Yangon。是否自願與安全持續爭議。
- G9 Norway：AP 10/4 10:29:41 UTC＝18:29:41 TPE；首次收錄，2死1重傷，動機未明。
- G10 Nolo：AP 10/4 21:05:24 UTC＝10/5 05:05:24 TPE；前次9/29同頁風暴背景，新為跨換日線、185 km/h與新預報。不是僅因改標題收錄。
- 補查 `Brazil.*vote|Brazil.*election|Bosnia.*vote|Dodik.*election|Norway.*hunting|Merz.*Kyiv|Nolo.*typhoon`，同14份日報無命中、未截斷；上述初查命中的背景則保留續報標示。
- 每項完整原始網址與來源名稱保留於當日日報對應段落；不採未讀取的聚合站推測。圖片查證與不使用原因見 presentation-2026-10-05.json。
