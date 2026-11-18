# Wiki 操作紀錄

只往後新增。每筆標題格式為 `## [YYYY-MM-DD] 類型 | 標題`，查詢方式：`grep "^## \[" wiki/log.md`。

## [2026-11-15] init | 建立 wiki 骨架
- 依需求訪談（10 題）建立 AGENTS.md、CLAUDE.md、wiki/index.md、wiki/log.md
- 建立資料夾：wiki/{papers,concepts,paradigms,syntheses,town}、slides/、cache/text/
- raw/ 有 5 篇論文：Axelrod1981、Berg1995、Horton2026（arXiv v2）、Park2023、Xie2024
- .gitignore 加入 cache/，因為抽出的文字有版權
- 分支 master 改名為 main
- 尚未執行：lint.py、PDF 抽文字、ingest

## [2026-11-15] extract | 以 pypdf 抽取 5 篇 PDF 文字
- 新增 extract.py；安裝 pypdf 7.1.0 到 Anaconda Python
- Axelrod1981：11 頁都有文字。這是 JSTOR 掃描檔，但內含 OCR 文字層，品質中等，例如 `strategies'?`、`Erzviron-mentcrl` 這類 OCR 錯誤
  - p.1 是 JSTOR 封面，p.2 開頭是前一篇文章的結尾
  - 英文引文要從 cache 文字取，不要從圖片重打，否則 lint (b) 會比對失敗
- Berg1995：21 頁全部沒有文字，是純圖片掃描檔，而且頁面圖片倒置 180°
  - 已試著讀取頁面圖片，可以清楚辨識（第 1 頁 = 期刊第 122 頁，與 page_offset 121 相符）
  - 待使用者決定是否人工轉錄
- Horton2026（53 頁）、Park2023（22 頁）、Xie2024（56 頁）：都有文字

## [2026-11-15] lint | 新增 lint.py，第一次執行通過
- 實作 (a)(b)(d)(e)(g)(h)(i)(k) 和「無出處句 (s)」；`--fix` 修機械性問題
- 已用含刻意錯誤的測試 wiki 驗證：每項都抓得到，`--fix` 後只剩內容問題
- 真正的 repo：0 個頁面，ERROR 0，WARN 1（Berg1995 沒有文字可比對）

## [2026-11-15] extract | Berg1995 人工轉錄 p.1–17，p.18–21 未轉錄
- 依頁面圖片人工轉錄到 cache/text/Berg1995.txt，檔頭標註 `# source: vision-transcribed`
  - 頁面圖片其實是上下翻轉存放，不是旋轉 180°
- 圖只轉錄圖說和圖內的小表格，不從圖上讀數值（Fig. 2–5 的個別資料點、Fig. 4 的箱型圖數值都沒有轉錄）
- p.18–21 未轉錄：轉錄被內容政策中斷，使用者指示停止、不重試
  - 檔頭加 `# untranscribed: 18-21`，頁內只放內容概述
- 這幾頁的內容：附錄 A 實驗說明（p.18–19）、社會歷史組拿到的報告表、附錄 B 每一對的原始數據、參考文獻（p.20–21）
- lint.py 新增：引用未轉錄頁面時發出 WARN，引文跳過自動比對，改為提醒人工核對
- 待使用者決定：抽查 2 頁實驗結果數據後，才開始 ingest
- 發現原文不一致：附錄 B 場次日期寫成 /92，p.9 Table I 寫成 /93，ingest 時要記錄

## [2026-11-15] decision | Berg1995 轉錄範圍
- 問題：轉錄被內容政策擋下，要怎麼處理？
- 使用者決定：停止轉錄、不重試；p.18–21 只看不抄，在 cache 和 AGENTS.md 註明未轉錄；lint 遇到引用這幾頁時提醒人工核對

## [2026-11-16] decision | Berg1995 轉錄抽查通過
- 使用者對照 PDF 抽查 p.10、p.14（期刊頁 131、135）的數字，全部正確，頁碼換算也正確

## [2026-11-16] decision | Axelrod1981 校準計畫
- 問題：還沒有資料的段落怎麼寫？→ 使用者決定新增〔待補〕標記；lint 跳過這些行，但要像〔待檢視〕一樣列出位置
- 問題：圖 1 的 S 值 OCR 沒有抽到，PDF 圖片是 JBIG2 格式無法解碼（沒有安裝 jbig2dec）→ 使用者對照 PDF 第 4 頁（期刊頁 1392）確認 R=3、T=5、P=1、S=0，條件是 T > R > P > S 且 R > (S+T)/2
- 問題：小鎮頁要現在建嗎？→ 現在建，但先只建 1 頁用來校準格式
- 術語：同意提案的譯名，但 ALL D 改譯為「永遠背叛」
- 頁面拆分：單次和重複囚犯困境合併成 paradigms/prisoners-dilemma.md，頁內分兩節；互惠和再相遇機率 w 保持兩頁，因為 w 之後會是小鎮的設計參數

## [2026-11-16] schema | 新增〔待補〕標記
- AGENTS.md §4.4 新增〔待補〕規則；原 §4.4、§4.5 改為 §4.5、§4.6
- lint.py：以〔待補〕開頭的行跳過「無出處句」檢查，(k) 列出所有〔待補〕的位置

## [2026-11-16] ingest | Axelrod1981
- 新增 8 頁：papers/axelrod1981.md、paradigms/prisoners-dilemma.md、concepts/tit-for-tat.md、concepts/evolutionarily-stable-strategy.md、concepts/reciprocity.md、concepts/continuation-probability.md、town/reciprocity-needs-recognition.md、glossary.md
- 頁面對應：PDF p.1 是 JSTOR 封面，p.2–8 是正文（p.2 = 期刊 1390，page_offset 1388），p.9–11 是 JSTOR 參考文獻連結頁
- OCR 的數學式有亂碼，例如 w ≥ (T−R)/(T−P)，一律用中文轉述加出處，不用英文原句引用
- 本篇沒有人類受試者，也沒有和其他頁面的矛盾，所以還沒建 contradictions.md

## [2026-11-16] lint | Axelrod1981 ingest 後
- `lint.py --fix`：通過，ERROR 0、WARN 0
- 自動修正：index.md 補上 8 頁
- 3 則英文引文都逐字比對成功
- 〔待補〕共 7 處：4 個概念頁的「爭議與未解問題」、囚犯困境頁的「人類基準數據」和「LLM 代理人的結果」、小鎮頁的「風險與待驗證」

