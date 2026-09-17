# 2026-09-17 來源筆記

- 研究截點：2026-09-17 08:02:33 Asia/Taipei = 2026-09-17 00:02:33 UTC；沿用既有 checkpoint，研究模式 `legacy`。
- 全球 24 小時：2026-09-16 08:02:33 至 2026-09-17 08:02:33 Asia/Taipei；UTC 2026-09-16 00:02:33 至 2026-09-17 00:02:33。
- 科技產品 168 小時：2026-09-10 08:02:33 至 2026-09-17 08:02:33 Asia/Taipei；UTC 2026-09-10 00:02:33 至 2026-09-17 00:02:33。
- 以 AP、Reuters、Engadget、Cool3c、Fed 與公司公告作跨來源重要性綜合判讀；不是量化討論量排名。只引用來源可證的事實，不把各站 `modified` 或首頁時間當事件時鐘。

## 跨日去重方法與結果

- 選題前執行 `python3 scripts/build_product_news_ledger.py`：574 筆產品變更、91 份既有日報；未將完整歷史表或歷史報告載入模型。
- 先用窄化 `rg -n -i` 查完整 `wiki/daily/` 下的 `daily-news-*.md`、`source-notes-*.md` 與完整產品 ledger，只讀命中列。查詢組合涵蓋 `Meta One|Sponsored Agents|ChatGPT Ads.*HubSpot|App Store.*Bundles|StoreKit.*Bundles` 及 `Thaci|al-Zara|Nikopol.*bus|India.*Pakistan.*naval|Canada.*associate|Gaza City.*collapse|North Kivu|South Sudan.*election.*chair|Saudi.*interceptors|Fed.*rate hike`。世界候選同事件未見已收錄；Fed 升息預期、剛果疫情主線、ChatGPT 廣告測試等舊主線另做語意判讀。
- 產品候選 Meta One、Sponsored Agents、StoreKit Bundles／Suites 窄搜無同一變更後，才完整讀取最近 7 天產品表 15 列；表內均無本次變更。完整歷史表未整份讀取。
- **續報**：OpenAI ChatGPT Ads 前次 2026-08-12 收錄原始廣告測試；本次 9/16 新增贊助代理對話、HubSpot／Shopify 與製作工具。剛果 Ebola 前次 2026-09-12 收錄 7,022 例／3,398 死與南烏班吉擴散；本次新增 WHO 9/16 的 Ituri 下降和 North Kivu 每週近倍增，非單純更新總數。沙國油管／燕布前次 2026-09-14、2026-09-16；本次是防空攔截器求援新節點，不再重報管線與貨單。
- **排除**：9/16 AP 回顧的美國眾院伊朗戰爭權力案 9/15 表決、沙國東西油管停運與燕布取消貨單、立陶宛擊落無人機、在軌武器承認、加密法案 49–50 表決，均已由 9/16 或更早日報收錄。印尼財長撤換發生 9/14，即使 Reuters 9/16 披露可能原因，也無新的撤換行為，不當成今日新事件。Engadget 搜尋結果混有 2025／7 月舊文與日期錯置，逐篇核對後未採；Cool3c 首頁候選缺較強官方時間證據的折扣、導購與舊評測未選。

## 產品候選：時間依據、`rg` 與歧異

| 編號 | 變更／比對鍵及歷史查詢 | 精確發布依據與新舊判讀 | 來源及保留疑義 |
|---|---|---|---|
| T1 | `OpenAI.*(Sponsored Agents|ChatGPT Ads.*HubSpot)|Sponsored Agents.*OpenAI|reimagining-advertising-with-ai`；完整歷史命中 2026-08-12 ChatGPT 原始廣告測試，未命中此新增功能；比對鍵 `openai-chatgpt-ads-sponsored-agents-20260916` | OpenAI Product 官方署期 2026-09-16，無時分，7 日窗內。美國選定廣告主測試 Sponsored Agents；HubSpot 和美國 Shopify App 同日可用。**續報 2026-08-12**，新增對話式贊助代理及商家工具；不把舊廣告測試再寫一次。 | https://openai.com/index/reimagining-advertising-with-ai/ ；https://openai.com/index/testing-ads-in-chatgpt/ 。Shopify 國際上架預定 9/23，效果與全面時程未公布。 |
| T2 | `Meta.*Meta One|Meta One.*(subscription|訂閱)|introducing-meta-one-subscription-service`；完整歷史無同一變更，才讀最近 7 日表；比對鍵 `meta-meta-one-subscriptions-launch-20260915` | Meta 官方公告署期 2026-09-15，Engadget 報導 9/15 11:00 EDT；7 日窗內。首次正式推出多層方案；之前 Plus 單品方案是背景，不當新品。 | https://about.fb.com/news/2026/09/introducing-meta-one-subscription-service-more-features-ai/ ；https://www.engadget.com/2258403/meta-adds-new-subscription-tiers-for-businesses-creators-and-ai-power-users/ 。美國價與地區價不同；1,500 萬是既有訂閱及試用累計。 |
| T3 | `Apple.*(Bundles.*Suites|StoreKit.*multiseat)|App Store.*Bundles.*Suites|likeohx4`；完整歷史無同一變更，才讀最近 7 日表；比對鍵 `apple-app-store-subscription-bundles-suites-multiseat-20260916` | Apple Developer 官方 2026-09-16 公告，無時分，7 日窗內。Bundles／Suites 開放申請，多席位購買當日預設啟用；iPhone Duo 9/9 已收錄但為不同產品變更。 | https://developer.apple.com/news/?id=likeohx4 。申請制、10/22 容量採購與冬季群組購買不得誤寫成全部今日可用。 |

