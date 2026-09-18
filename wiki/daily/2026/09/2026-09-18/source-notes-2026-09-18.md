---
title: "每日新聞來源筆記｜2026-09-18"
date: 2026-09-18
type: source-notes
status: research-complete
---

# 2026-09-18 來源與去重筆記

研究截點固定為 **2026-09-18 08:02:22 Asia/Taipei**（2026-09-18T00:02:22Z）；同日接續不得重設。

- 全球 24 小時：2026-09-17 08:02:22 至 2026-09-18 08:02:22（Asia/Taipei），等於 `2026-09-17T00:02:22Z` 至 `2026-09-18T00:02:22Z`。
- 科技產品 168 小時：2026-09-11 08:02:22 至 2026-09-18 08:02:22（Asia/Taipei），等於 `2026-09-11T00:02:22Z` 至 `2026-09-18T00:02:22Z`。
- 選題規則已讀 `wiki/daily/README.md`；流程 `python3 scripts/news_workflow.py status` 為 `legacy`，未改模式。選題前執行 `python3 scripts/build_product_news_ledger.py`，產生 577 筆／92 份日報。只用窄 `rg` 搜尋完整產品史、日報與來源筆記，沒有把完整歷史載入模型；產品候選無命中後才完整讀 `product-news-recent-7d.md`（15 筆）。世界候選亦用窄 `rg` 查全部歷史日報與來源筆記。

## 全球新聞逐項時間依據

| 項目 | 視窗內事件／首次可靠發佈（Asia/Taipei） | 來源與去重判斷 |
|---|---|---|
| G1 聯合國伊朗調查團 | 9/17 新報告；AP `2026-09-17T08:49:13Z` = 9/17 16:49:13 | https://apnews.com/article/99e690efd1e818e835d4f5a00e0d261b ; Reuters https://www.reuters.com/world/middle-east/un-mission-finds-grounds-believe-us-committed-war-crimes-iran-tehran-crimes-2026-09-17/ 。2/28 空襲為背景，今天是新調查結論；無同份報告歷史捕獲。美方反對或否認部分結論，並非司法定罪。 |
| G2 俄中安理會否決 | 9/17 表決；AP `2026-09-17T19:56:51Z` = 9/18 03:56:51 | https://apnews.com/article/c509e344bc45ba87670b9a668afbbb49 ; https://www.aljazeera.com/news/2026/9/17/russia-china-veto-un-mandate-to-monitor-iran-sanctions 。專家監督授權未延長，不是伊朗制裁全部撤銷；無同次表決歷史捕獲。 |
| G3 瑞典最終計票與辭職 | 9/17 最終計票／Kristersson 聲明；AP `2026-09-17T11:27:56Z` = 9/17 19:27:56 | https://apnews.com/article/bf88ef9771cdd4f435a1568b98a11790 ; https://www.val.se/english/election-results/elections-to-the-riksdag-and-regional-and-municipal-councils/election-results-2026 。**續報**：2026-09-14 投票，2026-09-15 初步 176:173；新增正式結果與辭職。組閣未定。 |
| G4 塔伊夫傷亡 | 9/17 民防通報；AP `2026-09-17T13:31:07Z` = 9/17 21:31:07 | https://apnews.com/article/d29f7fb71331bea0098cbdb38d7577e0 ; https://www.thenationalnews.com/news/gulf/2026/09/17/one-killed-and-two-injured-by-houthi-drone-debris-in-saudi-arabias-taif/ 。**續報**：2026-09-17 捕捉防空求援，新增攔截碎片致一死兩傷。無人機來源據沙國說法。 |
| G5 伊朗代表團簽證 | 9/17 國務院核准；AP `2026-09-17T18:38:45Z` = 9/18 02:38:45 | https://apnews.com/article/3f91ccc8def4a9d5499b7c8620450864 。視窗內實際外交／簽證決定，無同次核准歷史捕獲；核准不等於和談。 |
| G6 基輔新攻擊 | 9/17 凌晨至上午攻擊；AP `2026-09-17T06:39:59Z` = 9/17 14:39:59 | https://apnews.com/article/608408f47bcc9cce30b93f764d18b96b 。2026-09-17 尼科波爾巴士是不同地點與目標，這次新傷亡不重複。烏方傷亡數待更新。 |
| G7 羅馬尼亞提名 | 9/17 總統第三度正式提名；AP `2026-09-17T17:10:23Z` = 9/18 01:10:23 | https://apnews.com/article/5e2f45236148744c78c743b27b6f4485 。新提名，非已完成組閣；無同次提名歷史捕獲。 |
| G8 奈及利亞酒類事件 | 9/17 官方首次可靠披露累計數；AP `2026-09-17T09:20:52Z` = 9/17 17:20:52 | https://apnews.com/article/953036190416f202f812700f58aba05c 。最早死亡約兩週前；今日新聞基準是 48 死、約 100 人治療、15 人被捕的首次官方披露。甲醇仍屬疑似，未當作已驗證化驗結果。 |
| G9 越南洪災 | 9/17 洪水與官方災損；AP `2026-09-17T09:21:52Z` = 9/17 17:21:52 | https://apnews.com/article/1728f9ab865955ed520a63b7d07ba142 。本輪淹水與 2,000 戶住宅數為新通報，不併入舊颱風死傷。 |
| G10 巴西福利法令 | 9/17 簽署；Agência Brasil 9/17 12:36 BRT = 9/17 23:36 Taipei；AP `2026-09-17T17:40:25Z` = 9/18 01:40:25 | https://agenciabrasil.ebc.com.br/economia/noticia/2026-09/bolsa-familia-e-reajustado-em-15-medida-vale-partir-de-outubro ; https://apnews.com/article/b0e6975c4110dab4e4181760150fdb2c 。新法令，不是預期；新支付十月才開始。 |