## [2026-11-16] decision | w 門檻的寫法
- 問題：w ≥ 2/3 能不能改成英文原文引用？
- 查核：原文 p.5 有條件式，編號為條件 (1)，但 OCR 是亂碼（`w 2 (T - R)I(T - P)`）；p.2–8 沒有代入圖 1 數值的結果
- 使用者決定：cache 不改；條件式維持中文轉述加 [Axelrod1981, p.5]；2/3 保留〔推論〕並寫出計算式；囚犯困境頁和再相遇機率頁用同一句
- 已套用，lint 通過（ERROR 0、WARN 0）

## [2026-11-16] review | Axelrod1981 AI 審查
- 由全新的子代理人審查 8 頁，只提供頁面、原文 p.2–8、glossary.md
- 結果：ERROR 3、WARN 17、SUGGEST 6
- ERROR：小鎮頁 summary 含設計推論；互惠頁的摘要和術語表定義在內文中找不到出處；互惠頁把「回報是親緣程度的線索」誤寫成「回報是是否繼續合作的線索」（p.6）
- 依規則，內容問題只回報，等使用者決定是否修改

## [2026-11-16] decision | 第二輪競賽「200 步」的用字
- 問題：再相遇機率頁寫「w = .99654，期望長度 200 步」，但 1/(1−.99654) ≈ 289，0.99654^200 ≈ 0.5，200 步應是中位數
- 查核：原文 p.8 註 23（OCR）寫 "with an expected probability of 200 moves"，沒有用 median，也沒有寫成清楚的 expected length；「期望長度」是 wiki 的錯誤解讀
- 使用者決定：依原文修正
- 已修正論文頁和再相遇機率頁（寫法一致）：原文描述加 [Axelrod1981, p.8]，計算結果標〔推論〕；論文頁也補上「第二輪和第一輪一樣，每對比 5 場」（審查 S1）
- lint 通過（ERROR 0、WARN 0）

## [2026-11-16] lint | 擴充 lint (b)：內文英文片段也要逐字比對
- 起因：再相遇機率頁的 "an expected probability of 200 moves" 是夾在中文句中的片段，原本的 lint (b) 只檢查 `>` 開頭的整句引文，不會比對它
- 使用者決定：擴充 lint (b)。比對前的正規化和整句引文相同（合併斷行連字號、統一空白和引號）
- 測試：在再相遇機率頁暫時插入 4 行，結果符合預期
  - 用字錯誤（"an expected length of 200 moves"）→ ERROR：p.8 找不到
  - 頁碼錯誤（正確片段標成 p.5）→ ERROR：指出在 p.8 找到
  - 沒有出處 → ERROR：沒有出處，無法比對
  - 斷字正規化（cache 原文是 prob-\nability）→ 通過
- 測完依使用者指示，用測試前的備份 cp_backup.md 還原頁面（沒有用 git checkout），確認沒有「測試」字樣，lint 回到 ERROR 0
- 順便修正：lint.py --fix 在 Windows 寫檔時會把換行變成 CRLF（index.md 因此是 CRLF），改成一律用 LF 寫檔，並把 index.md 轉回 LF
- AGENTS.md §10.1 (b) 補上片段比對的說明

## [2026-11-16] schema | 英文雙引號只用在原文逐字引用
- 問題：術語或篇名如果用雙引號，擴充後的 lint (b) 會誤當成引文比對；要改成只比對 4 個字以上的片段，還是規定寫法？
- 查核：目前 wiki 裡雙引號括住的英文全是真正的引文（3 則 `>` 引文和 2 處片段），沒有誤報
- 使用者決定：規定寫法。英文雙引號只用在原文逐字引用；術語寫成「中文 (English)」，篇名用斜體，都不加雙引號
- AGENTS.md §4.5、§5 已更新；lint.py 不用改；lint 通過（ERROR 0）

## [2026-11-16] decision | 審查 ERROR E1–E3 的修正
- E1（town 頁 summary 含設計推論）：summary 改成「互惠合作要穩定，需要認得出對方，而且雙方很可能再碰面。」；被刪掉的後半句依使用者指示移到「設計點子」第一點，標〔推論〕
- E2（互惠定義沒有出處）：互惠頁的 summary、白話摘要和「定義」段改成照原文「以牙還牙照做對方上一步，作者稱之為以互惠為基礎的合作」[p.5]；術語表「互惠」一列一起改（W17）
  - 「原文沒有另外定義互惠」是對原文的「缺席」所做的判斷，原文不會寫，所以標〔推論〕，不標 p.5；術語表只保留有出處的部分
- E3（回報是親緣線索，寫反）：使用者要求先核對 p.6 的後半句。原文明確寫到 "modifiers for more selfish behavior after a negative response from the other are advantageous whenever the degree of relatedness is low or in doubt"，所以兩個半句都保留；主詞照原文寫成「修飾基因 (modifiers)」
- lint --fix：通過（ERROR 0），自動修正互惠頁 has_inference → true

## [2026-11-16] decision | 審查 WARN W11–W16（術語）的修正
- 使用者指示：「合作 (Cooperate)」「背叛 (Defect)」全 wiki 統一這個寫法，術語表也一致；W16 新術語的定義要照原文說法加頁碼，原文沒有明確定義的標〔推論〕，不要自行下定義
- 用腳本找出每頁術語第一次出現的位置，再逐處補英文，共 7 頁 19 處：
  - 合作 (Cooperate)、背叛 (Defect)：論文頁、以牙還牙頁、演化穩定策略頁、互惠頁、再相遇機率頁、小鎮頁
  - 再相遇機率 (Continuation Probability)：囚犯困境頁、以牙還牙頁、演化穩定策略頁、互惠頁、小鎮頁
  - 演化穩定策略頁的白話摘要補上囚犯困境、永遠背叛、以牙還牙的英文；再相遇機率頁的白話摘要補上以牙還牙、互惠
  - 論文頁的「友善 (nice)」改成「友善策略 (nice strategy)」（W12）