## 全球 Top 10：事件／首次可靠發布時間依據

| 編號 | 事件或新進展（Asia/Taipei；UTC） | 來源、去重及不確定性 |
|---|---|---|
| 1 | Fed FOMC 9/16 14:00 EDT 發布 12:0 升息決議 = **9/17 02:00 TPE；9/16 18:00 UTC**。 | https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm ；https://apnews.com/article/bab1bcb07e973bfb2dd0c3e5fbbb73b1 。前次只有升息預期；本次是實際 25 基點至 3.75%–4% 決議。未來路徑未定。 |
| 2 | AP **9/16 16:42:59 TPE；08:42:59 UTC** 首次披露沙國尋求四國防空援助與攔截器庫存壓力。 | https://apnews.com/article/895320bde6dc589cebb628b63832c38a 。**續報防務新節點**，前次 9/14、9/16 為油管及貨單，非相同變更。匿名官員來源；求援不等於盟軍已部署。麥加無人機沙國指控胡塞，胡塞否認。 |
| 3 | 9/16 Hague 法院宣判；AP **9/16 13:12:50 TPE；05:12:50 UTC** 首報。 | https://apnews.com/article/0b24b81d6e1ca8f01d8b8b54bb465ee9 。首次收錄最終宣判；四項戰爭罪成立、反人類罪部分無罪，可上訴。 |
| 4 | al-Zara 坍塌始於 9/13，9/16 地方官與救援組織更新 **已找到 82 具遺體**；AP **9/16 18:27:50 TPE；10:27:50 UTC** 首次可靠披露此數字。 | https://apnews.com/article/6a6f5bc2c2f847c16f8a4f8f422c6a82 。先前未收錄該礦災；此次只把 9/16 新增死亡數及搜救狀態當時間基準。早期消息曾說 67／70，並有坍塌起始日歧異。 |
| 5 | Nikopol 巴士於 9/16 當日遭無人機攻擊；AP **9/16 18:24:42 TPE；10:24:42 UTC** 首報。 | https://apnews.com/article/6c85022eda557416995d0c26a55fdda0 。與先前烏俄攻防不同事件；5 死 7 傷為烏方地方官數字，目標意圖與俄方回應未獨立確認。 |
| 6 | 印巴軍艦碰撞在 9/15；**9/16 互召外交官**是新的外交節點，AP **9/16 16:54:59 TPE；08:54:59 UTC** 首報。 | https://apnews.com/article/494234c16afbd84ee06032785db43c93 。歷史無相同碰撞／召見；巴方稱位於其 EEZ，印方稱公海，座標未獨立核定。 |
| 7 | von der Leyen 9/16 在歐洲議會正式提議加拿大準會員框架，AP **9/16 15:59:31 TPE；07:59:31 UTC** 首報。 | https://apnews.com/article/3fdb111dd4d23d88b3de88c274c52711 。與 CETA、SAFE 舊合作不同的新制度提案。尚無會員規則、批准或正式加盟；美方關稅威脅未實施。 |
| 8 | 9/16 加薩市受損樓房當日倒塌；AP 中東滾動頁 **9/16 15:04:34 TPE；07:04:34 UTC** 為頁面首次發布，採其中 `Rescuers search through rubble` 新事件段落，不引用後續改頁時間。 | https://apnews.com/article/567498d0aa85a32e9c294759bd943501 。先前 Gaza 遺骸與空襲是不同事件。21 死／14 傷為當地衛生部門數字；倒塌直接原因未明，不說成 9/16 新空襲。 |
| 9 | WHO 9/16 記者會新增 Ituri 下降、North Kivu 每週 100→逾 200 的分化；AP **9/16 22:31:05 TPE；14:31:05 UTC** 首報。 | https://apnews.com/article/9b4aa71b0354b8fa000ea9dc5de5979d 。**續報 2026-09-12**，前次僅有 7,022 例／3,398 死及新省份，今日新增區域趨勢。WHO 稱全國仍擴散，衝突區可能漏報。 |
| 10 | Kiir 9/15 晚宣布撤換選委會主席；AP **9/16 20:25:04 TPE；12:25:04 UTC** 首次可靠發布。採首發時間，不宣稱撤換在 9/16 發生。 | https://apnews.com/article/1c2cadb70c3e22d120de41be7684d6e0 。歷史無 Abednego Akok Kacuol 本次撤換。未公布理由，選舉尚未宣告延期。 |

## 發布與圖像紀錄

- 圖像如採用，須標示為主題配圖或官方產品圖，不將舊型號、戰場或災害示意照片當作本次事件現場。圖源與權利記在 `presentation-2026-09-17.json`。
- 內容發布 commit `fde1a64a87551fe3db456781063201409f4a981d`；Pages 日期頁、最新入口及根入口均通過 HTTP 與完整位元組雜湊驗證。唯一私人 watchdog 於 2026-09-17 08:09:32 Asia/Taipei 回報 `Sent LINE message`、exit 0；pipeline check 隨後 exit 0。
- 公開網址：https://lucaskk.github.io/daily-news/wiki/daily/2026/09/2026-09-17/slides-2026-09-17.html?v=20260917-080846-reader
