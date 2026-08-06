"""Small, transparent correction rules for the offline practice demo."""

from dataclasses import dataclass
import re


EXAMPLE_SENTENCES = (
    "I got a runny nose.",
    "I feel dizzy all the day.",
    "It's hard for me focus on my work.",
    "I know the noun, but I don't know which verb use.",
)


@dataclass(frozen=True)
class CorrectionResult:
    """The result returned after checking one sentence."""

    original: str
    corrected: str
    reasons: tuple[str, ...]

    @property
    def changed(self) -> bool:
        """Return whether an offline rule changed the sentence."""
        return self.original != self.corrected


RULES = (
    (
        re.compile(r"\bI got a runny nose\b", re.IGNORECASE),
        "I have a runny nose",
        "Use “have + symptom” for a symptom you have now. / 当前症状使用“have + 症状”。",
    ),
    (
        re.compile(r"\ball the day\b", re.IGNORECASE),
        "all day",
        "Use “all day”, without “the”. / 表示“一整天”时说 all day，不加 the。",
    ),
    (
        re.compile(r"\bhard for me focus\b", re.IGNORECASE),
        "hard for me to focus",
        "Use “for someone to do something”. / 使用“for someone to do something”结构。",
    ),
    (
        re.compile(r"\bwhich verb use\b", re.IGNORECASE),
        "which verb to use",
        "Use “which + noun + to do”. / 使用“which + 名词 + to do”结构。",
    ),
)


def correct_sentence(sentence: str) -> CorrectionResult:
    """Apply every matching offline rule to one sentence."""
    original = sentence.strip()
    corrected = original
    reasons: list[str] = []

    for pattern, replacement, reason in RULES:
        updated, count = pattern.subn(replacement, corrected)
        if count:
            corrected = updated
            reasons.append(reason)

    return CorrectionResult(
        original=original,
        corrected=corrected,
        reasons=tuple(reasons),
    )
