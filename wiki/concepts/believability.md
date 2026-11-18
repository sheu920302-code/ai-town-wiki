---
title: 可信度 (Believability)
type: concept
summary: 代理人的行為讓人覺得像真人、像是自己在做決定的程度；Park2023 把它當作設計目標和評估的依變數，由人類評分者依可信度排序。
sources: [Park2023, Xie2024, Horton2026]
related: [concepts/generative-agent.md, concepts/evaluation-and-ablation.md, papers/park2023.md, concepts/behavioral-alignment.md, papers/xie2024.md, concepts/ai-simulation-validity.md, papers/horton2026.md, glossary.md]
tags: [believability, evaluation, generative-agents]
status: draft
has_inference: true
created: 2026-11-17
updated: 2026-11-18
---
# 可信度 (Believability)

## 白話摘要
可信度 (believability) 指的是代理人的行為讓人覺得像真人、像是自己在做決定的程度，就像迪士尼動畫角色看起來有生命一樣。過去的研究把它當作打造代理人的核心目標，Park2023 也用它當評估標準：請人類評分者比較不同版本代理人的回答，排出哪個最可信。作者也提醒，可信不代表代理人有真正的能動性 (agency)。

## 定義
- 過去的文獻把可信度，也就是可信的代理人，描述為核心的設計和工程目標 [Park2023, p.3]。
- 可信的代理人要營造生命的錯覺，看起來像是依自己的意志做決定和行動，類似迪士尼電影的角色 [Park2023, p.3]。
- Park2023 受控評估的依變數就是行為的可信度 [Park2023, p.13]。

> "Prior literature has described believability, or believable agents, as a central design and engineering goal." [Park2023, p.3]
> 中譯：過去的文獻把可信度，也就是可信的代理人，描述為核心的設計和工程目標。

## 各論文的觀點

### Park2023

#### 怎麼衡量
- 100 位人類評分者比較同一代理人在不同條件下的訪談回答，依可信度由高到低排序 [Park2023, p.13]。
- 評分者先觀看隨機選出的一位代理人在 Smallville 生活的重播，並可以看到它記憶流 (memory stream) 中的所有資訊 [Park2023, p.13]。
- 完整架構產生的行為最可信，每拿掉一個元件可信度就下降，詳細數字見論文頁 [Park2023, p.14]。
- 作者也表示，人類群眾外包工作者 (crowdworker) 的條件不代表人類在可信度上的最佳表現 [Park2023, p.17]。

#### 當下的可信度和長期的可信度
- 作者指出，只追求當下的可信度會犧牲長期的可信度，例如沒有規劃的 Klaus 會連吃好幾次午餐 [Park2023, p.10–11]。
- 記憶越來越多時，有些代理人選擇較不典型的行動地點，行為可能隨時間變得較不可信 [Park2023, p.16]。

#### 可信不等於有能動性
- 作者說明，代理人的行為像迪士尼動畫角色一樣目的是營造可信的感覺，但不表示它們有真正的能動性 (agency) [Park2023, p.2]。

## 爭議與未解問題
- 〔推論〕可信度是人類評分者覺得像不像，不是代理人的選擇和真人實驗結果是否一致；要拿代理人代替人類玩信任或合作賽局，還需要比較行為本身。
- Xie2024 提出行為一致性 (behavioral alignment)，直接比較代理人和人類在影響行為的因素和行為動態上是否相似 [Xie2024, p.5]。
- 〔推論〕行為一致性比較的是代理人的選擇和人類實驗結果，可以補足可信度只看「像不像」的不足，詳見[行為一致性](behavioral-alignment.md)。
- Horton2026 拿 LLM 代理人重現 5 個經濟實驗，和原本的人類結果比較，並強調 AI 實驗的結果仍需要實證確認 [Horton2026, p.5; Horton2026, p.6]。
- 〔推論〕Xie2024 和 Horton2026 都拿既有的人類實驗結果當基準，評估的是行為本身；Park2023 的可信度則是請人判斷像不像，兩種評估可以互補，詳見[AI 模擬的效度](ai-simulation-validity.md)。

## 相關頁面
- [生成式代理人 (Generative Agent)](generative-agent.md)
- [受控評估與消融 (Controlled Evaluation and Ablation)](evaluation-and-ablation.md)
- [生成式代理人：人類行為的互動模擬 (Generative Agents: Interactive Simulacra of Human Behavior)](../papers/park2023.md)
- [行為一致性 (Behavioral Alignment)](behavioral-alignment.md)
- [大型語言模型代理人能模擬人類的信任行為嗎？ (Can Large Language Model Agents Simulate Human Trust Behavior?)](../papers/xie2024.md)
- [AI 模擬的效度 (Validity of AI Simulations)](ai-simulation-validity.md)
- [大型語言模型作為模擬的經濟代理人：我們能從矽基人學到什麼？ (Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?)](../papers/horton2026.md)
- [術語表 (Glossary)](../glossary.md)
