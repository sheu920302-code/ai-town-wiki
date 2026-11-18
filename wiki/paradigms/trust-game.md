---
title: 信任賽局 (Trust Game)
type: paradigm
summary: 甲方決定把多少錢交給匿名的乙方，錢會變成三倍，乙方再決定還多少；理論預測不送，實驗中多數人仍會送。
sources: [Berg1995, Xie2024]
related: [papers/berg1995.md, concepts/trust.md, concepts/reciprocity.md, concepts/social-history.md, town/social-history-shapes-trust.md, papers/xie2024.md, paradigms/dictator-game.md, paradigms/repeated-trust-game.md, concepts/agent-trust-properties.md, glossary.md]
tags: [trust-game, investment-game, trust, reciprocity, experimental-economics]
status: stable
has_inference: true
created: 2026-11-16
updated: 2026-11-18
---
# 信任賽局 (Trust Game)

## 白話摘要
甲方手上有 $10，可以把任意金額交給一位不認識、也永遠不會知道是誰的乙方；交出去的錢會變成三倍，乙方再決定要還甲方多少。照理論，乙方應該全部留下，所以甲方一毛都不該給；但在 Berg1995 的實驗裡，多數甲方都給了錢，而乙方有的還得多、有的幾乎不還。

## 名稱
- Berg1995 原文把這個遊戲稱為投資賽局 (Investment Game) [Berg1995, p.2]。
- 作者說明，投資賽局和 Kreps (1990) 的信任賽局 (Trust Game) 有相同的兩階段結構：把錢交給對方有風險，但會讓總額變大，其中一部分可能被還回來 [Berg1995, p.2]。
- 兩者的差別是：Kreps 的信任賽局每一階段只有兩個選項，投資賽局的選擇空間較大，可以表現不同程度的信任 (trust) 和互惠 (reciprocity) [Berg1995, p.2]。
- 〔推論〕之後的研究多半把 Berg1995 的投資賽局也稱為信任賽局，本 wiki 用「信任賽局」作為頁名，以便和之後的 LLM 論文並列。

## 規則
- 第一階段：房間 A 和房間 B 的受試者各拿到 $10 出場費 [Berg1995, p.3]。
- 房間 A 的受試者決定要把 $10 中的多少，送給房間 B 的一位匿名對象，這個金額記為 M_a [Berg1995, p.3]。
- 送出的金額會變成三倍，所以房間 B 的對象收到 3M_a [Berg1995, p.3–4]。
- 第二階段：房間 B 的對象決定要還多少，記為 k_b(3M_a) [Berg1995, p.4]。
- 房間 A 的策略是從 {0, 1, 2, …, 10} 中選一個 M_a，房間 B 的回報必須介於 0 和 3M_a 之間 [Berg1995, p.4]。
- 每位受試者只玩一次 [Berg1995, p.2]。

### 雙盲程序
- 實驗採用雙盲 (double-blind) 程序，目的是排除重複賽局效應，讓結果不能歸因於聲譽、勾結或懲罰的威脅 [Berg1995, p.6]。
- 在雙盲程序下，沒有任何人，包括實驗者，能把個別決策對應回做決定的人 [Berg1995, p.6]。
- 實際做法是在三個房間之間傳遞信封：房間 A、B 是受試者，房間 C 有 14 個信箱 [Berg1995, p.7]。
- 房間 A 的受試者在隔板後面，把要送出的錢放進有字母的小信封，自己留下對應字母的信箱鑰匙 [Berg1995, p.7–8]。
- 記錄員在走廊記錄送出金額、把錢變成三倍後，再由房間 B 的受試者私下決定還多少 [Berg1995, p.8]。
- 回報的錢放進房間 C 的信箱，房間 A 的受試者用鑰匙私下取回，沒有其他人知道用了哪把鑰匙或哪個信箱 [Berg1995, p.8]。

## 報酬結構
- 房間 A 的報酬是 P_a = $10 − M_a + k_b(3M_a) [Berg1995, p.4]。
- 房間 B 的報酬是 P_b = 3M_a − k_b(3M_a) [Berg1995, p.4]。
- 如果受試者只在乎自己的財富，房間 B 的優勢策略 (dominant strategy) 是全部留下，也就是 k_b(3M_a) = 0 [Berg1995, p.4]。
- 房間 A 如果推想到這一點，就應該一毛都不送，也就是 M_a = 0；這是子賽局完美預測 (subgame perfect prediction) [Berg1995, p.4]。
- 因為錢會變成三倍，雙方都有可能比子賽局完美的結果過得更好 [Berg1995, p.5]。

## 人類基準數據

