# 2026-10-22 來源筆記

研究截點：2026-10-22 07:57:13（Asia/Taipei），ISO 2026-10-22T07:57:13+08:00；UTC 2026-10-21T23:57:13Z。
全球24小時窗：2026-10-21T07:57:13+08:00至2026-10-22T07:57:13+08:00；UTC 2026-10-20T23:57:13Z至2026-10-21T23:57:13Z。
科技／AI 產品 14 日視窗：2026-10-08T07:57:13+08:00至2026-10-22T07:57:13+08:00；UTC 2026-10-07T23:57:13Z至2026-10-21T23:57:13Z。

- begin成功，legacy不變。僅比對10/08–10/21十四份日報與同窗60列產品表，不讀更早報告／來源筆記／完整歷史ledger。
- scan十二站皆取得內容；私人證據source-scan-20261021T235729581622.json，含取得時間、內容雜湊與原始頁位置。scan不等於選題完成。
- 已逐站讀首頁最新連結：Engadget的A1已收錄；新Xbox付費雲端、Claude Duet、Sony耳機為候選。Verge的PHP漏洞與EA關閉工作室另查事件；iPhone Duo評測須回查首發不可直接當新品。TechCrunch與WIRED均出現Recursive Flint模型，待官方核對。Ars列Xbox付費與OpenAI雲端分銷。Cool3c列Ricoh GR WORLD v2.0、Leica F1版與OPPO全球版，優惠不直接當新品。
- Yahoo科技入口混一般新聞，已下讀科技連結：Xbox掌機價格是傳聞，iPhone Duo開箱不重設發布日期。TechOrange列Mastercard Agent Pay示範；數位時代列DSX POD；TechNews列三星基頻傳聞與24家Robot Ready活動，未當已上市；OpenAI列10/21PHP協調揭露與生物研究；INSIDE的OSS Scanner原10/8發布已是舊事件，Grab禁結合另列全球候選。
- 第一輪全球候選：俄烏三方談判、駐沙國人員撤離、非洲CDC伊波拉會議、喬治亞禁黨案開庭、薩爾瓦多海地救援、台灣Grab結合禁令、義大利運輸抗議擴散、埃及對海界協議正式回應。尚在查證，不宣稱已完成或配送。

## 官方第二輪與入選科技

第二輪涵蓋消費軟體、開發／企業架構、相機與遊戲：Claude官方產品公告、NVIDIA newsroom與技術文、Xbox Wire、Ricoh版本頁與韌體更新，另查PHP正式安全公告作全球資安事件。沒有用十則上限當必須湊滿數量。

- T1 Claude Duet： https://claude.com/resources/articles/claude-duet ，官方10/21日期（metadata亦為date-only）。research preview、US Pro／Max waitlist、共享既有usage limits；具雲端VM／browser，背景檢查每幾小時一次也扣額度。送信、付款、簽署、刪除前須確認；仍可能誤判優先度。不是全球全面推出，也不是無限額度。全文已讀，未把宣傳個案當獨立實測。
- T2 NVIDIA OpenShell Reference Architecture： https://nvidianews.nvidia.com/news/openshell-reference-architecture ，10/21日期，Availability段明列now available。Vera Rubin推理、Vera CPU執行代理、BlueField-4／Sentry作獨立監測及政策執行。不是宣稱OpenShell軟體首次存在，亦非把所有夥伴整合都稱已完成。技術補充 https://developer.nvidia.com/blog/how-nvidia-openshell-reference-architecture-secures-and-governs-ai-agent-workloads-at-scale/ 。原廠倍數未當實測，本文不採效能倍數作結論。
- T3 Xbox Cloud Playtime： https://news.xbox.com/en-us/2026/10/21/cloud-playtime-now-available-to-test-with-xbox-insiders/ ，metadata首發10/21 18:00:03Z=10/22 02:00:03台北。無Game Pass的合格Insider可測試10／25／50小時包，US$3.99／7.99／11.99；無廣告、未用完不失效。須另有可雲端遊玩的遊戲授權（或合格免費遊戲）；市場、preview ring與裝置有限制。預定十一月擴展不是已普及。
- T4 GR WORLD2.0： https://www.ricoh-imaging.co.jp/japan/products/app/gr-world/ ，精確定位新着情報2026.10.21的2.0.0段。GR ID、App設定／相機註冊／image control／album／GR Log備份；照片本身不備份，最多五台智慧裝置。GR IV系列可共享image control與自訂結束畫面，不能說GR III全功能相同。GR IV韌體1.20、Monochrome1.10；30周年畫面選取期限日本時間12/31，綁ID後可續用。官方韌體依據 https://www.ricoh-imaging.co.jp/japan/support/download/digital/gr4_s.html 10/21段。

