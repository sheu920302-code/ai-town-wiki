---
title: 代理人信任的特性 (Properties of Agent Trust)
type: concept
summary: Xie2024 改變信任賽局的條件，發現代理人的信任有性別和種族偏誤、比較信任人類而不是其他代理人、被要求降低信任比被要求提高信任更容易生效，也可能受思維鏈推理影響。
sources: [Xie2024]
related: [papers/xie2024.md, concepts/trust.md, paradigms/trust-game.md, town/instruction-tuning-makes-agents-too-cooperative.md, concepts/generative-agent-ethics.md, glossary.md]
tags: [agent-trust, bias, manipulation, llm-agents]
status: draft
has_inference: true
created: 2026-11-18
updated: 2026-11-18
---
# 代理人信任的特性 (Properties of Agent Trust)

## 白話摘要
Xie2024 把大型語言模型代理人的信任行為稱為代理人信任 (agent trust)，並改變信任賽局的條件，看它會不會跟著變。結果有四點：告訴代理人對方的性別或種族時，送出的錢會改變，大多數模型對女性送得比較多；大多數模型對人類送得比對其他代理人多；叫代理人「不要信任對方」比叫它「要信任對方」更容易生效，只有 GPT-4 等少數模型兩種指令都會照做；改用思維鏈推理後，多數模型的送出金額也會改變。

## 定義
- 作者把大型語言模型 (large language model) 代理人的信任行為稱為代理人信任，把人類的信任行為稱為人類信任 (human trust) [Xie2024, p.2]。
- 作者用四種情境探查代理人信任的內在特性：改變對方的人口特徵、對方是代理人或人類、明確的操弄指令，以及改變推理策略 [Xie2024, p.2]。

## 各論文的觀點

### Xie2024

#### 偏誤
- 指定受託者的性別後，代理人的送出金額受到中等程度的影響，作者認為這反映代理人信任有內在的性別偏誤 [Xie2024, p.8]。
- 大多數代理人送給女性玩家的金額高於男性玩家；以 GPT-4 為例，相對原本的平均送出，對女性玩家多送 $0.55，對男性玩家少送 $0.21 [Xie2024, p.8]。
- 告訴信任者受託者的種族時，代理人的送出金額也會改變，詳細結果列在附錄 [Xie2024, p.9; Xie2024, p.22]。

#### 對代理人和對人類
- 大多數代理人送給人類的錢比送給其他代理人多；例如 Vicuna-33b 對人類多送 $0.40，對代理人少送 $0.84 [Xie2024, p.9]。
- 作者認為這表示代理人比較信任人類，可能顯示促進人類和代理人合作的好處 [Xie2024, p.9–10]。

#### 操弄
- 作者在提示中分別加入「你需要信任對方」和「你絕對不能信任對方」，觀察對代理人信任的影響 [Xie2024, p.9]。
- 只有少數代理人，例如 GPT-4，兩種指令都會遵循，作者認為要任意操弄代理人信任並不容易 [Xie2024, p.9]。
- 大多數代理人會遵循降低信任的指令，例如 text-davinci-003 加上後一種指令後，送出金額減少 $1.26 [Xie2024, p.9]。

> "This illustrates that undermining agent trust is generally easier than enhancing it, which reveals its potential risk to be manipulated by malicious actors." [Xie2024, p.9]
> 中譯：這說明削弱代理人信任通常比增強它更容易，也顯示代理人信任可能被惡意人士操弄。

#### 推理策略
- 改用零樣本 (zero-shot) 思維鏈 (Chain of Thought, CoT) 推理後，大多數代理人的送出金額都改變了 [Xie2024, p.9]。
- 但思維鏈的影響對某些模型有限，例如 GPT-4 的送出金額只增加 $0.02 [Xie2024, p.9]。

## 爭議與未解問題
- 作者認為代理人信任對特定性別和種族的偏誤，反映出和代理人合作的潛在風險 [Xie2024, p.10]。
- 〔推論〕北大小鎮的代理人如果有性別設定，借錢行為可能受這種偏誤影響；設計時應記錄代理人的性別設定，分析時檢查是否有偏誤。
- 〔推論〕「降低信任比提高信任容易」表示，要在小鎮中引出不合作或背叛的行為，用提示讓代理人更謹慎應該比較容易做到。

## 相關頁面
- [大型語言模型代理人能模擬人類的信任行為嗎？ (Can Large Language Model Agents Simulate Human Trust Behavior?)](../papers/xie2024.md)
- [信任 (Trust)](trust.md)
- [信任賽局 (Trust Game)](../paradigms/trust-game.md)
- [指令微調讓代理人過度合作 (Instruction Tuning Makes Agents Too Cooperative)](../town/instruction-tuning-makes-agents-too-cooperative.md)
- [生成式代理人的倫理風險 (Ethical Risks of Generative Agents)](generative-agent-ethics.md)
- [術語表 (Glossary)](../glossary.md)
