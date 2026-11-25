"""Offline regression tests: python3 scripts/test_weekly_review.py."""

from datetime import date
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import weekly_review as review


class WeeklyReviewTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.report = Path(self.temporary.name) / "data/output/session_reports/session.docx"

    def session(self, **overrides):
        data = {"date": "2026-11-25", "questions": [{"question": "What was challenging?", "band7_answer": "I checked the figures.", "original_answer": "PRIVATE WRONG ANSWER"}]}
        data.update(overrides)
        return data

    def test_old_schema_and_private_fields(self):
        target = review.append_weekly_listening_review(self.session(spoken_performance="PRIVATE SCORE"), self.report)
        text = target.read_text()
        self.assertIn("I checked the figures.", text)
        self.assertNotIn("PRIVATE", text)
        self.assertNotIn("Repeated-error", text)
        self.assertEqual(target.parent, (self.report.parent.parent / "listening_review_scripts").resolve())

    def test_rerun_and_revision_keep_other_sessions(self):
        target = review.append_weekly_listening_review(self.session(session_id="first"), self.report)
        review.append_weekly_listening_review(self.session(session_id="second"), self.report.with_name("second.docx"))
        revision = self.session(session_id="first", questions=[{"question": "Updated question?", "corrected_answer": "Updated full answer."}])
        review.append_weekly_listening_review(revision, self.report)
        review.append_weekly_listening_review(revision, self.report)
        text = target.read_text()
        self.assertEqual(text.count("Updated full answer."), 1)
        self.assertEqual(text.count("I checked the figures."), 1)

    def test_week_boundary_and_restart(self):
        sunday = review.append_weekly_listening_review(self.session(date="2026-11-29"), self.report)
        monday = review.append_weekly_listening_review(self.session(date="2026-11-30"), self.report)
        self.assertNotEqual(sunday, monday)
        # State is persisted on disk, not in a process global.
        persisted = json.loads(sunday.with_suffix(".sessions.json").read_text())
        self.assertEqual(len(persisted["sessions"]), 1)

    def test_year_and_month_boundaries_and_ordinals(self):
        monday, sunday = review.week_range_for(date(2027, 1, 1))
        self.assertEqual(review.format_weekly_script_name(monday, sunday), "Speaking Exercise 28th December 2026 to 3rd January 2027.txt")
        self.assertEqual([review.ordinal_day(x) for x in (1, 2, 3, 11, 12, 13, 21, 22, 23, 31)], ["1st", "2nd", "3rd", "11th", "12th", "13th", "21st", "22nd", "23rd", "31st"])

    def test_vocabulary_and_evidence_privacy(self):
        item = {"word": "volume", "ipa": "/test/", "meaning_zh": "数量", "confused_with": "value", "evidence": "PRIVATE EVIDENCE"}
        target = review.append_weekly_listening_review(self.session(repeated_vocabulary=[item, item]), self.report)
        text = target.read_text()
        self.assertIn("数量", text)
        self.assertIn("Distinguish from: value", text)
        self.assertEqual(text.count("volume"), 1)
        self.assertNotIn("PRIVATE", text)

    def test_invalid_data_keeps_previous_file(self):
        target = review.append_weekly_listening_review(self.session(), self.report)
        before = target.read_bytes()
        for overrides in ({"date": "Sample Session"}, {"questions": "bad"}, {"repeated_vocabulary": "bad"}, {"repeated_vocabulary": [{"word": "invented"}]}, {"questions": [{"question": "Q", "band7_answer": 7}]}):
            with self.subTest(overrides=overrides), self.assertRaises(ValueError):
                review.append_weekly_listening_review(self.session(**overrides), self.report)
            self.assertEqual(target.read_bytes(), before)

    def test_no_empty_file(self):
        self.assertIsNone(review.append_weekly_listening_review(self.session(questions=[]), self.report))
        self.assertFalse(self.report.parent.parent.exists())

    def test_legacy_text_preserved(self):
        directory = self.report.parent.parent / "listening_review_scripts"
        directory.mkdir(parents=True)
        target = directory / "Speaking Exercise 23rd November to 29th November 2026.txt"
        target.write_text("Existing review from older generator.\n")
        review.append_weekly_listening_review(self.session(), self.report)
        review.append_weekly_listening_review(self.session(), self.report)
        self.assertEqual(target.read_text().count("Existing review"), 1)

    def test_manual_edit_and_corrupt_index_preserved(self):
        target = review.append_weekly_listening_review(self.session(), self.report)
        target.write_text("Manually edited review.\n")
        with self.assertRaises(ValueError):
            review.append_weekly_listening_review(self.session(), self.report)
        self.assertEqual(target.read_text(), "Manually edited review.\n")
        target.with_suffix(".sessions.json").write_text("invalid JSON")
        with self.assertRaises(ValueError):
            review.append_weekly_listening_review(self.session(), self.report)
        self.assertEqual(target.read_text(), "Manually edited review.\n")

    def test_failed_replace_preserves_existing_text(self):
        target = review.append_weekly_listening_review(self.session(), self.report)
        before = target.read_bytes()
        with patch.object(review.os, "replace", side_effect=OSError("simulated write failure")):
            with self.assertRaises(OSError):
                review.append_weekly_listening_review(self.session(session_id="another"), self.report)
        self.assertEqual(target.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
