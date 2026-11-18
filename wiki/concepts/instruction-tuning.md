---
title: 指令微調 (Instruction Tuning)
type: concept
summary: Park2023 推測，底層模型的指令微調可能讓生成式代理人說話過於正式、整體上更客氣更合作，彼此之間似乎也過度合作；例如 Isabella 很少拒絕別人的點子。
sources: [Park2023, Xie2024, Horton2026]
related: [concepts/generative-agent.md, concepts/emergent-social-behavior.md, town/instruction-tuning-makes-agents-too-cooperative.md, papers/park2023.md, papers/xie2024.md, syntheses/contradictions.md, papers/horton2026.md, concepts/homo-silicus.md, glossary.md]
tags: [instruction-tuning, cooperation, llm-agents]
status: draft
has_inference: true
created: 2026-11-17
updated: 2026-11-18
---
# 指令微調 (Instruction Tuning)

## 白話摘要
Park2023 推測，用指令微調 (instruction tuning) 過的語言模型驅動代理人時，代理人說話常常過於正式，整體上更客氣、更合作，彼此之間似乎也過度合作。例如 Isabella 很少拒絕別人給的派對點子，時間久了，自己的興趣也被別人改變。作者也預期未來的模型能更好地控制說話風格。

## 定義
- 原文沒有給指令微調下定義，只推測代理人的部分行為可能和底層模型的指令微調有關 [Park2023, p.5; Park2023, p.17]。

> "We note that the conversational style of these agents can feel overly formal, likely a result of instruction tuning in the underlying models." [Park2023, p.5]
> 中譯：我們注意到這些代理人的對話風格可能顯得過於正式，很可能是底層模型指令微調的結果。

## 各論文的觀點

### Park2023
- 作者預期，未來的語言模型能更好地控制寫作風格 [Park2023, p.5]。
- 作者觀察到指令微調可能的影響：整體而言，代理人的行為被引導得更客氣、更合作 [Park2023, p.17]。
- 例如 Mei 和丈夫 John 說話時，常以正式的問候開頭，最後以客套話結束 [Park2023, p.17]。
- 作者也觀察到，指令微調似乎讓代理人彼此過度合作 [Park2023, p.17]。
- Isabella 收到和自己興趣不合的派對點子，例如莎士比亞朗讀會或專業交流活動，卻很少拒絕 [Park2023, p.17]。
- 時間久了，別人的興趣塑造了 Isabella 自己的興趣 [Park2023, p.17]。
- 實驗使用的模型是 gpt3.5-turbo [Park2023, p.8]。

### Horton2026
- Horton2026 指出，指令微調和人類回饋強化學習等後訓練方法，會讓模型避開訓練資料中的錯誤模式，轉向合作、聽從指令的行為；作者利用這個特性替代理人設定角色和偏好 [Horton2026, p.26]。
- 作者也發現，即使經過大量的後訓練微調，人類選擇中可能不理想的捷思特徵，例如現狀偏誤，仍然會出現在 LLM 的行為中 [Horton2026, p.17–18]。

> "Post-training methods (like instruction tuning or reinforcement learning with human feedback) steer models away from brittle responses driven by spurious patterns in their training data and toward cooperative, instruction-following behavior—we exploit this property when we endow agents with roles and preferences." [Horton2026, p.26]
> 中譯：後訓練方法（例如指令微調或人類回饋強化學習）會讓模型避開訓練資料中錯誤模式造成的脆弱回應，轉向合作、聽從指令的行為；我們替代理人設定角色和偏好時，正是利用這個特性。

## 爭議與未解問題
- 〔推論〕Horton2026 說的「合作」是指聽從使用者指令，Park2023 觀察到的是代理人彼此之間過度合作；兩者都指向後訓練的影響，但不是同一件事。
- 〔推論〕Park2023 只觀察到現象，並把它歸因於指令微調，沒有比較有無指令微調的模型，所以因果關係還沒有被驗證。
- Xie2024 的信任賽局中，GPT-4 大多數人物設定送出的金額高於人類平均的 $5.97，GPT-3.5-turbo-0613 則大多低於人類，而且是圖 2 比較的模型中信任最低的 [Xie2024, p.5]。
- 〔推論〕Xie2024 沒有討論指令微調；它的結果顯示，在有明確報酬的賽局中，GPT-3.5 系列不一定過度合作，Park2023 的觀察可能只適用於沒有報酬的日常互動，或和模型版本有關，詳見[矛盾總表](../syntheses/contradictions.md)。

## 相關頁面
- [生成式代理人 (Generative Agent)](generative-agent.md)
- [湧現的社會行為 (Emergent Social Behavior)](emergent-social-behavior.md)
- [指令微調讓代理人過度合作 (Instruction Tuning Makes Agents Too Cooperative)](../town/instruction-tuning-makes-agents-too-cooperative.md)
- [生成式代理人：人類行為的互動模擬 (Generative Agents: Interactive Simulacra of Human Behavior)](../papers/park2023.md)
- [大型語言模型代理人能模擬人類的信任行為嗎？ (Can Large Language Model Agents Simulate Human Trust Behavior?)](../papers/xie2024.md)
- [矛盾總表 (Contradictions)](../syntheses/contradictions.md)
- [大型語言模型作為模擬的經濟代理人：我們能從矽基人學到什麼？ (Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?)](../papers/horton2026.md)
- [矽基人 (Homo Silicus)](homo-silicus.md)
- [術語表 (Glossary)](../glossary.md)
