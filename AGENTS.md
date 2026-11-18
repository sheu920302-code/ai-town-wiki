# AGENTS.md — AI 代理人社會行為 LLM Wiki

本檔是維護這個 wiki 的規則本體。任何 AI 代理人在本 repo 工作前，必須先完整讀過本檔。

本 wiki 採用 Karpathy 的 LLM Wiki 構想（https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f）：
`raw/` 存放不可變的原始資料，`wiki/` 由 LLM 維護、可持續累積的知識庫，本檔則是兩者之間的規則（schema）。

- **主題**：AI 代理人模擬人類社會行為，聚焦在信任、合作與背叛
- **用途**：
  1. 製作教學 HTML 簡報
  2. 作為期末專案「AI 北大小鎮」的知識庫

---

## 0. 硬規則（不得違反）

1. **`raw/` 唯讀。** 不得新增、修改、刪除、搬移 `raw/` 內任何檔案。
2. **每個事實性主張都要有出處**，格式為 `[引用鍵, p.N]`。非原文的內容一律標 `〔推論〕`。兩者都沒有的句子視為違規。
3. **白話摘要只能改寫原文**，不得加入原文沒有的推論，也不得出現 `〔推論〕`。
4. **英文原文引用每次以一句為限**，而且必須逐字取自原文。
5. **頁面之間用標準 markdown 相對連結**，例如 `[信任](../concepts/trust.md)`。禁止使用 `[[ ]]`，因為 GitHub Pages 不支援。
6. **「通過」以 `lint.py` 的結果為準**，不得自行宣稱通過。
7. **commit 前一定要先問使用者。**
8. **核心結論互相矛盾時，必須停下來問使用者。** 提問內容和使用者的決定都要寫進 `wiki/log.md`。

---

## 1. 讀者與寫法

| 對象 | 說明 |
|---|---|
| **wiki 本體的主要讀者** | AI 代理人，例如 Claude 和之後小鎮裡的代理人 |
| **白話摘要與簡報的讀者** | 修課同學。他們大多聽過「囚犯困境」這個名詞，但不懂細節，也看不懂統計結果 |

寫法原則：

- **原子化**：一頁一個概念，頁面要短，方便檢索
- **斷言式**：一句一個事實，不用比喻來陳述事實（比喻容易被代理人誤當成事實）
- **保留原始數值**：保留數字、條件、樣本數和適用範圍（模型、情境），不要四捨五入成模糊的說法
- **白話摘要**：每頁開頭附 2–3 句，給人快速瀏覽用。內容不能超出內文

---

## 2. 資料夾結構

```
ai-town-wiki/
├── AGENTS.md            規則本體（本檔）
├── CLAUDE.md            只有一行：@AGENTS.md
├── index.html           GitHub Pages 入口，連到簡報與 wiki（做簡報時建立）
├── extract.py           PDF 抽文字腳本（§9.1）
├── lint.py              程式檢查腳本（§10.1）
├── raw/                 原始論文 PDF（唯讀，已列入 .gitignore）
├── cache/text/          PDF 抽出的文字 <citekey>.txt（已列入 .gitignore，因為有版權）
├── slides/              教學簡報 HTML 和 report.md
└── wiki/
    ├── index.md         所有頁面的目錄
    ├── log.md           依時間記錄的操作紀錄（只能往後新增）
    ├── glossary.md      術語表（第一次 ingest 時建立）
    ├── papers/          論文頁：一篇一頁
    ├── concepts/        概念頁：跨論文整合的概念
    ├── paradigms/       實驗範式頁：賽局規則、報酬結構、基準數據
    ├── syntheses/       綜合頁：跨論文問答，含 contradictions.md
    └── town/            小鎮應用頁：「AI 北大小鎮」的設計點子
```

---

## 3. 引用鍵對照表

| 引用鍵 | raw/ 檔名 | 備註 |
|---|---|---|
| `Axelrod1981` | `Axelrod_Hamilton1981_EvolutionOfCooperation.pdf` | 掃描檔，抽文字時要特別確認 |
| `Berg1995` | `Berg1995_TrustGame.pdf` | PDF 第 1 頁 = 期刊第 122 頁（`page_offset: 121`）。純圖片掃描檔，p.1–17 人工轉錄；p.18 只轉錄結論段、p.20 只轉錄報告表和附錄 B 數據表；**p.19、p.21 未轉錄** |
| `Horton2026` | `Horton_HomoSilicus.pdf` | arXiv v2 版 |
| `Park2023` | `Park2023_GenerativeAgents.pdf` | |
| `Xie2024` | `Xie2024_AgentTrust.pdf` | |

