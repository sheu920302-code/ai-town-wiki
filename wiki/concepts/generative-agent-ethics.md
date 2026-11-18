---
title: 生成式代理人的倫理風險 (Ethical Risks of Generative Agents)
type: concept
summary: Park2023 列出四種風險：類社會關係 (parasocial relationship)、錯誤推論造成的傷害、深度偽造和量身說服等濫用，以及過度依賴代理人而取代真人；並提出揭露身分、價值對齊、保留稽核紀錄、不取代真人意見等原則。
sources: [Park2023]
related: [concepts/generative-agent.md, concepts/believability.md, papers/park2023.md, glossary.md]
tags: [ethics, generative-agents]
status: draft
has_inference: true
created: 2026-11-17
updated: 2026-11-17
---
# 生成式代理人的倫理風險 (Ethical Risks of Generative Agents)

## 白話摘要
Park2023 提醒，行為像真人的 AI 角色也帶來風險。第一，使用者可能對它們產生不適當的情感依附；第二，代理人推論錯誤時可能造成困擾甚至傷害；第三，它們可能讓深度偽造 (deepfake)、假訊息和量身打造的說服更容易；第四，開發者或設計者可能過度依賴 (over-reliance) 代理人，取代真人的角色。作者建議代理人要揭露自己是電腦程式、價值要對齊、平台要保留輸入和輸出的紀錄，而且絕不能取代真人。

## 定義
- Park2023 在倫理與社會影響一節中，列出生成式代理人 (generative agent) 的四種風險 [Park2023, p.18]。

> "One risk is people forming parasocial relationships with generative agents, even when such relationships may not be appropriate." [Park2023, p.18]
> 中譯：其中一個風險是，人們可能和生成式代理人建立類社會關係，即使這種關係並不恰當。

## 各論文的觀點

### Park2023

#### 類社會關係 (parasocial relationship)
- 即使知道生成式代理人是電腦程式，使用者仍可能把它們擬人化 (anthropomorphize)，或對它們投入人類的情感 [Park2023, p.18]。
- 作者提出兩個原則：代理人應明確揭露自己是電腦程式；開發者要確保代理人的價值對齊 (value alignment)，例如不回應愛的告白 [Park2023, p.18]。

#### 錯誤的影響
- 如果應用程式根據代理人的預測錯誤推論使用者的目標，輕則造成困擾，重則造成傷害 [Park2023, p.18]。
- 作者把代理人放在互動式電子遊戲環境中，以降低這類傷害的可能 [Park2023, p.18]。

#### 濫用
- 生成式代理人可能加劇深度偽造 (deepfake)、假訊息和量身說服等風險 [Park2023, p.18]。
- 作者建議平台保留輸入和輸出的稽核紀錄，以便偵測和介入惡意使用 [Park2023, p.18]。
- 作者自己打造這套架構花了大約一年，這個門檻可能讓部分有心人卻步 [Park2023, p.18]。

#### 過度依賴
- 第四種風險是過度依賴：開發者或設計者可能用生成式代理人取代人類和系統利害關係人在設計流程中的角色 [Park2023, p.18]。
- 作者建議，在研究和設計流程中，生成式代理人絕不應取代真實人類的意見 [Park2023, p.18]。
- 作者認為，代理人適合用在設計早期難以找到參與者、或理論很難或很危險用真人測試的情況 [Park2023, p.18]。

#### 偏誤（出自論文的限制一節，不在上述四種風險之內）
- 語言模型已知的偏誤可能讓代理人出現偏頗的行為或刻板印象 [Park2023, p.17]。
- 由於資料有限，代理人可能難以為部分族群，特別是邊緣化族群，產生可信的行為 [Park2023, p.18]。

## 爭議與未解問題
- 〔推論〕北大小鎮是模擬研究，不直接和使用者互動，類社會關係的風險較低；但代理人模擬臺北大學學生時，仍可能出現刻板印象，報告時應說明代理人不代表真實學生。
- 〔推論〕依「不取代真人意見」的原則，小鎮的結果應定位為假設的初步測試，不是對真人行為的結論。

## 相關頁面
- [生成式代理人 (Generative Agent)](generative-agent.md)
- [可信度 (Believability)](believability.md)
- [生成式代理人：人類行為的互動模擬 (Generative Agents: Interactive Simulacra of Human Behavior)](../papers/park2023.md)
- [術語表 (Glossary)](../glossary.md)
