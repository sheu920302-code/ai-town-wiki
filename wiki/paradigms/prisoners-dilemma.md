---
title: 囚犯困境 (Prisoner's Dilemma)
type: paradigm
summary: 兩人各自選擇合作或背叛；不管對方怎麼選，背叛都比較划算，但兩人都背叛時比兩人都合作還差。
sources: [Axelrod1981]
related: [papers/axelrod1981.md, concepts/tit-for-tat.md, concepts/evolutionarily-stable-strategy.md, concepts/continuation-probability.md, glossary.md, paradigms/axelrod-tournament.md]
tags: [prisoners-dilemma, repeated-games, cooperation, defection]
status: stable
has_inference: true
created: 2026-11-16
updated: 2026-11-16
---
# 囚犯困境 (Prisoner's Dilemma)

## 白話摘要
兩個人各自選擇合作 (Cooperate) 或背叛 (Defect)。不管對方怎麼選，自己背叛都比較划算；但兩人都背叛時，結果比兩人都合作還差。如果兩人之後還可能再碰面，而且能認出對方、記得過去的互動，就變成重複囚犯困境 (Iterated Prisoner's Dilemma)；再碰面的機會夠大時，就沒有一個不管別人怎麼做都最好的策略，以牙還牙 (Tit-for-Tat) 這類策略也能穩定下來。

## 規則

### 單次
- 兩個玩家各自選擇合作或背叛 [Axelrod1981, p.3]。
- 在生物情境中，報酬以適應度 (fitness)，也就是存活與繁殖來計算 [Axelrod1981, p.3]。
- 不管對方怎麼選，背叛的報酬都比合作高；但雙方都背叛時，兩人都比雙方都合作時差 [Axelrod1981, p.3]。
- 兩人確定不會再相遇時，唯一稱得上解答的策略是永遠背叛 (ALL D) [Axelrod1981, p.3]。
- 配對隨機、不重複時，任何可遺傳的策略組合最後都會演化成全體背叛 [Axelrod1981, p.4]。

### 重複
- 如果個體能認出先前的互動對象並記得過去的結果，就變成重複囚犯困境 [Axelrod1981, p.4]。
- 在重複囚犯困境中，策略是一條決策規則，依照至今的互動歷史決定合作或背叛的機率 [Axelrod1981, p.4]。
- 如果雙方的互動次數事先已知，永遠背叛仍是唯一的演化穩定策略 (evolutionarily stable strategy)，因為最後一回合背叛是最佳選擇，往前倒推每一回合也都是 [Axelrod1981, p.4]。
- Axelrod1981 的模型改用機率 w 表示這次互動之後雙方會再相遇的機率，詳見[再相遇機率 (Continuation Probability)](../concepts/continuation-probability.md) [Axelrod1981, p.4]。
- 不論 w 多少，永遠背叛都是演化穩定策略 [Axelrod1981, p.4]。
- w 夠大時，不存在一個不管其他人怎麼做都最好的單一策略 [Axelrod1981, p.4]。
- [兩輪電腦競賽](axelrod-tournament.md)都由[以牙還牙 (Tit-for-Tat)](../concepts/tit-for-tat.md)獲勝；第一輪是平均分最高，第二輪原文寫的是再次獲勝 [Axelrod1981, p.5]。

## 報酬結構

| 代號 | 名稱 | 情況 | 圖 1 數值 |
|---|---|---|---|
| R | 互相合作的報酬 (reward for mutual cooperation) | 雙方都合作 | 3 [Axelrod1981, p.4] |
| T | 背叛的誘惑 (temptation to defect) | 自己背叛、對方合作 | 5 [Axelrod1981, p.4] |
| P | 互相背叛的懲罰 (punishment for mutual defection) | 雙方都背叛 | 1 [Axelrod1981, p.4] |
| S | 傻瓜報酬 (sucker's payoff) | 自己合作、對方背叛 | 0 [Axelrod1981, p.4] |

- 囚犯困境的條件是 T > R > P > S，而且 R > (S+T)/2 [Axelrod1981, p.4]。
- T > R 表示對方合作時背叛比較划算；P > S 表示對方背叛時背叛也比較划算 [Axelrod1981, p.3]。
- R > (S+T)/2 的作用是排除「輪流占對方便宜」比互相合作更好的可能 [Axelrod1981, p.8]。
- 以牙還牙 (Tit-for-Tat) 是演化穩定策略的條件是 w ≥ (T−R)/(T−P) 且 w ≥ (T−R)/(R−S)，原文編號為條件 (1) [Axelrod1981, p.5]。
- 〔推論〕以圖 1 的數值 T=5、R=3、P=1、S=0 代入條件 (1)：w ≥ max((T−R)/(T−P), (T−R)/(R−S)) = max(2/4, 2/3) = max(0.5, 0.667) = 2/3，也就是 w 至少約 0.67 [Axelrod1981, p.4–5]。

## 人類基準數據
〔待補〕Axelrod1981 沒有人類受試者實驗，等之後的論文補上。

## LLM 代理人的結果
〔待補〕尚無 LLM 代理人的資料，等之後 ingest 的 LLM 論文補上。

## 小鎮應用線索
- 〔推論〕小鎮裡「只見一次面」的互動（例如路過的訪客）適合用單次囚犯困境描述，預期背叛較多 [Axelrod1981, p.3]。
- 〔推論〕同系同學、室友這類會重複碰面的關係適合用重複囚犯困境描述，合作 (cooperation) 是否出現取決於 w [Axelrod1981, p.4]。
- 〔推論〕圖 1 的 R=3、T=5、P=1、S=0 可以直接當作小鎮互動的預設報酬表，方便和原文結果比較 [Axelrod1981, p.4]。

## 相關頁面
- [合作的演化 (The Evolution of Cooperation)](../papers/axelrod1981.md)
- [Axelrod 電腦競賽 (Axelrod Computer Tournament)](axelrod-tournament.md)
- [以牙還牙 (Tit-for-Tat)](../concepts/tit-for-tat.md)
- [演化穩定策略 (Evolutionarily Stable Strategy)](../concepts/evolutionarily-stable-strategy.md)
- [再相遇機率 (Continuation Probability)](../concepts/continuation-probability.md)
- [術語表 (Glossary)](../glossary.md)