- 術語表新增 4 個術語：互惠理論 [p.2]、生態分析 [p.5]、適應度 [p.3]、廣義適應度 [p.6]；4 個都能找到原文說法，不需要〔推論〕
- lint --fix：通過（ERROR 0）
- W1–W10 等使用者決定

## [2026-11-16] decision | 「合作」區分動作和名詞；審查 W1–W8、W10 的修正
- 使用者決定：囚犯困境的兩種動作寫成「合作 (Cooperate)」「背叛 (Defect)」；名詞「合作這件事」寫成 (cooperation)；「以互惠為基礎的合作」用原文詞組 (cooperation based on reciprocity)；術語表兩種都列並註明差別
- 上一輪統一時誤改成 (Cooperate) 的名詞已改回：論文頁、再相遇機率頁、互惠頁、以牙還牙頁、小鎮頁；演化穩定策略頁和囚犯困境頁的名詞第一次出現補上 (cooperation)
- 術語表：「合作」拆成「合作（動作）Cooperate」「合作（名詞）cooperation」，新增「以互惠為基礎的合作」；W6 引入的戀巢性 (Philopatry)、領域性 (Territoriality) 也加入術語表，定義照原文 p.7
- W1–W8 照審查建議全部修改：
  - W1 論文頁摘要加上「再相遇機率夠高時」的前提
  - W2 囚犯困境頁摘要補上「能認出對方、記得過去」，後半句改成和內文一致
  - W3 互惠頁摘要和 summary 改成「合作要能演化，其中兩個條件」
  - W4 論文頁改成「永遠背叛仍是唯一的演化穩定策略」；囚犯困境頁的同一句也一併改成一致的寫法
  - W5 清潔共生改成「似乎沒有已知例子」，並補上甲殼類
  - W6 戀巢性和領域性獨立成一點
  - W7 親屬關係改成「收益的一部分、廣義適應度」
  - W8 「齒輪只能往前轉」改成直接描述不對稱；引文中譯改成「社會演化的齒輪裝有棘輪」
- W10 使用者決定：允許頁碼範圍，只能用在連續頁；AGENTS.md §4.1 和 §10.1 已補上
  - lint (a) 新增範圍檢查，在 scratchpad 副本測試：p.4–5、p.6-7 通過；p.5–4、p.5–5 報錯（起始頁必須小於結束頁）；p.10–12 報錯（p.12 超出 11 頁）；Berg1995 p.17–19 對 p.18、p.19 發出未轉錄 WARN
- lint --fix：通過（ERROR 0、WARN 0）

## [2026-11-16] ingest | 新增 Axelrod 電腦競賽頁（審查 S5）
- 使用者決定：建立 S5，S2、S3、S4、S6 暫不建
- 新增 paradigms/axelrod-tournament.md：第一輪、第二輪、生態分析分節寫；每個數字都回 cache 核對並附頁碼（14 個策略加 1 個隨機、循環賽、200 步 [p.5]；62 個策略、6 國、300 萬次選擇 [p.5]；w = .99654、兩輪每對 5 場 [p.8]）
- 第二輪長度的原文說法和〔推論〕計算，和再相遇機率頁用同一句
- 核對時發現：
  - 使用者指示寫「30 萬次」，原文 p.5 是 "3 million choices"，頁面照原文寫 300 萬次
  - 原文前後不一致：第一輪只列出 4 個領域，第二輪卻說「第一輪的五個學科」；頁面照原文並用〔推論〕註明
- 和囚犯困境、以牙還牙、再相遇機率、小鎮、論文頁互相加連結；術語表新增電腦競賽 (Computer tournament)、循環賽 (Round robin)，生態分析的詳細頁面改指向新頁
- lint --fix：通過（ERROR 0），index.md 自動補上新頁
- 第二輪 AI 審查已開始（全新子代理人，審查全部 9 頁）

## [2026-11-16] review | Axelrod1981 第二輪 AI 審查
- 全新子代理人審查 9 頁（含新增的電腦競賽頁），只提供頁面、原文 p.2–8、glossary.md
- 結果：ERROR 0、WARN 15、SUGGEST 3
- 出處和數字全部對得上（含 p.4–5、p.6–7 範圍、page_offset 1388）；〔推論〕的計算（289、0.5、2/3）都正確
- WARN 主要是：「最簡單」只適用第一輪、town 頁把「認得出對方」寫成必要條件、詞組中插入英文、術語缺英文、術語表英文大小寫不一致、清潔魚與染色體推測的措辭
- 等使用者決定

## [2026-11-16] decision | 第二輪審查 R1–R15、大小寫規則、town 頁改名、個體辨識頁
- R1–R13、R15 照建議修改；額外處理：
  - R1/R2「兩輪都最高平均分」的說法另外出現在以牙還牙頁、囚犯困境頁、電腦競賽頁 summary，共 4 處一起改成「第一輪平均分最高，第二輪再次獲勝」
  - R5 依使用者指示，論文頁寫「小魚或甲殼類清潔者」；互惠頁的「清潔共生」是原文 cleaner mutualisms 的直譯，不改
  - R11「第二輪電腦競賽…」是三頁共用的同一句，三頁一起補上 (computer tournament)
- R14 大小寫：使用者確認清單，並把演化穩定策略移到一般概念類。規則寫進 AGENTS.md §5：賽局、策略名稱、動作用大寫；一般概念在內文用小寫；頁面標題、連結文字、篇名用 Title Case；術語表英文欄照內文寫法並保留代號
  - 內文 7 頁 15 行、術語表英文欄 20 列改成小寫
- town 頁改名：使用者指示標題改成「互惠需要無法匿名 (Reciprocity Requires Non-Anonymity)」，檔名改成 town/reciprocity-requires-non-anonymity.md
  - 用腳本替換 6 個檔案的路徑和標題，沒有殘留；log.md 只往後新增，舊紀錄中的舊檔名不改
  - lint (g)：沒有壞連結
- RS1 新增 concepts/individual-recognition.md（個體辨識），內容取自 p.4、p.7；RS2、RS3 暫不建
  - 和 town、互惠、論文頁互相連結；術語表新增個體辨識、臉孔失認症
  - 依使用者指示，「原文用……描述」的兩個片段改成英文雙引號；lint 確認 "recognize a previous interactant"、"distinguish between different individuals" 都在 p.4 逐字比對成功