科技窄化lookup：`Claude.*Duet|Anthropic.*Duet|NVIDIA.*OpenShell|OpenShell.*(參照|架構)|Xbox.*(playtime|時數|計時|按時)|GR WORLD.*(2.0|雲端)|Ricoh.*(2.0|30周年)`；10/08–10/21十四份日報無命中，輸出未截斷，因此完整核對同範圍60列recent-14d表（分段補讀尾段），四項皆無同事件。表內個別自動公司分類失準不作語意去重依據，仍核對產品與變更欄；不自行修改歷史日報或完整ledger。

## 逐站文章補充紀錄

| 啟用站 | 實際單篇／最新文章及發布依據 | 取捨 |
| --- | --- | --- |
| Engadget | https://www.engadget.com/2293646/claude-duet-is-anthropics-answer-to-meta-muse-and-openai-dots/ ，首頁10/21；https://www.engadget.com/2293519/xbox-is-previewing-paid-cloud-gaming-for-players-without-game-pass/ | 兩項回查官方採T1／T3；A1是昨天已收錄。iPhone Duo及OPPO hands-on先看新品線索，不以評測時間冒充首發。 |
| The Verge | https://www.theverge.com/tech/1015906/php2shell-vulnerability-october-2026 ，首頁最新10/21；https://www.theverge.com/tech/1015028/iphone-duo-review | PHP轉查原專案10/21修補為全球事件；折疊機評測不重設先前發布。首頁excerpt截斷後已另解析原始頁連結，不以節錄為全站。 |
| TechCrunch | https://techcrunch.com/2026/10/21/recursive-launches-flint-a-laptop-coding-model-it-says-was-largely-built-by-ai/ ，metadata10/21 20:27:41Z | Flint為候選，尚未完成官方模型與發布條件確認，未選不代表不存在；募資、Meta用戶數與Tesla財報不充當產品發布。 |
| WIRED | https://www.wired.com/story/recursive-self-improvement-flint-latest-model-scary-good/ ，metadata10/21 16:00Z | 與Flint同線索待官方確認；原文可取得，不是昨日404頁；折扣攝影機與地毯不直接當新品。 |
| Ars | https://arstechnica.com/gaming/2026/10/xbox-wants-you-to-pay-24-to-40-cents-per-hour-to-stream-games-you-already-bought/ ，首頁最新10/21 | 回查官方計時預覽採T3，不把付費雲端誤寫含遊戲買斷。其他硬體價格傳聞不採。 |
| Cool3c | https://www.cool3c.com/article/253231 ，metadata10/21 15:13台北，10/22 06:48修改 | GR WORLD回查原廠10/21段採T4；不是用更新時間。253237 OPPO實機、253217 Leica特別版留官方日期待查；HTC與Pixel出清排除價格事件。 |
| Yahoo科技 | https://tw.news.yahoo.com/tech-news/ 下讀科技連結：下一代Xbox價格文章電玩宅速配20261021、iPhone Duo台灣開箱 | 第一項明示傳聞未採；開箱與中國預購熱銷不是新的獨立發布。首頁混一般新聞不當作已無科技內容。 |
| TechOrange | https://techorange.com/2026/10/21/mastercard-agent-pay-for-machines/ ，metadata10/21 17:48:43台北 | Agent Pay示範待確認是否獨立可用性更新，未以示範直接當普遍可用產品；AWS投資是企業消息。 |
| 數位時代 | https://www.bnext.com.tw/article/92730/nvidia-dsx-pod-vera-rubin-ai-data-center-20261021 ，metadata10/21 17:53台北 | DSX POD另有候選；本次採OpenShell獨立安全架構，不混寫為同一產品。原廠第二輪已查NVIDIA newsroom，不宣稱只有入選四則合格。 |
| TechNews | https://technews.tw/2026/10/21/samsungs-next-generation-m2800-baseband-chip-will-be-built-at-2-nanometers/ ，日期路徑10/21，metadata未提供首發時分 | 製程／型號報導尚缺官方具體發布，不採。Robot Ready活動不是自動等於所有展示產品已上市。 |
| OpenAI | https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/ ，官方首頁10/21 | PHP揭露回查php.net正式更新，不另當模型產品；生物資料研究不自動當商用新品。 |
| INSIDE | https://www.inside.com.tw/article/42690-anthropic-oss-scanner-free-periodic-vulnerability-scans-open-source ，metadata10/22 07:45:32台北 | 文內原事件10/8，recent表有10/10收錄，排除重複；Grab10/21另以公平會原公告核對。 |

