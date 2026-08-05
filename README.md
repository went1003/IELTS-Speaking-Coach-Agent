# IELTS Speaking Coach Agent

A privacy-first, no-API workflow for personalized IELTS Speaking practice, feedback, long-term error tracking, and review.

**Status:** Working local prototype (v0.2), tested with ChatGPT Voice and Codex. No external AI API is required for the current workflow.

**中文简介：** 这是一个面向个人雅思口语训练的 Voice-first AI 学习工作流。它结合 ChatGPT Voice、可复用 Skill 规则与本地 Word 报告，在不接入外部 AI API 的情况下完成练习、纠错、重复复习和学习记录。

## Why This Is a Separate Project

The earlier `IELTS-Speaking-Personal-Coach` repository explored an offline Streamlit recording and playback prototype. That prototype answered a technical question: can a small local web app guide recording and replay without an AI API?

This repository addresses a different product problem. It defines a reusable coaching skill and a future learning-record system that complement voice conversation instead of recreating a voice interface.

## Product Concept

The intended workflow is:

```text
Voice or text practice
        -> structured coaching rules
        -> end-of-session feedback
        -> reusable language and error records
        -> review in a later session
```

The current reference implementation is optimized for ChatGPT Voice and Codex. This repository provides the coaching logic, local-file workflow, and report structure. In a ChatGPT desktop local project, the skill can use files that the project is permitted to access. It does not automatically gain access to unrelated local folders or ChatGPT history.

The core coaching workflow is platform-independent, but the skill package is not a universal plug-in format. The questioning, correction, review, and reporting rules could later be adapted for another voice-capable platform such as WorkBuddy or Tencent Yuanbao. Platform-specific discovery, permissions, local-file access, voice behavior, and Word generation would need separate implementation and testing.

## Current Scope - Version 0.2

- Daily conversation practice rules
- English-first voice practice, including the opening question and transitions
- IELTS Speaking Part 1, Part 2, and Part 3 test behavior
- Topic-focused practice using personal material
- End-of-session feedback structure
- Natural Band 7-level answer improvement without forced or overly fancy vocabulary
- Reusable collocations and verb-phrase extraction
- Capture of Chinese-to-English language gaps with alternatives and usage distinctions
- Compact one- or two-page A4 daily reports with an aligned annotation margin
- A deterministic local Word report builder
- Separate weekly progress reports on request
- Real, adapted, model, and unverified source labels
- Privacy rules for personal documents and generated reports
- A reusable Markdown session-report template

## Not Included Yet

- OpenAI or DeepSeek API integration
- Automatic access to ChatGPT Voice history
- Automatic speech-to-text
- SQLite error history
- A hosted or API-driven Word report service
- Cloud deployment or multi-user accounts

## Repository Structure

```text
IELTS-Speaking-Coach-Agent/
├── README.md
├── .gitignore
├── .agents/
│   └── skills/
│       └── ielts-speaking-coach/
│           ├── SKILL.md
│           ├── agents/openai.yaml
│           ├── references/
│           ├── assets/session_report_template.md
│           ├── assets/weekly_report_template.md
│           └── scripts/build_session_report.py
├── data/README.md
└── docs/
    ├── roadmap.md
    ├── tonight_quick_start.md
    ├── ielts_speaking_coach_agent_pm_case_study_bilingual.md
    └── wechat_article_ielts_speaking_coach_agent_development_story.md
```

## How to Use Version 0.2

Open this repository as the primary folder of a ChatGPT desktop local project. The desktop app automatically discovers repository skills stored under `.agents/skills`. Start a chat in the project, explicitly select `IELTS Speaking Coach`, and then switch to Voice for spoken practice.

For a first working session, follow [`docs/tonight_quick_start.md`](docs/tonight_quick_start.md) and use the ready-made starter in [`docs/tonight_session_starter.md`](docs/tonight_session_starter.md).

After the first setup test, normal daily use is intentionally short: open the local project, start Voice, and say `Start today's IELTS speaking practice.` A Chinese trigger phrase also works, but the coach begins the practice itself in English. The skill then looks for the private topic bank at its default ignored path. Explicitly select `IELTS Speaking Coach` only when implicit activation does not occur.

Example requests:

- `Start today's IELTS speaking practice.`
- `Run an IELTS Speaking mock test and do not correct me until the end.`
- `Review this transcript and improve my answers toward Band 7.5.`
- `Summarize my repeated errors and prepare a session report.`

During practice, the learner may ask a short Chinese vocabulary question such as `大城市怎么说？`. The coach records this as a Language gap, offers natural alternatives such as `major city`, `big city`, and `large metropolitan area`, and reuses the best option in the corrected answer and report.

## Project Documentation

- [Bilingual PM case study](docs/ielts_speaking_coach_agent_pm_case_study_bilingual.md) — an English-Chinese product narrative covering the original recorder prototype, the product pivot, the voice-first workflow, validation, limitations, and portfolio positioning.
- [Development story for WeChat](docs/wechat_article_ielts_speaking_coach_agent_development_story.md) — a two-part Chinese article about the development process, reusable mistakes, and the screen-free driving use case.
- Word editions are stored in the same `docs` folder for offline reading, printing, and portfolio preparation.

## Portfolio Relevance

This project demonstrates a complete small-product workflow rather than only a prompt file:

- Product discovery: the original offline recorder was tested, evaluated, and deliberately reframed around the learner's real Voice workflow.
- Prompt and interaction design: practice modes, test-mode boundaries, correction behavior, repeat-review loops, and report triggers are documented as reusable rules.
- Document automation: structured session data is converted into a compact bilingual A4 Word report with aligned study notes.
- Privacy-first engineering: personal topic banks, transcripts, reports, databases, and local configuration remain outside the public repository.
- Iterative development: real practice sessions produced specific product changes, validation steps, and version-controlled improvements.

## Privacy

Personal answer banks, transcripts, databases, work documents, and generated reports are intentionally excluded from Git. Only reusable rules, templates, and public documentation belong in this repository.

Public skill files use relative or home-relative paths. User-specific absolute paths and private local configuration must not be committed.
