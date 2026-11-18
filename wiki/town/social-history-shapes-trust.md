---
title: 社會歷史會影響信任 (Social History Shapes Trust)
type: town
summary: 讓人先看到前一批人怎麼做的摘要後，平均回報提高、送出與回報的相關變強，但部分變化不顯著。
sources: [Berg1995]
related: [concepts/social-history.md, concepts/trust.md, paradigms/trust-game.md, papers/berg1995.md]
tags: [town-design, social-history, trust, reputation]
status: stable
has_inference: true
created: 2026-11-16
updated: 2026-11-16
town_status: idea
---
# 社會歷史會影響信任 (Social History Shapes Trust)

## 白話摘要
Berg1995 讓第二批受試者先看前一批人的決策摘要：每個送出金額有幾個人選、平均拿回多少、平均賺或賠多少。看過摘要的這一組，平均回報從 $4.66 提高到 $6.46，送出金額和拿回金額的關聯也變強；不過有些變化在統計上不顯著，而且資料變得更分散。

## 研究依據
- 社會歷史 (social history) 組的受試者拿到一份前 32 對決策的摘要報告 [Berg1995, p.11]。
- 報告依送出金額分別列出人數、平均回報和平均淨報酬，是彙整後的數字，不是個人紀錄 [Berg1995, p.11–12]。
- 社會歷史組的平均回報是 $6.46，無歷史組是 $4.66 [Berg1995, p.10; Berg1995, p.13]。
- 平均淨報酬從 −$0.50 變成 +$1.10 [Berg1995, p.16]。
- 送出與回報的相關從 0.01 上升到 .34 [Berg1995, p.10–11; Berg1995, p.14]。
- 作者事前認為兩個方向都有可能：社會歷史可能讓人看到有人不回報而減少信任，也可能讓人注意到送 $5 和 $10 有正的淨報酬而增加信任 [Berg1995, p.12]。
- 作者認為社會歷史可能提高社會認同，並強化個人對信任 (trust) 的傾向 [Berg1995, p.11]。
- 比較兩組回報的檢定在 p = 0.1 的水準顯著，社會歷史組的資料也更分散 [Berg1995, p.13–14]。

## 設計點子
- 〔推論〕小鎮可以設一個「公告欄」，定期公布全鎮彙整後的互動結果，例如借出不同金額時平均拿回多少，作為代理人的社會歷史。
- 〔推論〕公告只放彙整數字、不放個人紀錄，才符合 Berg1995 的設計，也能和「個人聲譽」的效果分開觀察。
- 〔推論〕可以比較兩個版本的小鎮：有公告欄和沒有公告欄，看 LLM 代理人的借出金額和還款比例是否不同。
- 〔推論〕公告內容的呈現方式本身可能影響結果，Berg1995 為了減少呈現效果，只在說明中用一段話提到報告；小鎮也應固定公告的格式和措辭 [Berg1995, p.12]。

## 風險與待驗證
- 〔推論〕Berg1995 的部分效果在統計上不顯著，小鎮實驗不應預設社會歷史一定會提高信任。
- 〔推論〕如果公告凸顯「很多人不還錢」，可能反而降低信任，這是 Berg1995 事前也考慮過的相反方向 [Berg1995, p.12]。
- 〔待補〕需要 Xie2024 等 LLM 論文的資料，判斷 LLM 代理人是否會因為讀到社會歷史而改變信任行為。

## 相關頁面
- [社會歷史 (Social History)](../concepts/social-history.md)
- [信任 (Trust)](../concepts/trust.md)
- [信任賽局 (Trust Game)](../paradigms/trust-game.md)
- [信任、互惠與社會歷史 (Trust, Reciprocity, and Social History)](../papers/berg1995.md)
