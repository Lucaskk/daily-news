# 2026-10-26 來源筆記

研究截點：2026-10-26 08:03:35（Asia/Taipei），ISO 2026-10-26T08:03:35+08:00；UTC 2026-10-26T00:03:35Z。
全球24小時窗：2026-10-25T08:03:35+08:00至2026-10-26T08:03:35+08:00；UTC 2026-10-25T00:03:35Z至2026-10-26T00:03:35Z。
科技／AI 產品 14 日視窗：2026-10-12T08:03:35+08:00至2026-10-26T08:03:35+08:00；UTC 2026-10-12T00:03:35Z至2026-10-26T00:03:35Z。

- begin成功，legacy不變。只讀10/12–10/25十四份日報生成50列產品表，不查全歷史或歷史來源筆記。
- 十二啟用來源scan原始證據source-scan-20261026T000351676272.json保留私人目錄；逐站判讀及必要補查進行中，取得成功不等於全站已查。

## 第一批科技核對

- Engadget https://www.engadget.com/2296362/8bitdos-latest-button-only-arcade-controller-is-now-up-for-preorder/ metadata10/25 16:42:46Z，正文說六月曾揭露、本次是119.99美元預購與11/30出貨。官方 https://www.8bitdo.com/arcade-controller-pro/ 有美國Amazon及全球eShop預購連結；https://shop.8bitdo.com/products/8bitdo-arcade-controller-pro 標119.99USD、Ships on Nov30 2026。頁面靜態Sold out與Add to cart同存，不能由HTML字樣斷言每區有貨。較早10/23媒體已記錄開始預購，不稱10/25首次發表。只採預購狀態變更，不以六月舊揭露刷新日期。
- Yahoo最新文章提供UTM5.0正式版線索；官方GitHub API核實 https://api.github.com/repos/utmapp/UTM/releases?per_page=10 ：v5.0.8 published_at=2026-10-17T02:44:56Z、prerelease=false；此前v5.0.7（10/16）、5.0.6（9/24）至5.0.0均prerelease=true。採5.0系列正式穩定發布，不把10/26轉載當發布日。固定來源 https://github.com/utmapp/UTM/releases/tag/v5.0.8 。Notes明示圖形驅動仍實驗、遊戲相容有限、升級前應關閉VM，最低macOS12/iOS15。Changes5.0.8修正Rosetta不存在時DXMT備援與USB光碟安裝停頓；不把v5.0.7被刪除的刷新率修正列為已完成。
- lookup `8BitDo.*(Arcade|Pro)|Arcade Controller Pro|UTM.*5[.]0|5[.]0.*UTM`，只10/12–10/25十四份日報historical_match=false、truncated=false；再讀完整同窗50列產品表，兩事件未見。最初lookup PATH缺rg失敗，改既有runtime PATH後成功，不改系統設定。
- OpenAI首頁scan失敗，已逐站官方搜尋補查10/25論壇活動重播、10/20Terminal X個案與API changelog；重播／個案不作新品。10/22Decisions API GA為另一候選但未完成獨立去重與細節核對，本次不採，不稱無產品。

## 逐站查閱完成範圍

scan為11站retrieved、OpenAI failed。The Verge內容截斷，只判讀已取得最新文章，未宣稱全站窮盡。以下候選缺官方日期者保留待查，不以評論／評測標籤直接判舊，也不把存取失敗當作沒有新聞。

