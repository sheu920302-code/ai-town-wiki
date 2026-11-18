---
title: 再相遇機率 (Continuation Probability)
type: concept
summary: 這次互動結束後，同樣兩人會再碰面的機率 w；w 夠高時，以互惠為基礎的合作才會穩定。
sources: [Axelrod1981]
related: [papers/axelrod1981.md, paradigms/prisoners-dilemma.md, concepts/evolutionarily-stable-strategy.md, concepts/reciprocity.md, town/reciprocity-requires-non-anonymity.md, glossary.md, paradigms/axelrod-tournament.md]
tags: [continuation-probability, repeated-games, design-parameter]
status: stable
has_inference: true
created: 2026-11-16
updated: 2026-11-16
---
# 再相遇機率 (Continuation Probability)

## 白話摘要
再相遇機率 w (continuation probability) 是這次互動結束後，同樣兩個人還會再碰面的機率。w 夠高時，以牙還牙 (Tit-for-Tat) 這類以互惠為基礎的合作 (cooperation based on reciprocity) 才會穩定；壽命、移動範圍和健康都會影響 w，生病或衰老會讓 w 下降，背叛 (Defect) 的誘因就變大。

## 定義
- w 是目前這次互動結束後，同樣兩個個體會再相遇的機率 [Axelrod1981, p.4]。
- 第 n 次互動真的發生的機率是 w 的 (n−1) 次方 [Axelrod1981, p.5]。
- Axelrod1981 用 w 取代「事先固定的回合數」，作者認為這是更符合現實的假設 [Axelrod1981, p.4]。

## 各論文的觀點

### Axelrod1981
- 影響 w 的因素包括平均壽命、相對移動性和個體的健康 [Axelrod1981, p.4]。
- 以牙還牙 (Tit-for-Tat) 是演化穩定策略 (evolutionarily stable strategy) 的條件是 w ≥ (T−R)/(T−P) 且 w ≥ (T−R)/(R−S)，原文編號為條件 (1) [Axelrod1981, p.5]。
- 〔推論〕以圖 1 的數值 T=5、R=3、P=1、S=0 代入條件 (1)：w ≥ max((T−R)/(T−P), (T−R)/(R−S)) = max(2/4, 2/3) = max(0.5, 0.667) = 2/3，也就是 w 至少約 0.67 [Axelrod1981, p.4–5]。
- 第二輪電腦競賽 (computer tournament) 的每場長度不固定，作者把「每一步不是最後一步」的機率設為 w = .99654；原文對長度的描述是 "an expected probability of 200 moves"，沒有寫明 200 是期望值還是中位數 [Axelrod1981, p.8]。
- 〔推論〕依 w = .99654 計算，期望長度是 1/(1−w) = 1/0.00346 ≈ 289 步；而 0.99654^200 ≈ 0.5，所以 200 步是中位數長度，也就是大約一半的比賽會超過 200 步 [Axelrod1981, p.8]。
- 當 w 低於穩定門檻，回報對方的合作就不再划算 [Axelrod1981, p.7]。
- 夥伴生病而存活率下降，是 w 下降的一個可察覺訊號，雙方預期都會變得較不合作 [Axelrod1981, p.7]。
- 夥伴衰老的效果類似生病：未來互動機率變小時，會出現背叛一次撈好處的誘因 [Axelrod1981, p.7]。
- 同時能水平傳播和垂直傳播的共生微生物，預期會在和宿主繼續互動的機率下降時，從互利轉為寄生 [Axelrod1981, p.7]。

## 爭議與未解問題
〔待補〕目前只有 Axelrod1981 一篇，尚無其他論文的比較。

## 相關頁面
- [合作的演化 (The Evolution of Cooperation)](../papers/axelrod1981.md)
- [囚犯困境 (Prisoner's Dilemma)](../paradigms/prisoners-dilemma.md)
- [Axelrod 電腦競賽 (Axelrod Computer Tournament)](../paradigms/axelrod-tournament.md)
- [演化穩定策略 (Evolutionarily Stable Strategy)](evolutionarily-stable-strategy.md)
- [互惠 (Reciprocity)](reciprocity.md)
- [互惠需要無法匿名 (Reciprocity Requires Non-Anonymity)](../town/reciprocity-requires-non-anonymity.md)
- [術語表 (Glossary)](../glossary.md)