- lint --fix：通過（ERROR 0、WARN 0），index.md 自動補上新頁
- 第三輪 AI 審查已開始（全新子代理人，審查 10 頁）

## [2026-11-16] review | Axelrod1981 第三輪 AI 審查
- 全新子代理人審查 10 頁（含個體辨識頁、改名後的 town 頁）
- 結果：ERROR 1、WARN 8、SUGGEST 2
- ERROR：互惠頁白話摘要「互惠只出現在一個詞組裡」不符原文——p.3 另有 "stable reciprocity"、"invoke reciprocity"（已回 cache 核對屬實）。這句是上一輪處理 R4 時新寫的
- 另一個 WARN 和使用者的決定衝突：審查者建議把個體辨識頁的英文片段改成中文轉述，但這是使用者指定的寫法，也符合 AGENTS.md §4.5（句中片段加出處，由 lint 逐字比對）
- 等使用者決定

## [2026-11-16] decision | 第三輪審查 T1–T9 的修正與核對
- 使用者決定：T1–T3、T5–T9 照建議修改；T4 不改（英文片段是使用者指定，符合 §4.5，lint 已逐字比對）；TS1 報復、TS2 利他等 Berg1995 之後再決定
  - T9 依使用者指示拆成兩句：「沿用第一輪的循環賽」獨立一句並標〔推論〕
  - T3 術語表新增「互惠合作 (reciprocal cooperation)」，和 cooperation based on reciprocity 分開收錄，兩者的關係標〔推論〕
- lint --fix：通過；術語表 has_inference 自動改成 true
- 發現 lint 漏洞：index.md 的摘要不會隨頁面 summary 同步。town 頁在 index 上的摘要還是 E1 修正前、含設計推論的舊版；已用腳本同步 4 行（互惠、以牙還牙、電腦競賽、town）
- 新子代理人只核對這 8 處：通過 3 項（T6、T7、T9），有問題 5 項（都是 WARN）
  - 第 3 項的說法已回 cache 核對屬實：reciprocal cooperation 在 p.6 也出現過
- .gitignore 加入 __pycache__/ 和 *.pyc：用 Python import lint 驗證時產生了 __pycache__/lint.cpython-313.pyc，不 commit
- 頁面暫不改 stable，等使用者決定 5 項 WARN

## [2026-11-16] decision | 核對 WARN 的修正、lint (i) 補強、頁面改為 stable
- 使用者決定：5 處 WARN 照改，改完只跑 lint，不再開子代理人核對
  - 互惠頁摘要：刪掉「這類」，改成「稱以牙還牙…是一種以互惠為基礎的合作策略」[p.5]
  - 個體辨識頁細菌那句：改成「似乎都還沒有已知例子」[p.4]
  - 術語表「互惠合作」：改成「原文 p.6–7 的用語」，出處依 §4.1 寫成 [Axelrod1981, p.6–7]
  - 個體辨識頁摘要：照原文名詞結構改成「獎勵某一個體的合作 (cooperation)、懲罰另一個體的背叛」；「背叛 (Defect)」的英文移到頁面上第一次當動作用的「背叛的個體」
  - 論文頁：改成「合作要能演化，其中兩個條件是：背叛者必須逃不過有效的報復…」[p.7]，和互惠頁一致
- lint (i) 補強：index.md 每一行的標題、摘要必須和頁面 frontmatter 一致；--fix 自動同步。AGENTS.md §10.1 已更新
  - scratchpad 副本測試：把以牙還牙那行的摘要改成舊文字 → 不加 --fix 報 ERROR；加 --fix 自動同步；再跑通過
- Axelrod1981 的 10 頁全部從 draft 改成 stable：論文、囚犯困境、電腦競賽、以牙還牙、演化穩定策略、互惠、再相遇機率、個體辨識、town 頁、術語表
  - 依據：三輪 AI 審查（第一輪 ERROR 3／WARN 17；第二輪 ERROR 0／WARN 15；第三輪 ERROR 1／WARN 8）的問題都已處理或由使用者決定不改，最後的 8 處修改經子代理人核對，剩下的 5 處 WARN 也已依使用者指示修改
- lint --fix：通過（ERROR 0、WARN 0）
- 校準狀態：Axelrod1981 是兩篇校準論文的第一篇；校準要等 Berg1995 完成、使用者確認後才算完成

## [2026-11-16] decision | Berg1995 ingest 計畫
- D1：範式頁用 paradigms/trust-game.md，標題「信任賽局 (Trust Game)」，頁內註明 Berg1995 原文稱為投資賽局；「後來通稱信任賽局」標〔推論〕
- D2（依 §8 停下來詢問的可能核心矛盾）：Axelrod1981 單次賽局預測不合作、合作要能演化需要背叛者不能匿名；Berg1995 單次、雙盲下 32 人中 30 人送錢，社會歷史組 28 人中 13 人回報多於收到的
  - 使用者決定折衷：兩篇的理論預測一致（單次賽局都預測不合作），差別在 Berg 的人類行為偏離理論；兩篇的「匿名」意思不同（演化上躲進人群 vs 實驗雙盲）
  - contradictions.md 記成「適用條件差異」，並寫明 Berg 只有部分人回報（28 人中 13 人）
  - town 頁受影響的〔推論〕標〔待檢視〕、改 needs-review，使用者之後決定怎麼改寫
- D3：「報復」「利他」兩頁都建
- D4：新增一頁 Berg1995 的 town 頁
- D5：社會歷史獨立成頁
- 收尾方式：AI 審查只做一輪；措辭或補英文的 WARN 照改後跑 lint 即可；只有 ERROR 才針對那幾處再核對
- 附錄 B 和 Table I 日期不一致（/92、/93）：兩種都照原文寫，用〔推論〕註明，不替原文決定

## [2026-11-16] extract | Berg1995 補轉錄 p.18、p.20 的部分段落
- 使用者要求先轉錄 p.18–21，讓 p.18 的結論和 p.20 的日期能被 lint 比對
- 考量上次全文轉錄被內容政策中斷，只轉錄需要比對的部分：p.18 結論段（約 7 行）、p.20 的報告表和附錄 B 數據表；p.18–19 實驗說明全文、p.20–21 參考文獻維持概述
- 附錄 B 驗算：由數據表算出無歷史組 32 對、平均送出 5.16、平均回報 4.66；社會歷史組 28 對、5.36、6.46，和 p.9、p.12 一致；各場次對數 10/10/12、10/9/9 和 Table I 一致；依送出金額彙整也和 p.20 報告表一致
- cache 檔頭改成 `# untranscribed: 19,21`、`# partial: 18,20`
- lint.py：部分轉錄的頁，引文找不到時發 WARN（可能在未轉錄段落），不報 ERROR；scratchpad 測試 4 種情況都符合預期
- AGENTS.md §3、§9.1 已更新

