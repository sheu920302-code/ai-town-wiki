---
title: 合作的演化 (The Evolution of Cooperation)
type: paper
summary: 用囚犯困境模型和電腦競賽說明，以互惠為基礎的合作可以在自私的世界中出現、擴散，並在站穩後維持下去。
sources: [Axelrod1981]
related: [paradigms/prisoners-dilemma.md, paradigms/axelrod-tournament.md, concepts/tit-for-tat.md, concepts/evolutionarily-stable-strategy.md, concepts/reciprocity.md, concepts/continuation-probability.md, town/reciprocity-requires-non-anonymity.md, glossary.md, concepts/individual-recognition.md]
tags: [cooperation, reciprocity, repeated-games, evolutionary-game-theory]
status: stable
has_inference: true
created: 2026-11-16
updated: 2026-11-16
citekey: Axelrod1981
authors: [Robert Axelrod, William D. Hamilton]
year: 1981
venue: Science
version: published
raw_file: Axelrod_Hamilton1981_EvolutionOfCooperation.pdf
pdf_pages: 11
page_offset: 1388
---
# 合作的演化 (The Evolution of Cooperation)

## 白話摘要
兩個人只見一次面時，背叛 (Defect) 對自己最有利；但如果之後很可能再碰面，「第一次先合作 (Cooperate)、之後照抄對方上一步」的以牙還牙 (Tit-for-Tat) 策略就能站穩腳步。作者用電腦競賽 (computer tournament) 和數學證明說明，以互惠為基礎的合作 (cooperation based on reciprocity) 可以在大家都自私的世界裡出現、擴散，而且在再相遇機率 (continuation probability) 夠高時，一旦站穩就不會被入侵。

## 研究問題
- 演化理論以生存競爭為基礎，但合作 (cooperation) 在同一物種、甚至不同物種之間都很常見 [Axelrod1981, p.2]。
- 為了解釋合作，演化理論發展出兩種延伸：親屬理論 (kinship theory) 和互惠理論 (reciprocation theory) [Axelrod1981, p.2]。
- 作者把合作的演化拆成三個問題 [Axelrod1981, p.5]：
  - 穩健性 (robustness)：什麼策略能在各種策略混雜的環境中表現良好 [Axelrod1981, p.5]。
  - 穩定性 (stability)：這種策略站穩之後，能不能抵抗突變策略入侵 [Axelrod1981, p.5]。
  - 初始可行性 (initial viability)：在幾乎沒有人合作的環境中，這種策略要怎麼起步 [Axelrod1981, p.5]。

