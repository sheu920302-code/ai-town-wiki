# Wiki 目錄

主題：AI 代理人模擬人類社會行為（信任、合作、背叛）。維護規則見 [AGENTS.md](../AGENTS.md)。

格式：`- [標題](相對路徑) — summary`

## 論文 (Papers)

- [合作的演化 (The Evolution of Cooperation)](papers/axelrod1981.md) — 用囚犯困境模型和電腦競賽說明，以互惠為基礎的合作可以在自私的世界中出現、擴散，並在站穩後維持下去。
- [信任、互惠與社會歷史 (Trust, Reciprocity, and Social History)](papers/berg1995.md) — 在單次、完全匿名的投資賽局中，多數人仍會送錢給陌生人，部分收到錢的人回報多於對方送出的金額；提供前一批人的決策摘要後，回報增加。
- [生成式代理人：人類行為的互動模擬 (Generative Agents: Interactive Simulacra of Human Behavior)](papers/park2023.md) — 用大型語言模型加上記憶流、反思、規劃三個元件，打造能模擬可信人類行為的生成式代理人，並讓 25 個代理人在沙盒小鎮 Smallville 中互動兩天，觀察到資訊擴散、關係形成和協調等湧現行為。
- [大型語言模型代理人能模擬人類的信任行為嗎？ (Can Large Language Model Agents Simulate Human Trust Behavior?)](papers/xie2024.md) — 用信任賽局等 6 種賽局測試 GPT-4、GPT-3.5、Llama2、Vicuna 等多種 LLM 代理人，發現它們大致都有信任行為，GPT-4 和人類的行為一致性最高；代理人的信任也有性別和種族偏誤、比較信任人類，而且被要求降低信任比被要求提高信任更容易生效。
- [大型語言模型作為模擬的經濟代理人：我們能從矽基人學到什麼？ (Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?)](papers/horton2026.md) — 主張大型語言模型是人類的隱性計算模型（矽基人），可以像經濟學家使用經濟人一樣給予設定、放進情境觀察行為；作者用數十個模型重現 5 個經典經濟實驗，得到和原研究相似的核心質性結果，並主張矽基人最好理解成可以靈活執行的理論。

## 概念 (Concepts)

