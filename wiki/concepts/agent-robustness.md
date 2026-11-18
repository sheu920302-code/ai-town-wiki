---
title: 代理人的穩健性 (Robustness of Generative Agents)
type: concept
summary: Park2023 表示生成式代理人的穩健性大致仍未知；作者列出的弱點包括提示攻擊、記憶攻擊和幻覺，而且代理人會繼承語言模型的缺陷。
sources: [Park2023, Axelrod1981]
related: [concepts/hallucination.md, concepts/memory-stream.md, concepts/generative-agent-ethics.md, town/auditable-transaction-log.md, papers/park2023.md, glossary.md]
tags: [robustness, security, generative-agents]
status: draft
has_inference: true
created: 2026-11-17
updated: 2026-11-17
---
# 代理人的穩健性 (Robustness of Generative Agents)

## 白話摘要
Park2023 坦白說，代理人的穩健性 (robustness of generative agents) 大致還不清楚。作者列出的弱點包括：代理人可能受到提示攻擊 (prompt hacking)；可能受到記憶攻擊 (memory hacking)，也就是被精心設計的對話說服，相信一件從沒發生過的事；也可能產生幻覺 (hallucination)。語言模型的缺陷也會被代理人繼承。

## 定義
- Park2023 表示，生成式代理人 (generative agent) 的穩健性大致仍未知 [Park2023, p.17]。

> "Lastly, the robustness of generative agents is still largely unknown." [Park2023, p.17]
> 中譯：最後，生成式代理人的穩健性大致仍未知。

- Axelrod1981 的穩健性 (robustness) 指的是策略在各種策略混雜的環境中表現良好的能力 [Axelrod1981, p.5]。
- 〔推論〕這和 Park2023 所說的代理人穩健性是不同的概念，本 wiki 分開收錄。

## 各論文的觀點

### Park2023

#### 可能的弱點
- 代理人可能受到提示攻擊、記憶攻擊和幻覺 (hallucination) 影響 [Park2023, p.17]。
- 記憶攻擊是指精心設計的對話，可能讓代理人相信一件從沒發生過的事 [Park2023, p.17]。
- 語言模型的任何缺陷都會被生成式代理人 (generative agent) 繼承 [Park2023, p.17]。

#### 原文中可能相關的現象
- 〔推論〕下面這點是 wiki 自己和穩健性連結的現象，原文沒有把它放在穩健性的討論中。
- 使用者以「內心聲音」(inner voice) 的身分說話時，代理人比較可能把這句話當成指令 [Park2023, p.6]。

#### 作者的建議
- 作者建議未來研究全面測試這些穩健性問題 [Park2023, p.17]。
- 作者認為，隨著語言模型更能抵抗這類攻擊，生成式代理人也可以採用類似的防護 [Park2023, p.17]。
- 在倫理風險一節中，作者針對深度偽造、假訊息等濫用風險，建議平台保留輸入和輸出的稽核紀錄 (audit log)，以便偵測、驗證和介入惡意使用 [Park2023, p.18]。

## 爭議與未解問題
- 〔推論〕在北大小鎮的借錢遊戲中，想賴帳的代理人可能在對話中堅稱「我已經還過了」，這和記憶攻擊的情境很像；代理人如果只靠自己的記憶，可能被說服。

## 相關頁面
- [幻覺 (Hallucination)](hallucination.md)
- [記憶流 (Memory Stream)](memory-stream.md)
- [生成式代理人的倫理風險 (Ethical Risks of Generative Agents)](generative-agent-ethics.md)
- [保留可查核的交易紀錄 (Auditable Transaction Log)](../town/auditable-transaction-log.md)
- [生成式代理人：人類行為的互動模擬 (Generative Agents: Interactive Simulacra of Human Behavior)](../papers/park2023.md)
- [術語表 (Glossary)](../glossary.md)
