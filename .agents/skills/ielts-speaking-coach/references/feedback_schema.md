# Feedback Schema

Separate the spoken closing flow from the persistent report. Spoken feedback may be conversational; the daily report must be a compact retrieval and print document rather than an essay.

## Spoken Closing Flow

### 1. Spoken Recap

Write a concise recap suitable for reading aloud. Include the main strength, two correction targets, and three useful expressions.

### 2. Guided Repeat Review Decision

After the Spoken Recap, offer the three-pass listening and shadowing review described in `shadowing_review.md`.

- If Yes: complete the full selection at about 1.2x, then short thought groups at about 0.8x with 1-2-second gaps, then whole sentences at 1.0x with two-second gaps. No turn-taking waits, assessments, or confirmation between passes.
- If No: skip directly to report generation.
- Only after all three passes: offer full replay, partial replay, or report generation.
- For partial replay: read only the selected question and corrected answer, then offer the same three choices again.
- Do not ask any new practice question in either branch.

## Daily Report

Target one or two A4 pages and never exceed two pages unless the learner explicitly requests a full transcript. Reduce repeated packaging before shrinking essential learning content.

### 1. Header

- Title: `IELTS Speaking Practice Report - [date]`
- One short topic line
- Keep the title visually modest because the report is for private daily use.

### 2. Overall Snapshot

Keep this to two or three short lines:

- Topic
- Approximate spoken-performance range, clearly marked as formative rather than official
- The two most important blockers from this session

Do not include `What You Did Well` in a daily report. Do not add separate daily sub-scores unless they materially explain a correction. Do not score pronunciation without audio evidence.

### 3. Your Practice Answers and Corrections

Keep this as the main body and preserve the original question order. For each question include:

- Practice question
- Learner's original answer or a reliable concise transcript
- Key corrections, normally no more than three
- Natural Band 7 answer
- Natural word combinations aligned with that answer
- Language gaps raised in Chinese during the conversation

Use this correction form:

`When you said "[original]", a more natural way to express it is "[correction]". This is mainly a [specific issue] because [brief reason].`

When helpful, add one stronger but natural Band 7 version. Focus first on sentence completion, grammar, prepositions, verb choice, and collocations. Mark uncertain speech-recognition wording as `Possible transcription error`; do not manufacture an exact quotation.

For each Language gap, record:

- The learner's Chinese wording and the topic context
- Two to four natural English options when they add genuine value
- A concise usage distinction, such as neutral, informal, formal, or context-specific
- The best option used in the Natural Band 7 answer

Do not classify a Language gap as a grammar error. Example: `大城市` may be expressed as `major city` in a neutral IELTS answer, `big city` in everyday speech, or `large metropolitan area` when emphasizing scale and urban character.

### 4. Natural Word Combinations

Select only high-value items supported by the session. Usually include five to ten, with an upper limit of ten; use fewer when fewer are worth learning. For each item provide:

- English expression
- Concise Chinese meaning
- One or two natural synonyms or paraphrases
- One short reusable example

Bold or italicize the expression inside the Band 7 answer and place its explanation at the corresponding height in the annotation column. Do not repeat the same phrase again in a separate long vocabulary section.

### 5. Print Layout

- A4 portrait.
- Compact-reference style with a modest title, approximately 14 pt.
- Main text approximately 9.5 pt; headings approximately 10-11 pt.
- Use a two-column layout table, not newspaper-style flowing columns.
- Main content column: approximately 14-14.5 cm.
- Right annotation column: approximately 4-4.5 cm, with a light divider and approximately 7.5-8 pt text.
- Align each annotation cell vertically with the answer or correction it explains.
- Use the right column for Chinese meanings, synonyms/paraphrases, concise grammar labels, and short examples.
- Add visible inner padding on both sides of the vertical divider so neither column touches the line.
- Leave unused space in the right column blank for handwritten notes.
- Avoid decorative packaging, dense borders, generic advice, repeated spoken-recap text, and Guided Repeat Review metadata.

### 6. Report Save Status

- Format generated: Word or Markdown
- Archive status: project archive, temporary Voice workspace, skipped, or unavailable
- Exact save path, when created
- Session file policy: one separate report per session; never overwrite or merge automatically
- Return the final project-archive path when archival succeeds; do not return the temporary working-copy path instead.

### 7. Optional Final Focus

Include one short, session-specific focus only when it adds new information. Omit generic repeated advice such as `keep sentences shorter` or `practise active output`.

## Weekly Report

Generate only when the learner asks for a weekly report, including `I need a weekly report.` Summarize the available daily reports for the requested period. Include:

- What the learner did well
- Observable progress and changes across sessions
- Recurring sentence-completion, grammar, preposition, verb-choice, and collocation problems
- Useful language accumulated during the week without duplicating every daily list
- One next-week focus

Do not claim a trend from a single session. State which dated reports were available and which evidence was missing.

## Weekly Listening TXT (not a weekly progress report)

Generated alongside each daily Word report. Monday-Sunday files accumulate session questions and full corrected answers, followed by the session's optional `Repeated-error vocabulary` section. Keep scores, incorrect answers, and lengthy explanations out. The Word layout remains unchanged.

Session JSON accepts an optional stable `session_id` and an optional `repeated_vocabulary` list. Each vocabulary item uses:

```json
{
  "word": "target word or phrase",
  "ipa": "optional verified IPA",
  "meaning_zh": "concise Chinese meaning",
  "confused_with": "optional word the learner confuses it with",
  "evidence": "brief session evidence of recurrence, or learner-reported recurrence"
}
```

Keep `evidence` in the private source JSON, not in the listening text. Use available audio/transcript or an explicit learner report; do not invent recurrence, phonetic errors, or historical counts. The builder formats supplied items; it does not diagnose or detect errors from audio. A missing list is valid for older session data. Invalid dates must not silently send a session into the wrong week. Regenerating the same session must not duplicate it or erase other sessions.
