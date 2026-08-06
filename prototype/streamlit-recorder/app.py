"""Streamlit interface for offline IELTS speaking practice."""

import streamlit as st

from coach_rules import EXAMPLE_SENTENCES, correct_sentence


st.set_page_config(
    page_title="IELTS Speaking Personal Coach",
    page_icon="🗣️",
    layout="centered",
)

st.title("IELTS Speaking Personal Coach")
st.caption("Version 0.2 · Offline Speaking Practice / 离线口语练习版")

st.info(
    "This version does not use an AI API. You can record and replay your answer, "
    "but the app cannot transcribe or understand the recording yet.\n\n"
    "这个版本不调用 AI API，可以录音和回放，但暂时不能自动听懂或转写录音。"
)

QUESTIONS = (
    {
        "question": "How are you feeling today?",
        "translation": "你今天感觉怎么样？",
        "tips": (
            "I have + symptom.  Example: I have a runny nose.",
            "I feel + adjective.  Example: I feel dizzy.",
            "It is hard for me to + verb.  Example: It is hard for me to focus.",
        ),
    },
    {
        "question": "Tell me about your hometown.",
        "translation": "介绍一下你的家乡。",
        "tips": (
            "I come from ...",
            "It is known for ...",
            "What I like most about my hometown is ...",
        ),
    },
    {
        "question": "What did you do last weekend?",
        "translation": "你上周末做了什么？",
        "tips": (
            "Last weekend, I ...",
            "I spent some time + verb-ing ...",
            "The most memorable part was ...",
        ),
    },
)

if "sentence" not in st.session_state:
    st.session_state.sentence = EXAMPLE_SENTENCES[0]
if "result" not in st.session_state:
    st.session_state.result = None

speaking_tab, text_tab = st.tabs(
    ("Speaking Practice / 口语练习", "Text Demo / 文字演示")
)

with speaking_tab:
    question_index = st.selectbox(
        "Choose a question / 选择口语问题",
        range(len(QUESTIONS)),
        format_func=lambda index: QUESTIONS[index]["question"],
    )
    selected_question = QUESTIONS[question_index]

    st.subheader(selected_question["question"])
    st.caption(selected_question["translation"])
    st.write("先直接回答，不用追求完美。录完后播放一次，听听自己的表达。")

    first_recording = st.audio_input(
        "Step 1 — Record your first answer / 录制第一次回答",
        key=f"first_recording_{question_index}",
    )

    if first_recording:
        st.success("First attempt recorded. / 第一次回答已录制。")
        st.write("**Playback / 回放第一次回答**")
        st.audio(first_recording)

        st.write("**Expression tips / 表达提示**")
        for tip in selected_question["tips"]:
            st.write(f"- {tip}")

        st.write("参考提示重新组织答案，然后再说一遍。")
        second_recording = st.audio_input(
            "Step 2 — Record your second answer / 重新录制回答",
            key=f"second_recording_{question_index}",
        )

        if second_recording:
            st.success("Second attempt completed. / 第二次回答已完成。")
            st.write("**Playback / 回放第二次回答**")
            st.audio(second_recording)
            st.info("Compare the two recordings. / 对比两次录音中的流畅度和表达。")

with text_tab:
    st.caption("Optional offline grammar-rule demonstration / 可选的离线语法规则演示")
    selected_example = st.selectbox(
        "Choose an example / 选择练习例句",
        EXAMPLE_SENTENCES,
    )

    if st.button("Use this example / 使用这个例句"):
        st.session_state.sentence = selected_example
        st.session_state.result = None

    sentence = st.text_area(
        "Your English sentence / 输入你的英文句子",
        key="sentence",
        height=100,
    )

    if st.button("Check my sentence / 检查句子", type="primary"):
        st.session_state.result = correct_sentence(sentence)

    result = st.session_state.result
    if result:
        st.subheader("Feedback / 反馈")
        st.write("**Original / 原句**")
        st.write(result.original)

        if result.changed:
            st.write("**Correction / 修改后**")
            st.success(result.corrected)
            st.write("**Why / 原因**")
            for reason in result.reasons:
                st.write(f"- {reason}")
            st.warning(f"Please say this sentence again: {result.corrected}")
        else:
            st.warning(
                "No built-in rule matched this sentence. This does not prove that "
                "the sentence is correct. / 没有匹配到内置规则，不代表句子一定正确。"
            )

st.divider()
st.caption("Offline workflow: question → record → replay → tips → record again")
