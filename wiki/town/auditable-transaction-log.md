---
title: 保留可查核的交易紀錄 (Auditable Transaction Log)
type: town
summary: 生成式代理人可能取不到記憶、只取到片段或加油添醋，也可能被精心設計的對話說服而相信沒發生的事；Park2023 另外針對濫用風險建議平台保留稽核紀錄；Axelrod1981 則指出，背叛者必須逃不過報復，合作才能演化。
sources: [Park2023, Axelrod1981, Berg1995]
related: [concepts/social-history.md, concepts/hallucination.md, concepts/agent-robustness.md, concepts/memory-stream.md, concepts/individual-recognition.md, concepts/reciprocity.md, papers/park2023.md]
tags: [town-design, memory, lending, auditability]
status: draft
has_inference: true
created: 2026-11-17
updated: 2026-11-17
town_status: idea
---
# 保留可查核的交易紀錄 (Auditable Transaction Log)

## 白話摘要
Park2023 的代理人有時想不起該記得的事、只想起一半，或在知道的事上加油添醋；作者也提醒，精心設計的對話可能讓代理人相信一件從沒發生過的事。另外，作者在討論濫用風險時，建議平台保留輸入和輸出的稽核紀錄。Axelrod1981 則指出，合作要能演化，背叛的人必須逃不過報復、不能隱沒在人群中。

## 研究依據
- 代理人可能取不到正確的記憶，或只取到不完整的記憶片段 [Park2023, p.15]。
- 代理人有時會在自己知道的事上加油添醋 (embellishment)，例如說出兩人從沒談過的計畫 [Park2023, p.15]。
- 453 個關於是否認識其他代理人的回答中，有 1.3%（n = 6）是幻覺 (hallucination) [Park2023, p.16]。
- 代理人可能受到記憶攻擊 (memory hacking)：精心設計的對話可能讓代理人相信一件從沒發生過的事 [Park2023, p.17]。
- 作者針對深度偽造、假訊息等濫用風險，建議平台保留輸入和輸出的稽核紀錄 (audit log)，以便偵測、驗證和介入惡意使用 [Park2023, p.18]。
- 記憶流 (memory stream) 中的每筆記憶都有自然語言描述和建立時間 [Park2023, p.8]。
- 合作要能演化，背叛 (Defect) 的個體必須逃不過有效的報復 (retaliation)，不能隱沒在匿名的人群中 [Axelrod1981, p.7]。

## 設計點子
- 〔推論〕小鎮另外維護一份由程式寫入的借貸帳本，記錄借款人、貸款人、金額、時間和是否還款，作為唯一的事實來源，不由代理人自己生成。
- 〔推論〕代理人決定要不要借錢時，可以查詢帳本，而不是只靠自己記憶流中的印象；這樣「誰沒還錢」才不會因為檢索 (retrieval) 失敗或加油添醋而記錯。
- 〔推論〕代理人在對話中聲稱「已經還過了」時，系統以帳本為準，避免類似記憶攻擊的說服。
- 〔推論〕帳本同時也是實驗資料：期末可以直接從帳本算出各代理人的借出金額、還款比例和違約次數，和 Berg1995 的人類數據比較。
- 〔推論〕可以比較兩個版本：代理人能查帳本和只能靠記憶，觀察記憶錯誤對信任和合作的影響。

## 風險與待驗證
- Berg1995 的社會歷史報告依送出金額列出人數、平均回報和平均淨報酬，是彙整後的數字，不是個人紀錄 [Berg1995, p.11–12]。
- 〔推論〕如果每個代理人都能查到完整帳本，等於所有交易都公開，這比 Berg1995 的社會歷史更強，可能改變代理人的行為；帳本的公開範圍要另外設計。
- 〔推論〕原文沒有測試代理人在經濟遊戲中的記憶錯誤率，1.3% 是「是否認識某人」的幻覺比例，不一定適用於借貸紀錄。

## 相關頁面
- [幻覺 (Hallucination)](../concepts/hallucination.md)
- [代理人的穩健性 (Robustness of Generative Agents)](../concepts/agent-robustness.md)
- [記憶流 (Memory Stream)](../concepts/memory-stream.md)
- [個體辨識 (Individual Recognition)](../concepts/individual-recognition.md)
- [互惠 (Reciprocity)](../concepts/reciprocity.md)
- [社會歷史 (Social History)](../concepts/social-history.md)
- [生成式代理人：人類行為的互動模擬 (Generative Agents: Interactive Simulacra of Human Behavior)](../papers/park2023.md)