| 指標 | 無歷史組 | 社會歷史 (social history) 組 |
|---|---|---|
| 配對數 | 32 [Berg1995, p.9] | 28 [Berg1995, p.11] |
| 平均送出 | $5.16 [Berg1995, p.10] | $5.36 [Berg1995, p.13] |
| 平均回報 | $4.66 [Berg1995, p.10] | $6.46 [Berg1995, p.13] |
| 送 0 元的人數 | 32 人中 2 人 [Berg1995, p.10] | 28 人中 3 人 [Berg1995, p.14] |
| 收到超過 $1 的人中，只回 $0 或 $1 | 28 人中 12 人 [Berg1995, p.10] | 24 人中 6 人 [Berg1995, p.14] |
| 收到超過 $1 的人中，回報多於對方送出 | 28 人中 11 人 [Berg1995, p.10] | 24 人中 13 人 [Berg1995, p.14] |
| 送 $5 時的平均回報 | $7.17 [Berg1995, p.10] | $7.14 [Berg1995, p.14] |
| 送 $10 時的平均回報 | $10.20 [Berg1995, p.10] | $13.17 [Berg1995, p.14] |
| 送出與回報的 Spearman 相關 r_s（無歷史組比較的是回報比例） | 0.01 [Berg1995, p.10–11] | .34 [Berg1995, p.14] |
| 平均淨報酬 | −$0.50 [Berg1995, p.16] | +$1.10 [Berg1995, p.16] |

- 無歷史組中，32 人有 5 人送出全部的 $10 [Berg1995, p.10]。
- 無歷史組的送出金額變化很大，從 $1 到 $10 都有 [Berg1995, p.10]。
- 每一對的原始數據列在附錄 B [Berg1995, p.20]。

## LLM 代理人的結果
- Xie2024 讓多種大型語言模型 (large language model) 扮演 53 種人物設定 (persona)，以信任者身分玩信任賽局 [Xie2024, p.3–4]。
- Xie2024 的信任賽局：信任者拿到 $10，送出 $N，受託者收到 $3N 後可以回送一部分 [Xie2024, p.3]。
- 大部分模型的送出金額都在 $10 以內，而且大多是正數，作者認為代理人大致表現出信任行為 [Xie2024, p.4–5]。
- 和人類平均送出的 $5.97 相比，GPT-4 和 Vicuna-7b 大多數人物設定送得比較多，GPT-3.5-turbo-0613 等模型大多送得比較少 [Xie2024, p.5]。
- GPT-4 在信任賽局平均送出 $6.9，高於它在獨裁者賽局 (Dictator Game) 的 $6.3 [Xie2024, p.6]。
- 告訴代理人對方的性別、種族，或對方是人類還是代理人，送出金額都會改變，詳見[代理人信任的特性](../concepts/agent-trust-properties.md) [Xie2024, p.8–9]。
- 〔推論〕Xie2024 的人類平均 $5.97 和 Berg1995 無歷史組的 $5.16 不同，兩者來自不同研究，比較 LLM 結果時要注意用的是哪一個人類基準 [Xie2024, p.5; Berg1995, p.10]。

## 小鎮應用線索
- 〔推論〕信任賽局可以直接改寫成小鎮的借貸或合資互動：甲代理人決定借出多少，金額放大後由乙代理人決定還多少 [Berg1995, p.2]。
- 〔推論〕Berg1995 的兩組數據可以當作人類基準，用來比較小鎮 LLM 代理人的送出與回報分布 [Berg1995, p.10; Berg1995, p.14]。
- 〔推論〕要重現「單次、匿名」的條件，小鎮必須確保代理人之後不會再遇到同一個對象，也無法得知對方是誰 [Berg1995, p.6]。

## 相關頁面
- [信任、互惠與社會歷史 (Trust, Reciprocity, and Social History)](../papers/berg1995.md)
- [信任 (Trust)](../concepts/trust.md)
- [互惠 (Reciprocity)](../concepts/reciprocity.md)
- [社會歷史 (Social History)](../concepts/social-history.md)
- [社會歷史會影響信任 (Social History Shapes Trust)](../town/social-history-shapes-trust.md)
- [大型語言模型代理人能模擬人類的信任行為嗎？ (Can Large Language Model Agents Simulate Human Trust Behavior?)](../papers/xie2024.md)
- [獨裁者賽局 (Dictator Game)](dictator-game.md)
- [重複信任賽局 (Repeated Trust Game)](repeated-trust-game.md)
- [代理人信任的特性 (Properties of Agent Trust)](../concepts/agent-trust-properties.md)
- [術語表 (Glossary)](../glossary.md)
