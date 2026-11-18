---
title: 互惠需要無法匿名 (Reciprocity Requires Non-Anonymity)
type: town
summary: 以互惠為基礎的合作要能演化，背叛者不能隱沒在匿名的人群中（靠辨識個體或替代機制），而且雙方再相遇的機率要夠高。
sources: [Axelrod1981, Berg1995]
related: [syntheses/contradictions.md, concepts/reciprocity.md, concepts/continuation-probability.md, concepts/tit-for-tat.md, papers/axelrod1981.md, paradigms/axelrod-tournament.md, concepts/individual-recognition.md]
tags: [town-design, reciprocity, memory, continuation-probability]
status: needs-review
has_inference: true
created: 2026-11-16
updated: 2026-11-16
town_status: idea
---
# 互惠需要無法匿名 (Reciprocity Requires Non-Anonymity)

## 白話摘要
以互惠為基礎的合作 (cooperation based on reciprocity) 要能演化，背叛 (Defect) 的人不能隱沒在匿名的人群中：可以靠認出對方，也可以靠總是和同一個對象互動這類替代機制；而且雙方之後要很可能再碰面。碰面的機會變少時，例如對方生病或衰老，背叛的誘因就會變大。

## 研究依據
- 合作要能演化，背叛的個體必須逃不過有效的報復，不能隱沒在匿名的人群中，詳見[個體辨識](../concepts/individual-recognition.md) [Axelrod1981, p.7]。
- 同樣兩個個體的再相遇機率 (continuation probability) w 必須夠高 [Axelrod1981, p.7]。
- 以牙還牙 (Tit-for-Tat) 依照對方上一步的選擇行動，所以需要記得對方上一步做了什麼 [Axelrod1981, p.5]。
- 固定的見面地點和穩定的領域，能減少辨識個體的需求 [Axelrod1981, p.7]。
- 影響 w 的因素包括平均壽命、相對移動性和健康 [Axelrod1981, p.4]。
- 生病或衰老讓未來互動機率下降時，會出現背叛的誘因 [Axelrod1981, p.7]。

## 設計點子
- 〔待檢視〕〔推論〕小鎮代理人因此需要互動記憶和會重複相遇的空間，以下各點是具體做法。被 Berg1995 挑戰：單次、雙盲、完全匿名的實驗中，仍有部分受試者回報多於對方送出（無歷史組 28 人中 11 人、社會歷史組 24 人中 13 人），表示互惠不一定需要互動記憶和重複相遇，詳見[矛盾總表](../syntheses/contradictions.md) [Berg1995, p.10; Berg1995, p.14]。
- 〔推論〕每個代理人應保存「和誰互動過、對方怎麼回應」的互動記憶，否則無法實行以牙還牙這類互惠 (reciprocity) 策略。
- 〔推論〕小鎮地圖可以用固定場所（宿舍、系館、餐廳）提高同一批代理人重複碰面的機率，也就是提高 w。
- 〔推論〕w 可以做成可調整的設計參數，例如同系同學 w 高、校外訪客 w 低，觀察合作程度是否隨 w 改變。
- 〔推論〕即將畢業或離開小鎮的代理人，相當於 w 下降，可以觀察它們的背叛是否增加。
- 〔推論〕以牙還牙可以當作基準策略，用來和 LLM 代理人的實際行為比較。

## 風險與待驗證
- 〔推論〕Axelrod1981 的結論來自規則固定的程式策略，LLM 代理人不一定會依照 w 的門檻調整合作。
- 〔推論〕代理人的互動記憶如果有遺漏或錯誤，可能把合作誤記成背叛，Axelrod1981 沒有分析這種情況。
- 〔待補〕需要之後的 LLM 論文資料，判斷 LLM 代理人是否會依據過去的互動調整合作。

## 相關頁面
- [互惠 (Reciprocity)](../concepts/reciprocity.md)
- [個體辨識 (Individual Recognition)](../concepts/individual-recognition.md)
- [再相遇機率 (Continuation Probability)](../concepts/continuation-probability.md)
- [以牙還牙 (Tit-for-Tat)](../concepts/tit-for-tat.md)
- [Axelrod 電腦競賽 (Axelrod Computer Tournament)](../paradigms/axelrod-tournament.md)
- [矛盾總表 (Contradictions)](../syntheses/contradictions.md)
- [合作的演化 (The Evolution of Cooperation)](../papers/axelrod1981.md)