## [2026-11-16] ingest | Berg1995
- 新增 8 頁：papers/berg1995.md、paradigms/trust-game.md、concepts/trust.md、concepts/social-history.md、concepts/retaliation.md、concepts/altruism.md、town/social-history-shapes-trust.md、syntheses/contradictions.md
- 更新：concepts/reciprocity.md（新增 Berg1995 一節，〔待補〕換成兩條〔推論〕）、glossary.md（新增 22 個術語）、town/reciprocity-requires-non-anonymity.md
- 數字更正：計畫 D2 和使用者的折衷指示寫「社會歷史組 28 人中 13 人」，原文 p.14 的分母是收到超過 $1 的 24 人；頁面一律照原文寫「24 人中 13 人」（無歷史組照 p.10 寫「28 人中 11 人」）
- D2 執行：contradictions.md 記一筆「適用條件差異」；town 頁「設計點子」第一點標〔待檢視〕並註明被 Berg1995 挑戰的理由和出處，頁面改為 needs-review。其他設計點子不依賴「互惠一定需要非匿名」，沒有標
- 日期不一致：論文頁並列 Table I 的 /93 [p.9] 和附錄 B 的 /92 [p.20]，用〔推論〕註明
- p.18 的結論句 "Taken together, these results suggest that both positive and negative forms of reciprocity exist…" 放進論文頁關鍵引文，lint 在部分轉錄的 p.18 比對成功

## [2026-11-16] lint | Berg1995 ingest 後
- 第一次 --fix：ERROR 1，自動修正 14 項
  - ERROR：論文頁把兩個問句寫成「…？…？」，lint 以問號切句，前半句沒有出處 → 改成一句話
  - 矛盾總表的表格「處理狀態」欄寫了「標〔待檢視〕」來描述 town 頁，lint 誤以為這頁本身含〔待檢視〕而改成 needs-review → 改成不加括號的文字，status 改回 draft
  - 自動修正：利他頁、報復頁的 has_inference 改成 true；town 頁改成 needs-review、sources 補 Berg1995；index 補上 8 頁並同步互惠頁的摘要
- 修正後：通過（ERROR 0、WARN 0）；〔待檢視〕只剩 town 頁那一處
- AI 審查（只做一輪）已開始：全新子代理人審查 11 頁

## [2026-11-16] schema | 描述標記本身時不加括號
- 起因：矛盾總表用「標〔待檢視〕」描述 town 頁，lint 誤以為這頁本身含待檢視內容
- 使用者決定：寫進 AGENTS.md。新增 §4.6「描述標記本身時不加括號」；原 §4.6「免標出處的部分」改為 §4.7，§10.1 的引用同步更新

## [2026-11-16] review | Berg1995 AI 審查（只做一輪）
- 全新子代理人審查 11 頁，提供 Berg1995 全部轉錄文字和 Axelrod1981 p.2–8
- 結果：ERROR 1、WARN 18、SUGGEST 8
- 依使用者約定處理：
  - WARN 18 個（措辭、補英文、術語一致）直接修改
  - SUGGEST 中 6 個屬於頁碼精確度和措辭（p.13–14、p.17–18 範圍、刪掉評價性的「只」、補 p.12 出處、矛盾總表補無歷史組 11/28 和報復頁連結、信任頁 primitive 譯法統一），性質同 WARN，一併修改
  - SUGGEST 中 2 個建議新增頁面（雙盲 double-blind、獨裁者賽局 Dictator Game），等使用者決定
  - 重要更正：原文 p.10–11 比較的是「送出金額」和「回報比例」，不是回報金額；論文頁、信任賽局頁、社會歷史頁、互惠頁、town 頁的 Spearman 相關都改寫並改標 p.10–11
  - 術語表新增「納許均衡 (Nash equilibrium)」[p.2]；優勢策略的定義改成只寫 p.4 有的內容
- ERROR：利他頁的 summary 和白話摘要說「Axelrod1981 把利他和互惠分開」，內文沒有出處支持
  - 修正：內文新增兩句有出處的句子（親屬理論和互惠理論是兩種延伸 [Axelrod1981, p.2]；再相遇機率夠高時，以互惠為基礎的合作在沒有親緣的族群中也能穩定 [Axelrod1981, p.6]），摘要改成依這兩句改寫
  - 依約定，只針對這一處請新的子代理人核對
- 共修改 10 頁 45 處；lint --fix：通過（ERROR 0），index 自動同步 2 行摘要

## [2026-11-16] review | 利他頁 ERROR 修正的核對
- 全新子代理人只核對利他頁的修正：新增的兩句有出處的句子通過（p.2、p.6）
- WARN：摘要中「靠親緣」寫成必要條件、「只要…就能穩定」寫成單獨足夠的條件，都比內文強 → 依約定直接修改；另依建議把「相對地」改成「最後」，貼近原文 Finally 的先後語氣
- lint --fix：通過（ERROR 0），index 自動同步利他頁摘要

## [2026-11-16] decision | Berg1995 頁面改為 stable
- 8 頁 draft → stable：論文、信任賽局、信任、社會歷史、報復、利他、town「社會歷史會影響信任」、矛盾總表
- town「互惠需要無法匿名」依使用者指示維持 needs-review（設計點子第一點待檢視，等使用者改寫）
- 目前全 wiki：stable 17 頁、needs-review 1 頁
- 審查建議新增的雙盲、獨裁者賽局兩頁：等使用者決定
- 校準狀態：Axelrod1981、Berg1995 兩篇校準論文都已完成 ingest；「校準完成」要等使用者確認後才記錄