- [再相遇機率 (Continuation Probability)](concepts/continuation-probability.md) — 這次互動結束後，同樣兩人會再碰面的機率 w；w 夠高時，以互惠為基礎的合作才會穩定。
- [演化穩定策略 (Evolutionarily Stable Strategy)](concepts/evolutionarily-stable-strategy.md) — 一群人都用同一個策略時，少數改用其他策略的突變者無法入侵，這個策略就是演化穩定的。
- [互惠 (Reciprocity)](concepts/reciprocity.md) — 以牙還牙照做對方上一步，Axelrod1981 稱之為以互惠為基礎的合作；合作要能演化，其中兩個條件是背叛者逃不過有效的報復，以及雙方再相遇的機率夠高；Berg1995 的人類實驗則發現，單次、完全匿名時仍有部分人回報對方的信任。
- [以牙還牙 (Tit-for-Tat)](concepts/tit-for-tat.md) — 第一步合作、之後照做對方上一步的策略；第一輪電腦競賽平均分最高，第二輪再次獲勝。
- [個體辨識 (Individual Recognition)](concepts/individual-recognition.md) — 認出先前的互動對象、分辨不同個體的能力；它讓獎勵合作、懲罰背叛成為可能，認不出個體的生物則要靠替代機制。
- [利他 (Altruism)](concepts/altruism.md) — 犧牲自己的適應度去讓別人得益；Axelrod1981 把親屬理論和互惠理論分開解釋合作，Berg1995 則用獨裁者賽局的給予和投資賽局的回報做對照。
- [報復 (Retaliation)](concepts/retaliation.md) — 對背叛或不當行為做出反擊；Axelrod1981 認為有效的報復是合作演化的條件之一，Berg1995 則刻意排除懲罰威脅，並指出人們願意付出代價懲罰不當行為。
- [社會歷史 (Social History)](concepts/social-history.md) — 讓受試者先看到前一批人在同一個遊戲中怎麼做的摘要；Berg1995 的社會歷史組平均回報較高，送出與回報的相關也變強。
- [信任 (Trust)](concepts/trust.md) — 信任者把決定權交給受託者，自己承擔風險；Berg1995 採用和 Coleman 相近的定義，並認為信任可能是經濟行為的基本元素。
- [湧現的社會行為 (Emergent Social Behavior)](concepts/emergent-social-behavior.md) — 沒有事先寫好腳本、而是代理人互動後自然出現的群體行為；Park2023 測量了資訊擴散、關係形成和協調三種，例如派對消息從 1 位傳到 13 位、網路密度從 0.167 升到 0.74。
- [生成式代理人 (Generative Agent)](concepts/generative-agent.md) — 以大型語言模型為核心，加上記憶流、反思、規劃三個元件，能依自己過去的經歷和環境產生可信人類行為的計算代理人；作者強調它們沒有真正的能動性。
- [記憶流 (Memory Stream)](concepts/memory-stream.md) — 用自然語言完整記錄代理人所有經歷的資料庫；需要時依新近性、重要性、相關性三項分數取出最相關的記憶，再交給語言模型。
- [規劃 (Planning)](concepts/planning.md) — 代理人由上而下把一天的大致行程逐層拆成細部行動，存進記憶流；每個時間步再依觀察決定照原計畫進行或做出反應，需要互動時生成對話。
- [反思 (Reflection)](concepts/reflection.md) — 代理人定期把近期記憶整理成較高層、較抽象的想法，存回記憶流；Park2023 中重要性分數累積超過 150 時觸發，一天約兩到三次。
- [可信度 (Believability)](concepts/believability.md) — 代理人的行為讓人覺得像真人、像是自己在做決定的程度；Park2023 把它當作設計目標和評估的依變數，由人類評分者依可信度排序。
- [受控評估與消融 (Controlled Evaluation and Ablation)](concepts/evaluation-and-ablation.md) — Park2023 檢驗架構的方法：用自然語言訪談代理人五類能力，比較完整架構、三種拿掉元件的消融版本和人類群眾外包工作者的回答，由 100 位評分者依可信度排序，再轉成 TrueSkill 評分並做統計檢定。
- [生成式代理人的倫理風險 (Ethical Risks of Generative Agents)](concepts/generative-agent-ethics.md) — Park2023 列出四種風險：類社會關係 (parasocial relationship)、錯誤推論造成的傷害、深度偽造和量身說服等濫用，以及過度依賴代理人而取代真人；並提出揭露身分、價值對齊、保留稽核紀錄、不取代真人意見等原則。
- [幻覺 (Hallucination)](concepts/hallucination.md) — Park2023 所說的幻覺主要是加油添醋：代理人很少完全捏造，也沒有主動宣稱經歷過沒發生的事；錯誤還包括取不到記憶、只取到片段，或在已知的事上加入沒發生的細節，語言模型本身的世界知識也會滲入。
- [指令微調 (Instruction Tuning)](concepts/instruction-tuning.md) — Park2023 推測，底層模型的指令微調可能讓生成式代理人說話過於正式、整體上更客氣更合作，彼此之間似乎也過度合作；例如 Isabella 很少拒絕別人的點子。
- [檢索 (Retrieval)](concepts/retrieval.md) — 依代理人目前的情境，從記憶流中挑出最相關的一部分記憶交給語言模型；Park2023 用新近性、重要性、相關性三項分數加總排序，取放得進上下文視窗的最高分記憶。
- [代理人的穩健性 (Robustness of Generative Agents)](concepts/agent-robustness.md) — Park2023 表示生成式代理人的穩健性大致仍未知；作者列出的弱點包括提示攻擊、記憶攻擊和幻覺，而且代理人會繼承語言模型的缺陷。
- [反應與對話 (Reacting and Dialogue)](concepts/reacting-and-dialogue.md) — 生成式代理人在每個時間步感知周遭、決定照原計畫進行或做出反應；決定和其他代理人互動時，雙方各自依對彼此的記憶生成一句句對話，直到一方結束。
- [代理人信任的特性 (Properties of Agent Trust)](concepts/agent-trust-properties.md) — Xie2024 改變信任賽局的條件，發現代理人的信任有性別和種族偏誤、比較信任人類而不是其他代理人、被要求降低信任比被要求提高信任更容易生效，也可能受思維鏈推理影響。
- [行為一致性 (Behavioral Alignment)](concepts/behavioral-alignment.md) — Xie2024 提出的概念：比較大型語言模型和人類在影響行為的因素（行為因素）和行為隨時間的變化（行為動態）上是否相似，同時看行動和背後的推理；在信任行為上，GPT-4 的一致性最高。
- [信任的行為因素 (Behavioral Factors of Trust)](concepts/trust-behavioral-factors.md) — 人類研究指出三個影響信任行為的基本因素：預期互惠、風險感知和利社會偏好；Xie2024 用信任賽局的不同變化版本逐一比較，發現 GPT-4 在三個因素上都和人類相似，部分小模型則不然。
- [AI 模擬的效度 (Validity of AI Simulations)](concepts/ai-simulation-validity.md) — Horton2026 討論用 LLM 模擬人類時的效度問題：背誦和展演性、黑盒子、反覆換提示直到結果漂亮、因果推論和外部效度；作者建議公開程式碼、用多種提示版本做穩健性檢查，並以真人資料當基準。
- [矽基人 (Homo Silicus)](concepts/homo-silicus.md) — Horton2026 對大型語言模型的比喻：它是人類的隱性計算模型，可以像經濟人一樣給予設定、放進情境觀察行為；作者認為它最好理解成可以靈活執行的理論，適合試跑實驗和探索新情境、產生假說，但結果仍需要真人資料確認。
- [理論導向的人物設定 (Theory-Grounded Personas)](concepts/theory-grounded-personas.md) — 依某個可檢驗的理論設計代理人的人物設定，例如只在乎公平、只在乎總報酬、只在乎自己；Horton2026 把這三種設定依人類資料調整混合比例後，在新賽局的預測誤差約減半，而 Horton2026 引用的研究指出，和理論無關的特質幾乎沒有幫助。

