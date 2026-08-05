# IELTS Speaking Coach Agent — Bilingual PM Product Case Study

**From an Offline Prototype to a Voice-Native Personal Learning Workflow｜从离线原型到以语音为核心的个人学习工作流**

_Version 0.2 Working Prototype  |  5 August 2026  |  Personal AI Product Case_

| English | 中文 |
|---|---|
| **PRODUCT CASE STUDY & PM PRESENTATION SCRIPT**<br>A bilingual explanation of why the first recorder prototype led to a product pivot, how the Voice-based coaching skill was built, what has been validated, and what remains deliberately unfinished. | **产品案例复盘与 PM 双语介绍稿**<br>用中英双语说明：为什么第一版录音原型触发了产品转向、基于 Voice 的教练 Skill 如何形成、目前验证到了哪一步，以及哪些部分被有意留到以后。 |

## 1. Previous Project as the Product Prologue

### 前情提要：旧项目如何成为产品转向的证据

| English | 中文 |
|---|---|
| **Original attempt**<br>The earlier IELTS Speaking Personal Coach repository tested a no-API Streamlit flow: show a question, record an answer, replay it, review prompts, and record again. It completed the first idea-to-GitHub publishing loop. | **最初尝试**<br>上一仓库 IELTS Speaking Personal Coach 测试了一个不接 API 的 Streamlit 流程：显示题目、录音、回放、查看提示、再次录音，并第一次完整走通了从想法到 GitHub 发布的闭环。 |
| **Validated mismatch**<br>The recorder worked technically, but it could not understand speech, diagnose language, guide a conversation, or preserve learning. Rebuilding those capabilities would duplicate the stronger Voice experience already available. | **被验证的错位**<br>录音工具在技术上可以运行，但它不能理解语音、诊断语言、推进对话或沉淀学习记录。继续补齐这些能力，实际上是在重复已有且更成熟的 Voice 体验。 |
| **Product decision**<br>The first project was not abandoned. It became validated evidence for a pivot: keep the voice interface that already works, and build the learning rules, review loop, reports, and privacy boundary around it. | **产品决策**<br>第一个项目并不是被放弃，而是完成了验证任务，并成为产品转向的证据：保留已经好用的语音界面，把开发重点放到学习规则、复习闭环、报告和隐私边界上。 |

## 2. Real User Context — Voice-First and Screen-Free

### 真实使用场景：以语音为主，尽量不看屏幕

| English | 中文 |
|---|---|
| **Primary user**<br>I am the first user. I already have a personal answer bank, recurring language problems, and fixed periods such as driving time when looking at a screen is unsafe or impossible. | **第一位用户**<br>我是这个产品的第一位用户。我已经有个人答案库和反复出现的语言问题，也有开车等无法安全查看屏幕的固定时间。 |
| **Core job to be done**<br>The product must let me begin speaking quickly, keep the interaction concise, stop questioning when I request a summary, read corrected answers aloud, and preserve detailed feedback for later study. | **核心使用任务**<br>产品必须让我快速开口、保持简洁互动；当我要求总结时立即停止提问；能够朗读修正答案，并把详细反馈保存下来供以后复习。 |
| **Success criterion**<br>Success is not a feature-heavy standalone app. It is a repeatable hands-free learning loop that fits an existing daily routine and reduces the manual work previously required after every Voice session. | **成功标准**<br>成功不等于做出功能繁多的独立 App，而是建立一套可重复、适合免手操作、能够嵌入日常时间，并减少每次 Voice 练习后手工整理工作的学习闭环。 |

## 3. Product Definition and MVP Boundary

### 产品定义与 MVP 边界

| English | 中文 |
|---|---|
| **What the product is**<br>IELTS Speaking Coach Agent is a reusable coaching Skill and local-file workflow. The repository uses the word Agent as the product concept, while the current implementation is a Skill package that ChatGPT Voice and Codex can invoke. | **它是什么**<br>IELTS Speaking Coach Agent 是一套可复用的教练 Skill 与本地文件工作流。仓库用 Agent 表达产品概念；当前真正实现的是可被 ChatGPT Voice 和 Codex 调用的 Skill 包。 |
| **Completed v0.2 scope**<br>The working prototype covers English-first practice, Daily Conversation and IELTS modes, selective correction, Chinese-to-English language-gap capture, Guided Repeat Review, targeted replay, and compact daily or weekly report rules. | **v0.2 已完成范围**<br>可用原型已覆盖英文开场、日常对话与雅思模式、选择性纠错、中译英表达缺口记录、引导式复习、定向重读，以及紧凑的日报和周报规则。 |
| **Deliberate exclusions**<br>The MVP does not include an external API, cloud deployment, multi-user accounts, automatic access to unrelated ChatGPT history, automatic speech analysis, an SQLite learning database, or official IELTS scoring. | **主动排除项**<br>MVP 暂不包含外部 API、云端部署、多用户、自动读取无关 ChatGPT 历史、自动语音分析、SQLite 学习数据库或官方雅思评分。 |