## [2026-11-16] decision | 利他頁摘要改用原文的區分
- 使用者指出：補上的 p.2、p.6 兩句區分的是「親屬理論 vs 互惠理論」，不是「利他 vs 互惠」
- 使用者決定：摘要照原文說法改成「Axelrod1981 把親屬理論和互惠理論分開解釋合作」；如要保留利他的說法，必須標〔推論〕並說明對應關係
- 處理：summary 和白話摘要改成原文說法。依 §1，白話摘要和 summary 不能有〔推論〕，所以「親屬理論對應到利他」的說明放在「爭議與未解問題」段並標〔推論〕，註明原文沒有直接把利他和互惠當成對比
- 雙盲、獨裁者賽局兩頁：使用者決定之後再建
- lint --fix：通過（ERROR 0），index 自動同步利他頁摘要；利他頁維持 stable

## [2026-11-16] decision | 校準完成
- 使用者確認：Axelrod1981、Berg1995 兩篇校準論文完成，格式和語氣校準完成
- 後續論文（Park2023 → Xie2024 → Horton2026）的做法，使用者指定，並寫進 AGENTS.md §9.2：
  - 一次只處理一篇，每篇結束都停下來，不要連續做下一篇
  - 每篇仍跑一輪 AI 審查；措辭和補英文的 WARN 直接改
  - commit 前一定先給使用者：審查清單摘要（特別是所有 ERROR 和改動到的數字）＋ git status，使用者確認後才 commit
  - 遇到核心矛盾、要新增或改名頁面、要修改 town 頁時，停下來問使用者

## [2026-11-17] decision | Park2023 ingest 計畫
- 提出計畫：新增 7 頁、更新個體辨識頁和術語表；囚犯困境、信任賽局、Axelrod 競賽的 LLM 待補段落不動（Park2023 沒有賽局資料）
- 使用者決定：
  1. 架構拆成 4 個概念頁：generative-agent、memory-stream、reflection、planning
  2. 不建 Smallville 範式頁（範式模板的報酬結構、人類基準數據不適用），設定寫進論文頁和湧現行為頁
  3. 同意新增 town/instruction-tuning-makes-agents-too-cooperative.md；既有的 town/reciprocity-requires-non-anonymity.md 不動
  4. 受控評估的 TrueSkill 數字只放論文頁，概念頁只寫「拿掉元件可信度下降」

## [2026-11-17] ingest | Park2023
- 原文：cache/text/Park2023.txt（pypdf，22 頁）；p.18–21 前段為參考文獻未使用，p.21–22 附錄只引用了 p.21 的「只事先產生高層計畫」
- 新增：papers/park2023.md、concepts/generative-agent.md、concepts/memory-stream.md、concepts/reflection.md、concepts/planning.md、concepts/emergent-social-behavior.md、town/instruction-tuning-makes-agents-too-cooperative.md
- 更新：concepts/individual-recognition.md（〔待補〕換成 Park2023 一節，以及兩條推論）、glossary.md（新增 20 個術語）、index.md
- 矛盾檢查：和 Axelrod1981、Berg1995 沒有核心矛盾，也沒有細節差異
- 原文內部小差異（未寫進 wiki）：p.6 正文說 John 7 點起床，p.7 圖 3 說約 6 點起床
- 論文頁 title 含冒號，frontmatter 改加雙引號才能通過 YAML 解析
- lint --fix：通過（ERROR 0、WARN 0），index 自動補上 7 頁

## [2026-11-17] review | Park2023 AI 審查（一輪）
- 全新子代理人審查 7 個新頁面、個體辨識頁的 Park2023 部分、術語表 20 列；只提供頁面和 Park2023 原文（以及 Axelrod1981 p.4）
- 結果：ERROR 2、WARN 29、SUGGEST 8；所有數字和頁碼核對正確，沒有改動任何數字
- ERROR 1：湧現行為頁的白話摘要提到「Sam 參選」，內文沒寫 → 內文補一句 [Park2023, p.15]
- ERROR 2：town 頁 summary 含推論（借錢和背叛遊戲的風險）→ summary 和白話摘要改寫，只摘要研究依據
- WARN 依約定直接修改：補英文、措辭降級（「過於客氣」改「更客氣」、「比完全捏造常見」改「仍會加油添醋」）、論文頁拆開消融序列和群眾外包條件、論文頁和生成式代理人頁的白話摘要依內文改寫、術語「消融實驗」統一成「消融」、術語表兩列補頁碼
- SUGGEST：術語表新增 11 個術語（能動性、種子記憶、上下文視窗、反思樹、群眾外包工作者、受控評估、端到端評估、關係形成、代理人之間的協調、提示攻擊、記憶攻擊）；個體辨識頁把混在推論句裡的 Axelrod1981 事實拆成獨立的出處句
- SUGGEST 中 6 個新增頁面建議（檢索、可信度、幻覺、指令微調、評估方法、倫理風險）：等使用者決定

## [2026-11-17] review | ERROR 修正的核對
- 全新子代理人只核對兩處 ERROR：兩處都已修正
- 另提 WARN 2 個，依約定直接修改：湧現行為頁的白話摘要改成「一開始只有發起者知道」，並在內文補「初始化時寫進記憶」；town 頁研究依據補一句「彼此過度合作」[Park2023, p.17]，白話摘要改回原文的保留語氣
- lint --fix：通過（ERROR 0、WARN 0）

## [2026-11-17] decision | Park2023 審查建議的 6 頁
- 使用者決定：建立審查建議的 6 頁

## [2026-11-17] ingest | Park2023 補充 6 頁
- 新增：concepts/retrieval.md、believability.md、hallucination.md、instruction-tuning.md、evaluation-and-ablation.md、generative-agent-ethics.md
- 更新：論文頁、記憶流、生成式代理人、湧現行為、town 指令微調頁的相關頁面連結；術語表 14 列的詳細頁面改指向新頁，新增 5 個術語（TrueSkill 評分、擬人化、價值對齊、深度偽造、過度依賴）
- lint 第一次未通過：評估頁一句例題中間的驚嘆號被切成兩句，第一句沒有出處 → 改寫後通過

