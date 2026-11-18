---
title: 信任 (Trust)
type: concept
summary: 信任者把決定權交給受託者，自己承擔風險；Berg1995 採用和 Coleman 相近的定義，並認為信任可能是經濟行為的基本元素。
sources: [Berg1995, Xie2024]
related: [papers/berg1995.md, paradigms/trust-game.md, concepts/reciprocity.md, concepts/social-history.md, papers/xie2024.md, concepts/trust-behavioral-factors.md, concepts/agent-trust-properties.md, glossary.md]
tags: [trust]
status: stable
has_inference: true
created: 2026-11-16
updated: 2026-11-18
---
# 信任 (Trust)

## 白話摘要
信任 (trust) 是把決定權交給別人、讓自己承擔風險：如果對方守信，雙方都比不交易時好；如果對方不守信，自己就會吃虧。Berg1995 發現，即使只交易一次、彼此完全匿名，多數人仍然願意信任陌生人，所以作者認為信任可能是人類經濟行為的基本元素。

## 定義
- Berg1995 對信任的定義和 Coleman (1990) 相近 [Berg1995, p.5]。
- 在 Coleman 的用語中，房間 A 的受試者是信任者 (trustor)，送出 M_a > 0 稱為給予信任 (place a trust) [Berg1995, p.5]。
- 受託者 (trustee) 的回報多於信任者送出的金額，也就是 k_b(3M_a) > M_a 時，稱為履行信任 (keep the trust)，也就是互惠 (reciprocity) [Berg1995, p.5]。
- 信任可以用兩個動作定義：信任者把做決定的權利交給受託者，受託者再做出同時影響雙方的決定 [Berg1995, p.5]。
- 要說受試者用信任促成交換，需要滿足三個條件 [Berg1995, p.5]：
  - 給予信任會讓信任者承擔風險 [Berg1995, p.5]。
  - 在所有可能的行動中，受託者的決定會以自己的成本讓信任者得益 [Berg1995, p.5]。
  - 和信任者不信任受託者的結果相比，雙方都因為這次交易而變得更好 [Berg1995, p.5]。

## 各論文的觀點

### Berg1995
- 作者認為，排除聲譽、契約和懲罰之後仍然出現正的投資，顯示信任是一種經濟上的基本元素 (primitive) [Berg1995, p.2]。
- Arrow (1974) 把信任稱為社會系統重要的潤滑劑，並認為演化模型也許能解釋信任如何出現 [Berg1995, p.3]。
- 從演化的觀點看，信任可以視為在新情境中引導行為的、行為上的基本元素 (behavioral primitive)，但在某些情況下也可能消失，或被個人自利的決策能力取代 [Berg1995, p.3]。
- Williamson (1993) 區分兩種信任：根據期望效用計算決定是否信任的計算型信任 (calculative trust)，以及基於「覺得信任是對的」的個人信任 (personal trust) [Berg1995, p.5]。
- 作者在註腳中總結：信任可理解為依賴他人的互惠，也就是做了某件事或給了某樣東西後，會得到回報 [Berg1995, p.5]。
- 送 $1 可能代表對互惠的信念很弱，送 $10 則可能代表信念很強 [Berg1995, p.6]。
- 兩組實驗合計，房間 A 受試者在 60 次中有 55 次送了錢，強烈否定了「不會送任何錢」的子賽局完美預測 (subgame perfect prediction) [Berg1995, p.16]。

### Xie2024
- Xie2024 採用 Rousseau 等人的定義：信任包含基於對他人的正面期待，而願意讓自身利益承擔風險的意圖 [Xie2024, p.1]。
- 行為經濟學通常用信任者在信任賽局 (Trust Game) 中最初送出的金額衡量信任 [Xie2024, p.4]。
- 作者把大型語言模型 (large language model) 代理人的信任行為稱為代理人信任 (agent trust)，人類的稱為人類信任 (human trust) [Xie2024, p.2]。
- 作者認定代理人表現信任行為的兩個條件：送出金額為正、而且不超過手上的錢；以及送出的決定可以用它寫出的推理過程解釋 [Xie2024, p.4]。
- 人類研究指出三個影響信任的基本因素：預期互惠、風險感知和利社會偏好，詳見[信任的行為因素](trust-behavioral-factors.md) [Xie2024, p.5]。

## 爭議與未解問題
- 〔推論〕Berg1995 的信任定義強調把決定權交給受託者，Xie2024 的定義強調基於正面期待而承擔風險；兩者都把「願意承擔被辜負的風險」當作核心，沒有互相矛盾。

## 相關頁面
- [信任、互惠與社會歷史 (Trust, Reciprocity, and Social History)](../papers/berg1995.md)
- [信任賽局 (Trust Game)](../paradigms/trust-game.md)
- [互惠 (Reciprocity)](reciprocity.md)
- [社會歷史 (Social History)](social-history.md)
- [大型語言模型代理人能模擬人類的信任行為嗎？ (Can Large Language Model Agents Simulate Human Trust Behavior?)](../papers/xie2024.md)
- [信任的行為因素 (Behavioral Factors of Trust)](trust-behavioral-factors.md)
- [代理人信任的特性 (Properties of Agent Trust)](agent-trust-properties.md)
- [術語表 (Glossary)](../glossary.md)
