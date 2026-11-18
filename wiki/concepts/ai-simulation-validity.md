---
title: AI 模擬的效度 (Validity of AI Simulations)
type: concept
summary: Horton2026 討論用 LLM 模擬人類時的效度問題：背誦和展演性、黑盒子、反覆換提示直到結果漂亮、因果推論和外部效度；作者建議公開程式碼、用多種提示版本做穩健性檢查，並以真人資料當基準。
sources: [Horton2026]
related: [concepts/homo-silicus.md, concepts/theory-grounded-personas.md, concepts/believability.md, concepts/behavioral-alignment.md, papers/horton2026.md, glossary.md]
tags: [validity, simulation, methodology, llm-agents]
status: draft
has_inference: true
created: 2026-11-18
updated: 2026-11-18
---
# AI 模擬的效度 (Validity of AI Simulations)

## 白話摘要
用 AI 代理人模擬人類，最大的疑問是：結果能不能信？Horton2026 逐一討論幾個常見的質疑：模型會不會只是背出訓練資料裡的研究結果、研究者會不會一直換提示直到得到想要的結果、AI 實驗能不能做因果推論。作者的建議是：公開所有程式碼、用翻譯和改寫等多種版本做穩健性檢查 (robustness check)，而且要有真人資料當比較基準。作者也提醒，AI 模擬可能幫上忙，也可能帶來錯誤的結論。

## 定義
- 作者用一個四象限來看 AI 模擬的結果：支持真命題的真陽性 (true positive)、拒絕假命題的真陰性 (true negative)、支持假命題的偽陽性 (false positive)，以及拒絕真命題的偽陰性 (false negative) [Horton2026, p.31]。
- 研究者在真陽性和真陰性時受益，在偽陽性或忽略既有可靠結果時，AI 模擬可能放大錯誤 [Horton2026, p.31]。

> "Ultimately, we care about the behavior of actual humans, and so results from AI experiments will still require empirical confirmation (Ludwig et al., 2025)." [Horton2026, p.5]
> 中譯：我們最終關心的是真實人類的行為，所以 AI 實驗的結果仍需要實證確認。

## 各論文的觀點

### Horton2026

#### 背誦和展演性
- 有人擔心 LLM 只是背出訓練資料中的內容；作者指出，在訓練資料中已有的情境裡，AI 和人類受試者的回答仍有差異，所以不完全是背誦 [Horton2026, p.35]。
- 作者用囚犯困境 (Prisoner's Dilemma) 比喻：只背下「雙方都背叛是唯一的純策略納許均衡 (Nash equilibrium)」的學生無法類推，懂得均衡定義的學生才能應用到新情境 [Horton2026, p.35]。
- 展演性 (performativity) 是指代理人可能照著訓練資料中的理論和實證結果行動；作者認為，如果理論本身正確，這可能反而是優點 [Horton2026, p.35]。
- 為了測試是否只是背誦，作者把公平感實驗翻成 10 種語言、改寫成 10 種替代版本和 10 種對抗版本 [Horton2026, p.9]。

#### 黑盒子
- 作者指出，LLM 是黑盒子，可能以意想不到的方式無法類推 [Horton2026, p.29]。
- 目前還不知道為什麼某個提示能改善表現，也不知道驅動這些改善的內部表示和人類行為有什麼關係，所以「提示有效就代表人類照這個理論行事」的推論還太強 [Horton2026, p.30]。

#### 換提示直到結果漂亮
- 作者指出，研究者可能一直換提示，直到得到想要的結果，只報告有利的結果，這在概念上類似傳統實驗的 p-hacking [Horton2026, p.38]。
- 作者提出兩個解法：在多種部分受控的提示版本下呈現結果，以及公開所有模擬程式碼 [Horton2026, p.38]。

#### 因果推論 (causal inference)
- 雖然只有一個模型，但可以透過不同的提示讓它扮演很多不同的代理人，所以矽基人 (Homo silicus) 不只一個 [Horton2026, p.38]。
- 修改提示中的一個因素，可能不小心改變其他因素；作者認為這是外部效度 (external validity) 的問題，人類實驗也會遇到 [Horton2026, p.39]。
- 最低工資實驗中，有沒有提供參考工資會改變結果，作者推測沒提供時模型會自己補上一個參考工資 [Horton2026, p.39]。

#### 什麼時候比較可信
- 要得到無偏的推論，研究者通常需要真人資料作為基準 [Horton2026, p.32]。
- 模型在訓練資料中出現較多的領域，表現通常較好 [Horton2026, p.33]。
- 作者也指出，受過訓練的社會科學家預測實驗結果的能力也出乎意料地差，所以有用的預測工具門檻可能比想像中低 [Horton2026, p.31–32]。

## 爭議與未解問題
- 〔推論〕Park2023 用人類評分者判斷可信度，Xie2024 和 Horton2026 都拿既有的人類實驗結果當基準；後兩者比較接近 Horton2026 所說「需要真人資料當基準」的要求。
- 〔推論〕北大小鎮的模擬結果應定位為假設產生和試跑，報告時也應公開提示和程式碼，並至少用兩種提示版本確認結果穩健。

## 相關頁面
- [矽基人 (Homo Silicus)](homo-silicus.md)
- [理論導向的人物設定 (Theory-Grounded Personas)](theory-grounded-personas.md)
- [可信度 (Believability)](believability.md)
- [行為一致性 (Behavioral Alignment)](behavioral-alignment.md)
- [大型語言模型作為模擬的經濟代理人：我們能從矽基人學到什麼？ (Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?)](../papers/horton2026.md)
- [術語表 (Glossary)](../glossary.md)