## 全球去重與時間批次

lookup一：`三方.*談|Witkoff|威特科夫|沙烏地.*撤|伊波拉.*(奈及利亞|會議)|喬治亞.*(禁|政黨)|海地.*(薩爾瓦多|人質)|北韓.*廣播|Grab.*foodpanda|義大利.*(卡車|運輸|短缺)|埃及.*海|PHP.*(漏洞|修補)` 無命中。
lookup二：`北韓|金與正|奈及利亞|Nigeria|喬治亞|Georgia|布格磊|Bukele|三方|海界|Grab|foodpanda|PHP|OpenShell|GR WORLD|Duet|Cloud Playtime` 只有北韓10/15潛射巡弋飛彈及「第三方」文字誤命中，非本次廣播事件。
lookup三：`伊波拉|Ebola|烏克蘭.*(談|奧斯陸)|沙烏地.*(英國|戰機)|米蘭.*軍` 命中10/19剛果第八省、10/17肯亞第三例、10/14剛果統計。全球伊波拉將標續報，前次10/19，本次10/21區域危機會議召集，奈及利亞週二首例為背景。米蘭10/21部署軍人與本次卡車供應鏈抗議不同。

全球候選時間皆在10/21 23:57:13Z截點前，完整原始網址保留於日報逐篇來源：PHP官方10/21修補日期；俄三方談判AP07:54:34Z（Local10 metadata發布／修改欄顛倒，採AP首發不冒用更新）；駐沙國撤離AP20:31:41Z；Africa CDC會議AP11:04:27Z；喬治亞開庭AP17:29:04Z；公平會10/21官方日期；北韓廣播Reuters06:34Z／AP08:29:33Z；海地救援Reuters20:11Z／AP21:49:31Z；義大利供應Reuters13:52Z；埃及回應Reuters轉載10/21日期，Sowetan17:34南非時間=15:34Z。

奈及利亞病例感染來源存在不同敘述：烏干達否認感染源在當地，不能僅由旅經烏干達推論感染國。PHP舊文「沒有修補／舊版完全沒有修正」已落後：10/21正式公告明列支援分支版本及7.4／8.0／8.1 minimal source-backports，後者不是恢復一般維護。

## 逐篇圖片稽核與使用

