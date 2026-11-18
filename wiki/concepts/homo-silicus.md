---
title: 矽基人 (Homo Silicus)
type: concept
summary: Horton2026 對大型語言模型的比喻：它是人類的隱性計算模型，可以像經濟人一樣給予設定、放進情境觀察行為；作者認為它最好理解成可以靈活執行的理論，適合試跑實驗和探索新情境、產生假說，但結果仍需要真人資料確認。
sources: [Horton2026]
related: [papers/horton2026.md, concepts/theory-grounded-personas.md, concepts/ai-simulation-validity.md, concepts/generative-agent.md, concepts/behavioral-alignment.md, glossary.md]
tags: [homo-silicus, llm-agents, simulation, economics]
status: draft
has_inference: true
created: 2026-11-18
updated: 2026-11-18
---
# 矽基人 (Homo Silicus)

## 白話摘要
經濟學家常用一個理想化的「經濟人」來推導人會怎麼做。Horton2026 認為，大型語言模型也可以當成一種人類模型，叫矽基人 (Homo silicus)：給它稟賦，放進情境，用模擬看它怎麼選。它之所以能模仿人，是因為訓練資料裡同時有社會科學研究和大量一般人的文字。作者認為，矽基人比較像「可以執行的理論」，而不是實證資料：很適合用來低成本試跑實驗、產生假說，但結果仍需要真人資料確認。

## 定義
- Horton2026 主張，大型語言模型 (large language model) 因為訓練和設計的方式，可以視為人類的隱性計算模型，稱為矽基人 [Horton2026, p.2]。
- 矽基人可以像經濟學家使用經濟人 (Homo economicus) 一樣，給予稟賦、放進情境，再透過計算模擬而不是數學推導來觀察行為 [Horton2026, p.2]。

- 作者把主要概念貢獻概括為：矽基人最好理解成可以靈活執行的理論 [Horton2026, p.40]。

## 各論文的觀點

### Horton2026

#### 為什麼 LLM 能模擬人
- 作者認為核心原因有兩個：LLM 被設計成像人一樣回應提示，而且擁有大量社會資訊 [Horton2026, p.2]。
- LLM 透過兩條路徑取得社會資訊：明確地記住社會科學文獻的發現和理論，以及隱含地從新聞、社群媒體、書籍等文字中學到人類的實際行為 [Horton2026, p.24]。
- 後訓練 (post-training) 方法，例如指令微調 (instruction tuning) 和人類回饋強化學習 (reinforcement learning with human feedback)，會把模型導向合作、聽從指令的行為，作者利用這個特性來替代理人設定角色和偏好 [Horton2026, p.26]。

#### 比較像理論，不像實證
- 作者認為，LLM 實驗表面上像實證研究，實際上比較接近經濟理論的研究方式 [Horton2026, p.6; Horton2026, p.26]。
- 和傳統的經濟模型或機器學習模型不同，只要改寫提示裡的情境描述，LLM 就能在結構不同的新情境中做出預測 [Horton2026, p.28]。
- 作者建議把假設寫成明確的指令，例如「你只在乎效率」，讓模型在新情境中照著執行，也方便檢查它有沒有照做 [Horton2026, p.29]。

#### 用途
- 最明顯的用途是先在電腦中試跑實驗：探索參數範圍、測試題目措辭的影響、估算檢定力 [Horton2026, p.5]。
- 論文中的實驗只花幾分鐘、極少的費用就跑完 [Horton2026, p.5]。
- 在沒有既有資料的新情境中，研究目的通常不是無偏推論，而是探索和產生假說，所需的證據門檻低得多 [Horton2026, p.32]。
- 作者表示，最終關心的是真實人類的行為，所以 AI 實驗的結果仍需要實證確認 [Horton2026, p.5]。

## 爭議與未解問題
- 作者承認 LLM 是黑盒子，目前不知道為什麼某個提示能改善擬合，所以「提示有效就代表理論對人類成立」的推論還太強 [Horton2026, p.30]。
- 〔推論〕Park2023 的生成式代理人 (generative agent) 著重在長期記憶和日常行為的可信度，Horton2026 的矽基人著重在經濟決策和理論檢驗；兩者都把 LLM 當作人類的替身，但評估方式不同。

## 相關頁面
- [大型語言模型作為模擬的經濟代理人：我們能從矽基人學到什麼？ (Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?)](../papers/horton2026.md)
- [理論導向的人物設定 (Theory-Grounded Personas)](theory-grounded-personas.md)
- [AI 模擬的效度 (Validity of AI Simulations)](ai-simulation-validity.md)
- [生成式代理人 (Generative Agent)](generative-agent.md)
- [行為一致性 (Behavioral Alignment)](behavioral-alignment.md)
- [術語表 (Glossary)](../glossary.md)
