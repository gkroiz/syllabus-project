from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect

from syllabus_form.models import Course
from . import forms

# Create your views here
from django.http import FileResponse, Http404

#view pdf (this will be removed in the future)

from django.shortcuts import render
from django.shortcuts import redirect
from formtools.wizard.views import SessionWizardView

from .forms import CourseForm1, CourseForm2, CourseForm3, CourseForm4, CourseForm5, CourseForm6

TEMPLATES = {"1": "wizard.html",
             "2": "wizard.html",
             "3": "times.html",
             "4": "wizard.html",
             "5": "course_obj.html",
             "6": "wizard.html",
             "7": "wizard.html",
             "8": "wizard.html",
             "9": "wizard.html",
             "10": "grade_apport.html",
             "11": "wizard.html",
             "12": "wizard.html",
             "13": "wizard.html",
             "14": "wizard.html",
             "15": "wizard.html",
             "16": "wizard.html",
             "17": "wizard.html",
            }


class Wizard(SessionWizardView):

    form_list = []
    for i in range(17):
        form_list.append(exec(f'forms.CourseForm{i+1}'))
    def get_next_step(self, step=None):
        return self.request.POST.get('wizard_next_step', super().get_next_step(step))
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]
    def done(self, form_list, **kwargs):
        createPDF2(form_list)
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