## 方法
- 模型以兩人版本的囚犯困境 (Prisoner's Dilemma) 為基礎 [Axelrod1981, p.3]。
- 兩人之後是否再相遇由機率 w 決定，而不是事先固定回合數 [Axelrod1981, p.4]。
- 用演化穩定策略 (evolutionarily stable strategy) 的概念判斷一個策略能否抵抗入侵 [Axelrod1981, p.3]。
- 第一輪電腦競賽：14 個參賽策略加上 1 個隨機策略進行循環賽 (round robin)，每場 200 步，報酬依圖 1 [Axelrod1981, p.5]。
- 第一輪的策略由經濟學、社會學、政治學和數學領域的賽局理論學者提交 [Axelrod1981, p.5]。
- 第二輪電腦競賽：來自 6 個國家的 62 個參賽策略，參賽者大多是電腦愛好者 [Axelrod1981, p.5]。
- 第二輪電腦競賽 (computer tournament) 的每場長度不固定，作者把「每一步不是最後一步」的機率設為 w = .99654；原文對長度的描述是 "an expected probability of 200 moves"，沒有寫明 200 是期望值還是中位數 [Axelrod1981, p.8]。
- 〔推論〕依 w = .99654 計算，期望長度是 1/(1−w) = 1/0.00346 ≈ 289 步；而 0.99654^200 ≈ 0.5，所以 200 步是中位數長度，也就是大約一半的比賽會超過 200 步 [Axelrod1981, p.8]。
- 第二輪和第一輪一樣，每對策略比 5 場 [Axelrod1981, p.8]。
- 生態分析 (ecological analysis)：假設每個策略在下一輪的比例依前一輪的成績決定，反覆模擬 [Axelrod1981, p.5]。

## 主要發現
- 只玩一次的囚犯困境中，永遠背叛 (ALL D) 是演化穩定策略 [Axelrod1981, p.4]。
- 回合數事先已知時，永遠背叛仍是唯一的演化穩定策略，因為從最後一回合往回推，每一回合背叛都是最佳選擇 [Axelrod1981, p.4]。
- 不論 w 是多少，永遠背叛都是演化穩定策略 [Axelrod1981, p.4]。
- 第一輪競賽中，平均分最高的是所有參賽策略中最簡單的以牙還牙 [Axelrod1981, p.5]。
- 第二輪競賽中，以牙還牙再次獲勝 [Axelrod1981, p.5]。
- 以牙還牙的穩健性來自三個特徵：從不先背叛、對方背叛就報復、報復一次之後就原諒 [Axelrod1981, p.5]。
- 生態分析中，以牙還牙最後取代了所有其他策略 [Axelrod1981, p.5]。
- 當 w ≥ (T−R)/(T−P) 且 w ≥ (T−R)/(R−S) 時，以牙還牙是演化穩定策略 [Axelrod1981, p.5]。
- 合作可以透過親屬關係 (kinship) 或群聚 (clustering)，在永遠背叛的族群中起步 [Axelrod1981, p.6]。
- 友善策略 (nice strategy) 如果同時是演化穩定策略，就不會被成群而來的其他策略入侵 [Axelrod1981, p.6]。
- 合作要能演化，其中兩個條件是：背叛者必須逃不過有效的報復，而且同樣兩個個體再相遇的機率 w 要夠高 [Axelrod1981, p.7]。
- 作者把模型應用到生物現象，包括無花果小蜂、小魚或甲殼類清潔者、領域性 (territoriality) 鳥類和人類的臉孔辨識 [Axelrod1981, p.7]。
- 作者也把模型延伸到疾病的慢性與急性期，以及卵子形成時的染色體不分離 [Axelrod1981, p.8]。

## 限制
- 作者只分析兩人版本的囚犯困境 [Axelrod1981, p.3]。
- 模型假設雙方同時做選擇，作者認為改成輪流選擇差別不大 [Axelrod1981, p.4–5]。
- 作者表示有兩件事純屬推測：一是一顆發育中的卵發生「背叛」時，其他還在等待的卵能察覺到；二是染色體在配子細胞分裂時會有自我推進的行為 [Axelrod1981, p.8]。
- 〔推論〕本文沒有人類受試者實驗，結論來自數學分析和電腦模擬。
- 〔推論〕競賽策略由學者和電腦愛好者設計 [Axelrod1981, p.5]，不能直接代表一般人的行為。
- 〔推論〕本文沒有討論互動中「出錯」的情況，例如把對方的合作誤認為背叛。

## 關鍵引文
> "This strategy is simply one of cooperating on the first move and then doing whatever the other player did on the preceding move." [Axelrod1981, p.5]
> 中譯：這個策略就是第一步合作，之後照做對方上一步的選擇。

> "The gear wheels of social evolution have a ratchet." [Axelrod1981, p.6]
> 中譯：社會演化的齒輪裝有棘輪。

> "This establishes conditions under which cooperation based on reciprocity can evolve." [Axelrod1981, p.8]
> 中譯：這確立了以互惠為基礎的合作能夠演化出來的條件。

## 相關頁面
- [囚犯困境 (Prisoner's Dilemma)](../paradigms/prisoners-dilemma.md)
- [Axelrod 電腦競賽 (Axelrod Computer Tournament)](../paradigms/axelrod-tournament.md)
- [以牙還牙 (Tit-for-Tat)](../concepts/tit-for-tat.md)
- [演化穩定策略 (Evolutionarily Stable Strategy)](../concepts/evolutionarily-stable-strategy.md)
- [互惠 (Reciprocity)](../concepts/reciprocity.md)
- [再相遇機率 (Continuation Probability)](../concepts/continuation-probability.md)
- [個體辨識 (Individual Recognition)](../concepts/individual-recognition.md)
- [互惠需要無法匿名 (Reciprocity Requires Non-Anonymity)](../town/reciprocity-requires-non-anonymity.md)
- [術語表 (Glossary)](../glossary.md)
