#!/usr/bin/env python3
"""Build a compact A4 IELTS Speaking daily report from JSON session data."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor


PAGE_WIDTH_CM = 21.0
PAGE_HEIGHT_CM = 29.7
SIDE_MARGIN_CM = 1.15
VERTICAL_MARGIN_CM = 1.0
CONTENT_WIDTH_CM = PAGE_WIDTH_CM - 2 * SIDE_MARGIN_CM
MAIN_COLUMN_CM = 14.3
NOTES_COLUMN_CM = CONTENT_WIDTH_CM - MAIN_COLUMN_CM

BODY_FONT = "Arial"
EAST_ASIA_FONT = "Songti SC"
INK = RGBColor(34, 34, 34)
MUTED = RGBColor(94, 94, 94)
ACCENT = RGBColor(41, 73, 105)
DIVIDER = "C8CED6"


def set_run_font(run, size: float, *, bold: bool = False, italic: bool = False, color=INK):
    run.font.name = BODY_FONT
    r_fonts = run._element.get_or_add_rPr().rFonts
    r_fonts.set(qn("w:ascii"), BODY_FONT)
    r_fonts.set(qn("w:hAnsi"), BODY_FONT)
    r_fonts.set(qn("w:eastAsia"), EAST_ASIA_FONT)
    r_fonts.set(qn("w:cs"), BODY_FONT)
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color


def set_cjk_run_font(run, size: float, *, bold: bool = False, italic: bool = False, color=INK):
    run.font.name = EAST_ASIA_FONT
    r_fonts = run._element.get_or_add_rPr().rFonts
    for key in ("ascii", "hAnsi", "eastAsia", "cs"):
        r_fonts.set(qn(f"w:{key}"), EAST_ASIA_FONT)
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color


def add_mixed_text(paragraph, text, *, size, bold=False, italic=False, color=INK):
    for part in re.split(r"([^\x00-\x7F]+)", text):
        if not part:
            continue
        run = paragraph.add_run(part)
        if any(ord(char) > 127 for char in part):
            set_cjk_run_font(run, size, bold=bold, italic=italic, color=color)
        else:
            set_run_font(run, size, bold=bold, italic=italic, color=color)


def set_cell_margins(cell, top=35, start=70, bottom=35, end=70):
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for edge, value in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tc_mar.find(qn(f"w:{edge}"))
        if node is None:
            node = OxmlElement(f"w:{edge}")
            tc_mar.append(node)
        node.set(qn("w:w"), str(value))
        node.set(qn("w:type"), "dxa")


def set_cell_borders(cell, *, left=None, top=None, right=None, bottom=None):
    tc_pr = cell._tc.get_or_add_tcPr()
    borders = tc_pr.first_child_found_in("w:tcBorders")
    if borders is None:
        borders = OxmlElement("w:tcBorders")
        tc_pr.append(borders)
    for edge, spec in (("left", left), ("top", top), ("right", right), ("bottom", bottom)):
        if spec is None:
            continue
        node = borders.find(qn(f"w:{edge}"))
        if node is None:
            node = OxmlElement(f"w:{edge}")
            borders.append(node)
        node.set(qn("w:val"), spec.get("val", "nil"))
        if spec.get("val", "nil") != "nil":
            node.set(qn("w:sz"), str(spec.get("sz", 4)))
            node.set(qn("w:color"), spec.get("color", DIVIDER))


def set_table_geometry(table):
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = False
    tbl_pr = table._tbl.tblPr
    layout = tbl_pr.first_child_found_in("w:tblLayout")
    if layout is None:
        layout = OxmlElement("w:tblLayout")
        tbl_pr.append(layout)
    layout.set(qn("w:type"), "fixed")

    width_dxa = round(CONTENT_WIDTH_CM / 2.54 * 1440)
    main_dxa = round(MAIN_COLUMN_CM / 2.54 * 1440)
    notes_dxa = width_dxa - main_dxa

    tbl_w = tbl_pr.first_child_found_in("w:tblW")
    if tbl_w is None:
        tbl_w = OxmlElement("w:tblW")
        tbl_pr.append(tbl_w)
    tbl_w.set(qn("w:w"), str(width_dxa))
    tbl_w.set(qn("w:type"), "dxa")

    grid = table._tbl.tblGrid
    for child in list(grid):
        grid.remove(child)
    for width in (main_dxa, notes_dxa):
        col = OxmlElement("w:gridCol")
        col.set(qn("w:w"), str(width))
        grid.append(col)

    for row in table.rows:
        for cell, width, cm_width in zip(row.cells, (main_dxa, notes_dxa), (MAIN_COLUMN_CM, NOTES_COLUMN_CM)):
            cell.width = Cm(cm_width)
            tc_w = cell._tc.get_or_add_tcPr().first_child_found_in("w:tcW")
            if tc_w is None:
                tc_w = OxmlElement("w:tcW")
                cell._tc.get_or_add_tcPr().append(tc_w)
            tc_w.set(qn("w:w"), str(width))
            tc_w.set(qn("w:type"), "dxa")


def style_paragraph(paragraph, *, size=8.9, after=1.4, before=0, line=1.0, color=INK):
    fmt = paragraph.paragraph_format
    fmt.space_before = Pt(before)
    fmt.space_after = Pt(after)
    fmt.line_spacing = line


def add_labeled_paragraph(cell, label, text, *, size=8.9, after=1.5):
    paragraph = cell.add_paragraph() if cell.paragraphs[0].text else cell.paragraphs[0]
    label_run = paragraph.add_run(label)
    set_run_font(label_run, size, bold=True, color=ACCENT)
    text_run = paragraph.add_run(text)
    set_run_font(text_run, size)
    style_paragraph(paragraph, size=size, after=after)
    return paragraph


def add_highlighted_text(paragraph, text, phrases, *, size=8.9):
    valid_phrases = sorted({p.strip() for p in phrases if p and p.strip()}, key=len, reverse=True)
    if not valid_phrases:
        run = paragraph.add_run(text)
        set_run_font(run, size)
        return
    pattern = re.compile("(" + "|".join(re.escape(p) for p in valid_phrases) + ")", re.IGNORECASE)
    for part in pattern.split(text):
        if not part:
            continue
        is_phrase = any(part.casefold() == phrase.casefold() for phrase in valid_phrases)
        run = paragraph.add_run(part)
        set_run_font(run, size, bold=is_phrase)


def add_note(cell, label, text="", *, size=7.2, italic=False):
    paragraph = cell.add_paragraph() if cell.paragraphs[0].text else cell.paragraphs[0]
    label_run = paragraph.add_run(label)
    set_run_font(label_run, size, bold=True, color=ACCENT)
    if text:
        add_mixed_text(paragraph, text, size=size, italic=italic, color=MUTED)
    style_paragraph(paragraph, size=size, after=1.2, line=1.0, color=MUTED)


def add_body_row(table, *, main_builder, notes_builder=None, top_rule=False):
    cells = table.add_row().cells
    main, notes = cells
    for cell in cells:
        cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
        set_cell_margins(cell)
        set_cell_borders(cell, left={"val": "nil"}, right={"val": "nil"}, top={"val": "nil"}, bottom={"val": "nil"})
    set_cell_borders(notes, left={"val": "single", "sz": 5, "color": DIVIDER})
    if top_rule:
        set_cell_borders(main, top={"val": "single", "sz": 4, "color": DIVIDER})
        set_cell_borders(notes, top={"val": "single", "sz": 4, "color": DIVIDER}, left={"val": "single", "sz": 5, "color": DIVIDER})
    main_builder(main)
    if notes_builder:
        notes_builder(notes)
    return cells


def build_report(data: dict, output_path: Path):
    doc = Document()
    section = doc.sections[0]
    section.page_width = Cm(PAGE_WIDTH_CM)
    section.page_height = Cm(PAGE_HEIGHT_CM)
    section.top_margin = Cm(VERTICAL_MARGIN_CM)
    section.bottom_margin = Cm(VERTICAL_MARGIN_CM)
    section.left_margin = Cm(SIDE_MARGIN_CM)
    section.right_margin = Cm(SIDE_MARGIN_CM)
    section.header_distance = Cm(0.55)
    section.footer_distance = Cm(0.55)

    normal = doc.styles["Normal"]
    normal.font.name = BODY_FONT
    normal_fonts = normal._element.rPr.rFonts
    normal_fonts.set(qn("w:ascii"), BODY_FONT)
    normal_fonts.set(qn("w:hAnsi"), BODY_FONT)
    normal_fonts.set(qn("w:eastAsia"), EAST_ASIA_FONT)
    normal_fonts.set(qn("w:cs"), BODY_FONT)
    normal.font.size = Pt(8.9)
    normal.font.color.rgb = INK
    normal.paragraph_format.space_after = Pt(1.4)
    normal.paragraph_format.line_spacing = 1.0

    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    title_run = title.add_run(f"IELTS Speaking Practice Report - {data['date']}")
    set_run_font(title_run, 12.7, bold=True, color=ACCENT)
    title.paragraph_format.space_after = Pt(1.0)

    topic = doc.add_paragraph()
    topic_run = topic.add_run(f"Today's topic: {data['topic']}")
    set_run_font(topic_run, 9.0, bold=True)
    topic.paragraph_format.space_after = Pt(3)

    table = doc.add_table(rows=0, cols=2)

    def snapshot_main(cell):
        p = cell.paragraphs[0]
        run = p.add_run("OVERALL SNAPSHOT")
        set_run_font(run, 10.0, bold=True, color=ACCENT)
        style_paragraph(p, size=10.0, after=1.5)
        add_labeled_paragraph(cell, "Spoken performance: ", data["spoken_performance"])
        blockers = "; ".join(data.get("main_blockers", []))
        add_labeled_paragraph(cell, "Main blockers: ", blockers)

    def snapshot_notes(cell):
        add_note(cell, "FORMATIVE ONLY: ", "This is learning feedback, not an official IELTS score.", italic=True)

    add_body_row(table, main_builder=snapshot_main, notes_builder=snapshot_notes)

    for index, question in enumerate(data.get("questions", []), start=1):
        expressions = question.get("expressions", [])[:10]
        phrases = [item.get("phrase", "") for item in expressions]

        def question_main(cell, number=index, item=question):
            p = cell.paragraphs[0]
            run = p.add_run(f"QUESTION {number}")
            set_run_font(run, 10.0, bold=True, color=ACCENT)
            style_paragraph(p, size=10.0, after=1.0)
            q = cell.add_paragraph()
            q_run = q.add_run(item["question"])
            set_run_font(q_run, 9.1, bold=True)
            style_paragraph(q, size=9.1, after=1.5)

        add_body_row(table, main_builder=question_main, top_rule=True)

        def original_main(cell, item=question):
            add_labeled_paragraph(cell, "Your original answer\n", item.get("original_answer", "Not available."), after=1.8)

        def original_notes(cell):
            add_note(cell, "MY NOTES")

        add_body_row(table, main_builder=original_main, notes_builder=original_notes)

        corrections = question.get("corrections", [])[:3]

        def corrections_main(cell, items=corrections):
            p = cell.paragraphs[0]
            r = p.add_run("Key corrections")
            set_run_font(r, 9.1, bold=True, color=ACCENT)
            style_paragraph(p, size=9.1, after=1.0)
            for correction in items:
                cp = cell.add_paragraph()
                sentence = (
                    f"When you said \"{correction['original']}\", a more natural way to express it is "
                    f"\"{correction['natural']}\". {correction['reason']}"
                )
                cr = cp.add_run(sentence)
                set_run_font(cr, 8.6)
                style_paragraph(cp, size=8.6, after=1.3)

        def corrections_notes(cell, items=corrections):
            for correction in items:
                add_note(cell, f"{correction['issue']}: ", correction.get("explanation_zh", ""))

        add_body_row(table, main_builder=corrections_main, notes_builder=corrections_notes)

        def answer_main(cell, item=question, key_phrases=phrases):
            p = cell.paragraphs[0]
            r = p.add_run("Natural Band 7 answer")
            set_run_font(r, 9.1, bold=True, color=ACCENT)
            style_paragraph(p, size=9.1, after=1.0)
            answer = cell.add_paragraph()
            add_highlighted_text(answer, item["band7_answer"], key_phrases, size=8.9)
            style_paragraph(answer, size=8.9, after=1.5)

        def answer_notes(cell, items=expressions):
            for expression in items:
                parts = []
                if expression.get("meaning_zh"):
                    parts.append(expression["meaning_zh"])
                if expression.get("alternatives"):
                    parts.append(f"≈ {expression['alternatives']}")
                if expression.get("example"):
                    parts.append(f"e.g. {expression['example']}")
                add_note(cell, f"{expression.get('phrase', '')}: ", "; ".join(parts))

        add_body_row(table, main_builder=answer_main, notes_builder=answer_notes)

    if data.get("next_focus"):
        def focus_main(cell):
            add_labeled_paragraph(cell, "NEXT FOCUS: ", data["next_focus"], size=8.7)

        def focus_notes(cell):
            add_note(cell, "HANDWRITTEN NOTES", "\n\n")

        add_body_row(table, main_builder=focus_main, notes_builder=focus_notes, top_rule=True)

    set_table_geometry(table)

    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    footer_run = footer.add_run("Private learning report")
    set_run_font(footer_run, 7.2, color=MUTED)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(output_path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON session data")
    parser.add_argument("output", type=Path, help="Output DOCX path")
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    build_report(data, args.output)
    print(args.output)


if __name__ == "__main__":
    main()