## [2026-11-17] review | 補充 6 頁 AI 審查（一輪）
- 全新子代理人審查 6 頁和術語表新增 5 列：ERROR 6、WARN 19、SUGGEST 8；所有數字和頁碼正確，沒有改動任何數字
- 6 個 ERROR 都是白話摘要或 summary 寫了內文沒有的內容：檢索頁（規劃靠檢索）、可信度頁（summary 含推論）、幻覺頁（一般定義）、指令微調頁（外部定義）、評估頁（例題不在內文）、倫理頁（過度依賴的定義、「研究者」應為「開發者」）→ 都已修正，必要時在內文補有出處的句子
- WARN 直接修改：補英文、措辭降級（「只是」「歸因」「是保守的估計」）、術語表價值對齊和擬人化的定義、提示攻擊的詳細頁面改指論文頁
- SUGGEST 採用：可信度頁的群眾外包句移到「怎麼衡量」；評估頁補「每類只看到一題隨機題目」；倫理頁偏誤小節註明出自限制一節
- SUGGEST 未採用：評估頁寫出 TrueSkill 數字（使用者先前決定數字只放論文頁）
- 另建議新增 3 頁（反應與對話、穩健性、town 可查核的交易紀錄）：等使用者決定
- 全新子代理人核對 6 處 ERROR：全部通過；另 1 個 WARN（幻覺頁 summary 的「較常見」）和 1 個措辭建議已直接修改
- lint --fix：通過（ERROR 0、WARN 0）

## [2026-11-18] decision | 審查建議的 3 頁
- 使用者決定：建立反應與對話、代理人的穩健性、town 可查核的交易紀錄三頁

## [2026-11-18] ingest | Park2023 再補 3 頁
- 新增：concepts/reacting-and-dialogue.md、concepts/agent-robustness.md、town/auditable-transaction-log.md
- 「穩健性」和 Axelrod1981 的策略穩健性同名不同義：本頁取名「代理人的穩健性 (robustness of generative agents)」，術語表分開收錄
- 更新：論文頁、規劃、檢索、幻覺頁的相關頁面連結；術語表新增 4 個術語（反應、內心聲音、代理人的穩健性、稽核紀錄），提示攻擊、記憶攻擊改指穩健性頁
- lint --fix：通過，sources 自動補上 Axelrod1981

## [2026-11-18] review | 再補 3 頁 AI 審查（一輪）
- 全新子代理人審查 3 頁和術語表 4 列：ERROR 2、WARN 14、SUGGEST 1；沒有改動任何數字
- ERROR 1：反應與對話頁的白話摘要寫「根據前面的對話內容」，內文沒寫 → 內文補 [Park2023, p.12]
- ERROR 2：穩健性頁的白話摘要替提示攻擊加了原文沒有的定義 → 改成只列名稱
- WARN 直接修改：措辭（「可能」改「很可能」、「會加油添醋」改「有時會」）、稽核紀錄註明是作者針對濫用風險的建議（不是針對穩健性）、內心聲音改標為 wiki 自己的連結並刪掉關係較弱的一點、town 頁補 Berg1995 社會歷史的出處句、補英文
- SUGGEST 未採用：新增「過度合作」概念頁（內容已在指令微調頁和 town 頁）
- 全新子代理人核對 2 處 ERROR：通過；另 1 個 WARN（摘要「沒有給定義」內文未寫）和 2 個措辭小問題已直接修改
- lint --fix：通過（ERROR 0、WARN 0）

## [2026-11-18] decision | 「過度合作」頁
- 使用者同意不另建「過度合作」概念頁，內容維持在指令微調頁和 town 指令微調頁

## [2026-11-18] decision | Xie2024 ingest 計畫
- 提出計畫：新增 6 頁（論文、行為一致性、信任的行為因素、代理人信任的特性、獨裁者賽局、重複信任賽局），更新信任賽局、信任、可信度、互惠、利他、指令微調、矛盾總表、術語表
- 可能的核心矛盾：Park2023 說 gpt3.5-turbo 代理人過度合作，Xie2024 說 GPT-3.5-turbo-0613 是信任最低的模型
- 使用者決定：
  1. 6 頁照建議建
  2. 上述矛盾歸類為適用條件差異（情境、衡量對象、模型版本不同），不是核心矛盾，並列寫進矛盾總表
  3. 修改 town/instruction-tuning-makes-agents-too-cooperative.md：〔待補〕換成 Xie2024 資料，新增一條設計推論（降低信任比提高容易）
  4. town/reciprocity-requires-non-anonymity.md 不動；town/social-history-shapes-trust.md 的〔待補〕保留（Xie2024 沒有測社會歷史）

## [2026-11-18] contradiction | 人類在信任賽局的平均送出
- Berg1995 無歷史組 $5.16 [p.10]；Xie2024 圖 2 人類平均 $5.97 [p.5]；Xie2024 引用 Cox (2004) 為 $6.0 [p.6]
- 細節差異，並列於矛盾總表、信任賽局頁、行為一致性頁

## [2026-11-18] ingest | Xie2024
- 原文：cache/text/Xie2024.txt（pypdf，56 頁）；讀了正文 p.1–10 和附錄 A–F（p.19–22）；附錄 G–I（完整重複賽局結果、提示、BDI 範例）未引用
- 新增：papers/xie2024.md、concepts/behavioral-alignment.md、concepts/trust-behavioral-factors.md、concepts/agent-trust-properties.md、paradigms/dictator-game.md、paradigms/repeated-trust-game.md
- 更新：信任賽局（LLM 待補換成 Xie2024 結果）、信任（待補換成 Xie2024 一節）、可信度（Xie2024 的待補換掉，Horton2026 的保留）、互惠、利他、指令微調（待補換成 Xie2024 資料和推論）、town 指令微調頁、矛盾總表（新增 2 列）、術語表（新增 18 個術語；獨裁者賽局改指新頁）
- 論文標題含問號和括號，frontmatter 加雙引號
- lint --fix：通過（ERROR 0），sources 自動補 4 處、index 自動補 6 頁

