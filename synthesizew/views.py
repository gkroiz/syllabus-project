from django.shortcuts import render
from synthesizew.models import Syllabus
from synthesizew.extract_data import extract_data
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
import os
from syllabus import settings


# Create your views here.
def index(request):
    facts = Syllabus.objects.filter()
    context = {
        'facts': facts,
    }
    return render(request, 'synthesizew/index.html', context=context)


def add(request):
    # get the uploaded file, save it to a temp location, then run extract_data
    # to get the relevant information out of it
    pre_syllabus_wrapper = request.FILES.get('pdf_file')
    pdf_save_path = os.path.join(settings.BASE_DIR, "syllabi_upload", pre_syllabus_wrapper.name)
    with open(pdf_save_path, 'wb+') as destination:
        for chunk in pre_syllabus_wrapper.chunks():
            destination.write(chunk)
    pre_syllabus = pdf_save_path
    syllabus_data = extract_data(pdf_save_path)

    # setting up list of keys to check which values could be found and which values could not be found
    # if found, do nothing but if not create the key and keep it empty
    keys = ['syllabus_file', 'title', 'instructor_name', 'instructor_email', 'ta_name', 'ta_email',
            'course_site', 'instructor_phone', 'office_hours', 'course_time', 'course_description',
            'course_objectives', 'prereqs', 'textbook', 'instruct_methods', 'attendance_rule',
            'class_preparation', 'course_requirements', 'grade_breakdown', 'quizzes', 'exams',
            'prog_assignments', 'participation', 'hands_on', 'assignments', 'homework', 'late_policy',
            'makeup_policy']
    for key in keys:
        if key in syllabus_data:
            pass
        else:
            syllabus_data[key] = ""
        print(key + ": " + syllabus_data[key])
    # adding values from dictionary of extracted values of pdf (but not pdf file itself) to object,
    # then pushing it into database
    new_syllabus = Syllabus(syllabus_file=pre_syllabus, 
                            title=syllabus_data['title'],
                            instructor_name=syllabus_data['instructor_name'],
                            instructor_email=syllabus_data['instructor_email'],
                            ta_name=syllabus_data['ta_name'],
                            ta_email=syllabus_data['ta_email'],
                            course_site=syllabus_data['course_site'],
                            instructor_phone=syllabus_data['instructor_phone'],
                            office_hours=syllabus_data['office_hours'],
                            course_time=syllabus_data['course_time'],
                            course_description=syllabus_data['course_description'],
                            course_objectives=syllabus_data['course_objectives'],
                            prereqs=syllabus_data['prereqs'],
                            textbook=syllabus_data['textbook'],
                            instruct_methods=syllabus_data['instruct_methods'],
                            attendance_rule=syllabus_data['attendance_rule'],
                            class_preparation=syllabus_data['class_preparation'],
                            course_requirements=syllabus_data['course_requirements'],
                            grade_breakdown=syllabus_data['grade_breakdown'],
                            quizzes=syllabus_data['quizzes'],
                            exams=syllabus_data['exams'],
                            prog_assignments=syllabus_data['prog_assignments'],
                            participation=syllabus_data['participation'],
                            hands_on=syllabus_data['hands_on'],
                            assignments=syllabus_data['assignments'],
                            homework=syllabus_data['homework'],
                            late_policy=syllabus_data['late_policy'],
                            makeup_policy=syllabus_data['makeup_policy']
                            )
    new_syllabus.save()
    return HttpResponseRedirect(reverse('index'))
