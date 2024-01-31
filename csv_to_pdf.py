
from reportlab.platypus import Frame, PageTemplate, BaseDocTemplate, Table, Paragraph
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
import pandas as pd

def on_page(canvas, doc, pagesize=A4):
    page_num = canvas.getPageNumber()
    canvas.drawCentredString(pagesize[0]/2, 50, str(page_num))
    canvas.drawImage('/home/wroszu/GitHub/work-sql-to-pdf/see-more-sprite.png', 10, 740)

def df2table(df):
    return Table(
      [[Paragraph(col) for col in df.columns]] + df.values.tolist(), 
      style=[
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('LINEBELOW',(0,0), (-1,0), 1, colors.black),
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('ROWBACKGROUNDS', (0,0), (-1,-1), [colors.lightgrey, colors.white])],
      hAlign = 'LEFT')

csv_file_path = '/home/wroszu/GitHub/work-sql-to-pdf/sql_files/ddd.csv'
df = pd.read_csv(csv_file_path, sep=',')

padding = dict(leftPadding = 72, rightPadding = 72, topPadding = 72, bottomPadding = 18)

portrait_frame = Frame (0, 0, *A4, **padding)
landscape_frame = Frame (0, 0, *landscape(A4), **padding)

portrait_template = PageTemplate(id='portrait', frames=portrait_frame,onPage=on_page, pagesize=A4)

doc = BaseDocTemplate('report.pdf', pageTemplates=portrait_template)

doc.build([df2table(df)])