新增論文時：

1. 先在本表加一列，再 ingest
2. 引用鍵格式是「第一作者姓氏＋年份」
3. 同作者同年的論文，加 a、b 區分

---

## 4. 出處與〔推論〕

### 4.1 引用格式

- **格式**：`[引用鍵, p.N]`，例如 `[Berg1995, p.3]`。多個出處寫成 `[Berg1995, p.3; Xie2024, p.7]`
- **頁碼**：一律用 **PDF 頁數**（PDF 檢視器顯示的頁數），不用期刊印刷的頁碼
- **頁碼範圍**：一句話的依據跨越連續的頁面時，可以寫成 `[Axelrod1981, p.4–5]`（用 `–` 或 `-` 都可以）
  - 只能用在**連續的頁面**，起始頁必須小於結束頁
  - 不連續的頁面要分開列，例如 `[Axelrod1981, p.4; Axelrod1981, p.7]`
  - lint (a) 會檢查起訖頁都在 1 和 `pdf_pages` 之間；範圍內有未轉錄的頁面時發出 WARN
- **位置**：引用標在**句尾句號之前**，而且只涵蓋該句。一段多句時，每句都要標，不能只在段尾標一次

### 4.2 〔推論〕

凡是不是原文直接陳述的內容，句首都要加 `〔推論〕`，例如：

- wiki 對矛盾提出的解釋
- 跨論文的綜合判斷
- 小鎮設計點子

推論的依據可以附在句尾，例如：`〔推論〕信任賽局可直接改寫成小鎮的借貸互動 [Berg1995, p.2]。`

### 4.3 〔待檢視〕

既有的〔推論〕被新論文推翻時，**不要直接改寫**：

1. 在該句句首加上 `〔待檢視〕`，例如 `〔待檢視〕〔推論〕……`
2. 句尾註明是被哪篇推翻、推翻的理由和出處
3. 頁面 `status` 設為 `needs-review`
4. 在 log 記錄，等使用者決定

### 4.4 〔待補〕

段落還沒有資料時，例如囚犯困境頁的「LLM 代理人的結果」要等之後的論文：

- 寫一行以 `〔待補〕` 開頭的佔位說明，例如 `〔待補〕尚無 LLM 代理人的資料，預計由 Park2023 補上。`
- 這一行不需要出處，lint 的「無出處句」檢查會跳過它
- lint (k) 會列出所有〔待補〕的位置，提醒使用者
- 補上資料後，刪除這一行

### 4.5 英文原文引用

- 每次只引一句，逐字照抄，下一行附中譯：

  ```markdown
  > "Exact English sentence from the paper." [Berg1995, p.3]
  > 中譯：中文翻譯。
  ```

- 不得修改原句。如果需要省略，請改用中文轉述加上出處，不要用英文引用
- **英文雙引號只用在原文逐字引用**（包括 `"` 和 `“ ”`）：
  - 整句引文用上面的 `>` 格式；句中的引文片段也可以，但同一句一定要有出處
  - lint (b) 會比對所有用英文雙引號括住的英文，不論長短。比對不到、頁碼不對、沒有出處都會報錯
  - 作者的原話用語想保留原樣時，例如 Coleman 說的 "place a trust"，可以加雙引號，但要標出處，讓 lint 比對
  - 術語和篇名**不加雙引號**，寫法見 §5
  - 中文引號「」不受這條規則限制，lint 也不檢查

### 4.6 描述標記本身時不加括號

- 在 wiki 頁面裡，只要文字中出現 `〔推論〕`、`〔待檢視〕`、`〔待補〕`，lint 都會當成真的標記處理，例如把頁面改成 `needs-review`，或把 `has_inference` 改成 `true`
- 所以**描述這些標記本身**時（例如矛盾總表說明另一頁的處理狀態），一律寫成不加括號的「推論」「待檢視」「待補」
  - ✅ `town 頁受影響的推論已標為待檢視`
  - ❌ `town 頁受影響的〔推論〕標〔待檢視〕`
- 只有真正要標記某一句時，才在句首加上帶括號的標記
- 本檔（AGENTS.md）和 `log.md` 不在 lint 檢查範圍內，不受這條限制

