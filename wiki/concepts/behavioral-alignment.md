---
title: 行為一致性 (Behavioral Alignment)
type: concept
summary: Xie2024 提出的概念：比較大型語言模型和人類在影響行為的因素（行為因素）和行為隨時間的變化（行為動態）上是否相似，同時看行動和背後的推理；在信任行為上，GPT-4 的一致性最高。
sources: [Xie2024, Berg1995, Horton2026]
related: [papers/xie2024.md, concepts/trust-behavioral-factors.md, paradigms/repeated-trust-game.md, concepts/believability.md, papers/horton2026.md, concepts/theory-grounded-personas.md, glossary.md]
tags: [behavioral-alignment, llm-agents, evaluation]
status: draft
has_inference: true
created: 2026-11-18
updated: 2026-11-18
---
# 行為一致性 (Behavioral Alignment)

## 白話摘要
行為一致性 (behavioral alignment) 是 Xie2024 用來回答「AI 代理人的行為像不像人」的標準。它不只看代理人最後做了什麼，也看兩件事：影響決定的因素是不是和人一樣（行為因素），以及多次互動時行為的變化模式是不是和人一樣（行為動態）。作者也用代理人寫出的推理過程輔助判斷。結果 GPT-4 在信任行為上和人類最一致，參數較少的模型比較不一致。

## 定義
- 作者把行為一致性定義為大型語言模型 (large language model) 和人類在兩方面的相似性：影響行為的因素，稱為行為因素 (behavioral factors)；行動的動態，稱為行為動態 (behavioral dynamics) [Xie2024, p.5]。
- 作者說明，行為一致性涉及行動本身，以及行動背後的推理過程 [Xie2024, p.5]。

> "Because actions evolve over time and the reasoning that underlies them involves multiple factors, we define behavioral alignment as the analogy between LLMs and humans concerning factors impacting behavior, namely behavioral factors, and action dynamics, namely behavioral dynamics." [Xie2024, p.5]
> 中譯：因為行動會隨時間演變，而背後的推理又涉及多個因素，我們把行為一致性定義為大型語言模型和人類在影響行為的因素（行為因素）和行動動態（行為動態）上的相似性。

## 各論文的觀點

### Xie2024
- 作者指出，既有的對齊定義主要強調價值，目的是確保模型安全、有幫助，無法完整描述模型和人類之間多面向的相似性 [Xie2024, p.5]。
- 在信任行為上，作者檢查三個行為因素：預期互惠、風險感知和利社會偏好，詳見[信任的行為因素](trust-behavioral-factors.md) [Xie2024, p.5]。
- 行為動態則用重複信任賽局 (Repeated Trust Game) 檢查，看代理人多輪下來的模式是否和人類相同 [Xie2024, p.5]。
- 作者也用信念-慾望-意圖 (BDI) 框架解讀代理人寫出的推理，進一步驗證代理人是否有類似人類認知的推理過程 [Xie2024, p.5–6]。
- 作者的結論是：GPT-4 代理人在信任行為上有高度的行為一致性，參數較少、能力較弱的模型一致性較低 [Xie2024, p.8]。
- 作者認為這個發現為模擬更複雜的人類互動和社會制度鋪路 [Xie2024, p.8]。

## 爭議與未解問題
- 〔推論〕Park2023 評估的是可信度 (believability)，也就是人類評分者覺得代理人的回答像不像真人；Xie2024 的行為一致性則直接拿代理人的選擇和人類實驗的結果比較，兩者回答的是不同問題。
- 〔推論〕Xie2024 的人類數據取自既有研究，人類在信任賽局的平均送出是 $5.97（原文沒有說明來源）或引用 Cox (2004) 的 $6.0，而 Berg1995 的無歷史組是 $5.16；比較的人類基準不同，結論的強弱也會不同 [Xie2024, p.5; Xie2024, p.6; Berg1995, p.10]。
- Horton2026 在 5 個經濟實驗中大致得到和原研究相似的質性結果，但沒給人物設定的代理人在獨裁者賽局和人類差很多 [Horton2026, p.1; Horton2026, p.12–13]。
- 〔推論〕所以行為一致性可能因賽局、模型和人物設定方式而不同；Xie2024 的高度一致是在信任賽局、以 GPT-4 為主的條件下得到的。

## 相關頁面
- [大型語言模型代理人能模擬人類的信任行為嗎？ (Can Large Language Model Agents Simulate Human Trust Behavior?)](../papers/xie2024.md)
- [信任的行為因素 (Behavioral Factors of Trust)](trust-behavioral-factors.md)
- [重複信任賽局 (Repeated Trust Game)](../paradigms/repeated-trust-game.md)
- [可信度 (Believability)](believability.md)
- [大型語言模型作為模擬的經濟代理人：我們能從矽基人學到什麼？ (Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?)](../papers/horton2026.md)
- [理論導向的人物設定 (Theory-Grounded Personas)](theory-grounded-personas.md)
- [術語表 (Glossary)](../glossary.md)