| 來源 | 實際最新文章與日期 | 決定 |
|---|---|---|
| Engadget | https://www.engadget.com/2296362/8bitdos-latest-button-only-arcade-controller-is-now-up-for-preorder/ ，metadata10/25 16:42:46Z；https://www.engadget.com/2294849/asus-proart-p16-rtx-spark-review/ | 控制器採用；ProArt評測仍待官方首次日期，不把新評測直接當發布。首頁Meta政府／公益貼連結收費為測試執行爭議，待官方範圍，不採。 |
| The Verge | https://www.theverge.com/tech/1018275/zen-browser-arc-replacement ，最新評論；https://www.theverge.com/tech/1018169/what-to-expect-apple-pro-and-tell-event-touchscreen-macbook-pro ，10/24 | 瀏覽器替代心得與Apple活動預測沒有可定位的新公開版本／發布，不採。截斷未顯示的文章不推定不存在。 |
| TechCrunch | https://techcrunch.com/2026/10/25/grok-releases-the-first-seven-minutes-of-its-ai-generated-odyssey/ ；https://techcrunch.com/2026/10/25/the-hottest-ai-wearables-and-gadgets-you-should-know-about/ | 影片內容展示不自動等於產品變更；穿戴總覽作線索，不以總覽日期刷新裝置。Dessa昨日已收錄，不重用。 |
| WIRED | https://www.wired.com/review/ray-ban-meta-audio/ ；https://www.wired.com/review/wallhack-m-001/ ；https://www.wired.com/story/kernel-panic-the-php-meltdown-shows-how-ai-makes-bugs-more-exploitable/ | 前兩者新品線索缺官方事件日期仍待查；PHP評論不等於新的正式修補。 |
| Ars Technica | https://arstechnica.com/gadgets/2026/10/updated-google-privacy-policy-says-your-gmail-might-be-used-for-advertising/ ；https://arstechnica.com/gadgets/2026/10/spotify-ramps-up-policy-enforcement-on-family-plans/ | 權限／執行政策候選仍待確切生效日期與官方段落，不採。火星／冰蓋科學不是產品發布。 |
| Cool3c | https://www.cool3c.com/article/253386 Xbox Nano台灣開賣；https://www.cool3c.com/article/253382 Googlebook翻轉螢幕；https://www.cool3c.com/article/253358 HHKB限量鍵盤 | Nano既有預購事件已10/15收錄，不能用文章說法重刊；Googlebook及HHKB仍待官方特定機型／首次日期。253387 LEGO特價是購物，不採。 |
| Yahoo奇摩科技 | https://tw.news.yahoo.com/utm-5-0%E6%AD%A3%E5%BC%8F%E7%89%88%E9%87%8B%E5%87%BA-windows-11-223345370.html ；https://tw.news.yahoo.com/linux-%E8%B7%91-mac-app-%E6%88%90%E7%9C%9F-223255355.html | 本次混合首頁確有最新UTM與Reef科技文章，UTM回官方GitHub採用；Reef相容層線索待官方發布紀錄，不據媒體轉載直接採用。 |
| TechOrange | https://techorange.com/2026/10/25/taipei-taiwan-ai-city/ ；https://techorange.com/2026/10/24/robotics-readiness-gap/ | 城市治理觀點與準備度研究不作產品；1Password10/23已收錄、非獨立新事件。 |
| 數位時代 | https://www.bnext.com.tw/article/92788/ntu-ic-design-ai-engine-taiwan-7-frontier-technologies ；https://www.bnext.com.tw/article/92752/cxmt-dram-boom-market-cap-ranking | 前沿研究與估值評論未找到對外產品發布／存取日期，待查或排除評論，不稱無新品。 |
| TechNews | https://technews.tw/2026/10/25/php-vulnerability/ ；https://technews.tw/2026/10/24/all-dlss-features-including-ray-reconstruction-have-been-ported-to-rdna-4-and-3/ | PHP第三漏洞須回正式修補段落才算產品更新，未完成不採；非官方模組需維護者版本日期，待查。供應鏈與市場預測不作產品發布。 |
| OpenAI | https://developers.openai.com/api/docs/changelog 10/22 Decisions GA；https://openai.com/index/terminal-x/ 10/20；https://forum.openai.com/public/videos/event-replay-building-ireland-and-europes-ai-advantage-innovation-competitiveness-and-skills 10/25 | 首頁失敗以官方限定搜尋補查成功；後二者案例／重播排除，GA留候選未完成去重不採。 |
| INSIDE | https://www.inside.com.tw/article/42728-volvo-launching-lower-priced-ev-2027 10/24；https://www.inside.com.tw/article/42726-kia-ev3-chinese-evs-canada 10/24；https://www.inside.com.tw/article/42724-tesla-cybertruck-au-nz | 車款路線與地區供應為候選，尚缺可定位官方首次日期；不以不同市場文章重寫為新品。 |

