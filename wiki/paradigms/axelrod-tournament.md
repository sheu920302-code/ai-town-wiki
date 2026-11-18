---
title: Axelrod 電腦競賽 (Axelrod Computer Tournament)
type: paradigm
summary: 讓各方提交的重複囚犯困境策略互相對戰的兩輪電腦競賽；第一輪由以牙還牙拿到最高平均分，第二輪以牙還牙再次獲勝。
sources: [Axelrod1981]
related: [papers/axelrod1981.md, paradigms/prisoners-dilemma.md, concepts/tit-for-tat.md, concepts/continuation-probability.md, town/reciprocity-requires-non-anonymity.md, glossary.md]
tags: [tournament, repeated-games, tit-for-tat, simulation]
status: stable
has_inference: true
created: 2026-11-16
updated: 2026-11-16
---
# Axelrod 電腦競賽 (Axelrod Computer Tournament)

## 白話摘要
Axelrod 邀請各方寫好重複囚犯困境 (Iterated Prisoner's Dilemma) 的策略程式，讓所有程式兩兩對戰，看誰的平均分最高。比賽辦了兩輪，第一輪每場固定 200 步，第二輪每場的長度不固定；兩輪都由以牙還牙 (Tit-for-Tat) 獲勝，它也是第一輪參賽策略中最簡單的一個。

## 規則

### 第一輪
- 由作者之一 (R.A.) 舉辦的囚犯困境 (Prisoner's Dilemma) 電腦競賽 (computer tournament)，目的是看哪種策略能在策略多樣的環境中表現良好 [Axelrod1981, p.5]。
- 參賽策略由經濟學、社會學、政治學和數學領域的賽局理論學者提交 [Axelrod1981, p.5]。
- 14 個參賽策略加上 1 個完全隨機的策略，彼此進行循環賽 (round robin) [Axelrod1981, p.5]。
- 報酬依照圖 1，每場長度是 200 步 [Axelrod1981, p.5]。
- 每對策略比 5 場 [Axelrod1981, p.8]。
- 有些參賽策略相當複雜，例如每一步都把對手的行為建模成馬可夫過程，再用貝氏推論選擇長期最佳的一步 [Axelrod1981, p.5]。
- 結果：平均分最高的是所有參賽策略中最簡單的以牙還牙 [Axelrod1981, p.5]。

### 第二輪
- 第一輪的結果公開後，再徵求第二輪的參賽策略 [Axelrod1981, p.5]。
- 共有來自 6 個國家的 62 個參賽策略 [Axelrod1981, p.5]。
- 參賽者大多是電腦愛好者，也有演化生物學、物理學、電腦科學的教授，以及第一輪的五個學科 [Axelrod1981, p.5]。
- 〔推論〕原文描述第一輪時只列出經濟學、社會學、政治學、數學四個領域，描述第二輪時卻說「第一輪的五個學科」，兩處數字不一致 [Axelrod1981, p.5]。
- 以牙還牙再次由第一輪的優勝者 Anatol Rapoport 提交，並再次獲勝 [Axelrod1981, p.5]。
- 第二輪電腦競賽 (computer tournament) 的每場長度不固定，作者把「每一步不是最後一步」的機率設為 w = .99654；原文對長度的描述是 "an expected probability of 200 moves"，沒有寫明 200 是期望值還是中位數 [Axelrod1981, p.8]。
- 〔推論〕依 w = .99654 計算，期望長度是 1/(1−w) = 1/0.00346 ≈ 289 步；而 0.99654^200 ≈ 0.5，所以 200 步是中位數長度，也就是大約一半的比賽會超過 200 步 [Axelrod1981, p.8]。
- 和第一輪一樣，每對策略比 5 場 [Axelrod1981, p.8]。
- 分析第二輪中的 300 萬次選擇後，作者歸納出以牙還牙穩健的三個特徵：從不先背叛 (Defect)、對方背叛就報復、報復一次之後就原諒 [Axelrod1981, p.5]。

### 生態分析
- 生態分析 (ecological analysis) 以現有的策略種類為前提，觀察它們彼此互動時隨時間的表現 [Axelrod1981, p.5]。
- 做法是假設第二輪的每個策略，依照它在前一輪的成績，按比例提交到一個假想的下一輪，再反覆進行 [Axelrod1981, p.5]。
- 較不成功的策略被淘汰後，以牙還牙仍和原本名列前茅的策略表現良好 [Axelrod1981, p.5]。
- 長期下來，以牙還牙取代了所有其他策略 [Axelrod1981, p.5]。

## 報酬結構
- 兩輪都使用囚犯困境 (Prisoner's Dilemma) 圖 1 的報酬，數值見[囚犯困境](prisoners-dilemma.md)頁 [Axelrod1981, p.5]。

## 人類基準數據
〔待補〕本競賽的參賽者是人類設計的程式策略，不是人類受試者直接對戰；目前沒有人類受試者在同樣規則下的數據。

## LLM 代理人的結果
〔待補〕尚無 LLM 代理人參加同樣規則競賽的資料，等之後 ingest 的 LLM 論文補上。

## 小鎮應用線索
- 〔推論〕可以讓小鎮的 LLM 代理人照第二輪的規則（w = .99654、每對 5 場）互相對戰，再和以牙還牙的成績比較 [Axelrod1981, p.8]。
- 〔推論〕原文只寫明第一輪是循環賽，沒有寫明第二輪的賽制；小鎮重現時可以沿用第一輪的循環賽 [Axelrod1981, p.5]。
- 〔推論〕如果小鎮要重現第二輪，比賽長度要用 w 隨機決定，不要固定成 200 步，否則就變回第一輪的設定 [Axelrod1981, p.5; Axelrod1981, p.8]。
- 〔推論〕生態分析的做法，可以改成「表現好的代理人策略，下一輪被更多代理人採用」，觀察小鎮裡的策略分布怎麼變化 [Axelrod1981, p.5]。

## 相關頁面
- [合作的演化 (The Evolution of Cooperation)](../papers/axelrod1981.md)
- [囚犯困境 (Prisoner's Dilemma)](prisoners-dilemma.md)
- [以牙還牙 (Tit-for-Tat)](../concepts/tit-for-tat.md)
- [再相遇機率 (Continuation Probability)](../concepts/continuation-probability.md)
- [互惠需要無法匿名 (Reciprocity Requires Non-Anonymity)](../town/reciprocity-requires-non-anonymity.md)
- [術語表 (Glossary)](../glossary.md)