## [2026-11-18] review | Xie2024 AI 審查（一輪）
- 全新子代理人審查 6 個新頁面、8 個更新頁面的 Xie2024 部分、術語表 Xie2024 各列：ERROR 7、WARN 16、SUGGEST 2
- 所有主要數字和頁碼正確（$5.97、$6.0/$3.6、$6.9/$6.3、72%/21%、54%/29%、16 組比例、$0.55/−$0.21、$0.40/−$0.84、$1.26、$0.02）；沒有改動任何數字
- ERROR 1–5：「9 種模型」原文正文沒有直接支持（圖 2 有 10 個模型，p.4 寫「GPT-4 以外另有 9 個」），散在 5 頁 → 改成「多種」或「圖 2 比較的模型中」
- ERROR 6：論文頁白話摘要說 GPT-4 在三個行為因素上都和人類最像，內文沒寫 → 主要發現補上預期互惠、風險感知、利社會偏好三句，摘要改成「都和人類相似，整體一致性最高」
- ERROR 7：獨裁者賽局頁 summary 說 Berg1995 用它對照投資賽局，內文沒寫 → 補上 35 分的對照句 [Berg1995, p.16–17] 和 Xie2024 預期互惠句 [p.6]
- WARN 直接修改：補英文（trustor、trustee、t 檢定、human trust、zero-shot）、GPT-3.5 註明重複賽局用的是 GPT-3.5-turbo-0613-16k、10% 門檻頁碼改 p.7–8、重複賽局頁的 Axelrod 推論降級並拆出出處句、town 頁設計推論從「應該能有效」降為「值得測試」、矛盾總表的「沒有報酬」移到條件欄、差額改成 $0.6 到 $0.8、行為一致性頁註明 $5.97 原文未說明來源、合作優勢改引 p.9–10
- 術語表新增 3 個（人類信任、樂透賽局、零樣本）
- SUGGEST 未採用：MAP 信任賽局獨立頁、人類基準數據綜合頁（時間考量，內容已在現有頁面）
- 全新子代理人核對 ERROR 修正：全部通過；另 1 個 WARN（論文頁利社會偏好和重複賽局缺「類似人類」的結論句）已補上 [p.7]、[p.8]
- lint --fix：通過（ERROR 0、WARN 0）

## [2026-11-18] decision | Horton2026 ingest 計畫
- 使用者確認：4 頁照建議（論文頁、矽基人、理論導向的人物設定、AI 模擬的效度）、新增 town 頁（用理論類型設計小鎮代理人）、5 個實驗只寫在論文頁
- 人口特徵式人物設定（Xie2024 vs Horton2026）歸類為適用條件差異，不列核心矛盾

## [2026-11-18] ingest | Horton2026
- 原文：cache/text/Horton2026.txt（arXiv v2，53 頁）；讀了正文 p.1–40；附錄（p.41 以後）未引用
- 新增：papers/horton2026.md、concepts/homo-silicus.md、concepts/theory-grounded-personas.md、concepts/ai-simulation-validity.md、town/theory-grounded-agent-types.md
- 更新：獨裁者賽局（Charness-Rabin 一節）、指令微調（後訓練 p.26、現狀偏誤 p.17–18）、可信度和行為一致性（Horton2026 的待補換掉）、生成式代理人（連到矽基人）、矛盾總表（新增 1 列）、術語表（新增 11 個術語）
- lint --fix：通過（ERROR 0），sources 自動補 3 處、index 自動補 5 頁

## [2026-11-18] review | Horton2026 AI 審查（一輪）
- 全新子代理人審查 5 個新頁面、6 個更新頁面的 Horton2026 部分：ERROR 4、WARN 8、SUGGEST 4
- 所有主要數字、頁碼和直接引文正確（82%、10/10/10 版本、0.37/0.10/0.53、0.094/0.182、15,200、43 個模型、$1.3、三個月、52%）
- ERROR 1：論文頁 summary 的「可以靈活執行的理論」內文沒有 → 主要發現補 p.40 句子
- ERROR 2：論文頁白話摘要只舉「只在乎公平」，內文沒寫三種設定，且 3 個模型的公平型比例是 0 → 內文補三種設定 [p.11; p.13]，摘要改列三種
- ERROR 3：矽基人頁「產生假說」內文沒有 → 補 p.32 句子
- ERROR 4：效度頁 summary 有「黑盒子」，內文沒有 → 新增黑盒子一節 [p.29; p.30]
- WARN 直接修改：人口特徵和刻板印象的說法改回條件句（town 頁、矛盾總表）；矛盾總表把沒給設定的結果標為背景；嗜好和電視節目的發現改成「Horton2026 引用的研究」；論文頁補核心質性結果句 [p.1; p.40]；p.40 的引文不是完整句子，改成中文改寫；矽基人頁白話摘要改為「稟賦」；town 頁 Berg1995 改成 32 對並引 [Berg1995, p.9]；各頁補英文
- SUGGEST 採用：論文頁利益衝突拆成事實句和推論句；人物設定頁和 town 頁補「3 個模型的公平型比例是 0」[p.14]
- SUGGEST 未採用：現狀偏誤 p.4 和 p.17 的措辭對照、p.41 的適用條件（時間考量）
- 全新子代理人核對 ERROR 修正：全部通過；另 1 個小問題（矛盾總表寫「本文沒有直接測試人口特徵式設定」，但公平感實驗有政治立場設定 [p.7]）已改成「沒有在分配賽局中測試」
- lint --fix：通過（ERROR 0、WARN 0）

## [2026-11-18] decision | 簡報大綱
- 使用者確認：14 頁大綱照提案生成；視覺風格用北大藍加暖色點綴
- town/reciprocity-requires-non-anonymity.md 仍是 needs-review，簡報先不引用（第 7 頁只講兩篇論文的矛盾）

## [2026-11-18] lint | Berg1995 白話摘要用詞
- 生成簡報時發現：論文頁白話摘要寫「還得比收到的多」，內文是「回報多於對方送出的金額」[Berg1995, p.10; p.14]（收到的是送出的三倍，兩者不同）→ 白話摘要和 summary 都改成「回報多於對方送出的金額」

## [2026-11-18] slides | v1（14 頁）
- 大綱經使用者確認後逐頁生成 slides/index.html；另建 slides/graph.html（Loop/Graph 圖）、根目錄 index.html、slides/report.md
- 自我檢查抓到 Berg1995 白話摘要用詞錯誤，回頭修 wiki（見上一筆 lint）
- 全新子代理人逐頁核對：12 頁通過、2 頁退回（第 8 頁出處缺幻覺頁並漏寫另一個種子設定；第 14 頁出處缺矽基人頁），另採用 1 個用詞建議（利他改利社會偏好）
- 修正後全新子代理人覆核第 4、7、8、9、14 頁：全部通過；第 14 頁「每一句話」改成「每個研究主張」
