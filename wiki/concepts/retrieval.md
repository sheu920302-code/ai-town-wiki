---
title: 檢索 (Retrieval)
type: concept
summary: 依代理人目前的情境，從記憶流中挑出最相關的一部分記憶交給語言模型；Park2023 用新近性、重要性、相關性三項分數加總排序，取放得進上下文視窗的最高分記憶。
sources: [Park2023]
related: [concepts/memory-stream.md, concepts/reflection.md, concepts/planning.md, concepts/hallucination.md, papers/park2023.md, concepts/reacting-and-dialogue.md, glossary.md]
tags: [retrieval, memory, generative-agents]
status: draft
has_inference: true
created: 2026-11-17
updated: 2026-11-17
---
# 檢索 (Retrieval)

## 白話摘要
代理人的記憶流 (memory stream) 越來越長，不可能每次都整份交給語言模型。檢索 (retrieval) 就是「挑重點」：根據代理人現在的情境，替每筆記憶打三個分數，包括最近有沒有用到（新近性 (recency)）、重不重要（重要性 (importance)）、和現在的情境相不相關（相關性 (relevance)），三項相加後取最高分的幾筆。反思 (reflection) 和決定要不要對觀察做出反應時，也靠檢索取得需要的記憶；檢索失敗時，代理人就會想不起來或只想起一半。

## 定義
- 檢索函數以代理人目前的情境為輸入，從記憶流中挑出一部分交給語言模型 [Park2023, p.8]。
- 檢索分數是新近性、重要性和相關性三項的加權總和 [Park2023, p.9]。

> "Our architecture implements a retrieval function that takes the agent’s current situation as input and returns a subset of the memory stream to pass on to the language model." [Park2023, p.8]
> 中譯：我們的架構實作了一個檢索函數，以代理人目前的情境為輸入，回傳記憶流的一部分交給語言模型。

## 各論文的觀點

### Park2023

#### 為什麼需要檢索
- 完整的記憶流會讓模型分心，而且放不進有限的上下文視窗 (context window) [Park2023, p.8]。
- 作者指出，檢索函數有很多可能的實作方式，取決於代理人在決定行動時需要考慮什麼 [Park2023, p.8]。

#### 三項分數
- 新近性：以上次被取用後經過的遊戲時數做指數衰減，衰減係數是 0.995 [Park2023, p.9]。
- 重要性：記憶建立時，請語言模型在 1 到 10 分之間評分 [Park2023, p.9]。
- 相關性取決於查詢：例如學生和同學討論化學考試時，關於早餐的記憶相關性低，關於老師和課業的記憶相關性高 [Park2023, p.9]。
- 相關性以記憶的嵌入向量 (embedding vector) 和查詢的嵌入向量之間的餘弦相似度 (cosine similarity) 計算 [Park2023, p.9]。
- 三項分數都正規化到 0 到 1，作者的實作中三個權重都設為 1 [Park2023, p.9]。
- 分數最高、而且放得進上下文視窗的記憶，會放進提示裡 [Park2023, p.9]。

#### 其他元件怎麼使用檢索
- 計畫和反思一樣存入記憶流，也會被檢索取出，讓代理人決定行為時能一併考慮觀察、反思和規劃 (planning) 的內容 [Park2023, p.11]。
- 反思時，代理人先提出問題，再把這些問題當作查詢去檢索相關記憶 [Park2023, p.10]。
- 決定是否對觀察做出反應時，系統用兩個查詢檢索記憶，例如「觀察者和被觀察者的關係」，再把結果摘要成情境 [Park2023, p.11]。

#### 檢索失敗
- 代理人可能取不到正確的記憶，例如 Rajiv 聽說過 Sam 參選，卻說自己沒怎麼關注選舉 [Park2023, p.15]。
- 代理人也可能只取到不完整的記憶片段：Tom 記得要在派對上和 Isabella 談選舉，卻不確定派對是否真的存在 [Park2023, p.15]。

## 爭議與未解問題
- 作者認為，微調新近性、重要性和相關性三個函數，可能讓檢索取到更相關的資訊 [Park2023, p.17]。
- 〔推論〕三個權重都設為 1 是作者的實作選擇，原文沒有比較其他權重的效果。
- 〔推論〕如果小鎮代理人要依過去的借貸紀錄決定是否借錢，「被欠錢」這類記憶的重要性分數和檢索方式，可能直接影響代理人會不會記得誰沒還錢。

## 相關頁面
- [記憶流 (Memory Stream)](memory-stream.md)
- [反思 (Reflection)](reflection.md)
- [規劃 (Planning)](planning.md)
- [幻覺 (Hallucination)](hallucination.md)
- [生成式代理人：人類行為的互動模擬 (Generative Agents: Interactive Simulacra of Human Behavior)](../papers/park2023.md)
- [反應與對話 (Reacting and Dialogue)](reacting-and-dialogue.md)
- [術語表 (Glossary)](../glossary.md)
