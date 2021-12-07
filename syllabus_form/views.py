from re import M, search
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
from formtools.wizard.views import SessionWizardView, WizardView

from .forms import WelcomeForm

from synthesizew.models import Syllabus

TEMPLATES = {"1": "wizard.html",
             "2": "wizard.html",
             "3": "times.html",
             "4": "wizard.html",
             "5": "course_obj.html",
             "6": "instruction_methods.html",
             "7": "wizard.html",
             "8": "wizard.html",
             "9": "wizard.html",
             "10": "grade_apport.html",
             "11": "wizard.html",
             "12": "wizard.html",
             "13": "wizard.html",
             "14": "wizard.html",
             "15": "wizard.html",
             "16": "schedule.html",
             "17": "wizard.html",
            }

#views for the wizard welcome page
def wizardWelcome(request):
    form = WelcomeForm(request.POST or None)

    if request.method == 'POST':
        #if you want to go directly to wizard without importing syllabus
        if "goto" in request.POST:
            return HttpResponseRedirect('wizard')
        #if you want to go to wizard with syllabus
        if "yes" in request.POST:

            #getting wanted values from syllabus
            course = request.session.get('course_name')
            search_results = Syllabus.objects.filter(title__contains=course)
            instructor_name = search_results.values('instructor_name')[0].get('instructor_name')
            course_name = search_results.values('title')[0].get('title')
            instructor_email = search_results.values('instructor_email')[0].get('instructor_email')
            office_hours = search_results.values('office_hours')[0].get('office_hours')
            instructor_phone = search_results.values('instructor_phone')[0].get('instructor_phone')
            course_time = search_results.values('course_time')[0].get('course_time')
            textbook = search_results.values('textbook')[0].get('textbook')
            course_description = search_results.values('course_description')[0].get('course_description')
            prereqs = search_results.values('prereqs')[0].get('prereqs')
            course_obj = search_results.values('course_objectives')[0].get('course_objectives')
            instruction_method = search_results.values('instruct_methods')[0].get('instruct_methods')
            attendance = search_results.values('attendance_rule')[0].get('attendance_rule')
            class_preparation = search_results.values('class_preparation')[0].get('class_preparation')
            course_requirements = search_results.values('course_requirements')[0].get('course_requirements')
            grade_apportionment = search_results.values('grade_breakdown')[0].get('grade_breakdown')
            quizzes = search_results.values('quizzes')[0].get('quizzes')
            exams = search_results.values('exams')[0].get('exams')
            projects = search_results.values('prog_assignments')[0].get('prog_assignments')
            participation = search_results.values('participation')[0].get('participation')
            hands_on = search_results.values('hands_on')[0].get('hands_on')
            assignments = search_results.values('assignments')[0].get('assignments')
            homework = search_results.values('homework')[0].get('homework')
            late_policy = search_results.values('late_policy')[0].get('late_policy')
            makeup_policy = search_results.values('makeup_policy')[0].get('makeup_policy')

            grade_descriptions = ''
            if (quizzes != ''):
                grade_descriptions = grade_descriptions + 'Quizzes: ' + quizzes
            if (exams != ''):
                grade_descriptions = grade_descriptions + '\n\nExams: ' + exams
            if (projects != ''):
                grade_descriptions = grade_descriptions + '\n\nProjects: ' + projects
            if (participation != ''):
                grade_descriptions = grade_descriptions + '\n\nParticipation: ' + participation
            if (hands_on != ''):
                grade_descriptions = grade_descriptions + '\n\nHands On: ' + hands_on
            if (assignments != ''):
                grade_descriptions = grade_descriptions + '\n\nAssignments: ' + assignments
            if (homework != ''):
                grade_descriptions = grade_descriptions + '\n\nHomeworks: ' + homework
            
            #creating an initial dictionary to have pre-filled values
            initial_dict = {'1': {'course_number': course.split(' ')[1], 'course_name':course_name, 'course_acronym': course.split(' ')[0]},
                '2': {'instructor_name':instructor_name, 'instructor_phone':instructor_phone, 'instructor_email':instructor_email, 'instructor_fax':'', 'instructor_website':'', 'instructor_course_delivery_site':'', 'instructor_office_hours':office_hours},
                '3':{'meeting_times':course_time},
                '4':{'textbook':textbook, 'course_description':course_description, 'prerequisites':prereqs},
                '5':{'course_objectives':course_obj},
                '6':{'instruction_method':instruction_method},
                '7':{'attendance_participation': attendance},
                '8':{'class_pre_and_student_success':class_preparation},
                '9':{'course_requirements':course_requirements},
                '11':{},
                '12':{'due_dates':late_policy},
                '13':{'make_up_policy': makeup_policy},
                '14':{},
                '15':{},
                '16':{},
                '17':{}
                }
            if grade_descriptions != '':
                initial_dict['10'] = {'grade_apportionment':grade_apportionment, 'descriptions': grade_descriptions}
            else:
                initial_dict['10'] = {'grade_apportionment':grade_apportionment}
            request.session['initial'] = initial_dict
            return HttpResponseRedirect('wizard')

        #if you want to search for another syllabus
        if "no" in request.POST:
            return render(request, 'welcome.html', {'form': form})

        #search for syllabus
        if "search" in request.POST:
            course_name = request.POST.get('course')
            if course_name == '':
                return render(request, 'welcome.html', {'form': form})
 
            search_results = Syllabus.objects.filter(title__contains=course_name)
            if search_results:
                request.session['course_name'] = course_name
                return render(request, 'welcome_yes.html', {'form': form, 'course_name': course_name})
            else:
                return render(request, 'welcome_no.html', {'course_name': course_name})

    return render(request, 'welcome.html', {'form': form})


