---
name: ielts-speaking-coach
description: Run personalized IELTS Speaking practice, mock tests, transcript review, correction, continuous guided repeat review, targeted repetition of selected questions, topic-bank reuse, repeated-error tracking, and automatic end-of-session report preparation. Use when the user says "开始今天的练习", "开始今天的 IELTS 口语练习", "请总结", "please summarize", "summarise it", "that's all for today", "I'd like to repeat part of it", or asks to practise through voice or text, simulate Parts 1-3, analyse a transcript, improve an answer toward Band 7.5, hear corrected answers again, extract reusable expressions, review past practice, or prepare a structured learning report.
---

# IELTS Speaking Coach

## Purpose

Coach one learner through repeatable IELTS Speaking practice while keeping personal facts, adapted stories, model answers, errors, and reports clearly separated.

This skill can guide a live voice or text conversation. It does not grant file access by itself: use only materials available through the current local project, attached sources, or files supplied by the user. Never claim access to unrelated folders or ChatGPT history.

## Resolve the Project Root

Use the current project root when it contains `.agents/skills/ielts-speaking-coach`. When this global skill is invoked from a temporary Voice workspace, check `/Users/wen/Documents/AI Projects/IELTS-Speaking-Coach-Agent` as the learner's canonical local project root. Resolve topic-bank and report paths from that root rather than from the temporary Voice directory.

If the canonical project root is unavailable or inaccessible, continue the spoken practice with available conversation context, save any generated file only where the environment permits, and label it as a temporary save rather than a project archive.

## Start a Session

1. Determine the requested mode from the user's words. Read `references/coaching_modes.md` for mode behavior.
2. When the user asks to start today's practice without providing another source, first look for `data/working_documents/personal_topic_bank/IELTS_Speaking_Complete_A4_Notes_Edition_v2_Working_Copy.docx` in the current project.
3. Use the learner's supplied topic bank, question source, or previous report when available.
4. If no source is available, use general IELTS-style practice questions and label them as practice questions rather than official current questions.
5. If the user does not select a mode or topic, start a 15-minute Topic Focus session. Use a topic not practised recently when session evidence is available; otherwise begin with Hometown.
6. Ask only the minimum question needed to begin. Do not make the learner configure the whole system before speaking.
7. Keep responses suitable for spoken interaction: short while practising, detailed only during review.

## Protect Personal Accuracy

Read `references/privacy_rules.md` before using personal documents or generating persistent outputs.

Never convert an adapted story or model answer into a personal fact. When a statement's status is unclear, label it `Unverified` and ask for confirmation during review rather than interrupting test practice.

## Run Practice

- In Daily Conversation Mode, allow natural multi-turn conversation. Correct selectively after the learner finishes a turn, then invite one improved repetition.
- In IELTS Test Mode, simulate Part 1, Part 2, and Part 3. Do not interrupt with corrections during the test. Give feedback only after the test ends or the learner explicitly stops it.
- In Topic Focus Mode, reuse one personal topic across several relevant question types and show how the same material can be adapted without sounding memorized.
- In Review Mode, use available past reports or transcripts. Never invent previous sessions.

See `references/coaching_modes.md` for the complete interaction rules and transition phrases.

## Produce Feedback

When the learner says "please summarize," "give me feedback," or an equivalent phrase:

1. Stop asking practice questions immediately. Treat this phrase as a request to end the session, not as a request for a mid-session comment.
2. Separate observed evidence from estimates.
3. Give a cautious approximate band range, not an official score.
4. Identify the highest-impact grammar, vocabulary, fluency, and pronunciation issues supported by the available transcript or audio evidence.
5. Show the learner's original wording, a minimal correction, and a natural Band 7.5-level alternative.
6. Explain why the change helps in plain language.
7. Extract reusable collocations, phrasal verbs, and sentence patterns.
8. Map useful material to other IELTS topics.
9. Choose a small number of repeated errors for later review.
10. Give a short spoken recap suitable for listening while driving.
11. Ask exactly one closing question: "Would you like me to read today's questions and corrected answers aloud at a normal pace for you to follow silently?"
12. Wait for the learner's answer before generating the detailed report.

Interpret an affirmative answer such as "Yes," "Yes, I need it," or "Let's review" as a request for Guided Repeat Review:

1. Read one practice question aloud.
2. Read the learner's corrected natural answer aloud once at a normal, clear speaking pace.
3. Continue directly to the next practised question and corrected answer. Do not insert artificial pauses, ask the learner to speak, or wait for a response between sentences or questions.
4. Continue in the original session order until every practised question has been reviewed, unless the learner interrupts.
5. After the full pass, ask exactly one loop question: "Would you like to hear the full review again, repeat only part of it, or finish and generate the report?"

Handle the loop answer as follows:

- Full review again: repeat the complete question-and-corrected-answer set at normal pace, then ask the same loop question again.
- Finish, No, or generate the report: stop reading and proceed immediately to report generation.
- Repeat part, including "I'd like to repeat part of it": identify the requested question from its number, topic, or wording. If the target is unclear, ask only which question the learner wants. Read only that question and its corrected answer at normal pace, then ask the same loop question again.
- Never ask the learner to repeat aloud, never wait for shadowing, and never assess the learner's silent repetition.

Interpret a negative answer such as "No," "No, thanks," or "Skip it" as a request to skip Guided Repeat Review and proceed immediately to report generation.

Follow `references/feedback_schema.md`. Use `assets/session_report_template.md` when preparing a persistent session report.

## Save or Export Results

- After an end-of-session summary command, generate the detailed report automatically after the Guided Repeat Review is completed or skipped. Do not require a second file request.
- When the current project root is available, save private reports under `data/output/session_reports/` using a date-and-topic filename. Create the output directories when needed.
- Create one separate report per practice session. Do not merge a new session into an earlier Word report or overwrite an earlier report. Create a separate weekly or monthly combined review only when the learner explicitly requests one.
- Keep generated reports separate from raw source documents.
- Never overwrite the learner's original answer bank.
- Prefer Word (`.docx`) when document-generation capability is available.
- If Word generation is unavailable, return the report in the same structured Markdown format for later conversion.
- If the current environment is a temporary Voice workspace rather than the IELTS project, do not imply that the report has entered the long-term project archive. State the actual temporary path and identify that project archival is still pending.
- State clearly whether saving was completed, temporarily saved, skipped, or unavailable, and give the exact path when a file was created.

## Finish a Session

When the learner says the session is finished:

1. Stop all new practice questions.
2. Provide the short spoken recap if it has not already been given.
3. Offer the optional Guided Repeat Review and wait for a Yes or No answer.
4. Complete or skip the Guided Repeat Review according to the learner's answer.
5. Generate the detailed report automatically.
6. State whether the report was archived in the project or only saved temporarily, and give its exact path.
7. Suggest only one next practice focus based on the current evidence.