### 4.7 免標出處的部分

lint 的「無出處句」檢查會跳過以下內容：

- 標題列
- frontmatter
- `## 白話摘要` 段落（改由 AI 審查 (c) 負責）
- `## 相關頁面` 段落的連結清單
- 程式碼區塊
- 表格標題列
- 以 `〔待補〕` 開頭的佔位行（§4.4）

表格內容中的事實性儲存格仍然要標出處。

---

## 5. 語言與命名

- **內文語言**：繁體中文。術語在**每一頁**第一次出現時，附上英文，例如「信任賽局 (Trust Game)」
- **術語用詞**：一律和 `wiki/glossary.md` 一致。新術語要先加進術語表
- **術語的英文**：寫成「中文 (English)」，**不加雙引號**，例如「信任者 (trustor)」，不要寫成「信任者 ("trustor")」
- **篇名**：用斜體，**不加雙引號**，例如 *Trust, Reciprocity, and Social History*
- **英文大小寫**：
  - **賽局、策略名稱和動作用大寫**：Prisoner's Dilemma、Iterated Prisoner's Dilemma、Tit-for-Tat、ALL D、Cooperate、Defect
  - **一般概念用小寫**：例如 reciprocity、continuation probability、evolutionarily stable strategy、cooperation、cooperation based on reciprocity、computer tournament、round robin、ecological analysis、kinship、fitness、reward for mutual cooperation
  - **頁面標題、「相關頁面」的連結文字、篇名用 Title Case**（實詞首字大寫）：例如 `# 互惠 (Reciprocity)`、`[再相遇機率 (Continuation Probability)](...)`、*The Evolution of Cooperation*。所以同一個概念在標題和連結裡是大寫，在內文裡是小寫
  - 術語表的英文欄照內文的寫法；有代號的保留代號，例如 continuation probability (w)、reward for mutual cooperation (R)
  - 合作要分兩種寫法：囚犯困境的動作寫「合作 (Cooperate)」，名詞「合作這件事」寫「合作 (cooperation)」
- 英文雙引號保留給原文逐字引用（§4.5）
- **頁面標題**：一級標題寫成 `# 中文 (English)`，例如 `# 信任賽局 (Trust Game)`
- **檔名**：英文 kebab-case，只能用小寫英數和 `-`，例如 `concepts/tit-for-tat.md`
  - 論文頁檔名是小寫引用鍵，例如 `papers/berg1995.md`
- **tags**：英文 kebab-case，例如 `trust`、`repeated-games`

---

## 6. Frontmatter

每頁（`index.md`、`log.md` 除外）都必須有 YAML frontmatter。之後要接 RAG，所以欄位要嚴格遵守。

### 6.1 共通欄位（全部必填）

```yaml
---
title: 信任賽局 (Trust Game)       # 與一級標題相同
type: paradigm                     # paper | concept | paradigm | synthesis | town | glossary
summary: 一句話白話摘要（只能改寫原文，不能加推論）
sources: [Berg1995, Xie2024]       # 本頁引用到的所有引用鍵
related: [concepts/trust.md, concepts/reciprocity.md]   # 路徑相對於 wiki/
tags: [trust, experimental-economics]
status: draft                      # draft | stable | needs-review
has_inference: true                # 本頁含〔推論〕就必須是 true
created: 2026-11-15
updated: 2026-11-15
---
```

- **`status` 規則**：
  - 新頁一律從 `draft` 開始
  - lint 和 AI 審查都通過後，改為 `stable`
  - 頁面含〔待檢視〕時，一律設為 `needs-review`（lint 會自動修正）
- **`has_inference`**：由 lint 核對。頁面有〔推論〕就必須是 `true`，否則必須是 `false`，不一致就報錯
- **`sources`**：必須涵蓋內文出現的所有引用鍵

### 6.2 論文頁額外欄位

```yaml
citekey: Berg1995
authors: [Joyce Berg, John Dickhaut, Kevin McCabe]
year: 1995
venue: Games and Economic Behavior
version: published                 # 例如 published、arXiv v2
raw_file: Berg1995_TrustGame.pdf
pdf_pages: 21                      # PDF 總頁數，lint (a) 會用到
page_offset: 121                   # 期刊頁碼 = PDF 頁數 + page_offset；沒有就填 0
```

### 6.3 小鎮頁額外欄位

```yaml
town_status: idea                  # idea | adopted | rejected
```

