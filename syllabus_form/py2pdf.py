from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

from .forms import CourseForm

styles = getSampleStyleSheet()

styles.add(ParagraphStyle(name='Normal_CENTER',
                          parent=styles['Normal'],
                          fontName='Helvetica',
                          wordWrap='LTR',
                          alignment=TA_CENTER,
                          fontSize=12,
                          leading=13,
                          textColor=colors.black,
                          borderPadding=0,
                          leftIndent=0,
                          rightIndent=0,
                          spaceAfter=0,
                          spaceBefore=0,
                          splitLongWords=True,
                          spaceShrinkage=0.05,
                          ))
styles.add(ParagraphStyle(name='New Style',
                          alignment=TA_LEFT,
                          fontName='Helvetica',
                          fontSize=7,
                          textColor=colors.darkgray,
                          leading=8,
                          textTransform='uppercase',
                          wordWrap='LTR',
                          splitLongWords=True,
                          spaceShrinkage=0.05,
                          ))

def createPDF(form):
    print(form)
    doc = SimpleDocTemplate("syllabus.pdf",pagesize=letter,
                            rightMargin=inch,leftMargin=inch,
                            topMargin=inch,bottomMargin=inch)

    Story=[]

    className = form.cleaned_data['className']
    professor = form.cleaned_data['professor']
    # email = form.cleaned_data['email']
    location = form.cleaned_data['location']
    # body1 = form.cleaned_data['body']
    Story.append(Paragraph(className, styles["Normal_CENTER"]))
    Story.append(Paragraph(professor, styles=['Normal']))
    Story.append(Paragraph(location, styles=['Normal']))

    

    doc.build(Story)
