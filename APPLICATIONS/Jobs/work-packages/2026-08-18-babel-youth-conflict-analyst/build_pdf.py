from pathlib import Path

from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "output" / "pdf"
OUT.mkdir(parents=True, exist_ok=True)


def page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 9)
    canvas.drawCentredString(LETTER[0] / 2, 0.5 * inch, f"{doc.page}")
    canvas.restoreState()


def markdown_blocks(path):
    blocks = []
    for raw in path.read_text(encoding="utf-8").split("\n\n"):
        block = " ".join(line.strip() for line in raw.splitlines()).strip()
        if block:
            blocks.append(block)
    return blocks


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="AppTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=18, leading=22, alignment=TA_CENTER, spaceAfter=8))
styles.add(ParagraphStyle(name="AppMeta", parent=styles["Normal"], fontName="Helvetica", fontSize=10, leading=13, alignment=TA_CENTER, spaceAfter=18))
styles.add(ParagraphStyle(name="AppBody", parent=styles["BodyText"], fontName="Times-Roman", fontSize=11, leading=16, spaceAfter=10, firstLineIndent=18))
styles.add(ParagraphStyle(name="AppNote", parent=styles["BodyText"], fontName="Helvetica-Oblique", fontSize=8.5, leading=11, spaceBefore=8))


def build_sample():
    target = OUT / "piter-garcia-becoming-the-teacher-i-needed-writing-sample.pdf"
    doc = SimpleDocTemplate(str(target), pagesize=LETTER, leftMargin=0.9 * inch, rightMargin=0.9 * inch, topMargin=0.75 * inch, bottomMargin=0.75 * inch, title="Becoming the Teacher I Needed", author="Piter Garcia")
    blocks = markdown_blocks(ROOT / "writing-sample.md")
    story = [Paragraph("Becoming the Teacher I Needed", styles["AppTitle"]), Paragraph("Piter Garcia | Writing Sample", styles["AppMeta"])]
    for block in blocks[1:-1]:
        story.append(Paragraph(block.replace("&", "&amp;"), styles["AppBody"]))
    story.append(Paragraph(blocks[-1].replace("&", "&amp;"), styles["AppNote"]))
    doc.build(story, onFirstPage=page_number, onLaterPages=page_number)
    return target


def build_interest():
    target = OUT / "piter-garcia-babel-interest-statement.pdf"
    doc = SimpleDocTemplate(str(target), pagesize=LETTER, leftMargin=0.9 * inch, rightMargin=0.9 * inch, topMargin=0.85 * inch, bottomMargin=0.85 * inch, title="Babel Institute Interest Statement", author="Piter Garcia")
    story = [Paragraph("Interest Statement", styles["AppTitle"]), Paragraph("Children and Youth in Conflict Analyst | Piter Garcia", styles["AppMeta"])]
    for block in markdown_blocks(ROOT / "interest-statement.md"):
        story.append(Paragraph(block.replace("&", "&amp;"), styles["AppBody"]))
    doc.build(story, onFirstPage=page_number, onLaterPages=page_number)
    return target


if __name__ == "__main__":
    print(build_sample())
    print(build_interest())