def createPDF2(form):
    print(form)
    doc = SimpleDocTemplate("syllabus.pdf",pagesize=letter,
                            rightMargin=inch,leftMargin=inch,
                            topMargin=inch,bottomMargin=inch)

    Story=[]
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
    styles.add(ParagraphStyle(name='Department_Info',
                                parent=styles['Normal'],
                                fontName='Helvetica-Bold',
                                wordWrap='LTR',
                                alignment=TA_CENTER,
                                fontSize=12,
                                leading=13,
                                textColor=colors.black,
                                borderPadding=0,
                                leftIndent=0,
                                rightIndent=0,
                                spaceAfter=8,
                                spaceBefore=0,
                                splitLongWords=True,
                                spaceShrinkage=0.05,
                                ))
    styles.add(ParagraphStyle(name='course_title',
                                parent=styles['Normal'],
                                fontName='Helvetica',
                                wordWrap='LTR',
                                alignment=TA_CENTER,
                                fontSize=15,
                                leading=13,
                                textColor=colors.black,
                                borderPadding=0,
                                leftIndent=0,
                                rightIndent=0,
                                spaceAfter=8,
                                spaceBefore=0,
                                splitLongWords=True,
                                spaceShrinkage=0.05,
                                ))
    styles.add(ParagraphStyle(name='instructor_info',
                                parent=styles['Normal'],
                                fontName='Helvetica',
                                wordWrap='LTR',
                                alignment=TA_LEFT,
                                fontSize=11,
                                leading=13,
                                textColor=colors.black,
                                borderPadding=0,
                                leftIndent=0,
                                rightIndent=0,
                                spaceAfter=2,
                                spaceBefore=0,
                                splitLongWords=True,
                                spaceShrinkage=0.05,
                                ))
    styles.add(ParagraphStyle(name='paragraph_text',
                                parent=styles['Normal'],
                                fontName='Helvetica',
                                wordWrap='LTR',
                                alignment=TA_LEFT,
                                fontSize=12,
                                leading=13,
                                textColor=colors.black,
                                borderPadding=0,
                                leftIndent=0,
                                rightIndent=0,
                                spaceAfter=2,
                                spaceBefore=0,
                                splitLongWords=True,
                                spaceShrinkage=0.05,
                                ))

    print('in creator')
    print(form[1])

    indent = ' &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp'

    #from CourseForm1
    department = form[0].cleaned_data['department']
    department_office = form[0].cleaned_data['department_office']
    department_phone = form[0].cleaned_data['department_phone']
    course_number = form[0].cleaned_data['course_number']
    course_name = form[0].cleaned_data['course_name']
    semester = form[0].cleaned_data['semester']
    year = form[0].cleaned_data['year']
    course_acronym = form[0].cleaned_data['course_acronym']

    semesters = {'1': 'Spring', '2': 'Summer', '3': 'Fall', '4':'Winter'}
    years = {'1':'2021', '2':'2022', '3':'2023', '4':'2024'}

    year = years[year]
    semester = semesters[semester]

    #from CourseForm2
    instructor_name = form[1].cleaned_data['instructor_name']
    instructor_phone = form[1].cleaned_data['instructor_phone']
    instructor_email = form[1].cleaned_data['instructor_email']
    instructor_fax = form[1].cleaned_data['instructor_fax']
    instructor_website = form[1].cleaned_data['instructor_website']
    instructor_course_delivery_site = form[1].cleaned_data['instructor_course_delivery_site']
    instructor_office_hours = form[1].cleaned_data['instructor_office_hours']

    #from CourseForm3
    meeting_times = form[2].cleaned_data['meeting_times']

    #from CourseForm4
    textbook = form[3].cleaned_data['textbook']
    course_description = form[3].cleaned_data['course_description']
    num_credits = form[3].cleaned_data['num_credits']
    prerequisites = form[3].cleaned_data['prerequisites']

    #from CourseForm5
    course_objectives = form[4].cleaned_data['course_objectives']

    #from CourseForm6
    instructional_methods = form[5].cleaned_data['instructional_methods'] 

    #from CourseForm7
    attendance_participation = form[6].cleaned_data['attendance_participation'] 

    #from CourseForm8
    class_pre_and_student_success = form[7].cleaned_data['class_pre_and_student_success'] 

    #from CourseForm9
    course_requirements = form[8].cleaned_data['course_requirements']

    #from CourseForm10
    #need to add grading split, and description about each portion of the grade split
    grade_apportionment = form[9].cleaned_data['grade_apportionment']

    #from CourseForm11
    grading_standards = form[10].cleaned_data['grading_standards']

    #from CourseForm12
    due_dates = form[11].cleaned_data['due_dates']

    #from CourseForm13
    make_up_policy = form[12].cleaned_data['make_up_policy']

    #from CourseForm14
    academic_integrity = form[13].cleaned_data['academic_integrity']

    #from CourseForm15
    accomodations = form[14].cleaned_data['accomodations']

    #from CourseForm16
    #needs to be worked on
    course_schedule = form[15].cleaned_data['course_schedule']

    #from CourseForm17
    inclement_weather = form[16].cleaned_data['inclement_weather']


    Story=[]

    #department info
    Story.append(Paragraph(department, styles['Department_Info']))
    Story.append(Paragraph('University of Maryland Baltimore County', styles['Department_Info']))
    Story.append(Paragraph('Baltimore, Maryland. 21250', styles['Department_Info']))
    Story.append(Paragraph('Departmental Office: ' + department_office + ', Phone: ' + department_phone, styles['Department_Info']))

    Story.append(Paragraph('', styles['Department_Info']))
    Story.append(Paragraph('', styles['Department_Info']))

    #course title
    Story.append(Paragraph(course_acronym + ' ' + course_number + ' ' + course_name, styles['course_title']))
    Story.append(Paragraph(semester + ' ' + year, styles['course_title']))

    Story.append(Paragraph('', styles['Department_Info']))

    #instructor info
    Story.append(Paragraph('<b><u>Instructor:</u></b> ' + instructor_name, styles['instructor_info']))
    Story.append(Paragraph(indent + ' Phone: ' + instructor_phone, styles['instructor_info']))
    Story.append(Paragraph(indent + ' E-mail: ' + instructor_email, styles['instructor_info']))
    Story.append(Paragraph(indent + ' Course Delivery Site:' + instructor_course_delivery_site, styles['instructor_info']))
    Story.append(Paragraph(indent + ' Office Hours: ' + instructor_office_hours, styles['instructor_info']))

    Story.append(Paragraph('', styles['Department_Info']))
    Story.append(Paragraph('', styles['Department_Info']))

    #meeting times
    if '\n' in meeting_times:
        meeting_times_split = meeting_times.split('\n')
        Story.append(Paragraph('<b><u>Meeting Times:</u></b> ', styles['instructor_info']))
        for i in range(len(meeting_times_split)):
            Story.append(Paragraph(indent + ' ' + meeting_times_split[i], styles['paragraph_text']))
    else:
        Story.append(Paragraph('<b><u>Meeting Time:</u></b> ' + meeting_times, styles['paragraph_text']))

    Story.append(Paragraph('', styles['Department_Info']))
    Story.append(Paragraph('', styles['Department_Info']))

    #textbook
    Story.append(Paragraph('<b><u>Textbook:</u></b> ' + textbook, styles['instructor_info']))

    Story.append(Paragraph('', styles['Department_Info']))
    Story.append(Paragraph('', styles['Department_Info']))

    #course description
    Story.append(Paragraph('<b><u>Course Description and Rationale:</u></b> ' + course_description + ' This course is ' + num_credits + ' credits.', styles['paragraph_text']))

    Story.append(Paragraph('', styles['Department_Info']))
    Story.append(Paragraph('', styles['Department_Info']))

    #pre-reqs
    Story.append(Paragraph('<b><u>Prerequisites:</u></b> ' + prerequisites, styles['paragraph_text']))

    Story.append(Paragraph('', styles['Department_Info']))
    Story.append(Paragraph('', styles['Department_Info']))

    #course objectives
    if '\n' in course_objectives:
        course_objectives_split = course_objectives.split('\n')
        Story.append(Paragraph('<b><u>Course Objectives:</u></b> ', styles['paragraph_text']))
        for i in range(len(course_objectives_split)):
            Story.append(Paragraph(indent + ' ' + course_objectives_split[i], styles['paragraph_text']))
    else:
        Story.append(Paragraph('<b><u>Course Objectives:</u></b> ' + course_objectives, styles['paragraph_text']))

    Story.append(Paragraph('', styles['Department_Info']))
    Story.append(Paragraph('', styles['Department_Info']))

    #instructional methods
    Story.append(Paragraph('<b><u>Instructional Methods:</u></b> ' + instructional_methods, styles['paragraph_text']))

    Story.append(Paragraph('', styles['Department_Info']))
    Story.append(Paragraph('', styles['Department_Info']))

    #attendance and participation
    Story.append(Paragraph('<b><u>Attendance and Participation:</u></b> ' + attendance_participation, styles['paragraph_text']))

    Story.append(Paragraph('', styles['Department_Info']))
    Story.append(Paragraph('', styles['Department_Info']))

    #class prep
    Story.append(Paragraph('<b><u>Class Preparation and Student Success:</u></b> ' + class_pre_and_student_success, styles['paragraph_text']))

    Story.append(Paragraph('', styles['Department_Info']))
    Story.append(Paragraph('', styles['Department_Info']))

    #course requirements
    Story.append(Paragraph('<b><u>Course Requirements:</u></b> ' + course_requirements, styles['paragraph_text']))

    Story.append(Paragraph('', styles['Department_Info']))
    Story.append(Paragraph('', styles['Department_Info']))

    #grade apportionment
    grade_apportionment_split = grade_apportionment.split('\n')
    Story.append(Paragraph('<b><u>Grade Apportionment:</u></b> ', styles['paragraph_text']))
    for i in range(len(grade_apportionment_split)):
        Story.append(Paragraph(indent + ' ' + grade_apportionment_split[i], styles['paragraph_text']))

    Story.append(Paragraph('', styles['Department_Info']))
    Story.append(Paragraph('', styles['Department_Info']))

    #grading standards
    Story.append(Paragraph('<b><u>Grading Standards:</u></b> ' + grading_standards, styles['paragraph_text']))

    Story.append(Paragraph('', styles['Department_Info']))
    Story.append(Paragraph('', styles['Department_Info']))

    #due dates
    Story.append(Paragraph('<b><u>Due Dates:</u></b> ' + due_dates, styles['paragraph_text']))

    Story.append(Paragraph('', styles['Department_Info']))
    Story.append(Paragraph('', styles['Department_Info']))

    #make up policy
    Story.append(Paragraph('<b><u>Make-up Policy:</u></b> ' + make_up_policy, styles['paragraph_text']))

    Story.append(Paragraph('', styles['Department_Info']))
    Story.append(Paragraph('', styles['Department_Info']))

    #academic integrity
    Story.append(Paragraph('<b><u>Academic Integrity:</u></b> ' + academic_integrity, styles['paragraph_text']))

    Story.append(Paragraph('', styles['Department_Info']))
    Story.append(Paragraph('', styles['Department_Info']))

    #accomodations
    Story.append(Paragraph('<b><u>Accessibility and Disability Accomodations, Guidance and Resources:</u></b> ' + accomodations, styles['paragraph_text']))

    Story.append(Paragraph('', styles['Department_Info']))
    Story.append(Paragraph('', styles['Department_Info']))

    #schedule
    Story.append(Paragraph('<b><u>Course Schedule:</u></b> ' + course_schedule, styles['paragraph_text']))

    Story.append(Paragraph('', styles['Department_Info']))
    Story.append(Paragraph('', styles['Department_Info']))

    #inclement weather
    Story.append(Paragraph('<b><u>Inclement Weather:</u></b> ' + inclement_weather, styles['paragraph_text']))


    doc.build(Story)