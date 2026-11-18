---
title: 用理論類型設計小鎮代理人 (Theory-Grounded Agent Types for the Town)
type: town
summary: Horton2026 發現，沒給設定的模型在獨裁者賽局和人類差很多，給予自利、公平、效率等理論導向的設定並依人類資料調整混合比例後，預測誤差約減半；Horton2026 引用的研究指出，和理論無關的特質幾乎沒有幫助。
sources: [Horton2026, Berg1995]
related: [concepts/theory-grounded-personas.md, concepts/homo-silicus.md, paradigms/trust-game.md, town/instruction-tuning-makes-agents-too-cooperative.md, papers/horton2026.md]
tags: [town-design, persona, calibration]
status: draft
has_inference: true
created: 2026-11-18
updated: 2026-11-18
town_status: idea
---
# 用理論類型設計小鎮代理人 (Theory-Grounded Agent Types for the Town)

## 白話摘要
Horton2026 發現，沒有任何人物設定的語言模型，在獨裁者賽局的選擇和人類差很多，不同模型之間也不一樣。給代理人「只在乎公平」、「只在乎總報酬」、「只在乎自己」三種設定時，它們大致照設定行動；把三種代理人依人類資料調整比例後，在新賽局的預測誤差約減半。Horton2026 引用的研究指出，給嗜好或喜歡的電視節目這類特質幾乎沒有幫助；作者也提醒，只給人口特徵時，模型的世界模型如果不穩，可能變成刻板印象。

## 研究依據
- 沒給人物設定的代理人，在獨裁者賽局 (Dictator Game) 的選擇和人類受試者差很多，不同模型之間也不同 [Horton2026, p.12–13]。
- 有不平等趨避型 (inequity-averse)、效率型 (efficient)、自利型 (self-interested) 人物設定 (persona) 的代理人，大致都照設定行動 [Horton2026, p.11; Horton2026, p.13]。
- 依人類資料調整三種代理人的比例後，在新的兩階段賽局中預測誤差從 0.182 降到 0.094 [Horton2026, p.15]。
- Horton2026 引用 Manning 和 Horton (2025) 的發現：給代理人嗜好或喜歡的電視節目，幾乎沒有改善擬合 [Horton2026, p.30]。
- Llama-3-70B、Claude-Sonnet-3.5 和 Deepseek 校準後的不平等趨避型比例都是 0 [Horton2026, p.14]。
- 作者在註腳中指出，只用人口特徵當指令時，如果模型的世界模型不穩，模擬可能退化成刻板印象 [Horton2026, p.37]。

## 設計點子
- 〔推論〕北大小鎮的 AI 學生，除了「會計系大三」這類身分描述，也應該明確指定經濟偏好類型，例如自利型、公平型、效率型，讓它們在借錢和合作時的行為有理論依據。
- 〔推論〕各類型的比例可以先用 Berg1995 的人類數據校準：例如讓小鎮在單次信任賽局中的平均送出和回報接近 Berg1995 的結果，再拿去跑重複借錢等新情境。
- 〔推論〕可以準備一組「沒有偏好設定」的對照組代理人，比較兩組的借貸和還款行為，檢查設定是否真的讓結果更接近人類。
- 〔推論〕這也是處理過度合作的方法之一：明確放入自利型代理人，而不是只靠預設的模型行為。

## 風險與待驗證
- 〔推論〕Horton2026 的校準是在獨裁者賽局上做的，換成信任或借貸情境時，三種類型是否仍是合適的理論，需要測試。
- Berg1995 的無歷史組只有 32 對受試者 [Berg1995, p.9]。
- 〔推論〕用來校準的人類資料不多，比例可能不穩定。
- 〔推論〕Horton2026 校準後三個模型的公平型比例都是 0，小鎮若硬性放入公平型代理人，需要確認是否仍貼近人類資料。
- 〔推論〕Xie2024 只用人口特徵式的人物設定，GPT-4 在信任賽局仍和人類高度一致，所以人口特徵不一定無效，小鎮可以兩種設定都試。

## 相關頁面
- [理論導向的人物設定 (Theory-Grounded Personas)](../concepts/theory-grounded-personas.md)
- [矽基人 (Homo Silicus)](../concepts/homo-silicus.md)
- [信任賽局 (Trust Game)](../paradigms/trust-game.md)
- [指令微調讓代理人過度合作 (Instruction Tuning Makes Agents Too Cooperative)](instruction-tuning-makes-agents-too-cooperative.md)
- [大型語言模型作為模擬的經濟代理人：我們能從矽基人學到什麼？ (Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?)](../papers/horton2026.md)
