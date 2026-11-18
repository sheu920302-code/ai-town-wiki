---
title: "大型語言模型作為模擬的經濟代理人：我們能從矽基人學到什麼？ (Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?)"
type: paper
summary: 主張大型語言模型是人類的隱性計算模型（矽基人），可以像經濟學家使用經濟人一樣給予設定、放進情境觀察行為；作者用數十個模型重現 5 個經典經濟實驗，得到和原研究相似的核心質性結果，並主張矽基人最好理解成可以靈活執行的理論。
sources: [Horton2026]
related: [concepts/homo-silicus.md, concepts/theory-grounded-personas.md, concepts/ai-simulation-validity.md, paradigms/dictator-game.md, concepts/instruction-tuning.md, town/theory-grounded-agent-types.md, syntheses/contradictions.md, glossary.md]
tags: [homo-silicus, llm-agents, experimental-economics, simulation]
status: draft
has_inference: true
created: 2026-11-18
updated: 2026-11-18
citekey: Horton2026
authors: [John J. Horton, Apostolos Filippas, Benjamin S. Manning]
year: 2026
venue: arXiv (econ.GN)
version: arXiv v2
raw_file: Horton_HomoSilicus.pdf
pdf_pages: 53
page_offset: 0
---
# 大型語言模型作為模擬的經濟代理人：我們能從矽基人學到什麼？ (Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?)

## 白話摘要
經濟學家常用一個理想化的「經濟人」推導人會怎麼做。作者認為，大型語言模型也可以當成一種人類模型，稱為矽基人：給它錢、資訊和偏好，放進情境裡，看它怎麼選。作者用數十個模型重現了 5 個經典實驗，包括漲價公不公平、獨裁者賽局、現狀偏誤、沒有風險時的展望理論，以及最低工資下的雇用，得到和原研究相似的核心質性結果。沒給人物設定的模型在獨裁者賽局和人類差很多；給代理人自利型、不平等趨避型、效率型三種設定，再依人類資料調整三者的比例後，在新賽局的預測誤差大約減半。作者強調，這些結果仍需要真人資料確認，並把矽基人理解成可以靈活執行的理論。

## 研究問題
- 作者主張，大型語言模型 (large language model) 因為訓練和設計的方式，可以視為人類的隱性計算模型，也就是矽基人 (Homo silicus) [Horton2026, p.2]。
- 矽基人可以像經濟學家使用經濟人 (Homo economicus) 一樣：給予稟賦、放進情境，再透過模擬觀察行為 [Horton2026, p.2]。
- 作者想回答，這類 AI 模擬為什麼、在什麼時候能幫助我們理解真實的人類 [Horton2026, p.2; Horton2026, p.6]。

## 方法
- 作者重現並延伸 4 個實驗室實驗和 1 個田野實驗 [Horton2026, p.6]。
- 作者刻意使用「重現」(recapitulate) 而不是「複製」(replicate)，因為不把 LLM 實驗視為原實驗的直接複本 [Horton2026, p.6]。
- 初稿使用已停用的 GPT-3，新版改用數十個開源和專有的模型 [Horton2026, p.4]。
- 作者發布開源 Python 套件，讓所有實驗都能換上幾乎任何模型、按一下就重跑 [Horton2026, p.5]。

