# Development Roadmap

This roadmap keeps each version small, testable, and reversible.

## Version 0.1 — Project Foundation

Goal: complete the first publishing cycle from an idea to a public GitHub project.

- [x] Create the local Git repository
- [x] Write the initial README
- [x] Create a runnable Python entry point
- [x] Add dependency and privacy rules
- [x] Define the prompt and data plans
- [x] Create the first Git commit
- [x] Publish the repository on GitHub
- [ ] Add the project to the personal website

## Version 0.2 — Offline Speaking Prototype

Goal: test a minimal offline speaking and recording workflow before investing
in speech recognition or a paid AI API.

- [x] Add a minimal Streamlit speaking interface
- [x] Show a speaking question and useful expression prompts
- [x] Record, replay, and repeat a spoken answer
- [x] Keep the transparent offline correction-rule demo as an optional tab
- [x] Test microphone recording and playback locally with the user
- [x] Record the decision not to duplicate GPT Voice

Outcome: the prototype works, but a separate voice interface does not provide
enough additional value. Keep the prototype as a completed experiment and move
the project toward a GPT Voice companion workflow.

## Version 0.3 — Session Report Processor

Goal: turn one completed GPT Voice conversation into a consistent private Word
report without requiring the user to purchase an API.

- Read a user-selected GPT Voice conversation transcript
- Apply one stable Speaking Coach report structure
- Extract estimated performance, grammar issues, verb collocations, and useful
  topic links
- Generate a Word report inside `data/output/`
- Keep personal reports and transcripts outside the public Git repository

## Version 0.4 — Structured Learning Records

Goal: preserve long-term learning history in SQLite.

- Create the database inside `data/database/`
- Save session dates, modes, topics, questions, corrections, and error types
- Track important verb collocations and repeat frequency
- Preserve old records when the schema changes
- Verify that records remain after restarting the application

## Version 0.5 — Review and Retrieval

Goal: support commands such as "review People topics" or "review last week's
verb collocations."

- Retrieve sessions by date, topic, and error type
- Connect personal experiences to reusable IELTS topic categories
- Build a review queue from repeated mistakes
- Produce a concise spoken-review script for GPT Voice
- Keep source metadata for permitted practice questions

## Later — Connected Speaking Coach Agent

Goal: reduce the manual handoff between GPT Voice and the local learning
records when the product value justifies the additional complexity.

- Let a connected tool retrieve prior records before a Voice session
- Save a completed session from one explicit user command
- Generate and deliver the Word report automatically
- Add API or MCP-style integration only after privacy, cost, and reliability
  requirements are clear

## Not Planned for the Early MVP

- Multi-user accounts
- Commercial features
- Mobile applications
- Building a replacement for GPT Voice
- Speech recognition inside the Streamlit prototype
- Complex agent frameworks
- Vector databases
- Automated official IELTS scoring

## Development Principle

Complete and verify one small version before adding the next set of features.