---

## 7. 頁面內文模板

每頁都依這個順序寫：一級標題 → `## 白話摘要` → 各類型專屬段落 → `## 相關頁面`。

### 7.1 論文頁 `papers/`
```
# 中文標題 (English Title)
## 白話摘要
## 研究問題
## 方法            （受試者或模型、樣本數、實驗設計）
## 主要發現        （保留原始數值）
## 限制            （作者自述的限制要標出處；wiki 自己看出的限制要標〔推論〕）
## 關鍵引文        （1–3 則，每則一句）
## 相關頁面
```

### 7.2 概念頁 `concepts/`
```
# 概念 (Concept)
## 白話摘要
## 定義            （如果各論文定義不同，就並列）
## 各論文的觀點
## 爭議與未解問題
## 相關頁面
```

### 7.3 實驗範式頁 `paradigms/`
```
# 範式 (Paradigm)
## 白話摘要
## 規則
## 報酬結構
## 人類基準數據
## LLM 代理人的結果
## 小鎮應用線索    （全部標〔推論〕）
## 相關頁面
```

### 7.4 綜合頁 `syntheses/`
```
# 問題或主題 (English)
## 白話摘要
## 問題
## 證據            （依論文並列，各標出處與適用條件）
## 綜合判斷        （全部標〔推論〕）
## 相關頁面
```

`syntheses/contradictions.md` 是矛盾總表，格式如下：

| 主題 | 主張 A（出處、條件） | 主張 B（出處、條件） | 類型（核心或細節） | 處理狀態 | 相關頁面 |
|---|---|---|---|---|---|

### 7.5 小鎮應用頁 `town/`
```
# 設計點子 (English)
## 白話摘要        （只摘要研究依據，不寫設計推論）
## 研究依據        （有出處）
## 設計點子        （全部標〔推論〕）
## 風險與待驗證
## 相關頁面
```

### 7.6 術語表 `glossary.md`

用表格整理：

| 中文 | English | 一句定義 | 出處 | 詳細頁面 |
|---|---|---|---|---|

---

## 8. 論文矛盾處理

1. **一律並陳，不裁決。** 在相關頁面並列兩方說法，各自標出處和適用條件（模型、樣本、情境）
2. **集中記錄。** 同時寫進 `syntheses/contradictions.md`
3. **wiki 可以提出解釋**，但必須標〔推論〕
4. **矛盾分兩種：**
   - **核心矛盾**：主要結論的方向不同，例如「LLM 的信任行為和人類一致」對上「不一致」
     → **停下來問使用者**，把問題和使用者的決定寫進 log（類型 `decision`）
   - **細節差異**：數字、定義、參數不同
     → 直接並列，記在 log（類型 `contradiction`），不中斷
5. **舊推論被推翻** → 依 §4.3 標〔待檢視〕，記在 log，等使用者決定

---

## 9. 工作流程

### 9.1 PDF 抽文字（ingest 前先做）

1. 執行 `python extract.py`，把每篇 PDF 抽成 `cache/text/<citekey>.txt`
   - 引用鍵和檔名的對照，直接讀取 §3 的表格
   - 每頁開頭用 `=== p.N ===` 分隔，N 是 PDF 頁數
   - 檔頭記錄 PDF 的 sha256；只要 PDF 不變，就不重抽
   - 每頁少於 50 個非空白字元時，視為「沒抽到文字」
2. 抽完逐篇檢查每頁是否真的有文字。**`Axelrod1981` 是掃描檔，要特別確認**
3. 如果抽不到文字：
   - **先回報使用者，不要自行安裝 OCR（例如 Tesseract）**
   - 經使用者同意後，可以改成直接讀 PDF 頁面圖片，人工轉錄
   - 轉錄的檔案第一行標註 `# source: vision-transcribed`。lint (b) 比對這類檔案時，應在報告中註明比對可信度較低
   - 沒有轉錄的頁面列在檔頭 `# untranscribed: 19,21`，頁內只放內容概述，不放原文
   - 只轉錄部分段落的頁面列在檔頭 `# partial: 18,20`。lint 比對時，引文在已轉錄段落找到就通過；找不到則發 WARN（可能在未轉錄段落），不報 ERROR