| 項目 | 原文及og查核 | 決定 |
| --- | --- | --- |
| T1 Duet | 官方og https://claude.com/resources/articles/claude-duet/opengraph-image/og ，下載403；正文另有SVG App icon、三名受訪者肖像及連接器logo拼圖 https://assets.claude.com/c3618d5ce675bcaa9716a06d180879c2b94161c3.png 。 | 有圖但og存取失敗，肖像與logo不代替操作畫面，省略，不寫沒有圖片。 |
| T2 OpenShell | 官方og原圖 https://iprsoftwaremedia.com/219/files/202610/b61bfda00ad668f9890d5b5b0d775b1e/6ad693aa3d63324483072858_NVIDIA-OpenShell-Reference-Architecture/NVIDIA-OpenShell-Reference-Architecture_21af43b3-e9a2-4b8b-a792-e5382e40f9aa-prv.jpg?v=21af43b3-e9a2-4b8b-a792-e5382e40f9aa ，下載並目視核對1920x1080三晶片／安全符號示意。 | 本地openshell.jpg，明標官方架構硬體示意，非部署現場或防護效果證明。NVIDIA權利保留，非自由授權。 |
| T3 Xbox | 官方og https://xboxwire.thesourcemediaassets.com/sites/2/2026/05/Bootup_Wire-9c068aa206c9a72d2b1f.png ，是通用Xbox品牌預覽，不是新計時購買介面。 | 省略，不把品牌圖當新品UI。 |
| T4 GR WORLD | 官方og只是 https://www.ricoh-imaging.co.jp/common/img/og-image.gif ，另逐篇找到實際備份畫面 https://www.ricoh-imaging.co.jp/resources/japan/products/app/gr-world/top/img/update_img_04.png ，下載目視核對，明列照片不備份。 | 本地gr-world.png，官方日文示範畫面，內部10/6樣本日期不是發布日；不裁切。Ricoh權利保留，非自由授權。 |
| 全球1 PHP | php.net og https://www.php.net/images/meta-image.png 為一般專案預覽；安全公告以文字為主，非受害站點現場。 | 省略品牌圖，不宣稱各報導都無圖。 |
| 全球2 俄談判 | Local10原文與og有AP照片 https://www.local10.com/resizer/v2/QGV4GMGGPXJEVEOMM6ITXZOSDQ.jpg?auth=77b0c5611e6b5f2c8b657aed21f45467fa07f490693d1b36a8f19fcd9ebd3d2c&width=700 。 | 有照片，未核再利用權利，省略而非無圖。 |
| 全球3 撤離 | CityNews照片10/14利雅德街景，AP／Baraa Anwer；og https://ottawa.citynews.ca/wp-content/blogs.dir/sites/4/2026/10/b13efdc0f06eeb811135961f2266ba29d311c97a5f7171df89645f92eab4ba1e.jpg 。 | 舊街景不是今日撤離現場，權利未核，省略。 |
| 全球4 伊波拉 | Euronews原文有剛果Beni治療中心AP／Sebastien Kitsa Musayi圖；og https://images.euronews.com/articles/stories/09/96/20/58/1200x675_cmsv2_be4245aa-154e-5bbb-8661-ad3320d05bee-9962058.jpg 。 | 不能當奈及利亞病患或未舉行會議現場，權利未核，省略。 |
| 全球5 喬治亞 | AP直接403；MRT轉載可搜尋到10/21巴統法院入口保安照片，但直接擷取沒有可用metadata。 | 圖片線索存在但未取得可核原圖URL與再利用條件，省略，不說原文無圖。 |
| 全球6 Grab | Focus Taiwan有CNA資料照；og https://imgcdn.cna.com.tw/Eng/WebEngPhotos/WebOg/600/2026/20261021/1023x536_914024239777.jpg 。公平會原站Python憑證驗證失敗，網頁搜尋工具成功讀官方稿，不改SSL安全設定。 | 有照片但屬資料照、權利未核，省略，不當10/21表決現場。 |
| 全球7 北韓 | Korea JoongAng Daily有2025/8/11擴音器資料照，og https://image.koreajoongangdaily.com/12932850.jpg?imageId=12932850&x=0&y=5.28&cropw=100&croph=71.67&panox=0&panoy=5.28&panow=100&panoh=71.67&width=1200&height=683 。 | 不是本月部署完成證據，權利未核，省略。 |
| 全球8 海地 | AP與MarketScreener直接403，後者搜尋可讀Reuters全文。未可靠取得原圖URL；不能推論原文無配圖。 | 存取限制而省略，不是無圖結論。 |
| 全球9 義大利 | Internazionale有Reuters／Ciro De Luca10/20拿坡里空貨架手機照；og https://media.internazionale.it/images/2026/10/21/361825-hd.jpeg 。 | 明確前一天照片、權利未核，本次省略，不冒充週三現場。 |
| 全球10 埃及 | Sowetan有2022/2/10利比亞Tobruk國會保安Reuters／Esam Omran Al-Fetori照片；og https://www.sowetan.co.za/resizer/v2/RPX5LP6OXJG5DC2RWVCIXO4AAI.JPG?smart=true&auth=20ad63141c08e78c80712f7f70535d36d432d80f269f8024fc1ae7c379deebbd&width=1200&height=630 。 | 歷史資料照不當今日埃及聲明現場，權利未核，省略。 |

## 發布交接

最終採4則科技、10則全球。產品段落、全球時間依據、續報與圖片設定已完成；直接交finish渲染及發布驗證。研究筆記不手寫成功狀態，Pages與LINE以pipeline及私人watchdog結果為準。
