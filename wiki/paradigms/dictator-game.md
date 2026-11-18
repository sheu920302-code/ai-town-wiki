---
title: 獨裁者賽局 (Dictator Game)
type: paradigm
summary: 一方拿到一筆錢，決定分多少給另一方，對方不能回應；Berg1995 用它對照投資賽局的回報，Xie2024 用它和信任賽局比較，檢查人類和代理人是否會預期互惠。
sources: [Berg1995, Xie2024, Horton2026]
related: [paradigms/trust-game.md, concepts/trust-behavioral-factors.md, concepts/altruism.md, concepts/reciprocity.md, papers/berg1995.md, papers/xie2024.md, papers/horton2026.md, concepts/theory-grounded-personas.md, glossary.md]
tags: [dictator-game, altruism, reciprocity, experimental-economics]
status: draft
has_inference: true
created: 2026-11-18
updated: 2026-11-18
---
# 獨裁者賽局 (Dictator Game)

## 白話摘要
獨裁者賽局 (Dictator Game) 中，一方拿到一筆錢，自己決定要分多少給另一方，另一方只能接受，沒辦法回送或報復。因為沒有回報的可能，它常被拿來和信任賽局對照：兩個遊戲如果只差在「對方能不能回送」，人在信任賽局送得比較多，就表示期待對方回報會提高信任。人類在信任賽局平均送 $6.0、在獨裁者賽局送 $3.6；GPT-4 也是信任賽局送得比較多，但它兩個賽局都送得比人類多。

## 規則
- Berg1995 描述的獨裁者賽局：獨裁者拿到一筆錢，常見是 $10，決定要不要分一部分給第二位玩家 [Berg1995, p.6]。
- Xie2024 的版本：信任者 (trustor) 從初始的 $10 中送出 $N，受託者 (trustee) 收到 $3N [Xie2024, p.3]。
- 和信任賽局 (Trust Game) 相比，唯一的差別是受託者不能回送，而且信任者也知道對方不能回報 [Xie2024, p.3]。

> "Compared to the Trust Game, the only difference is that the trustee does not have the option to return money in the Dictator Game and the trustor is also aware that the trustee cannot reciprocate." [Xie2024, p.3]
> 中譯：和信任賽局相比，唯一的差別是獨裁者賽局中受託者不能回送，而且信任者也知道受託者無法回報。

## 報酬結構
- Xie2024 的版本中，送出的錢會變成三倍給受託者，這一點和信任賽局相同 [Xie2024, p.3]。
- 〔推論〕Berg1995 引述的獨裁者賽局沒有提到金額會放大，和 Xie2024 的版本不完全相同。

## 人類基準數據
- Forsythe 等人 (FHSS) 的 $10 獨裁者賽局中，獨裁者給出的金額高於自利預測的 0 [Berg1995, p.6]。
- Hoffman 等人 (HMSS) 採用雙盲 (double-blind) 程序後，自利行為顯著增加 [Berg1995, p.6]。
- HMSS 的雙盲獨裁者賽局中，77 位受試者每從實驗者那裡拿到 1 元，平均送出 11 分 [Berg1995, p.16]。
- Berg1995 拿它和投資賽局對照：投資賽局中 55 位收到錢的房間 B 受試者，平均每收到 1 元回送 35 分 [Berg1995, p.16–17]。
- Xie2024 指出，人類在信任賽局送得比獨裁者賽局多，表示預期互惠 (reciprocity anticipation) 會提高人類的信任 [Xie2024, p.6]。
- Xie2024 引用 Cox (2004) 的人類研究：信任賽局平均送出 $6.0，獨裁者賽局 $3.6，差異顯著（p = 0.01）[Xie2024, p.6]。

## LLM 代理人的結果
- GPT-4 在信任賽局平均送出 $6.9，在獨裁者賽局送出 $6.3，差異顯著（p = 0.05）[Xie2024, p.6]。
- 參數較少的模型，例如 Llama2-13b，在兩個賽局之間沒有出現這個傾向 [Xie2024, p.6]。
- GPT-4 在獨裁者賽局的推理著重公平和人性的善良，和信任賽局的推理不同 [Xie2024, p.6]。
- Horton2026 重現 Charness 和 Rabin 的單邊獨裁者賽局 (unilateral dictator game)：獨裁者在兩種金額分配之間二選一，例如對方 400、自己 600，或對方 700、自己 300 [Horton2026, p.11]。
- 在 Barc2 這個賽局中，原研究有 52% 的人類受試者選擇左邊的分配 [Horton2026, p.12]。
- 沒給人物設定的代理人，選擇和人類受試者差很多，不同模型之間也不同，例如 Llama-3-70B 看起來比較自私 [Horton2026, p.12–13]。
- 給予自利、公平或效率的人物設定後，代理人大致照設定選擇，詳見[理論導向的人物設定](../concepts/theory-grounded-personas.md) [Horton2026, p.13]。

## 小鎮應用線索
- 〔推論〕北大小鎮可以同時設計「借錢」和「送錢」兩種互動：比較代理人借出和白白送出的金額，就能檢查它們是否預期對方會還錢。
- 〔推論〕GPT-4 在獨裁者賽局送出的 $6.3 遠高於人類的 $3.6，表示小鎮代理人可能比真人更大方；解讀小鎮結果時要考慮這個差距。

## 相關頁面
- [信任賽局 (Trust Game)](trust-game.md)
- [信任的行為因素 (Behavioral Factors of Trust)](../concepts/trust-behavioral-factors.md)
- [利他 (Altruism)](../concepts/altruism.md)
- [互惠 (Reciprocity)](../concepts/reciprocity.md)
- [信任、互惠與社會歷史 (Trust, Reciprocity, and Social History)](../papers/berg1995.md)
- [大型語言模型代理人能模擬人類的信任行為嗎？ (Can Large Language Model Agents Simulate Human Trust Behavior?)](../papers/xie2024.md)
- [大型語言模型作為模擬的經濟代理人：我們能從矽基人學到什麼？ (Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?)](../papers/horton2026.md)
- [理論導向的人物設定 (Theory-Grounded Personas)](../concepts/theory-grounded-personas.md)
- [術語表 (Glossary)](../glossary.md)