## 主要發現
- 作者表示，這些實驗重現了對應人類實驗中的核心質性型態，偏離之處本身也可能對未來研究有啟發 [Horton2026, p.1; Horton2026, p.40]。
- 作者把主要概念貢獻概括為：矽基人最好理解成可以靈活執行的理論 [Horton2026, p.40]。
- 公平感：原研究中約 82% 的受試者認為雪後把鏟子從 $15 漲到 $20 不公平或非常不公平 [Horton2026, p.7]。
- 作者給 GPT-4 代理人從社會主義者到自由意志主義者的政治立場，左傾代理人認為漲價不公平，右傾代理人較能接受，漲得越多越被認為不公平 [Horton2026, p.7]。
- 作者把題目翻譯成 10 種語言、改寫成 10 種替代版本和 10 種對抗版本，都無法讓左傾代理人比右傾代理人更認為漲價公平 [Horton2026, p.9–10]。
- 獨裁者賽局 (Dictator Game)：沒給人物設定 (persona) 的代理人，選擇和人類受試者差很多，雖然原研究幾乎一定在訓練資料中 [Horton2026, p.12–13]。
- 作者給代理人三種設定：自利型 (self-interested)、不平等趨避型 (inequity-averse)、效率型 (efficient)，有設定的代理人大致照設定行動 [Horton2026, p.11; Horton2026, p.13]。
- 依人類資料調整三種設定的混合比例後，在新的兩階段賽局中，預測誤差（均方誤差，mean-squared error，MSE）是 0.094，約為沒給人物設定時 0.182 的一半 [Horton2026, p.15]。
- 現狀偏誤 (status quo bias)：所有代理人都有相當程度的現狀偏誤，GPT-4o 較輕微 [Horton2026, p.17]。
- 作者認為，即使經過大量的後訓練微調，人類選擇中可能不理想的捷思 (heuristic) 特徵仍然會出現在 LLM 的行為中 [Horton2026, p.18]。
- 展望理論 (prospect theory)：在 5 個模型、15,200 筆模擬中，有風險的樂透條件和沒有風險的鏡像條件結果同步，沒有出現只有樂透條件呈現四重型態 (fourfold pattern) 的情況 [Horton2026, p.19]。
- 作者認為這個結果支持 Oprea 的看法：四重型態不只是風險下的現象 [Horton2026, p.20]。
- 最低工資 (minimum wage)：用 43 個模型模擬雇主，沒有參考工資時，最低工資讓被雇用者的時薪增加約 $1.3 [Horton2026, p.22]。
- 有參考工資 (reference wage) 時，最低工資讓雇主雇用的人平均多約三個月的經驗，方向和 Horton (2025) 的田野實驗一致 [Horton2026, p.23]。

## 限制
- 作者表示，最終關心的是真實人類的行為，所以 AI 實驗的結果仍需要實證確認 [Horton2026, p.5]。
- 作者表示，訓練資料的兩種資訊來源都不完整、也不具代表性，所以 AI 模擬不應被當成人類行為的確定證據 [Horton2026, p.25]。
- 作者表示，隨著新模型推出，他們更新後的實驗也會過時 [Horton2026, p.4]。
- 論文揭露作者之一是 Anthropic 的經濟顧問，所有作者都和 expectedparrot.com 有財務利益 [Horton2026, p.1]。
- 〔推論〕讀者應注意潛在的利益衝突。

## 關鍵引文
> "In this paper, we argue that large language models (LLMs)—because of how they are trained and designed—can be thought of as implicit computational models of humans—a Homo silicus." [Horton2026, p.2]
> 中譯：本文主張，大型語言模型因為訓練和設計的方式，可以被視為人類的隱性計算模型，也就是矽基人。

> "The MSE of the calibrated samples (0.094) is about half of the persona-less control MSE (0.182)." [Horton2026, p.15]
> 中譯：校準後樣本的均方誤差 (0.094) 約為沒有人物設定的對照組 (0.182) 的一半。

## 相關頁面
- [矽基人 (Homo Silicus)](../concepts/homo-silicus.md)
- [理論導向的人物設定 (Theory-Grounded Personas)](../concepts/theory-grounded-personas.md)
- [AI 模擬的效度 (Validity of AI Simulations)](../concepts/ai-simulation-validity.md)
- [獨裁者賽局 (Dictator Game)](../paradigms/dictator-game.md)
- [指令微調 (Instruction Tuning)](../concepts/instruction-tuning.md)
- [用理論類型設計小鎮代理人 (Theory-Grounded Agent Types for the Town)](../town/theory-grounded-agent-types.md)
- [矛盾總表 (Contradictions)](../syntheses/contradictions.md)
- [術語表 (Glossary)](../glossary.md)
