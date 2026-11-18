---
title: 湧現的社會行為 (Emergent Social Behavior)
type: concept
summary: 沒有事先寫好腳本、而是代理人互動後自然出現的群體行為；Park2023 測量了資訊擴散、關係形成和協調三種，例如派對消息從 1 位傳到 13 位、網路密度從 0.167 升到 0.74。
sources: [Park2023]
related: [concepts/generative-agent.md, concepts/memory-stream.md, concepts/individual-recognition.md, papers/park2023.md, town/instruction-tuning-makes-agents-too-cooperative.md, concepts/hallucination.md, concepts/instruction-tuning.md, glossary.md]
tags: [emergent-behavior, information-diffusion, coordination, generative-agents]
status: draft
has_inference: true
created: 2026-11-17
updated: 2026-11-17
---
# 湧現的社會行為 (Emergent Social Behavior)

## 白話摘要
湧現的社會行為 (emergent social behavior) 指的是沒有人寫好劇本、而是代理人彼此互動後自然出現的群體行為。Park2023 讓 25 個代理人在小鎮裡生活兩個遊戲日，一開始只有 Isabella 知道自己要辦情人節派對、只有 Sam 知道自己要參選。兩天後，知道派對的代理人從 1 位變成 13 位，知道參選的從 1 位變成 8 位，彼此認識的程度也大幅提高；最後 12 位受邀者中有 5 位真的到場。

## 定義
- Park2023 指出，代理人的社會行為是湧現的，而不是事先寫好程式的 [Park2023, p.6]。
- Park2023 測量三種湧現結果：資訊擴散 (information diffusion)、關係形成 (relationship formation) 和代理人之間的協調 (agent coordination) [Park2023, p.15]。

## 各論文的觀點

### Park2023

#### 怎麼測量
- 模擬開始時，兩則資訊只有發起者知道：Sam 知道自己參選，Isabella 知道自己要辦派對；這兩則資訊是在初始化時寫進角色記憶的 [Park2023, p.15]。
- 資訊擴散：在兩個遊戲日結束時訪談 25 個代理人，問他們是否知道情人節派對、是否知道誰在競選 [Park2023, p.15]。
- 作者會到記憶流 (memory stream) 中找出提供資訊的那段對話，確認代理人的回答不是幻覺 (hallucination) [Park2023, p.15]。
- 關係形成：在模擬開始和結束時，問每個代理人是否認識其他每個代理人，雙方都認識才算形成關係，再計算網路密度 (network density) [Park2023, p.15–16]。
- 協調：計算聽說派對後真的到場的代理人數 [Park2023, p.16]。

#### 結果
- 知道 Sam 參選的代理人從 1 位 (4%) 增加到 8 位 (32%) [Park2023, p.16]。
- 知道 Isabella 派對的代理人從 1 位 (4%) 增加到 13 位 (52%) [Park2023, p.16]。
- 這些資訊的擴散都沒有使用者介入 [Park2023, p.16]。
- 網路密度從 0.167 上升到 0.74 [Park2023, p.16]。
- 453 個關於是否認識其他代理人的回答中，1.3%（n = 6）是幻覺 [Park2023, p.16]。
- 12 位受邀的代理人中有 5 位到場；沒到的 7 位中，3 位說有衝突，4 位表示有興趣但當天沒有安排前往 [Park2023, p.16]。
- 使用者只設定了 Isabella 想辦派對和 Maria 暗戀 Klaus；傳話、布置、邀約和到場都是由代理人架構自己啟動的 [Park2023, p.7]。

> "None who claimed to know about this information had hallucinated it." [Park2023, p.16]
> 中譯：宣稱知道這些資訊的代理人，沒有一位是出於幻覺。

## 爭議與未解問題
- 作者觀察到，指令微調 (instruction tuning) 似乎讓代理人更客氣，也過度合作 [Park2023, p.17]。
- 〔推論〕Park2023 觀察到的協調都是友善的合作情境，沒有涉及利益衝突；代理人在需要拒絕或背叛 (Defect) 時是否也會出現類似的湧現行為，目前 wiki 中還沒有資料。

## 相關頁面
- [生成式代理人 (Generative Agent)](generative-agent.md)
- [記憶流 (Memory Stream)](memory-stream.md)
- [個體辨識 (Individual Recognition)](individual-recognition.md)
- [生成式代理人：人類行為的互動模擬 (Generative Agents: Interactive Simulacra of Human Behavior)](../papers/park2023.md)
- [指令微調讓代理人過度合作 (Instruction Tuning Makes Agents Too Cooperative)](../town/instruction-tuning-makes-agents-too-cooperative.md)
- [幻覺 (Hallucination)](hallucination.md)
- [指令微調 (Instruction Tuning)](instruction-tuning.md)
- [術語表 (Glossary)](../glossary.md)
