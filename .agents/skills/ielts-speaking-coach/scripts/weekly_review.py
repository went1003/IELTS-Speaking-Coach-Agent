"""Private weekly listening scripts; no audio service or extra dependencies."""

from datetime import date, timedelta
import hashlib
import json
import os
from pathlib import Path
import tempfile

MONTHS = ("January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December")


def ordinal_day(day):
    suffix = "th" if 10 <= day % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
    return f"{day}{suffix}"


def week_range_for(day):
    monday = day - timedelta(days=day.weekday())
    return monday, monday + timedelta(days=6)


def format_weekly_script_name(monday, sunday):
    start = f"{ordinal_day(monday.day)} {MONTHS[monday.month - 1]}"
    end = f"{ordinal_day(sunday.day)} {MONTHS[sunday.month - 1]} {sunday.year}"
    if monday.year != sunday.year:
        start += f" {monday.year}"
    return f"Speaking Exercise {start} to {end}.txt"


def text_field(value, name):
    if value is None:
        return ""
    if not isinstance(value, str):
        raise ValueError(f"{name} must be text")
    return value.strip()


def build_listening_review_text(data):
    lines = []
    questions = data.get("questions", [])
    if not isinstance(questions, list):
        raise ValueError("questions must be a list")
    for index, question in enumerate(questions, 1):
        if not isinstance(question, dict):
            raise ValueError("Each question must be an object")
        prompt = text_field(question.get("question"), "question")
        answer = text_field(question.get("band7_answer") or question.get("corrected_answer"), "corrected answer")
        if prompt and answer:
            lines.extend([f"Question {index}: {prompt}", f"Corrected answer: {answer}", ""])

    vocabulary = data.get("repeated_vocabulary", [])
    if not isinstance(vocabulary, list):
        raise ValueError("repeated_vocabulary must be a list")
    entries, seen = [], set()
    for item in vocabulary:
        if not isinstance(item, dict):
            raise ValueError("Each repeated vocabulary item must be an object")
        word = text_field(item.get("word"), "word")
        if not word or word.casefold() in seen:
            continue
        if not text_field(item.get("evidence"), "evidence"):
            raise ValueError(f"Repeated vocabulary '{word}' needs session evidence or learner-reported recurrence")
        seen.add(word.casefold())
        parts = [word]
        for field in ("ipa", "meaning_zh"):
            value = text_field(item.get(field), field)
            if value:
                parts.append(value)
        confusion = text_field(item.get("confused_with"), "confused_with")
        if confusion:
            parts.append(f"Distinguish from: {confusion}")
        entries.append(" — ".join(parts))
    if entries:
        lines.extend(["Repeated-error vocabulary", *entries])
    return "\n".join(lines).strip()


def resolve_project_output_dir(output_path):
    resolved = Path(output_path).resolve()
    for parent in resolved.parents:
        if parent.name == "output" and parent.parent.name == "data":
            return parent
    # Temporary environments stay temporary; never infer a project from an arbitrary 'data' folder.
    return resolved.parent


def atomic_write(path, content):
    """A failed write must leave the previous usable file intact."""
    descriptor, temporary = tempfile.mkstemp(prefix=".weekly-", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def append_weekly_listening_review(data, output_path):
    # Validate everything before writing; unknown dates must not fall back to today.
    try:
        day = date.fromisoformat(str(data.get("date", "")))
    except ValueError as error:
        raise ValueError("Weekly TXT requires the actual session date as YYYY-MM-DD") from error
    entry = build_listening_review_text(data)
    if not entry:
        return None
    monday, sunday = week_range_for(day)
    directory = resolve_project_output_dir(output_path) / "listening_review_scripts"
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / format_weekly_script_name(monday, sunday)
    index_path = target.with_suffix(".sessions.json")
    if index_path.exists():
        state = json.loads(index_path.read_text(encoding="utf-8"))
        if not isinstance(state, dict) or state.get("version") != 1 or not isinstance(state.get("sessions"), dict):
            raise ValueError("Weekly session index is invalid; existing TXT left intact")
        if not isinstance(state.get("legacy_text", ""), str) or not all(isinstance(v, str) for v in state["sessions"].values()):
            raise ValueError("Weekly session index entries are invalid; existing TXT left intact")
        # Preserve manual edits rather than silently replacing them during a rebuild.
        expected = render_state(state)
        if target.exists() and target.read_text(encoding="utf-8") != expected:
            raise ValueError("Weekly TXT differs from its index; preserve it and reconcile manual edits before updating")
    else:
        state = {"version": 1, "legacy_text": target.read_text(encoding="utf-8") if target.exists() else "", "sessions": {}}
    identity = text_field(data.get("session_id"), "session_id") or str(Path(output_path).resolve())
    key = hashlib.sha256(identity.encode("utf-8")).hexdigest()
    state["sessions"][key] = entry
    # TXT first: a rare index-write failure leaves the new text usable; retry safely refuses mismatch.
    atomic_write(target, render_state(state))
    atomic_write(index_path, json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    return target


def render_state(state):
    parts = [state.get("legacy_text", "").strip(), *state["sessions"].values()]
    return "\n\n".join(part for part in parts if part) + "\n"
