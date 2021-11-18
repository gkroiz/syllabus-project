from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
# from .forms import CourseForm
# Create your views here.


def syllabus_form(request,):
    return render(request, 'syllabus_form')


def course(request):
    print(request.POST)
    if 'add-new-box' in request.POST:
        print('add new box')
    if request.method == 'POST':
        if 'add' in request.POST:
            print('you pressed add button')
            print('count: ' + str(request.POST.get('extra_field_count')))
            form = CourseForm(request.POST, extra=request.POST.get('extra_field_count'))
            return render(request, 'base.html', {'form': form}) 
        if 'remove' in request.POST:
            print('you pressed remove button')
            print('count: ' + str(request.POST.get('extra_field_count')))
            form = CourseForm(request.POST, extra=request.POST.get('extra_field_count'))
            return render(request, 'base.html', {'form': form}) 
        if 'update' in request.POST:
            print('you pressed update button')
            form = CourseForm(request.POST, extra=request.POST.get('extra_field_count'))
            createPDF(form)
            return render(request, 'base.html', {'form': form}) 
        # form = CourseForm(request.POST)
        # form = CourseForm(request.POST, extra=request.POST.get('total_input_fields'))
        if 'submit' in request.POST:
            print('you pressed submit button')
            form = CourseForm(request.POST, extra=request.POST.get('extra_field_count'))
            if form.is_valid():
                # createPDF(form)
                form = form.save()
                return render(request, 'submit.html', {'form': form})

    else:
        form = CourseForm()
    return render(request, 'base.html', {'form': form})


from django.http import FileResponse, Http404

#view pdf (this will be removed in the future)
def pdf_view(request):
    try:
        return FileResponse(open('syllabus.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()



################ python to create pdf ###################
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



def createPDF(form):
    print(form)
    doc = SimpleDocTemplate("syllabus.pdf",pagesize=letter,
                            rightMargin=inch,leftMargin=inch,
                            topMargin=inch,bottomMargin=inch)

    Story=[]
    styles = getSampleStyleSheet()
    # styles.add(ParagraphStyle(name='Title',
    #                         parent=styles['Normal'],
    #                         fontName='Helvetica',
    #                         wordWrap='LTR',
    #                         alignment=TA_CENTER,
    #                         fontSize=24,
    #                         leading=13,
    #                         textColor=colors.black,
    #                         borderPadding=0,
    #                         leftIndent=0,
    #                         rightIndent=0,
    #                         spaceAfter=0,
    #                         spaceBefore=0,
    #                         splitLongWords=True,
    #                         spaceShrinkage=0.05,
    #                         ))
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
    styles.add(ParagraphStyle(name='Header',
                            parent=styles['Normal'],
                            fontName='Helvetica',
                            wordWrap='LTR',
                            alignment=TA_LEFT,
                            fontSize=14,
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
    className = form.cleaned_data['className']
    professor = form.cleaned_data['professor']
    # email = form.cleaned_data['email']
    location = form.cleaned_data['location']
    # body1 = form.cleaned_data['body']
    Story.append(Paragraph(className, styles["Title"]))
    Story.append(Paragraph('Professor: ' + professor, styles['Normal']))
    Story.append(Paragraph('Class location: ' + location, styles['Normal']))

    bodyExists = True
    bodyString = 'extra_field_'
    counter = 0
    while bodyExists:
        if bodyString + str(counter) in form.cleaned_data:
            body = form.cleaned_data[bodyString + str(counter)]
            # Story.append(Spacer(width = inch, height = inch))
            Story.append(Paragraph('Body '+ str(counter), styles['Header']))
            Story.append(Paragraph(body, styles['BodyText']))
        else:
            bodyExists = False
        counter += 1

    

    doc.build(Story)