FORMS = [('1', forms.CourseForm1),
         ('2', forms.CourseForm2),
         ('3', forms.CourseForm3),
         ('4', forms.CourseForm4),
         ('5', forms.CourseForm5),
         ('6', forms.CourseForm6),
         ('7', forms.CourseForm7),
         ('8', forms.CourseForm8),
         ('9', forms.CourseForm9),
         ('10', forms.CourseForm10),
         ('11', forms.CourseForm11),
         ('12', forms.CourseForm12),
         ('13', forms.CourseForm13),
         ('14', forms.CourseForm14),
         ('15', forms.CourseForm15),
         ('16', forms.CourseForm16Full),
         ('17', forms.CourseForm17),
         ]
#wizard, which goes through each form
class Wizard(SessionWizardView):
    form_list = []
    for i in range(17):
        if i == 15:
            form_list.append(exec(f'forms.CourseForm16Full'))
        else:
            form_list.append(exec(f'forms.CourseForm{i+1}'))
    def get_next_step(self, step=None):
        return self.request.POST.get('wizard_next_step', super().get_next_step(step))
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, form_dict, **kwargs):
        createPDF2(form_list)
        try:
            return FileResponse(open('syllabus.pdf', 'rb'), content_type='application/pdf')
        except FileNotFoundError:
            raise Http404()
    def get_form_initial(self, step):
        if self.request.session.get('initial') != None:
            initial = self.request.session.get('initial')
            return initial.get(step,{})
    def get_form(self, step=None, data=None, files=None):

        return super().get_form(step=step, data=data, files=files)



################ python to create pdf ###################
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

def createPDF2(form):
    course_acronym = form[0].cleaned_data['course_acronym']
    course_number = form[0].cleaned_data['course_number']

    doc = SimpleDocTemplate("syllabus_form/syllabus_pdfs/" + course_acronym + course_number + "-syllabus.pdf",pagesize=letter,
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

    grade_descriptions = form[9].cleaned_data['descriptions']

    #from CourseForm11
    grading_standards = form[10].cleaned_data['grading_standards']

    #from CourseForm12
    due_dates = form[11].cleaned_data['due_dates']

    #from CourseForm13
    make_up_policy = form[12].cleaned_data['make_up_policy']

    #from CourseForm14
    academic_integrity = form[13].cleaned_data['academic_integrity']

    #from CourseForm15
    accommodations = form[14].cleaned_data['accommodations']

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

    grade_descriptions_split = grade_descriptions.split('\r\n\r\n')
    for i in range(len(grade_descriptions_split)):
        grade_type = grade_descriptions_split[i].split(':')[0]
        Story.append(Paragraph('<b><u>' + grade_type + ':</u></b>' + grade_descriptions_split[i].split(':')[1], styles['paragraph_text']))
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

    #accommodations
    Story.append(Paragraph('<b><u>Accessibility and Disability accommodations, Guidance and Resources:</u></b> ' + accommodations, styles['paragraph_text']))

    Story.append(Paragraph('', styles['Department_Info']))
    Story.append(Paragraph('', styles['Department_Info']))

    #schedule
    #needs to be worked on
    table = []
    if form[15].cleaned_data['lecture0'] != '':
        table.append(['Week', 'Material', 'Due'])
        for index in range(16):
            row = []
            if (form[15].cleaned_data['lecture{index}'.format(index=index)] != ''):
                row.append(form[15].cleaned_data['lecture{index}'.format(index=index)])
                row.append(form[15].cleaned_data['material{index}'.format(index=index)])
                row.append(form[15].cleaned_data['due{index}'.format(index=index)])
            else:
                break
            table.append(row)
        schedule=Table(table,3*[2.15*inch], len(table)*[0.25*inch])

        schedule.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold')
        ]))

        Story.append(Paragraph('<b><u>Course Schedule:</u></b> ', styles['paragraph_text']))

        Story.append(Paragraph('', styles['Department_Info']))

        Story.append(schedule)

    Story.append(Paragraph('', styles['Department_Info']))
    Story.append(Paragraph('', styles['Department_Info']))

    #inclement weather
    Story.append(Paragraph('<b><u>Inclement Weather:</u></b> ' + inclement_weather, styles['paragraph_text']))


    doc.build(Story)