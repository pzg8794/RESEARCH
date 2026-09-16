from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib import colors
from pathlib import Path

out = Path(__file__).resolve().parents[4] / 'output/pdf/2026-09-09-cardiff-cover-letter.pdf'
out.parent.mkdir(parents=True, exist_ok=True)
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyCover', fontName='Helvetica', fontSize=11, leading=16, spaceAfter=13))
story = [Paragraph('Piter Garcia', styles['Title']), Paragraph('Rochester, NY | pzg8794@rit.edu | github.com/pzg8794', styles['Normal']), Spacer(1,24)]
paras = [
'September 9, 2026',
'Dear Cardiff Hiring Team,',
'I am applying for the Python Engineer, Financial Data Platform &amp; Integrations role. My experience building Python data pipelines and AWS-based workflows, combined with graduate research in reproducible systems and model evaluation, aligns with your emphasis on reliable data before downstream automation.',
'At VEDADATA, I designed data ingestion, cleaning, preprocessing, and validation workflows and built AWS quality checks to improve the traceability and usability of production data. At VIOME, I developed Python machine-learning workflows for healthcare applications, including data preparation, feature engineering, and evaluation. My current research at RIT extends that discipline through automated validation, structured logging, and comparison-ready experiments.',
'What interests me most about Cardiff is the responsibility for making provider data trustworthy enough to support real decisions. I would bring a practical approach: understand the business process and source data, establish a baseline, build one integration at a time, test failure cases, and measure reliability before expanding. I see AI as one tool in that process, not a substitute for sound data engineering or human judgment.',
'My strongest demonstrated experience is in Python, SQL, pandas, AWS workflows, and validation. I would welcome a discussion of how those skills transfer to your financial-provider integrations and the platform-specific experience you need. I am based in Rochester, New York, and interested in the remote contract opportunity.',
'Thank you for considering my application. I would appreciate the opportunity to discuss my work and how I could contribute to Cardiff\'s data platform.',
'Best regards,<br/>Piter Garcia'
]
story += [Paragraph(p, styles['BodyCover']) for p in paras]
SimpleDocTemplate(str(out), pagesize=letter, leftMargin=54,rightMargin=54,topMargin=48,bottomMargin=48).build(story)
print(out)
