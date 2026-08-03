# IELTS Speaking Coach Agent

A privacy-first, no-API workflow for personalized IELTS Speaking practice, feedback, long-term error tracking, and review.

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

The conversational layer may be ChatGPT Voice or another voice-capable assistant. This repository provides the coaching logic and report structure. In a ChatGPT desktop local project, the skill can use files that the project is permitted to access. It does not automatically gain access to unrelated local folders or ChatGPT history.

## Version 0.1 Scope

- Daily conversation practice rules
- IELTS Speaking Part 1, Part 2, and Part 3 test behavior
- Topic-focused practice using personal material
- End-of-session feedback structure
- Approximate Band 7.5-level answer improvement
- Reusable collocations and verb-phrase extraction
- Real, adapted, model, and unverified source labels
- Privacy rules for personal documents and generated reports
- A reusable Markdown session-report template

## Not Included Yet

- OpenAI or DeepSeek API integration
- Automatic access to ChatGPT Voice history
- Automatic speech-to-text
- SQLite error history
- Automatic Word report generation
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
│           └── assets/session_report_template.md
├── data/README.md
└── docs/
    ├── roadmap.md
    └── tonight_quick_start.md
```

## How to Use Version 0.1

Open this repository as the primary folder of a ChatGPT desktop local project. The desktop app automatically discovers repository skills stored under `.agents/skills`. Start a chat in the project, explicitly select `IELTS Speaking Coach`, and then switch to Voice for spoken practice.

For a first working session, follow [`docs/tonight_quick_start.md`](docs/tonight_quick_start.md) and use the ready-made starter in [`docs/tonight_session_starter.md`](docs/tonight_session_starter.md).

After the first setup test, normal daily use is intentionally short: open the local project, start Voice, and say `开始今天的 IELTS 口语练习。` The skill then looks for the private topic bank at its default ignored path. Explicitly select `IELTS Speaking Coach` only when implicit activation does not occur.

Example requests:

- `Start today's IELTS speaking practice.`
- `Run an IELTS Speaking mock test and do not correct me until the end.`
- `Review this transcript and improve my answers toward Band 7.5.`
- `Summarize my repeated errors and prepare a session report.`

## Privacy

Personal answer banks, transcripts, databases, work documents, and generated reports are intentionally excluded from Git. Only reusable rules, templates, and public documentation belong in this repository.