## 4. System Design — Voice, Skill, and Local Files

### 系统设计：Voice、Skill 与本地文件

| English | 中文 |
|---|---|
| **Conversation layer**<br>ChatGPT Voice handles listening, speaking, turn-taking, interruption, and the natural rhythm of practice. The project does not rebuild microphone capture or speech playback. | **对话层**<br>ChatGPT Voice 负责倾听、说话、轮流对话、打断和自然练习节奏；项目不再重新开发麦克风录音或语音播放。 |
| **Coaching layer**<br>The Skill defines how to ask questions, when corrections are allowed, how to improve basic wording without forcing fancy vocabulary, how to treat Chinese questions, and how to close a session consistently. | **教练规则层**<br>Skill 规定如何提问、何时允许纠错、如何在不堆砌生僻词的前提下升级基础表达、如何处理中文提问，以及如何一致地结束练习。 |
| **Learning-record layer**<br>A private topic bank and separate session reports stay in ignored local folders. A deterministic Word builder turns structured session evidence into a compact two-column A4 report with space for handwritten notes. | **学习记录层**<br>私人话题库与单次训练报告保存在 Git 忽略的本地目录中。确定性的 Word 生成器把结构化练习证据转成双栏紧凑 A4 报告，并保留手写笔记空间。 |

## 5. Interaction Design Through Real Practice

### 通过真实练习迭代交互规则

| English | 中文 |
|---|---|
| **English-first opening**<br>Testing showed that a Chinese setup explanation delayed speaking. The rule was changed so that greeting, mode confirmation, first question, corrections, and transitions begin in English unless the learner explicitly requests Chinese. | **英文优先开场**<br>测试发现，中文设置说明会拖延开口。规则因此改为：除非学习者明确要求中文，否则问候、模式确认、第一道题、纠错和过渡都使用英文。 |
| **Natural rather than fancy**<br>Corrections follow a stable form: quote the learner, give a more natural version, name one primary issue, explain it briefly, and offer a stronger Band 7-level alternative when the original is vague or fragmented. | **自然，而不是刻意高级**<br>纠错使用稳定表达：引用学习者原话、给出更自然的说法、指出一个主要问题并简短解释；当原表达过于基础或零碎时，再提供自然的 Band 7 水平版本。 |
| **Chinese language gaps**<br>If the learner asks in Chinese how to express an idea, the coach answers briefly, records it as a Language gap rather than a grammar error, provides useful alternatives, and reuses the best choice in the corrected answer and report. | **中文表达缺口**<br>如果学习者用中文询问某个意思如何表达，教练会先简短回答，并把它记录为 Language gap，而不是语法错误；随后给出可用替代说法，并把最佳选项放入修正答案和报告。 |

## 6. Closing Loop — Feedback, Review, and Report

### 结束闭环：反馈、复习与报告

| English | 中文 |
|---|---|
| **Stop condition**<br>When the learner says “Please summarize” or “That’s all for today”, the coach stops all new questions immediately, separates evidence from estimates, and gives a short spoken recap suitable for listening while driving. | **停止条件**<br>当学习者说 “Please summarize” 或 “That’s all for today” 时，教练立即停止所有新问题，区分事实证据与估计，并给出适合驾车时收听的简短口头总结。 |
| **Guided Repeat Review**<br>The coach asks whether to read every practised question and corrected answer at a normal pace. It does not pause for shadowing. After one pass, the learner may replay everything, request only a selected question, or finish. | **引导式重复复习**<br>教练询问是否以正常语速朗读全部练习题与修正答案，不为跟读刻意停顿。完成一遍后，学习者可以重听全部内容、只重听指定问题，或结束复习。 |
| **Persistent output**<br>After the review is completed or skipped, a detailed report is generated automatically. Each session receives a separate file; reports are never merged or overwritten unless a weekly or monthly review is explicitly requested. | **可保存输出**<br>复习完成或被跳过后，系统自动生成详细报告。每次训练单独保存文件；除非明确要求周报或月报，否则不会自动合并或覆盖旧报告。 |

## 7. No-API Architecture, Privacy, and Portability

### 无 API 架构、隐私与平台适配

