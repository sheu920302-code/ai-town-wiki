---
title: 反應與對話 (Reacting and Dialogue)
type: concept
summary: 生成式代理人在每個時間步感知周遭、決定照原計畫進行或做出反應；決定和其他代理人互動時，雙方各自依對彼此的記憶生成一句句對話，直到一方結束。
sources: [Park2023]
related: [concepts/planning.md, concepts/retrieval.md, concepts/memory-stream.md, concepts/instruction-tuning.md, papers/park2023.md, glossary.md]
tags: [reacting, dialogue, generative-agents]
status: draft
has_inference: true
created: 2026-11-17
updated: 2026-11-17
---
# 反應與對話 (Reacting and Dialogue)

## 白話摘要
生成式代理人 (generative agent) 會依周遭情況調整行動。每一個時間步，它都會看看周遭發生了什麼，把看到的事記進記憶流 (memory stream)，再決定要照原計畫做，還是對眼前的事做出反應。例如 John 看到 Eddy 在散步，就決定去問他作曲作業做得如何，並從這一刻起重新安排計畫。兩個代理人說話時，每一句都根據說話者對另一方的記憶產生，回話時再加上前面的對話內容，直到其中一方決定結束。

## 定義
- 代理人在一個行動迴圈中運作：每個時間步感知周遭，把觀察 (observation) 存進記憶流，再由語言模型判斷要繼續原計畫還是做出反應 [Park2023, p.11]。

> "Generative agents operate in an action loop where, at each time step, they perceive the world around them and those perceived observations are stored in their memory stream." [Park2023, p.11]
> 中譯：生成式代理人在一個行動迴圈中運作：每個時間步都感知周遭，並把感知到的觀察存進記憶流。

## 各論文的觀點

### Park2023

#### 決定要不要反應
- 站在畫架前畫畫時觀察到畫架，不太可能引起反應；但 John 看到 Eddy 在散步時，情況就不同 [Park2023, p.11]。
- 判斷時，系統先用兩個查詢檢索 (retrieval) 記憶：觀察者和被觀察者的關係，以及被觀察者正在做的事，再把結果摘要成情境 [Park2023, p.11]。
- 模型的輸出建議 John 可以問 Eddy 的作曲計畫，系統再從反應的時間點開始重新產生 John 的計畫 [Park2023, p.11]。
- 代理人知道自己附近有哪些其他代理人，由架構決定要擦身而過還是開始交談 [Park2023, p.5]。

#### 生成對話
- 如果決定的行動涉及代理人之間的互動，系統就生成雙方的對話 [Park2023, p.11]。
- 對話以說話者對另一方的記憶為條件生成 [Park2023, p.11]。
- John 開口後，Eddy 把 John 開啟對話這件事當作一個可能要反應的事件，檢索自己和 John 的關係，以及和 John 那句話相關的記憶 [Park2023, p.12]。
- Eddy 的回話以他摘要後的記憶和目前的對話紀錄生成 [Park2023, p.12]。
- 對話用同樣的機制一直延續，直到其中一方決定結束 [Park2023, p.12]。
- 作者提到，另一種可能的優化是把雙方的對話合併成一個提示一次生成，而不是兩方來回生成 [Park2023, p.21]。

#### 使用者的介入
- 使用者用「內心聲音」(inner voice) 的身分對代理人說話時，代理人比較可能把這句話當成指令 [Park2023, p.6]。
- 例如使用者以 John 內心聲音的身分告訴他要出來競選，John 就決定參選，並告訴妻子和兒子 [Park2023, p.6]。

## 爭議與未解問題
- 作者觀察到，代理人的對話可能過於正式，很可能是指令微調 (instruction tuning) 的結果 [Park2023, p.5]。
- 〔推論〕北大小鎮的借錢談判、催討還款都會透過這種對話機制進行，代理人對另一方的記憶是否正確，會直接影響它說什麼、借不借錢。

## 相關頁面
- [規劃 (Planning)](planning.md)
- [檢索 (Retrieval)](retrieval.md)
- [記憶流 (Memory Stream)](memory-stream.md)
- [指令微調 (Instruction Tuning)](instruction-tuning.md)
- [生成式代理人：人類行為的互動模擬 (Generative Agents: Interactive Simulacra of Human Behavior)](../papers/park2023.md)
- [術語表 (Glossary)](../glossary.md)
