---
title: 指令微調讓代理人過度合作 (Instruction Tuning Makes Agents Too Cooperative)
type: town
summary: Park2023 觀察到，指令微調似乎讓代理人更客氣、彼此過度合作；例如 Isabella 很少拒絕和自己興趣不合的點子，時間久了，自己的興趣也被別人改變。
sources: [Park2023, Xie2024]
related: [papers/park2023.md, concepts/generative-agent.md, concepts/emergent-social-behavior.md, concepts/reciprocity.md, paradigms/trust-game.md, paradigms/prisoners-dilemma.md, concepts/instruction-tuning.md, papers/xie2024.md, concepts/agent-trust-properties.md]
tags: [town-design, cooperation, instruction-tuning, llm-agents]
status: draft
has_inference: true
created: 2026-11-17
updated: 2026-11-18
town_status: idea
---
# 指令微調讓代理人過度合作 (Instruction Tuning Makes Agents Too Cooperative)

## 白話摘要
Park2023 的代理人在小鎮中互動時，說話可能過於正式，彼此之間似乎也過度合作。例如 Isabella 籌辦派對時，收到各種和她自己興趣不合的點子，她卻很少拒絕；時間一久，別人的興趣甚至改變了她自己的興趣。作者推測這是指令微調 (instruction tuning) 造成的。

## 研究依據
- 作者觀察到指令微調 (instruction tuning) 可能的影響：整體而言，代理人的行為被引導得更客氣、更合作 [Park2023, p.17]。
- 作者也觀察到，指令微調似乎讓代理人彼此過度合作 [Park2023, p.17]。
- 代理人的對話可能過於正式，例如 Mei 和丈夫 John 說話時，常以正式的問候開頭 [Park2023, p.17]。
- Isabella 收到別人建議的派對點子，例如莎士比亞朗讀會或專業交流活動，雖然不符合她自己的興趣和個性，她卻很少拒絕 [Park2023, p.17]。
- 隨著時間過去，別人的興趣塑造了 Isabella 自己的興趣 [Park2023, p.17]。
- 作者在介紹代理人時就提到，對話風格過於正式，可能是底層模型指令微調的結果 [Park2023, p.5]。
- 實驗使用的模型是 gpt3.5-turbo [Park2023, p.8]。

## 設計點子
- 〔推論〕北大小鎮的借錢、合作、背叛遊戲，需要代理人在某些情況下拒絕或背叛 (Defect)；如果直接用預設的指令微調模型，代理人可能幾乎都選擇合作 (Cooperate)，賽局就失去意義。
- 〔推論〕可以在代理人的種子記憶或角色描述中，明確寫出自利的目標或底線，例如「這學期生活費很緊，借出去的錢一定要拿回來」，測試能否抵銷過度合作的傾向。
- 〔推論〕小鎮實驗可以先跑一個「基準版」，記錄代理人在沒有特別設定時的合作比例；如果合作比例遠高於 Berg1995 的人類數據，就代表需要調整。
- 〔推論〕可以比較不同模型或不同版本的代理人，看過度合作的程度是否不同，因為 Park2023 只用了一種模型。
- 〔推論〕Xie2024 發現叫代理人「不要信任對方」比叫它「要信任對方」更容易生效 [Xie2024, p.9]，在種子記憶或提示中寫入自利目標或謹慎的態度，可能也比較容易生效，值得測試；但 Xie2024 只測試了明確的指令。

## 風險與待驗證
- 〔推論〕Park2023 的觀察來自友善的日常情境，沒有直接測試賽局；代理人在有明確報酬的賽局中是否也過度合作，還需要其他論文的數據。
- Xie2024 的信任賽局中，GPT-3.5-turbo-0613 是圖 2 比較的模型中信任最低的，大多數人物設定送得比人類少；GPT-4 則大多送得比人類多 [Xie2024, p.5]。
- 〔推論〕所以「代理人過度合作」不一定適用於所有模型和情境；小鎮應先跑基準版，確認所選模型在借錢情境中到底偏大方還是偏小氣。
- 〔推論〕刻意讓代理人更自私時，可能矯枉過正，讓代理人比真人更不信任別人，也需要和人類基準數據比較。

## 相關頁面
- [生成式代理人：人類行為的互動模擬 (Generative Agents: Interactive Simulacra of Human Behavior)](../papers/park2023.md)
- [生成式代理人 (Generative Agent)](../concepts/generative-agent.md)
- [湧現的社會行為 (Emergent Social Behavior)](../concepts/emergent-social-behavior.md)
- [互惠 (Reciprocity)](../concepts/reciprocity.md)
- [信任賽局 (Trust Game)](../paradigms/trust-game.md)
- [囚犯困境 (Prisoner's Dilemma)](../paradigms/prisoners-dilemma.md)
- [指令微調 (Instruction Tuning)](../concepts/instruction-tuning.md)
- [大型語言模型代理人能模擬人類的信任行為嗎？ (Can Large Language Model Agents Simulate Human Trust Behavior?)](../papers/xie2024.md)
- [代理人信任的特性 (Properties of Agent Trust)](../concepts/agent-trust-properties.md)
