---
title: 矛盾總表 (Contradictions)
type: synthesis
summary: 整理論文之間看似衝突的主張，並列出處、適用條件和處理狀態。
sources: [Axelrod1981, Berg1995, Park2023, Xie2024, Horton2026]
related: [papers/axelrod1981.md, papers/berg1995.md, concepts/reciprocity.md, town/reciprocity-requires-non-anonymity.md, concepts/retaliation.md, papers/park2023.md, papers/xie2024.md, concepts/instruction-tuning.md, paradigms/trust-game.md, papers/horton2026.md, concepts/theory-grounded-personas.md]
tags: [contradictions, synthesis]
status: stable
has_inference: true
created: 2026-11-16
updated: 2026-11-18
---
# 矛盾總表 (Contradictions)

## 白話摘要
這頁整理不同論文之間看起來互相衝突的說法。每一筆都並列兩邊的出處和適用條件，標明是核心矛盾還是適用條件不同，以及目前怎麼處理。

## 問題
- 〔推論〕不同論文的研究方法、研究對象和情境不同，表面上相反的結論，可能只是適用條件不同；這頁的目的是把差異攤開，不替論文裁決。

## 證據

| 主題 | 主張 A（出處、條件） | 主張 B（出處、條件） | 類型 | 處理狀態 | 相關頁面 |
|---|---|---|---|---|---|
| 單次、匿名情境下會不會合作 (cooperation) 或互惠 (reciprocity) | Axelrod1981：只玩一次的囚犯困境 (Prisoner's Dilemma)，唯一稱得上解答的策略是永遠背叛 (ALL D) [Axelrod1981, p.3]；合作要能演化，背叛 (Defect) 的個體不能隱沒在匿名的人群中 [Axelrod1981, p.7]。條件：演化理論和電腦模擬，囚犯困境 | Berg1995：單次、雙盲 (double-blind) 的投資賽局 (Investment Game) 中，32 人中 30 人送錢 [Berg1995, p.2]；無歷史組收到超過 $1 的 28 人中，11 人回報多於對方送出 [Berg1995, p.10]；社會歷史組收到超過 $1 的 24 人中，13 人回報多於對方送出，但也有 6 人只回 $0 或 $1 [Berg1995, p.14]。條件：人類受試者實驗，投資賽局 | 適用條件差異（使用者決定） | 已並陳；town 頁受影響的推論已標為待檢視，等使用者改寫 | [互惠](../concepts/reciprocity.md)、[互惠需要無法匿名](../town/reciprocity-requires-non-anonymity.md)、[報復](../concepts/retaliation.md) |
| GPT-3.5 系列代理人是否過度合作 | Park2023：使用 gpt3.5-turbo 的代理人似乎彼此過度合作，Isabella 很少拒絕別人的點子 [Park2023, p.8; Park2023, p.17]。條件：25 個代理人的沙盒小鎮，日常互動、沒有設定報酬，質性觀察 | Xie2024：信任賽局中 GPT-3.5-turbo-0613 是圖 2 比較的模型中信任最低的，大多數人物設定送得比人類平均 $5.97 少 [Xie2024, p.5]。條件：有明確報酬的單次信任賽局，53 種人物設定 | 適用條件差異（使用者 2026-11-18 決定不列為核心矛盾） | 並列；instruction-tuning 概念頁和 town 頁已補上 Xie2024 的資料 | [指令微調](../concepts/instruction-tuning.md)、[指令微調讓代理人過度合作](../town/instruction-tuning-makes-agents-too-cooperative.md) |
| 人類在信任賽局的平均送出 | Berg1995：無歷史組平均送出 $5.16，社會歷史組 $5.36 [Berg1995, p.10; Berg1995, p.13]。條件：明尼蘇達大學學生，單次、雙盲 | Xie2024：人類平均送出 $5.97 [Xie2024, p.5]；引用 Cox (2004) 時為 $6.0 [Xie2024, p.6]。條件：Xie2024 引用的既有人類研究 | 細節差異（數字） | 並列，不裁決；比較 LLM 結果時註明用的是哪一個人類基準 | [信任賽局](../paradigms/trust-game.md)、[行為一致性](../concepts/behavioral-alignment.md) |
| 只給人口特徵的人物設定，能否讓代理人像人類 | Xie2024：人物設定包含姓名、年齡、性別、住址、職業和背景 [Xie2024, p.3–4]；GPT-4 代理人在信任行為上和人類高度一致 [Xie2024, p.8]。條件：信任賽局等 6 種賽局，GPT-4 等多種模型 | Horton2026：註腳指出只用人口特徵當指令時，如果模型的世界模型不穩，模擬可能退化成刻板印象 [Horton2026, p.37]；本文沒有在分配賽局中測試人口特徵式設定，公平感實驗則給過政治立場設定 [Horton2026, p.7]（另一個背景發現是沒給任何設定的代理人在獨裁者賽局和人類差很多 [Horton2026, p.12–13]）。條件：Charness 和 Rabin 的分配賽局，GPT-4o、Claude、Llama、Deepseek | 適用條件差異（使用者 2026-11-18 決定不列為核心矛盾） | 並列；理論導向的人物設定頁和 town 頁已註明 | [理論導向的人物設定](../concepts/theory-grounded-personas.md)、[用理論類型設計小鎮代理人](../town/theory-grounded-agent-types.md) |

## 綜合判斷
- 〔推論〕兩篇的理論預測其實一致：Axelrod1981 指出單次囚犯困境的解答是永遠背叛，Berg1995 的子賽局完美預測 (subgame perfect prediction) 也是一毛都不送 [Axelrod1981, p.3; Berg1995, p.4]。
- 〔推論〕差別在於 Berg1995 的人類受試者偏離了理論預測，而且只有部分人回報：無歷史組收到超過 $1 的 28 人中 11 人、社會歷史組 24 人中 13 人回報多於對方送出 [Berg1995, p.10; Berg1995, p.14]。
- 〔推論〕兩篇的「匿名」意思不同：Axelrod1981 指的是背叛者在演化上可以躲進人群、逃過報復；Berg1995 的雙盲指的是實驗中沒有人能把決策對應回個人 [Axelrod1981, p.7; Berg1995, p.6]。
- 〔推論〕因此這筆紀錄被歸為適用條件差異，而不是核心矛盾；但 town 頁「互惠需要無法匿名」的設計推論，在 Berg1995 的人類資料前需要重新檢視。
- 〔推論〕GPT-3.5 系列是否過度合作的兩筆證據，情境不同（日常互動對有報酬的賽局）、衡量的東西不同（願不願意拒絕對送出多少錢），模型版本也可能不同（Park2023 只寫 gpt3.5-turbo），所以列為適用條件差異。
- 〔推論〕人類在信任賽局的平均送出，Berg1995 和 Xie2024 引用的研究相差約 $0.6 到 $0.8，可能來自受試者、年代和實驗程序的差異；兩篇都沒有說明差異的原因。
- 〔推論〕人口特徵式設定的兩筆證據，賽局不同（信任賽局對分配賽局）、模型不同、比較的指標也不同；Horton2026 的保留看法出自註腳的一般性評論，沒有直接測試信任賽局，所以列為適用條件差異。

## 相關頁面
- [合作的演化 (The Evolution of Cooperation)](../papers/axelrod1981.md)
- [信任、互惠與社會歷史 (Trust, Reciprocity, and Social History)](../papers/berg1995.md)
- [互惠 (Reciprocity)](../concepts/reciprocity.md)
- [互惠需要無法匿名 (Reciprocity Requires Non-Anonymity)](../town/reciprocity-requires-non-anonymity.md)
- [報復 (Retaliation)](../concepts/retaliation.md)
- [生成式代理人：人類行為的互動模擬 (Generative Agents: Interactive Simulacra of Human Behavior)](../papers/park2023.md)
- [大型語言模型代理人能模擬人類的信任行為嗎？ (Can Large Language Model Agents Simulate Human Trust Behavior?)](../papers/xie2024.md)
- [指令微調 (Instruction Tuning)](../concepts/instruction-tuning.md)
- [信任賽局 (Trust Game)](../paradigms/trust-game.md)
- [大型語言模型作為模擬的經濟代理人：我們能從矽基人學到什麼？ (Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?)](../papers/horton2026.md)
- [理論導向的人物設定 (Theory-Grounded Personas)](../concepts/theory-grounded-personas.md)