| English | 中文 |
|---|---|
| **Why no API yet**<br>The current workflow uses capabilities already available in ChatGPT Voice and Codex. API integration is deferred until repeated use proves that automatic transfer, deeper audio analysis, or cloud delivery is valuable enough to justify cost and maintenance. | **为什么暂不接 API**<br>当前工作流优先使用 ChatGPT Voice 与 Codex 已有能力。只有持续使用证明自动转移、更深语音分析或云端交付值得付出成本和维护时，才考虑 API 集成。 |
| **Privacy boundary**<br>GitHub contains reusable rules, templates, report code, and documentation. Personal topic banks, transcripts, reports, databases, local configuration, and secrets stay outside the public repository. | **隐私边界**<br>GitHub 只公开可复用规则、模板、报告代码和说明文档。个人话题库、对话文字稿、报告、数据库、本地配置和密钥都不进入公开仓库。 |
| **Platform boundary**<br>The coaching logic can be adapted to another voice platform, but the current Skill package is not a universal plug-in. Discovery, permissions, file access, voice behaviour, and Word generation must be reimplemented and tested per platform. | **平台边界**<br>教练逻辑可以适配其他语音平台，但当前 Skill 包不是通用插件。不同平台的发现机制、权限、文件访问、语音行为和 Word 生成都需要单独实现与测试。 |

## 8. Validation, Current Status, and Honest Limits

### 验证结果、当前状态与诚实限制

| English | 中文 |
|---|---|
| **Validated today**<br>The global Skill matches the repository version. Voice practice, multiple closing-flow iterations, targeted repeat rules, personal topic-bank lookup, and separate local Word reports have been exercised in real use. | **目前已验证**<br>全局安装的 Skill 与仓库版本一致。语音练习、多轮结束流程迭代、定向重读规则、个人话题库查找，以及独立本地 Word 报告都经过了真实使用。 |
| **What “complete” means**<br>Version 0.2 is complete as a working personal prototype and portfolio case. It is not a finished commercial product, autonomous cloud agent, official examiner, or platform-independent mobile application. | **“完成”的准确含义**<br>Version 0.2 已经作为个人可用原型和作品集案例完成；但它不是成熟商业产品、自治云端 Agent、官方考官或跨平台手机应用。 |
| **Known limitations**<br>Mobile Remote pairing remains unverified after testing stopped with an outdated iPhone ChatGPT app. Long-term querying across sessions still needs SQLite, and question sources must continue to be labelled accurately rather than called official without evidence. | **已知限制**<br>手机 Remote 配对尚未验证：本次测试在发现 iPhone ChatGPT App 未更新后暂停。跨训练长期查询仍需 SQLite；题目来源也必须继续准确标注，不能在没有证据时称为官方题目。 |

## 9. PM Takeaways and 60-Second Introduction

### PM 方法总结与 60 秒产品介绍

| English | 中文 |
|---|---|
| **PM takeaway**<br>The strongest product decision was not adding more technology. It was recognising a duplicated capability, narrowing the job to be done, testing rules through real sessions, and converting each failure into a specific interaction or reporting requirement. | **PM 方法总结**<br>最重要的产品决策不是继续增加技术，而是识别重复能力、收窄真实任务、通过实际练习测试规则，并把每次失败转化成具体的交互或报告要求。 |
| **60-second introduction**<br>IELTS Speaking Coach Agent is a voice-first personal learning workflow built from a product pivot. An earlier Streamlit recorder proved that recording alone did not solve the real problem and duplicated an existing Voice capability. I therefore kept ChatGPT Voice as the conversation layer and built a reusable Skill for questioning, correction, Chinese language gaps, guided replay, and structured Word reports. The current no-API v0.2 has been tested in real practice and keeps personal material outside GitHub. It demonstrates MVP scoping, evidence-based iteration, prompt and interaction design, document automation, privacy boundaries, and an honest distinction between a working prototype and a finished commercial product. | **60 秒产品介绍**<br>IELTS Speaking Coach Agent 是一套从产品转向中形成的、以语音为主的个人学习工作流。早期 Streamlit 录音原型证明：录音本身没有解决真实问题，而且重复了已有 Voice 能力。因此，我保留 ChatGPT Voice 作为对话层，并构建可复用 Skill，规范提问、纠错、中文表达缺口、引导式重听和结构化 Word 报告。目前无 API 的 v0.2 已经过真实练习测试，个人材料不会上传 GitHub。这个案例展示了 MVP 范围控制、基于证据的迭代、Prompt 与交互设计、文档自动化、隐私边界，以及如何诚实区分可用原型与成熟商业产品。 |
