---
title: 信任的行為因素 (Behavioral Factors of Trust)
type: concept
summary: 人類研究指出三個影響信任行為的基本因素：預期互惠、風險感知和利社會偏好；Xie2024 用信任賽局的不同變化版本逐一比較，發現 GPT-4 在三個因素上都和人類相似，部分小模型則不然。
sources: [Xie2024]
related: [concepts/behavioral-alignment.md, concepts/trust.md, concepts/reciprocity.md, paradigms/trust-game.md, paradigms/dictator-game.md, papers/xie2024.md, glossary.md]
tags: [trust, reciprocity, risk, prosocial-preference]
status: draft
has_inference: true
created: 2026-11-18
updated: 2026-11-18
---
# 信任的行為因素 (Behavioral Factors of Trust)

## 白話摘要
人為什麼願意信任別人？人類研究找到三個基本因素：期待對方會回報（預期互惠 (reciprocity anticipation)）、覺得風險有多大（風險感知 (risk perception)）、以及比起單純碰運氣，更願意把機會交給人（利社會偏好 (prosocial preference)）。Xie2024 設計了幾組只差一個條件的賽局來分別測這三個因素。人類和 GPT-4 都是：對方能回報時送得比較多、風險越低越願意信任、比起賭博更願意信任他人。部分參數較少的模型則沒有這些傾向。

## 定義
- 預期互惠是期待對方會做出互惠的行動，它可以正向影響人類的信任行為 [Xie2024, p.6]。
- 人類研究顯示，信任行為和風險感知高度相關，風險降低時人類的信任會增加 [Xie2024, p.6]。
- 利社會偏好是指在涉及社會互動的情境中，人類傾向信任其他人 [Xie2024, p.7]。

> "Reciprocity anticipation, the expectation of a reciprocal action from the other player, can positively influence human trust behavior (Berg et al., 1995)." [Xie2024, p.6]
> 中譯：預期互惠，也就是期待對方做出互惠的行動，可以正向影響人類的信任行為。

## 各論文的觀點

### Xie2024

#### 預期互惠：信任賽局對照獨裁者賽局
- 信任賽局 (Trust Game) 和獨裁者賽局 (Dictator Game) 唯一的差別，是受託者 (trustee) 能不能回送錢，所以預期互惠只在信任賽局中發揮作用 [Xie2024, p.6]。
- 人類在信任賽局平均送出 $6.0，在獨裁者賽局送出 $3.6（單尾獨立樣本 t 檢定 (One-Tailed Independent Samples t-test)，p = 0.01）[Xie2024, p.6]。
- GPT-4 在信任賽局平均送出 $6.9，在獨裁者賽局送出 $6.3（p = 0.05），也是在信任賽局中顯著較高 [Xie2024, p.6]。
- 參數較少的模型，例如 Llama2-13b，沒有出現這個傾向 [Xie2024, p.6]。
- GPT-4 在信任賽局的推理強調「相信人」，在獨裁者賽局的推理則著重公平和人性的善良 [Xie2024, p.6]。

#### 風險感知：MAP 信任賽局和風險獨裁者賽局
- MAP 信任賽局 (MAP Trust Game) 中，信任者 (trustor) 決定是否信任：不信任時雙方各得 $10，雙方都選信任時各得 $15，信任者信任而受託者不信任時，信任者得 $8、受託者得 $22 [Xie2024, p.3]。
- 風險獨裁者賽局 (Risky Dictator Game) 只差一點：受託者不能選擇，結果完全由機率 p 決定 [Xie2024, p.3]。
- 作者讓 p 從 0.1 到 1.0 共做 10 組實驗，計算選擇信任的比例，也就是信任率 (Trust Rate) [Xie2024, p.20]。
- GPT-4、GPT-3.5-turbo-0613 和 text-davinci-003 的信任大致隨風險降低而增加，其中 GPT-4 的曲線最接近人類 [Xie2024, p.6–7]。
- Vicuna-13b 等參數較少的模型，信任率沒有隨風險降低而出現類似的變化 [Xie2024, p.7]。

#### 利社會偏好：兩種樂透賽局
- 樂透賭博賽局 (Lottery Gamble Game) 中，信任者在一場獲勝機率為 p 的賭局和固定金額之間選擇；樂透他人賽局 (Lottery People Game) 則是在信任對方和固定金額之間選擇；p 依人類研究設為 46% [Xie2024, p.3]。
- 人類選擇信任他人的比例高於選擇賭博（54% 對 29%）[Xie2024, p.7]。
- GPT-4 選擇信任他人的比例遠高於選擇賭博（72% 對 21%）[Xie2024, p.7]。
- 除了 Vicuna-13b，大部分模型都有同樣的傾向 [Xie2024, p.7]。

## 爭議與未解問題
- 〔推論〕GPT-4 在獨裁者賽局也送出 $6.3，比人類的 $3.6 高很多；它和人類的「方向」一致，但「水準」不同，代理人整體上比人類更願意給錢。
- 〔推論〕這個水準差異和 Park2023 觀察到的代理人過度合作可能有關，但 Xie2024 沒有討論原因。

## 相關頁面
- [行為一致性 (Behavioral Alignment)](behavioral-alignment.md)
- [信任 (Trust)](trust.md)
- [互惠 (Reciprocity)](reciprocity.md)
- [信任賽局 (Trust Game)](../paradigms/trust-game.md)
- [獨裁者賽局 (Dictator Game)](../paradigms/dictator-game.md)
- [大型語言模型代理人能模擬人類的信任行為嗎？ (Can Large Language Model Agents Simulate Human Trust Behavior?)](../papers/xie2024.md)
- [術語表 (Glossary)](../glossary.md)
