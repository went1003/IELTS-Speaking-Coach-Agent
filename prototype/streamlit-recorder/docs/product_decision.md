# Product Decision: Use GPT Voice Instead of Rebuilding Voice Conversation

**Date:** 2026-07-30

**Status:** Accepted after testing the Version 0.2 prototype

## Context

The original plan was to build a standalone IELTS speaking coach with a local
Streamlit interface, microphone recording, AI feedback, learning records, and
long-term personalisation.

Version 0.2 tested the smallest offline workflow:

1. Show a speaking question.
2. Record and replay a first answer.
3. Show useful expression prompts.
4. Record and replay a second answer.

The microphone and playback workflow worked successfully on the user's Mac.

## What We Learned

- Streamlit can provide a simple local microphone interface.
- Recording and playback alone do not create a useful AI speaking coach.
- Automatic speech understanding would require another speech-recognition
  layer before an AI model could analyse the answer.
- GPT Voice already provides a stronger real-time listening and speaking
  experience.
- The unmet need is not another voice interface. It is consistent training
  rules, structured reports, long-term error records, and targeted review.

## Decision

Do not continue building a replacement for GPT Voice.

Use GPT Voice for real-time conversation, and develop the project as a
Speaking Coach Agent that can:

- plan sessions from personal goals and previous errors;
- process Voice conversation transcripts;
- estimate performance without claiming an official IELTS score;
- extract grammar errors, verb collocations, and reusable expressions;
- generate private Word reports;
- store structured learning records;
- retrieve prior material by date, topic, and error type; and
- prepare concise scripts for spoken review.

## First Implementation Boundary

The first Agent workflow will use a manual handoff:

1. The user completes a practice session in GPT Voice.
2. The user asks Codex to read the selected Voice conversation.
3. Codex generates the report and updates local learning records.

This approach provides most of the learning value without purchasing an API or
rebuilding real-time voice technology.

## What Remains Manual

- The user switches from GPT Voice to Codex after a session.
- GPT Voice cannot directly read the local SQLite database.
- Word reports are not automatically delivered from a Voice command.
- Transcript-only analysis cannot fully assess pronunciation, pace, or pauses.
- Review plans must be passed back to Voice until a connected tool is added.

These gaps may later be addressed with an API, MCP-style tool connection, or a
ChatGPT app if the additional automation justifies the cost and complexity.

## Preserved Work

The Version 0.2 Streamlit prototype remains in the repository as a runnable,
tested experiment and as evidence supporting this product decision.