4. **Berg1995 p.18–21**：2026-11-15 全文轉錄時被內容政策中斷（很可能是連續逐字輸出大量原文）
   - 2026-11-16 依使用者要求，只補轉錄 ingest 需要比對的部分：p.18 的結論段、p.20 的報告表和附錄 B 數據表
   - 附錄 B 的轉錄已用原文的平均值驗算：兩組的對數、平均送出、平均回報，以及各場次對數，都和 p.9、p.12 一致
   - p.18–19 的實驗說明全文、p.20–21 的參考文獻**不轉錄**；引用這些部分時 lint 會發 WARN，必須對照 PDF 人工核對

### 9.2 Ingest（一次一篇）

**順序**：`Axelrod1981 → Berg1995 → Park2023 → Xie2024 → Horton2026`。之後新增的論文附加在最後面。

**校準階段**：前兩篇（Axelrod1981、Berg1995）是格式和語氣的校準期。

- 讀完後先提出計畫，列出要新增或更新的頁面和重點摘要
- **等使用者確認後才寫入**
- 使用者確認校準完成後，在 log 記一筆 `decision | 校準完成`（2026-11-16 已記錄）
- 是否已經校準，以 log 是否有這筆紀錄為準

**校準完成後的做法**（2026-11-16 使用者指定）：

- **一次只處理一篇**，每篇結束都停下來，不要連續做下一篇
- 每篇仍跑**一輪** AI 審查（§10.2）；措辭和補英文的 WARN 直接改，跑 lint 即可；只有 ERROR 才針對那幾處再請新的子代理人核對
- **commit 前一定先給使用者**：審查清單摘要（特別是所有 ERROR 和改動到的數字）＋ `git status`，使用者確認後才 commit
- 遇到以下情況要**停下來問使用者**：核心矛盾（§8）、新增或改名頁面、修改 town 頁

**每篇的步驟：**

1. 確認 `cache/text/<citekey>.txt` 存在而且有內容
2. 完整讀過原文
3. （校準階段）提出計畫，等使用者確認
4. 建立論文頁 `papers/<citekey>.md`
5. 新增或更新相關的 `concepts/`、`paradigms/`、`syntheses/`、`town/`，以及 `glossary.md`
6. 檢查是否和既有內容矛盾，依 §8 處理
7. 更新 `wiki/index.md`，在 `wiki/log.md` 新增紀錄
8. 執行 lint（§10）：機械性問題自動修，內容問題回報
9. 用子代理人做 AI 審查（§10.2）
10. 回報結果：審查清單摘要（所有 ERROR、改動到的數字）＋ `git status`，**使用者確認後才 commit**

### 9.3 查詢

- 回答 wiki 相關問題時，先讀 `wiki/index.md` 找相關頁面，再深入閱讀
- 回答同樣要標出處
- 有價值的回答可以存成 `syntheses/` 頁，但**存之前先問使用者**。存檔後要更新 index 和 log

---

## 10. Lint

lint 發現問題時：

- **機械性問題**自動修，例如連結、index、`status`、`has_inference`、格式
- **內容問題**只回報，不自行改寫
- 結果都記在 log

### 10.1 程式檢查：`lint.py`

「通過」以腳本的結束狀態和輸出為準。

- **執行方式**：ingest 後跑 `python lint.py --fix`；不加 `--fix` 則只回報
- **結果判定**：結束代碼 0 = 通過。WARN 和 INFO 不影響通過
- **依賴套件**：`pypdf`、`pyyaml`。本機請用 `C:\ProgramData\anaconda3\python.exe`，Windows 的 `python` 指令只是 Microsoft Store 的捷徑
- **`--fix` 只修這些**：
  - `has_inference`
  - `status`（〔待檢視〕→ `needs-review`）
  - `sources` 缺少的引用鍵
  - `index.md` 缺漏的頁面，以及標題、摘要和頁面不一致的行（自動同步成頁面 frontmatter 的內容）
  - 能唯一對應到頁面的 `[[ ]]`
- **其他問題一律只回報**，交給人或 AI 修正內容