第二輪已查8BitDo官方產品／商店（硬體）、UTM固定release與API版本歷程（消費軟體／開發工具）、OpenAI官方changelog（AI）。採用兩則已核實獨立變更，不湊十則，不宣稱待查候選均不合格。

## 全球選題、時間與去重

窄化lookup `塞爾維亞|Vucic|Machado|馬查多|Hebron|希布倫|西岸|Prospector|Gabon|加彭|Boelo|波羅|Four Corners|里斯本|Lisbon|Vance|巴西|第聶伯羅|Dnipropetrovsk`，只10/12–10/25十四日報，14份、未截斷。命中：10/25巴西最後辯論、10/24希伯崙攻擊與準備封鎖、10/24 Vance二級；今日分別採實際決選／延長及恢復計票、實施工人通行限制／新流離失所、降熱帶風暴及新公報。其餘相同地理詞命中不等於同事件，例如WFP減援、工時修憲與西岸軍事行動不同。其餘候選未見同事件。

| 項目 | 時間基準與採用內容 |
|---|---|
| 1 塞爾維亞 | Reuters認敗專稿10/25 16:43EDT＝20:43Z＝10/26 04:43台北。AP/DW滾動頁有05:58／05:32Z開頁早時刻，不能把夜間認敗寫成早上；採Reuters具體新發布。135–140席為Vucic陣營樣本推估，不是選委會最終結果。 |
| 2 巴西 | Reuters首發10/25 08:01EDT＝12:01Z＝20:01台北報實際投票，晚間新法院延長與22:00Z恢復計票皆早於截點；AFP／Le Nouvelliste逐段已讀。AP滾動頁05:00Z不可當延長發布時刻，保留原文更新差異。截點前未取得最終勝者，不追用之後結果。 |
| 3 西岸 | AP10/25 08:03:37Z＝16:03:37台北，今日新增工人週日／一通行限制，希伯崙市府稱逾2600人流離失所。續10/24準備命令；不能把拘捕者涉武裝指控當定罪。 |
| 4 Machado | AP10/25 16:02:42Z＝10/26 00:02:42台北首次返國消息；Reuters／AOL完整後續19:18Z仍在窗內。今日實際返國，不把較早返國計畫或諾獎重刊。 |
| 5 烏克蘭 | ABC10/25 08:02美東＝12:02Z＝20:02台北，新一夜襲擊與當日更新傷亡；四死包含週日醫院死亡。ABC總區域22傷與KyivPost Synelnykove13傷範圍不同，不混加。沒有用昨日已收錄Starlink條款爭議再補一則。 |
| 6 歐洲風暴 | AP10/25 10:37:28Z＝18:37:28台北；myMotherLode轉載12:14:33Z、18:14:50Z更新。Boelo週日英國北部停電與交通中斷及向歐洲移動，不以星期五Austen舊災情刷新。 |
| 7 加彭 | Reuters初報10/25 02:30EDT＝06:30Z＝14:30台北；公司稿10:22Z。事故10/24 20:37當地＝19:37Z在24h外，採週日首次可靠公司確認／搜救與停產更新。公司初報5失聯；Reuters後續3消息源稱1死4失聯，政府尚未確認死亡，不抹平。 |
| 8 葡萄牙 | Reuters10/24 23:28EDT＝10/25 03:28Z＝11:28台北。今日凌晨2時後新清場，與10/20清場不同。Anewz10/25 06:57Z補查；不同時點拘捕數有差異，本文省略未核定總數，不重用55人舊數。 |
| 9 美國洪災 | AP10/25 17:18:03Z＝10/26 01:18:03台北；ABC全文當日晚版。週日新增洪水監視與清理危害，早前多日降雨為背景；不稱週日才開始下雨。 |
| 10 Vance | NHC固定第18報10/25 21:00Z＝10/26 05:00台北。降熱帶風暴、110km/h，無沿岸警戒，但仍有雨、土石流與長浪風險。續10/24二級颶風；不以17報仍颶風數值混用18報。 |

排除Starlink重複爭議、台灣10/24已發布616傷舊統計（10/25報紙不能刷新）、去年Sudan el-Fasher事件、Portugal10/20舊55拘捕，以及只含評論的候選。無法定位事件日者不湊名額。

