---
title: 重複信任賽局 (Repeated Trust Game)
type: paradigm
summary: 同樣兩人連續玩多輪信任賽局，每輪信任者都拿到相同的初始金額；人類有三個常見規律，GPT-4 在 16 組中大多符合，GPT-3.5 較少符合。
sources: [Xie2024, Axelrod1981]
related: [paradigms/trust-game.md, concepts/behavioral-alignment.md, concepts/continuation-probability.md, papers/xie2024.md, glossary.md]
tags: [repeated-trust-game, trust, reciprocity, behavioral-dynamics]
status: draft
has_inference: true
created: 2026-11-18
updated: 2026-11-18
---
# 重複信任賽局 (Repeated Trust Game)

## 白話摘要
重複信任賽局 (Repeated Trust Game) 是讓同樣兩個人連續玩好幾輪信任賽局，每一輪信任者 (trustor) 都重新拿到一樣多的錢。人類的表現雖然因人而異，但有三個常見規律：回送的錢通常比送出的多；送出和回送的比例大致穩定，只有最後一輪例外；金額不會一直大幅跳動。Xie2024 讓 GPT-4 和 GPT-3.5 各玩 16 組，GPT-4 大多符合這三個規律，GPT-3.5 則常常不符合。

## 規則
- Xie2024 依 Cochard 等人 (2004) 的設定，讓同樣兩位玩家連續玩多輪信任賽局 (Trust Game)，每一輪信任者都重新拿到相同的初始金額 [Xie2024, p.3]。

> "We follow the setting of the Repeated Trust Game in (Cochard et al., 2004), where the Trust Game is played for multiple rounds with the same players and each round begins anew with the trustor allocated the same initial money." [Xie2024, p.3]
> 中譯：我們依照 Cochard 等人 (2004) 的重複信任賽局設定：同樣兩位玩家連續玩多輪信任賽局，每一輪重新開始，信任者都拿到相同的初始金額。

## 報酬結構
- 每一輪和信任賽局相同：信任者送出 $N，受託者收到 $3N，再決定回送多少 [Xie2024, p.3; Xie2024, p.7]。

## 人類基準數據
- 作者表示，人類的信任動態因人而異、相當複雜，16 組人類實驗的完整結果列在附錄 [Xie2024, p.7]。
- 常見規律一：每一輪的回送金額通常大於送出金額 [Xie2024, p.7]。
- 常見規律二：回送和三倍送出金額的比例大致穩定，只有最後一輪例外；連續兩輪的波動在 10% 以內就視為穩定 [Xie2024, p.7–8]。
- 常見規律三：送出或回送的金額不會在各輪之間頻繁波動 [Xie2024, p.8]。

## LLM 代理人的結果
- 作者讓 GPT-4 和 GPT-3.5-turbo-0613-16k（原文簡稱 GPT-3.5）各玩 16 組，每組兩位玩家的人物設定 (persona) 不同、模型相同 [Xie2024, p.8]。
- GPT-4 符合三個規律的比例分別是 87.50%、87.50% 和 100.00% [Xie2024, p.8]。
- GPT-3.5 符合的比例分別是 62.50%、56.25% 和 43.75% [Xie2024, p.8]。
- 作者認為，這類行為規律可能需要較強的認知能力 [Xie2024, p.8]。

## 小鎮應用線索
- 〔推論〕北大小鎮的代理人會在一學期中反覆互相借錢，比單次的信任賽局更接近重複信任賽局。
- Axelrod1981 指出，互動次數事先已知時，最後一回合背叛是最佳選擇，往前倒推每一回合也都是 [Axelrod1981, p.4]。
- 〔推論〕人類的比例在最後一輪變得不穩定，但 Xie2024 正文沒有說明變化的方向，和 Axelrod1981 的論證是否有關，還需要看附錄的完整資料；小鎮如果讓代理人知道學期快結束，值得觀察是否有最後一輪效應。
- 〔推論〕Xie2024 只比較了 GPT-4 和 GPT-3.5，小鎮選用的模型如果較弱，借貸行為可能不符合人類的規律。

## 相關頁面
- [信任賽局 (Trust Game)](trust-game.md)
- [行為一致性 (Behavioral Alignment)](../concepts/behavioral-alignment.md)
- [再相遇機率 (Continuation Probability)](../concepts/continuation-probability.md)
- [大型語言模型代理人能模擬人類的信任行為嗎？ (Can Large Language Model Agents Simulate Human Trust Behavior?)](../papers/xie2024.md)
- [術語表 (Glossary)](../glossary.md)
