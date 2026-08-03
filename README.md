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

The conversational layer may be ChatGPT Voice or another voice-capable assistant. This repository provides the coaching logic and report structure. Version 0.1 does not automatically connect ChatGPT Voice to local files or ChatGPT history.

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
├── skill/
│   └── ielts-speaking-coach/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── references/
│       └── assets/session_report_template.md
├── data/README.md
└── docs/roadmap.md
```

## How to Use Version 0.1

Use the skill instructions in an environment that supports skills, or adapt the rules into a ChatGPT Project or Custom GPT instruction set. Supply a transcript or approved personal source when requesting historical review.

Example requests:

- `Start today's IELTS speaking practice.`
- `Run an IELTS Speaking mock test and do not correct me until the end.`
- `Review this transcript and improve my answers toward Band 7.5.`
- `Summarize my repeated errors and prepare a session report.`

## Privacy

Personal answer banks, transcripts, databases, work documents, and generated reports are intentionally excluded from Git. Only reusable rules, templates, and public documentation belong in this repository.
