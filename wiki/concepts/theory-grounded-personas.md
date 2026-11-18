---
title: 理論導向的人物設定 (Theory-Grounded Personas)
type: concept
summary: 依某個可檢驗的理論設計代理人的人物設定，例如只在乎公平、只在乎總報酬、只在乎自己；Horton2026 把這三種設定依人類資料調整混合比例後，在新賽局的預測誤差約減半，而 Horton2026 引用的研究指出，和理論無關的特質幾乎沒有幫助。
sources: [Horton2026, Xie2024]
related: [concepts/homo-silicus.md, paradigms/dictator-game.md, town/theory-grounded-agent-types.md, papers/horton2026.md, concepts/agent-trust-properties.md, glossary.md]
tags: [persona, calibration, llm-agents, social-preferences]
status: draft
has_inference: true
created: 2026-11-18
updated: 2026-11-18
---
# 理論導向的人物設定 (Theory-Grounded Personas)

## 白話摘要
如果直接拿沒有任何設定的語言模型玩獨裁者賽局，它的選擇和人類差很多。Horton2026 改成給代理人依理論設計的人物設定 (persona)：「只在乎公平」、「只在乎兩人的總報酬」、「只在乎自己」，代理人大致照設定行動。接著作者調整三種代理人的混合比例，讓整體選擇最接近人類受試者，再拿這組代理人去玩沒看過的新賽局，預測誤差大約減半。相反地，Horton2026 引用的研究指出，給代理人嗜好或喜歡的電視節目這類和理論無關的特質，幾乎沒有幫助。

## 定義
- 作者所說的「理論導向」，是指人物設定依據某個我們大致了解、可以清楚評估、而且合理預期能預測相關人類行為的理論 [Horton2026, p.13]。
- 例如 Charness 和 Rabin 的經濟模型中的公平、自利和效率，就對應到三種代理人 [Horton2026, p.13]。

> "The MSE of the calibrated samples (0.094) is about half of the persona-less control MSE (0.182)." [Horton2026, p.15]
> 中譯：校準後樣本的均方誤差 (0.094) 約為沒有人物設定的對照組 (0.182) 的一半。

## 各論文的觀點

### Horton2026

#### 沒有設定和有設定的差別
- 沒給人物設定的代理人，在 Charness 和 Rabin 的獨裁者賽局 (Dictator Game) 中，選擇和人類受試者差很多，雖然原研究幾乎一定在訓練資料中 [Horton2026, p.12–13]。
- 不同模型的反應也不同，例如 Llama-3-70B 看起來比較自私 [Horton2026, p.13]。
- 作者給代理人三種設定：不平等趨避型 (inequity-averse，只在乎兩人之間的公平)、效率型 (efficient，只在乎兩人的總報酬)、自利型 (self-interested，只在乎自己的報酬) [Horton2026, p.11]。
- 除了少數例外，例如 Deepseek 和 Llama-3-70B 在 Berk23 中沒有選擇不平等趨避的選項，有設定的代理人大致都照設定行動 [Horton2026, p.13]。

#### 校準混合比例
- 作者找出三種代理人的混合比例，讓整體選擇最接近人類受試者在單階段獨裁者賽局的選擇 [Horton2026, p.13–14]。
- 以 GPT-4o 為例，效率型、不平等趨避型、自利型的最佳比例是 0.37、0.10 和 0.53 [Horton2026, p.14]。
- Llama-3-70B、Claude-Sonnet-3.5 和 Deepseek 的不平等趨避型比例都是 0，校準後的組合主要由效率型和自利型組成 [Horton2026, p.14]。
- 每個模型依這個比例隨機抽出 100 個代理人，形成校準樣本 (calibrated sample)，讓它們在兩階段賽局中分別扮演兩個角色各 5 次 [Horton2026, p.14]。
- 校準後樣本在新賽局中的預測誤差（均方誤差，mean-squared error，MSE）是 0.094，約為沒給人物設定時 0.182 的一半 [Horton2026, p.15]。

#### 什麼樣的設定沒有用
- Manning 和 Horton (2025) 發現，給代理人嗜好或喜歡的電視節目，對擬合 Charness 和 Rabin 的賽局幾乎沒有幫助，以社會偏好為基礎的設定才有幫助 [Horton2026, p.30]。
- 作者在註腳中指出，只用「30 歲男性」這類人口特徵當指令的研究，假設模型能正確表示這些特徵如何影響策略情境；模型的世界模型不穩時，模擬可能退化成刻板印象 [Horton2026, p.37]。

## 爭議與未解問題
- 作者表示，目前還不能從「哪個提示改善擬合」推論出人類真的照這個理論行事 [Horton2026, p.30]。
- 〔推論〕Xie2024 用包含姓名、年齡、性別、職業和背景的人物設定，發現 GPT-4 在信任賽局和人類高度一致 [Xie2024, p.3–4; Xie2024, p.8]；這和 Horton2026 對人口特徵式設定的保留看法有張力，但兩者的賽局、模型和比較指標不同，詳見[矛盾總表](../syntheses/contradictions.md)。

## 相關頁面
- [矽基人 (Homo Silicus)](homo-silicus.md)
- [獨裁者賽局 (Dictator Game)](../paradigms/dictator-game.md)
- [用理論類型設計小鎮代理人 (Theory-Grounded Agent Types for the Town)](../town/theory-grounded-agent-types.md)
- [代理人信任的特性 (Properties of Agent Trust)](agent-trust-properties.md)
- [大型語言模型作為模擬的經濟代理人：我們能從矽基人學到什麼？ (Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?)](../papers/horton2026.md)
- [術語表 (Glossary)](../glossary.md)
