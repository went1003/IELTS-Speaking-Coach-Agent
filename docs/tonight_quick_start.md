# Tonight Quick Start

This is the minimum no-API workflow for completing one useful speaking session tonight.

## Daily Shortcut

The longer `Read docs...` message is only a first-time setup test. For normal daily use, open this local project, start Voice, and say:

```text
开始今天的 IELTS 口语练习。
```

The skill should activate implicitly, read the default private topic-bank path, and begin a 15-minute Topic Focus session. If implicit activation does not occur, explicitly select `IELTS Speaking Coach` once and repeat the same sentence.

## Before the Session

1. Open the `IELTS-Speaking-Coach-Agent` folder as a local project in the ChatGPT desktop app.
2. Keep this folder as the project's primary folder so the app can automatically discover `.agents/skills/ielts-speaking-coach`.
3. Confirm that the `IELTS Speaking Coach` skill appears in the skill selector.
4. Start a new chat inside this local project.
5. For the first setup test only, select the skill and send the text in `docs/tonight_session_starter.md`.
6. Start Voice after the first question appears.

## During the Session

- Answer naturally instead of reading the model answer word for word.
- Let the coach ask one question at a time.
- If the coach becomes too verbose, say: `Please keep the practice conversational and save detailed feedback until the end.`
- If a personal detail is wrong, correct it immediately so it is not reused later.

## End the Session

Say: `Please summarize this session now.`

Check that the response contains:

- approximate band range;
- priority corrections;
- Band 7.5-level alternatives;
- reusable expressions and verb phrases;
- topic reuse suggestions;
- repeat-practice sentences;
- a short spoken recap.

Version 0.1 does not automatically save a Word report or long-term database record. Preserve the chat after the session; report export and persistent error tracking are planned for later versions.