| 代號 | 檢查內容 |
|---|---|
| (a) | 引用鍵存在於 §3 對照表，頁碼介於 1 和該論文的 `pdf_pages` 之間；頁碼範圍（§4.1）的起始頁必須小於結束頁，起訖頁都要合法；引用到未轉錄的頁面（例如 Berg1995 p.18–21）時發出 WARN，提醒人工核對 |
| (b) | 英文引文逐字出現在 `cache/text/` 原文中，而且只有一句。比對前兩邊都先正規化：合併連續空白和換行、去除行尾的斷行連字號（`-\n`）、統一引號。**內文裡用雙引號括起來的英文片段**也要逐字比對，出處取同一句的引用；片段不檢查「只能一句」，沒有出處就報錯 |
| (d) | frontmatter 必填欄位齊全，格式正確；`has_inference` 和頁面是否含〔推論〕一致；`sources` 涵蓋內文所有引用鍵 |
| (e) | 一級標題符合 `中文 (English)`，和 `title` 一致；檔名是英文 kebab-case |
| (g) | 沒有失效的相對連結，也沒有 `[[ ]]` |
| (h) | 沒有孤兒頁（沒有任何頁面連過去的頁）。`index.md` 的連結不算 |
| (i) | `wiki/index.md` 列出所有頁面，而且每一行的標題和摘要都和該頁 frontmatter 的 `title`、`summary` 一致 |
| (k) | 列出所有〔待檢視〕，並確認所在頁面的 `status` 是 `needs-review`；也列出所有〔待補〕的位置 |
| — | 句子既沒有出處、也沒有〔推論〕（豁免範圍見 §4.7） |

### 10.2 AI 審查：子代理人

- **一律開全新的子代理人**，不用 fork，也不繼承目前對話
- **只給它**：要審查的頁面，以及對應的 `cache/text/` 原文頁段。(f) 另外附上 `glossary.md`
- **不得由寫入者審查自己剛寫的內容**

| 代號 | 檢查內容 |
|---|---|
| (c) | 白話摘要和 `summary` 忠於內文，沒有內文以外的主張，也沒有〔推論〕 |
| (f) | 術語第一次出現附英文，而且用詞和 `glossary.md` 一致 |
| (j) | 內文提到、但還沒有頁面的概念，列為「建議新增」 |
| (l) | `contradictions.md` 和各頁的並陳內容一致 |

---

## 11. 簡報產出：`slides/`

- **規格**：
  - 10–15 頁，大約 10 分鐘
  - 單一 HTML 檔，**不用 reveal.js 或其他框架**
  - 用鍵盤翻頁（← → 鍵和空白鍵）
  - 能直接放上 GitHub Pages
- **內容來源**：只能取自 `wiki/`，不能直接從 `raw/` 新增主張
- **受眾**：同學看不懂統計結果，所以
  - 每個主題從生活例子講起
  - **不放迴歸表**，數字轉成白話說法
- **出處**：每頁角落顯示對應的 wiki 頁面，用相對連結，讀者看得到
- **〔推論〕**：可以寫，但投影片上要有明顯標示，例如徽章
- **入口**：根目錄的 `index.html` 連到簡報和 `wiki/index.md`
  - GitHub Pages 會用 Jekyll 把 `.md` 轉成網頁
- **檢查報告**：每次生成簡報都要寫 `slides/report.md`，記錄：
  - 檢查了哪些項目：頁數、每個主張都對得上 wiki 頁面、〔推論〕都有標示、連結有效、鍵盤翻頁可用
  - 哪幾頁被退回重做、原因、怎麼修正
  - 主張對應 wiki 的檢查，由子代理人執行（規則同 §10.2）

---

## 12. Log 格式：`wiki/log.md`

- 只能往後新增，不改舊紀錄
- 每筆的標題格式固定，方便用 `grep "^## \["` 查詢：

  ```markdown
  ## [YYYY-MM-DD] 類型 | 標題
  - 重點條列
  ```

- **類型**：
  - `init`：初始化
  - `extract`：抽 PDF 文字
  - `ingest`：處理論文
  - `lint`：lint 結果
  - `review`：AI 審查
  - `contradiction`：細節差異
  - `decision`：停下來問使用者的內容和使用者的決定
  - `query`：查詢
  - `slides`：生成簡報
  - `schema`：修改本檔

## 13. Index 格式：`wiki/index.md`

- 依頁面類型分節
- 每頁一行：`- [標題](相對路徑) — summary`
- 每次新增或刪除頁面都要同步更新

---

## 14. Git

- 主分支是 `main`
- 每次 ingest 或 lint 修正後 commit，**commit 前先問使用者**
- commit 訊息格式：
  - `ingest: Berg1995`
  - `lint: fix links`
  - `slides: v1`
  - `schema: 更新 AGENTS.md`
- 不得 commit `raw/` 和 `cache/`
