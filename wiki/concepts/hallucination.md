---
title: 幻覺 (Hallucination)
type: concept
summary: Park2023 所說的幻覺主要是加油添醋：代理人很少完全捏造，也沒有主動宣稱經歷過沒發生的事；錯誤還包括取不到記憶、只取到片段，或在已知的事上加入沒發生的細節，語言模型本身的世界知識也會滲入。
sources: [Park2023]
related: [concepts/memory-stream.md, concepts/retrieval.md, concepts/emergent-social-behavior.md, papers/park2023.md, concepts/agent-robustness.md, town/auditable-transaction-log.md, glossary.md]
tags: [hallucination, memory, errors, generative-agents]
status: draft
has_inference: true
created: 2026-11-17
updated: 2026-11-17
---
# 幻覺 (Hallucination)

## 白話摘要
Park2023 所說的幻覺 (hallucination)，主要是加油添醋 (embellishment)：代理人在知道的事上多說一些沒發生過的細節。代理人很少完全憑空捏造，也沒有主動宣稱自己經歷過沒發生的事；語言模型本身的知識也可能混進來。另外，代理人有時想不起來，或只想起一半。

## 定義
- Park2023 把代理人替自己的知識加上沒有發生過的細節，稱為幻覺式的加油添醋 [Park2023, p.15]。

> "At times, the agents hallucinated embellishments to their knowledge." [Park2023, p.15]
> 中譯：有時代理人會對自己的知識產生幻覺式的加油添醋。

## 各論文的觀點

### Park2023

#### 錯誤的類型
- 技術評估和端到端評估 (end-to-end evaluation) 中最常見的錯誤，是代理人沒有取回相關記憶、替記憶加油添醋，以及沿用語言模型過於正式的說話或行為 [Park2023, p.3]。
- 代理人很少完全捏造知識，它們可能想不起某件事，並承認自己不記得 [Park2023, p.15]。
- 代理人沒有主動宣稱自己經歷過沒發生的事 [Park2023, p.15]。
- 加油添醋的例子：Isabella 知道 Sam 參選，卻多說 Sam 明天會發表聲明，但兩人從沒談過這件事 [Park2023, p.15]。
- 語言模型的世界知識也會滲入：Yuriko 說鄰居 Adam Smith 寫了《國富論》，那其實是 18 世紀同名經濟學家的著作 [Park2023, p.15]。
- 代理人也會只取到不完整的記憶片段，例如 Tom 記得要在派對上談選舉，卻不確定派對是否存在 [Park2023, p.15]。

#### 怎麼確認不是幻覺
- 在資訊擴散 (information diffusion) 的測量中，作者到記憶流 (memory stream) 中找出提供資訊的那段對話，確認回答不是幻覺 [Park2023, p.15]。
- 宣稱知道參選或派對消息的代理人，沒有一位是出於幻覺 [Park2023, p.16]。
- 453 個關於是否認識其他代理人的回答中，有 1.3%（n = 6）是幻覺 [Park2023, p.16]。

## 爭議與未解問題
- 作者提到代理人可能受到記憶攻擊 (memory hacking)：精心設計的對話可能讓代理人相信一件從沒發生過的事 [Park2023, p.17]。
- 作者認為，語言模型的缺陷都會被生成式代理人 (generative agent) 繼承 [Park2023, p.17]。
- 〔推論〕在借錢遊戲中，如果代理人把「誰欠我錢」記錯或加油添醋，可能誤判對方是否守信，所以小鎮需要保留可以查核的原始交易紀錄。

## 相關頁面
- [記憶流 (Memory Stream)](memory-stream.md)
- [檢索 (Retrieval)](retrieval.md)
- [湧現的社會行為 (Emergent Social Behavior)](emergent-social-behavior.md)
- [生成式代理人：人類行為的互動模擬 (Generative Agents: Interactive Simulacra of Human Behavior)](../papers/park2023.md)
- [代理人的穩健性 (Robustness of Generative Agents)](agent-robustness.md)
- [保留可查核的交易紀錄 (Auditable Transaction Log)](../town/auditable-transaction-log.md)
- [術語表 (Glossary)](../glossary.md)
