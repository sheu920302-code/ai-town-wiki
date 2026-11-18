---
title: 記憶流 (Memory Stream)
type: concept
summary: 用自然語言完整記錄代理人所有經歷的資料庫；需要時依新近性、重要性、相關性三項分數取出最相關的記憶，再交給語言模型。
sources: [Park2023]
related: [concepts/generative-agent.md, concepts/reflection.md, concepts/planning.md, concepts/individual-recognition.md, papers/park2023.md, concepts/retrieval.md, concepts/hallucination.md, glossary.md]
tags: [memory, retrieval, generative-agents]
status: draft
has_inference: true
created: 2026-11-17
updated: 2026-11-17
---
# 記憶流 (Memory Stream)

## 白話摘要
記憶流 (memory stream) 像是代理人的日記，把它看到、做過的事都用自然語言記下來。記憶太多、塞不進語言模型時，系統會替每筆記憶打三個分數：最近有沒有用到（新近性 (recency)）、這件事重不重要（重要性 (importance)）、跟現在的情境有沒有關係（相關性 (relevance)），把分數最高的幾筆交給語言模型參考。拿掉記憶的代理人，連認識的人都說不認得；但有記憶的代理人有時也會想不起來，或替記憶加油添醋 (embellishment)。

## 定義
- 記憶流是記錄代理人經歷的資料庫，每個記憶物件包含自然語言描述、建立時間和最近一次被存取的時間 [Park2023, p.8]。
- 記憶流最基本的元素是觀察 (observation)，也就是代理人直接感知到的事件 [Park2023, p.8]。
- 檢索 (retrieval) 函數以代理人目前的情境為輸入，從記憶流中挑出一部分交給語言模型 [Park2023, p.8]。

> "The memory stream maintains a comprehensive record of the agent’s experience." [Park2023, p.8]
> 中譯：記憶流完整記錄代理人的經歷。

## 各論文的觀點

### Park2023

#### 為什麼需要檢索
- 完整的記憶流會讓模型分心，也放不進有限的上下文視窗 (context window) [Park2023, p.8]。
- 把 Isabella 的所有經歷硬濃縮成摘要時，她的回答變得空泛；改用檢索相關記憶後，回答變得更具體 [Park2023, p.8]。

#### 檢索分數的三個部分
- 新近性 (recency)：最近被存取的記憶分數較高，以遊戲時數做指數衰減，衰減係數是 0.995 [Park2023, p.9]。
- 重要性 (importance)：直接請語言模型在 1 到 10 分之間評分，例如打掃房間得 2 分、約暗戀對象出去得 8 分 [Park2023, p.9]。
- 重要性分數在記憶建立時就產生 [Park2023, p.9]。
- 相關性 (relevance)：用語言模型產生每筆記憶的嵌入向量 (embedding vector)，計算它和查詢的餘弦相似度 (cosine similarity) [Park2023, p.9]。
- 三項分數都用最小最大縮放 (min-max scaling) 正規化到 0 到 1，再加權相加；作者的實作中三個權重都是 1 [Park2023, p.9]。
- 分數最高、而且放得進上下文視窗的記憶，會放進提示裡 [Park2023, p.9]。

#### 記憶的效果和錯誤
- 沒有觀察記憶的 Abigail 說不認識 Rajiv；有記憶時，她能想起並描述 Rajiv [Park2023, p.15]。
- 代理人可能取不到正確的記憶，例如 Rajiv 聽說過 Sam 參選，卻說自己沒怎麼關注選舉 [Park2023, p.15]。
- 代理人也會替記憶加油添醋 (embellishment)，例如 Isabella 說 Sam 明天會宣布，但兩人從沒談過這件事 [Park2023, p.15]。
- 作者觀察到，代理人很少完全捏造經歷，但仍會在已知的事上加油添醋 [Park2023, p.15]。
- 語言模型本身的世界知識也會滲入，例如 Yuriko 說鄰居 Adam Smith 寫了《國富論》[Park2023, p.15]。
- 記憶越來越多時，不只檢索變難，代理人選擇行動地點也變得較不典型，例如有些代理人改去酒吧吃午餐 [Park2023, p.16]。

## 爭議與未解問題
- 作者認為，調整新近性、重要性和相關性函數，可能讓檢索取到更相關的資訊 [Park2023, p.17]。
- 作者提到代理人可能受到記憶攻擊 (memory hacking)：精心設計的對話可能讓代理人相信一件從沒發生過的事 [Park2023, p.17]。
- 〔推論〕記憶流讓代理人能記得「誰對我做過什麼」，這是互惠 (reciprocity) 需要的條件之一；但 Park2023 本身沒有測試賽局中的記憶。

## 相關頁面
- [生成式代理人 (Generative Agent)](generative-agent.md)
- [反思 (Reflection)](reflection.md)
- [規劃 (Planning)](planning.md)
- [個體辨識 (Individual Recognition)](individual-recognition.md)
- [生成式代理人：人類行為的互動模擬 (Generative Agents: Interactive Simulacra of Human Behavior)](../papers/park2023.md)
- [檢索 (Retrieval)](retrieval.md)
- [幻覺 (Hallucination)](hallucination.md)
- [術語表 (Glossary)](../glossary.md)
