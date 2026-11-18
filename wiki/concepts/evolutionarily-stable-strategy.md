---
title: 演化穩定策略 (Evolutionarily Stable Strategy)
type: concept
summary: 一群人都用同一個策略時，少數改用其他策略的突變者無法入侵，這個策略就是演化穩定的。
sources: [Axelrod1981]
related: [papers/axelrod1981.md, paradigms/prisoners-dilemma.md, concepts/tit-for-tat.md, concepts/continuation-probability.md, glossary.md]
tags: [evolutionary-game-theory, stability, strategy]
status: stable
has_inference: false
created: 2026-11-16
updated: 2026-11-16
---
# 演化穩定策略 (Evolutionarily Stable Strategy)

## 白話摘要
如果一群人都用同一個策略，少數改用別的策略的人也占不到便宜，這個策略就是演化穩定策略 (evolutionarily stable strategy)。在囚犯困境 (Prisoner's Dilemma) 裡，「永遠背叛」(ALL D) 不管怎樣都是穩定的；「以牙還牙」(Tit-for-Tat) 只有在雙方很可能再碰面時才穩定。

## 定義
- 如果一群使用某個策略的個體，無法被少數採用其他策略的突變者入侵，這個策略就是演化穩定的 [Axelrod1981, p.4]。

## 各論文的觀點

### Axelrod1981
- 只玩一次的囚犯困境 (Prisoner's Dilemma) 中，沒有任何策略能入侵永遠背叛 (ALL D)，所以永遠背叛是演化穩定策略 [Axelrod1981, p.4]。
- 不論再相遇機率 (continuation probability) w 是多少，永遠背叛都是演化穩定策略 [Axelrod1981, p.4]。
- 以牙還牙 (Tit-for-Tat) 是演化穩定策略的充分必要條件是 w ≥ (T−R)/(T−P) 且 w ≥ (T−R)/(R−S) [Axelrod1981, p.5]。
- 證明只需要檢查兩種策略：永遠背叛，以及背叛 (Defect) 與合作 (Cooperate) 輪流；這兩種都無法入侵以牙還牙時，就沒有任何策略能入侵 [Axelrod1981, p.5]。
- 永遠背叛也是穩定的，這引出一個問題：合作 (cooperation) 一開始要怎麼起步 [Axelrod1981, p.6]。
- 第一種起步方式是親屬關係 (kinship)：重新計算報酬，讓個體在夥伴的收益中占有一部分利益，也就是以廣義適應度 (inclusive fitness) 計算，常常能消除 T > R 和 P > S 這兩個不等式，使合作變成無條件有利 [Axelrod1981, p.6]。
- 第二種起步方式是群聚 (clustering)：一小群以牙還牙者有一定比例 p 的互動發生在彼此之間，當 p 和 w 夠大時，就能在永遠背叛的族群中起步 [Axelrod1981, p.6]。
- 友善策略 (nice strategy) 是從不先背叛的策略 [Axelrod1981, p.6]。
- 一個友善且演化穩定的策略，不會被成群而來的其他策略入侵 [Axelrod1981, p.6]。
- 這是一種不對稱：以牙還牙可以靠群聚在永遠背叛的族群中起步，但友善且演化穩定的策略站穩之後，不會被任何群聚入侵 [Axelrod1981, p.6]。

## 爭議與未解問題
〔待補〕目前只有 Axelrod1981 一篇，尚無其他論文的比較。

## 相關頁面
- [合作的演化 (The Evolution of Cooperation)](../papers/axelrod1981.md)
- [囚犯困境 (Prisoner's Dilemma)](../paradigms/prisoners-dilemma.md)
- [以牙還牙 (Tit-for-Tat)](tit-for-tat.md)
- [再相遇機率 (Continuation Probability)](continuation-probability.md)
- [術語表 (Glossary)](../glossary.md)