## 逐篇圖片稽核

T1：官方商店og https://shop.8bitdo.com/cdn/shop/files/911.jpg?v=1792643978 ，已下載與目視，機身明標Arcade Controller Pro，有螢幕及磁吸腕托，不是舊Arcade Controller。8BitDo版權產品宣傳圖，非自由授權；來源、原圖及署名入manifest。
T2：GitHub固定release og為專案社群預覽，不代表新功能畫面。官方 https://getutm.app/ 有Windows11實際VM示範 https://getutm.app/assets/img/windows11.webp ，已下載目視，畫面系統日期10/16，標明官方示範，不說本報實測或保證3A效能。網站另有og https://getutm.app/assets/img/og.jpg 。權利屬UTM專案／相關系統權利人。

| 全球 | 原文／og檢查 | 決定 |
|---|---|---|
| 1 | DW成功，og https://static.dw.com/image/79758102_6.jpg ，Students' List勝選慶祝；Reuters／AP照片 | 未取得商業照片再用權，不發布，不稱無圖。 |
| 2 | MarketScreener與SooLeader403；AFP／Le Nouvelliste補查成功，og https://media.lenouvelliste.com/articles/2026-10-06/d1357563-3d90-4daa-af38-664501d6e6c9.jpg 為候選人合成資料圖 | 非當日投票或計票現場，權利未確認，省略。 |
| 3 | AP403、2news429，搜尋補到AP全文及2news照片說明：Mahmoud Illean/AP，10/24軍事閘門運送物資 | og未能直接取得，不能稱原文無圖；已知資料照且未取得再用權，省略。 |
| 4 | Reuters／AOL成功，og https://hermes.media.static.aol.com/media/2026/10/25/fa67d985-2281-31ed-b0ed-e13e876d6afa/b24f4db7-3dfb-4b35-ad73-bd4cf67746f5.jpg | 圖片存在；未完整確認再用權／影像拍攝條件，不發布。 |
| 5 | ABC成功，og https://i.abcnewsfe.com/a/36b40c00-fe56-4f19-9590-46f9b7181ebf/Kharkiv-DB-261025_1792928018662_hpMain_16x9.jpg?w=1600 ，正文10/24晚Kharkiv消防 | 存在事件配圖，未取得再用權，省略；另10/23Zelensky訪談照不冒充今日。 |
| 6 | myMotherLode成功，og https://mymotherlode.com/wp-content/uploads/2026/10/AP_8ed16cc14af9428fa48816bcb3bfdeb5_2aa5bf4dc7.jpg | AP照片存在，權利未取得，省略。 |
| 7 | 公司稿StockTitan成功，og https://static.stocktitan.net/company-logo/borr-lg.png?v=e110a104f3 僅logo；Offshore報導配圖明示Grok AI產生地圖 | 不用logo或AI圖當沉沒現場，省略，不稱所有媒體無圖。 |
| 8 | MarketScreener403，Anewz補查成功，og https://anewz.tv/data/images/2026-10-25/38224_2026-10-25t033050z-1-lynxnpem9o032-rtroptp-4-portugal-politics-protests_f.JPG?t=1792913912 ，說明為10/24示威Reuters | 是較早示威照片，非已驗證週日清場，且未取得再用權，省略。 |
| 9 | ABC成功，og https://i.abcnewsfe.com/a/c3d2d46b-6389-4717-9fb3-815a0bcaeb8e/wirestory_961459bac9d5db8dc9e5260cac61aec3_16x9.jpg?w=1600 ，South Fork Fire Rescue via AP，10/23露營車淹水 | 舊現場、權利未確認，省略，不說無圖。 |
| 10 | NHC18報文字頁只有機關標誌；AP／AOL補查有og https://hermes.media.static.aol.com/media/2026/10/25/e602fd2b-5025-341d-aaae-61323af5d82e/31505f0a-598c-46a0-819a-5ba32dffbec3.jpg | 未確認這張圖精確拍攝時間及權利，不發布；不把公報機關logo當氣象照片。 |

私人原始快取不加入Git。沒有安裝套件、變更研究模式、排程、憑證或配送防護。
