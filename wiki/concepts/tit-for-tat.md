---
title: 以牙還牙 (Tit-for-Tat)
type: concept
summary: 第一步合作、之後照做對方上一步的策略；第一輪電腦競賽平均分最高，第二輪再次獲勝。
sources: [Axelrod1981]
related: [papers/axelrod1981.md, paradigms/prisoners-dilemma.md, concepts/evolutionarily-stable-strategy.md, concepts/reciprocity.md, glossary.md, paradigms/axelrod-tournament.md]
tags: [tit-for-tat, strategy, reciprocity, repeated-games]
status: stable
has_inference: false
created: 2026-11-16
updated: 2026-11-16
---
# 以牙還牙 (Tit-for-Tat)

## 白話摘要
以牙還牙 (Tit-for-Tat) 的做法很簡單：第一次先合作 (Cooperate)，之後對方上一步怎麼做，自己這一步就怎麼做。它在第一輪電腦競賽 (computer tournament) 拿到最高平均分，第二輪又再次獲勝，成功的原因是從不先背叛 (Defect)、被背叛就回擊、回擊一次後就原諒。

## 定義
- 以牙還牙在第一步合作，之後照做對方上一步的選擇 [Axelrod1981, p.5]。
- 作者稱它是一種以互惠為基礎的合作 (cooperation based on reciprocity) 策略 [Axelrod1981, p.5]。
- 以牙還牙只記得上一步，所以對方一次合作就能把局面重設回遊戲開始時的狀態 [Axelrod1981, p.5]。

## 各論文的觀點

### Axelrod1981
- 第一輪競賽有 14 個參賽策略加 1 個隨機策略，以牙還牙是所有參賽策略中最簡單的，卻拿到最高平均分 [Axelrod1981, p.5]。
- 第二輪競賽有 62 個參賽策略，以牙還牙再次由 Anatol Rapoport 提交，並再次獲勝 [Axelrod1981, p.5]。
- 分析第二輪的 300 萬次選擇後，作者歸納出以牙還牙穩健的三個特徵 [Axelrod1981, p.5]：
  - 從不先背叛 [Axelrod1981, p.5]。
  - 對方背叛就報復 (provocable) [Axelrod1981, p.5]。
  - 報復一次之後就原諒 (forgiving) [Axelrod1981, p.5]。
- 生態分析 (ecological analysis) 中，較不成功的策略被淘汰後，以牙還牙最後取代所有其他策略 [Axelrod1981, p.5]。
- 當再相遇機率 (continuation probability) w 夠大，以牙還牙是演化穩定策略 (evolutionarily stable strategy)，任何突變策略都無法入侵 [Axelrod1981, p.5]。
- 以牙還牙屬於友善策略 (nice strategy)，也就是從不先背叛的策略 [Axelrod1981, p.6]。
- 當群內互動比例 p 和再相遇機率 w 都夠大時，一小群以牙還牙者形成的群聚 (clustering) 可以在永遠背叛 (ALL D) 的族群中起步 [Axelrod1981, p.6]。

## 爭議與未解問題
〔待補〕目前只有 Axelrod1981 一篇，尚無其他論文的比較。

## 相關頁面
- [合作的演化 (The Evolution of Cooperation)](../papers/axelrod1981.md)
- [囚犯困境 (Prisoner's Dilemma)](../paradigms/prisoners-dilemma.md)
- [Axelrod 電腦競賽 (Axelrod Computer Tournament)](../paradigms/axelrod-tournament.md)
- [演化穩定策略 (Evolutionarily Stable Strategy)](evolutionarily-stable-strategy.md)
- [互惠 (Reciprocity)](reciprocity.md)
- [術語表 (Glossary)](../glossary.md)
