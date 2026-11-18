---
title: 生成式代理人 (Generative Agent)
type: concept
summary: 以大型語言模型為核心，加上記憶流、反思、規劃三個元件，能依自己過去的經歷和環境產生可信人類行為的計算代理人；作者強調它們沒有真正的能動性。
sources: [Park2023]
related: [papers/park2023.md, concepts/memory-stream.md, concepts/reflection.md, concepts/planning.md, concepts/emergent-social-behavior.md, concepts/believability.md, concepts/evaluation-and-ablation.md, concepts/generative-agent-ethics.md, concepts/instruction-tuning.md, concepts/homo-silicus.md, glossary.md]
tags: [generative-agents, llm-agents, architecture]
status: draft
has_inference: true
created: 2026-11-17
updated: 2026-11-18
---
# 生成式代理人 (Generative Agent)

## 白話摘要
生成式代理人 (generative agent) 是一種用大型語言模型 (large language model) 驅動的 AI 角色。它會把經歷用自然語言記下來（記憶流 (memory stream)），隨時間把記憶整理成較高層的想法（反思 (reflection)），再把這些結論和目前的環境轉成行動計畫（規劃 (planning)）。Park2023 的人類評分者認為，三個元件都保留時，代理人的回答最可信。作者也特別說明，這些代理人像迪士尼動畫角色一樣只是「看起來可信」，並沒有真正的能動性 (agency)。

## 定義
- Park2023 把生成式代理人定義為：運用生成式模型來模擬可信人類行為的代理人 [Park2023, p.2]。
- 生成式代理人以目前的環境和過去的經歷作為輸入，產生行為作為輸出 [Park2023, p.8]。
- 架構由三個主要元件組成：記憶流 (memory stream)、反思 (reflection) 和規劃 (planning) [Park2023, p.2]。
- 記憶流用自然語言完整記錄代理人的經歷；反思隨時間把記憶整合成較高層的推論；規劃把這些結論和目前的環境轉成高層的行動計畫，再遞迴拆成細部的行動和反應 [Park2023, p.2]。
- 反思和計畫會再存回記憶流，影響代理人之後的行為 [Park2023, p.2]。
- 作者說明，描述代理人「做什麼」只是為了好讀，不表示它們有像人一樣的能動性 [Park2023, p.2]。

## 各論文的觀點

### Park2023
- 作者的關鍵觀察是：大型語言模型 (large language model) 從訓練資料中編碼了範圍很廣的人類行為 [Park2023, p.4]。
- 只靠大型語言模型也能產生行為，但代理人可能不會依過去經歷反應、做不出重要推論，也無法長期保持一致 [Park2023, p.8]。
- 所有內容都以自然語言記錄和推理，讓架構可以直接運用大型語言模型 [Park2023, p.8]。
- 人類評分者評比可信度 (believability) 時，完整架構的表現勝過拿掉任一元件的版本，也勝過人類群眾外包工作者扮演角色的回答 [Park2023, p.14]。
- 作者預期，即使語言模型進步，記憶、規劃和反思這些架構基礎很可能維持不變 [Park2023, p.8]。

> "The behaviors of our agents, akin to animated Disney characters, aim to create a sense of believability, but they do not imply genuine agency." [Park2023, p.2]
> 中譯：我們的代理人的行為就像迪士尼動畫角色，目的是營造可信的感覺，但並不表示它們有真正的能動性。

## 爭議與未解問題
- 〔推論〕Park2023 評估的是可信度，不是代理人的選擇是否和真人實驗一致；生成式代理人能不能代替人類受試者玩信任或合作賽局，要看後續論文的比較。
- 作者主張，生成式代理人應該用在早期設計或難以找到受試者的情境，不應取代真實人類的意見 [Park2023, p.18]。

## 相關頁面
- [生成式代理人：人類行為的互動模擬 (Generative Agents: Interactive Simulacra of Human Behavior)](../papers/park2023.md)
- [記憶流 (Memory Stream)](memory-stream.md)
- [反思 (Reflection)](reflection.md)
- [規劃 (Planning)](planning.md)
- [湧現的社會行為 (Emergent Social Behavior)](emergent-social-behavior.md)
- [可信度 (Believability)](believability.md)
- [受控評估與消融 (Controlled Evaluation and Ablation)](evaluation-and-ablation.md)
- [生成式代理人的倫理風險 (Ethical Risks of Generative Agents)](generative-agent-ethics.md)
- [指令微調 (Instruction Tuning)](instruction-tuning.md)
- [矽基人 (Homo Silicus)](homo-silicus.md)
- [術語表 (Glossary)](../glossary.md)
