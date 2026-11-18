---
title: 規劃 (Planning)
type: concept
summary: 代理人由上而下把一天的大致行程逐層拆成細部行動，存進記憶流；每個時間步再依觀察決定照原計畫進行或做出反應，需要互動時生成對話。
sources: [Park2023]
related: [concepts/generative-agent.md, concepts/memory-stream.md, concepts/reflection.md, papers/park2023.md, concepts/reacting-and-dialogue.md, glossary.md]
tags: [planning, generative-agents]
status: draft
has_inference: false
created: 2026-11-17
updated: 2026-11-17
---
# 規劃 (Planning)

## 白話摘要
如果每次只問語言模型「這個角色現在該做什麼」，它可能讓角色 12 點吃午餐、12 點半又吃一次、1 點再吃一次。規劃 (planning) 解決這個問題：代理人先排出一天的大致行程，再一層層拆成每小時、每 5 到 15 分鐘的行動，並把計畫存進記憶。遇到新狀況時，代理人會判斷要照原計畫進行還是做出反應；要和別人互動時，再根據彼此的記憶生成對話。

## 定義
- 計畫描述代理人未來的一連串行動，內容包括地點、開始時間和持續時間 [Park2023, p.11]。
- 計畫和反思 (reflection) 一樣存放在記憶流 (memory stream) 中，也會在檢索 (retrieval) 時被取出 [Park2023, p.11]。

> "Plans describe a future sequence of actions for the agent, and help keep the agent’s behavior consistent over time." [Park2023, p.11]
> 中譯：計畫描述代理人未來的一連串行動，幫助代理人的行為在一段時間內保持一致。

## 各論文的觀點

### Park2023

#### 為什麼需要規劃
- 只依當下情境產生行為時，Klaus 會在 12 點、12 點半和 1 點各吃一次午餐 [Park2023, p.10–11]。
- 作者指出，只追求當下的可信度 (believability)，會犧牲長時間的可信度 [Park2023, p.11]。

#### 由上而下拆解
- 第一步是根據代理人的摘要描述和前一天的摘要，產生一天的大致行程 [Park2023, p.11]。
- 大致行程分成五到八段 [Park2023, p.11]。
- 接著把行程拆成以小時為單位的行動，再拆成 5 到 15 分鐘的行動 [Park2023, p.11]。
- 代理人只事先產生高層計畫，近期的細部行動則在需要時才拆解 [Park2023, p.21]。

#### 反應與對話
- 代理人在每個時間步感知周遭，把觀察 (observation) 存進記憶流，再由語言模型判斷要繼續原計畫還是做出反應 [Park2023, p.11]。
- 決定反應時，系統從反應的時間點開始重新產生計畫 [Park2023, p.11]。
- 對話依雙方對彼此的記憶生成，一直持續到其中一方決定結束 [Park2023, p.11–12]。

## 爭議與未解問題
- 作者提到，代理人可能不知道某些地點的規範，例如宿舍浴室只能一人使用、商店約下午 5 點打烊，因而做出不合理的行動 [Park2023, p.17]。
- 作者認為，把這些規範寫進地點的狀態，例如把浴室描述成「單人浴室」，可能就能解決 [Park2023, p.17]。

## 相關頁面
- [生成式代理人 (Generative Agent)](generative-agent.md)
- [記憶流 (Memory Stream)](memory-stream.md)
- [反思 (Reflection)](reflection.md)
- [生成式代理人：人類行為的互動模擬 (Generative Agents: Interactive Simulacra of Human Behavior)](../papers/park2023.md)
- [反應與對話 (Reacting and Dialogue)](reacting-and-dialogue.md)
- [術語表 (Glossary)](../glossary.md)
