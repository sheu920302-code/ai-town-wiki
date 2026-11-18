---
title: 受控評估與消融 (Controlled Evaluation and Ablation)
type: concept
summary: Park2023 檢驗架構的方法：用自然語言訪談代理人五類能力，比較完整架構、三種拿掉元件的消融版本和人類群眾外包工作者的回答，由 100 位評分者依可信度排序，再轉成 TrueSkill 評分並做統計檢定。
sources: [Park2023]
related: [concepts/believability.md, concepts/generative-agent.md, papers/park2023.md, glossary.md]
tags: [evaluation, ablation, methodology]
status: draft
has_inference: true
created: 2026-11-17
updated: 2026-11-17
---
# 受控評估與消融 (Controlled Evaluation and Ablation)

## 白話摘要
要知道觀察 (observation)、反思 (reflection)、規劃 (planning) 這幾種記憶是否真的有用，Park2023 做了受控評估 (controlled evaluation)：直接用問題「訪談」代理人，例如請它介紹自己，或問它早餐燒焦時會怎麼做。同一個代理人的回答有五種版本：完整架構、三種拿掉部分元件的消融 (ablation) 版本，以及由真人扮演角色寫的回答。100 位評分者把這些回答依可信度 (believability) 排序，作者再用統計方法檢驗差異。另外還有端到端評估 (end-to-end evaluation)，讓代理人連續互動兩天，觀察群體行為。

## 定義
- Park2023 做了兩種評估：受控評估檢驗代理人單獨的行為是否可信，端到端評估讓代理人在兩個遊戲日中自由互動，了解穩定性和湧現的社會行為 (emergent social behavior) [Park2023, p.3]。
- 消融版本拿掉代理人在記憶流 (memory stream) 中可以使用的部分或全部記憶類型：觀察 (observation)、反思 (reflection) 和規劃 (planning) [Park2023, p.13]。

> "The interview includes five question categories, each designed to assess one of the five key areas: maintaining self-knowledge, retrieving memory, generating plans, reacting, and reflecting." [Park2023, p.13]
> 中譯：訪談包含五類問題，分別評估五個關鍵能力：維持自我認識、取回記憶、產生計畫、做出反應和反思。

## 各論文的觀點

### Park2023

#### 訪談設計
- 每一類問題各有 5 題，例如請代理人介紹自己，或問它早餐燒焦時會怎麼做 [Park2023, p.13]。
- 每位評分者在每一類問題中只看到一題隨機抽出的題目，以及各條件的回答 [Park2023, p.13]。
- 受訪的代理人取自完整架構跑完兩個遊戲日之後，已經累積了互動和記憶 [Park2023, p.13]。

#### 比較的條件
- 三種消融架構是：完全沒有記憶流內容、只有觀察、有觀察和計畫但沒有反思 [Park2023, p.13]。
- 完全消融的條件，代表先前用大型語言模型 (large language model) 打造代理人的做法 [Park2023, p.13]。
- 所有架構都能使用代理人到訪談當下為止累積的記憶，作者認為觀察到的差異可能是保守的估計 [Park2023, p.13]。
- 人類條件為 25 個代理人各招募一位群眾外包工作者 (crowdworker)，看完重播後以該代理人的口吻回答 [Park2023, p.14]。
- 有 4 組群眾外包的回答沒有達到基本品質，由其他工作者重寫 [Park2023, p.14]。

#### 評分與分析
- 評分者透過 Prolific 招募，共 100 位，每小時報酬 15 美元，參與約 30 分鐘 [Park2023, p.14]。
- 排序資料轉換成 TrueSkill 評分 (TrueSkill rating)；TrueSkill 是西洋棋 Elo 評分在多人情境下的推廣 [Park2023, p.14]。
- 統計檢定使用 Kruskal-Wallis 檢定、Dunn 事後檢定，並以 Holm-Bonferroni 方法調整多重比較的 p 值 [Park2023, p.14]。
- 第一作者另外用開放編碼做質性分析，比較各條件回答的差異 [Park2023, p.14]。
- 評估結果的數字見論文頁 [Park2023, p.14]。

## 爭議與未解問題
- 作者表示，評估的時間尺度相對短，人類條件也不代表人類的最佳表現 [Park2023, p.17]。
- 〔推論〕這套方法比較的是「哪個版本更可信」，沒有拿代理人的選擇和真人實驗的結果比較；評估經濟賽局中的行為需要不同的方法。

## 相關頁面
- [可信度 (Believability)](believability.md)
- [生成式代理人 (Generative Agent)](generative-agent.md)
- [生成式代理人：人類行為的互動模擬 (Generative Agents: Interactive Simulacra of Human Behavior)](../papers/park2023.md)
- [術語表 (Glossary)](../glossary.md)