## 科技產品候選與跨日比對

先用 `rg -n -i 'ChatGPT for Word|CC.*families|UN System Data Commons|Data Commons.*UN|SCIM.*API Platform|Monster Hunter Wilds.*appearance|魔物獵人.*捏臉' wiki/daily/product-news-ledger.md wiki/daily --glob 'daily-news-*.md' --glob 'source-notes-*.md'` 窄搜。公司、產品與更新動作組合後，T1／T2／T3 均無相同變更命中；再完整讀最近 7 日比對表，亦無重複。可重用的關鍵比對式如下：

| 候選／比對鍵查詢詞 | 精確官方日期、URL | 歷史命中與裁決 |
|---|---|---|
| OpenAI／ChatGPT for Word／推出 Word 增益集 | 2026-09-17，https://help.openai.com/en/articles/6825453-chatgpt-release-notes ，頁面 `# September 17, 2026` 下 `## ChatGPT for Word` | 無相同變更；最近 7 日表亦無，收錄 T1。整頁「Updated 1 hour ago」不是本條時間依據。 |
| Google Labs／CC／家庭共享代理六人 | 2026-09-17，https://blog.google/innovation-and-ai/models-and-research/google-labs/cc-expanding-to-groups/ | 無同一群組能力變更；最近 7 日表亦無，收錄 T2。個人 CC 舊版本只作背景。 |
| UN system／Google／UN System Data Commons／平台推出 | 2026-09-17，https://blog.google/innovation-and-ai/technology/ai/google-un-data-commons-platform/ | 無平台推出變更；最近 7 日表亦無，收錄 T3。2027 年覆蓋率屬未來目標。 |
| OpenAI／Enterprise SCIM／API Platform 權限 | 2026-09-17，https://help.openai.com/en/articles/10128477-chatgpt-enterprise-edu-release-notes | 官方 release notes 可查，因篇幅與直接受眾較窄未入選；不表示已被其他日期捕獲。 |

另外已檢查 https://www.engadget.com/ 與 https://www.cool3c.com/ 最新頁面。兩站提供候選／脈絡，但當下首頁的購物導購、舊產品評論與折扣不作新品變更。產品發布日期未有時分時僅記官方日期，不虛構午夜。

## 排除與歧異

- Fiji HIV 緊急狀態雖有 9/17 報導，實際正式宣布在 9/16，早於 24 小時起點；排除，不因後續刊登而當今日新聞。
- 美國眾院對俄制裁案投票實際在 9/16（早於今日起點），9/17 分析文章不算新表決；排除。
- 9/17 對既有伊朗戰況的評論、預測與首長措辭，缺乏具體新節點者排除。
- 瑞典 176:173 在 9/15 已屬初步數字；今天真正新增是最終確認與首相辭職，已明標續報。
- 沙國 9/16 防空求援與 9/17 塔伊夫碎片致死傷屬不同進展；歸責依沙國官方說法。
- 尼日利亞甲醇成分待化驗，巴西福利提升十月才執行，聯合國調查團報告非終局司法裁定；報告均保留限定語。

## 發布紀錄

待 `scripts/daily_news_pipeline.py finish` 回填公開頁、LINE watchdog 與本機預覽結果。