## 實驗範式 (Paradigms)

- [囚犯困境 (Prisoner's Dilemma)](paradigms/prisoners-dilemma.md) — 兩人各自選擇合作或背叛；不管對方怎麼選，背叛都比較划算，但兩人都背叛時比兩人都合作還差。
- [Axelrod 電腦競賽 (Axelrod Computer Tournament)](paradigms/axelrod-tournament.md) — 讓各方提交的重複囚犯困境策略互相對戰的兩輪電腦競賽；第一輪由以牙還牙拿到最高平均分，第二輪以牙還牙再次獲勝。
- [信任賽局 (Trust Game)](paradigms/trust-game.md) — 甲方決定把多少錢交給匿名的乙方，錢會變成三倍，乙方再決定還多少；理論預測不送，實驗中多數人仍會送。
- [獨裁者賽局 (Dictator Game)](paradigms/dictator-game.md) — 一方拿到一筆錢，決定分多少給另一方，對方不能回應；Berg1995 用它對照投資賽局的回報，Xie2024 用它和信任賽局比較，檢查人類和代理人是否會預期互惠。
- [重複信任賽局 (Repeated Trust Game)](paradigms/repeated-trust-game.md) — 同樣兩人連續玩多輪信任賽局，每輪信任者都拿到相同的初始金額；人類有三個常見規律，GPT-4 在 16 組中大多符合，GPT-3.5 較少符合。

## 綜合 (Syntheses)

- [矛盾總表 (Contradictions)](syntheses/contradictions.md) — 整理論文之間看似衝突的主張，並列出處、適用條件和處理狀態。

## 小鎮應用 (Town)

- [互惠需要無法匿名 (Reciprocity Requires Non-Anonymity)](town/reciprocity-requires-non-anonymity.md) — 以互惠為基礎的合作要能演化，背叛者不能隱沒在匿名的人群中（靠辨識個體或替代機制），而且雙方再相遇的機率要夠高。
- [社會歷史會影響信任 (Social History Shapes Trust)](town/social-history-shapes-trust.md) — 讓人先看到前一批人怎麼做的摘要後，平均回報提高、送出與回報的相關變強，但部分變化不顯著。
- [指令微調讓代理人過度合作 (Instruction Tuning Makes Agents Too Cooperative)](town/instruction-tuning-makes-agents-too-cooperative.md) — Park2023 觀察到，指令微調似乎讓代理人更客氣、彼此過度合作；例如 Isabella 很少拒絕和自己興趣不合的點子，時間久了，自己的興趣也被別人改變。
- [保留可查核的交易紀錄 (Auditable Transaction Log)](town/auditable-transaction-log.md) — 生成式代理人可能取不到記憶、只取到片段或加油添醋，也可能被精心設計的對話說服而相信沒發生的事；Park2023 另外針對濫用風險建議平台保留稽核紀錄；Axelrod1981 則指出，背叛者必須逃不過報復，合作才能演化。
- [用理論類型設計小鎮代理人 (Theory-Grounded Agent Types for the Town)](town/theory-grounded-agent-types.md) — Horton2026 發現，沒給設定的模型在獨裁者賽局和人類差很多，給予自利、公平、效率等理論導向的設定並依人類資料調整混合比例後，預測誤差約減半；Horton2026 引用的研究指出，和理論無關的特質幾乎沒有幫助。

## 術語表 (Glossary)

- [術語表 (Glossary)](glossary.md) — 本 wiki 使用的術語中英對照、一句定義與出處，所有頁面的用詞以此為準。
