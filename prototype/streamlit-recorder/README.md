# Phase 1 — Offline Streamlit Recorder Prototype

This folder preserves the first tested implementation behind the IELTS Speaking Coach Agent. It is a completed product experiment, not the current coaching interface.

The original commit history remains available in the archived [`IELTS-Speaking-Personal-Coach`](https://github.com/went1003/IELTS-Speaking-Personal-Coach) repository.

**中文简介：** 这是项目第一阶段的离线 Streamlit 录音原型，用来验证“是否需要重新制作一个口语界面”。测试结果促成了后续向 GPT Voice + Skill 工作流的产品转向。

## Product Hypothesis

The original hypothesis was that a small standalone application could make IELTS Speaking practice easier by showing a question, recording an answer, replaying it, presenting useful expression prompts, and recording a second attempt.

The prototype deliberately avoided an AI API. Its purpose was to test the interaction workflow before investing in speech recognition, model integration, a database, or a polished interface.

## What the Prototype Does

- Presents a small set of speaking questions.
- Records and replays a first spoken answer.
- Displays expression prompts after the first attempt.
- Records and replays a second answer.
- Includes a transparent rule-based text-correction demonstration.

## What User Testing Showed

- The microphone, recording, and playback flow worked on macOS.
- Recording alone did not provide the most valuable coaching functions.
- Automatic feedback would first require speech-to-text and model analysis.
- GPT Voice already offered a stronger real-time speaking experience.
- The unmet need was consistent coaching rules, structured correction, repeat review, private reports, and long-term learning records.

## Product Decision

The team stopped extending the standalone recorder and retained it as evidence for a **product pivot**. The current implementation uses GPT Voice as the conversation layer and a reusable Skill as the coaching and reporting layer.

See [`docs/product_decision.md`](docs/product_decision.md) for the original decision record.

## Run the Historical Prototype

From this folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

The browser should open a local Streamlit page where a question can be selected and two recordings can be made and replayed.

## Known Limitations

- It does not transcribe or understand recorded speech.
- It does not provide automatic AI correction or scoring.
- The text demonstration uses only a few explicit correction rules.
- Recordings and practice history are not stored in a database.
- It is preserved for product-development evidence rather than daily use.

## Files

```text
streamlit-recorder/
├── README.md
├── app.py
├── coach_rules.py
├── requirements.txt
├── prompts/
│   └── speaking_coach_prompt.md
└── docs/
    ├── product_decision.md
    └── legacy_roadmap.md
```

Private learning materials, generated reports, local environments, and recordings are not included.
