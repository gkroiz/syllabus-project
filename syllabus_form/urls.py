from django.urls import path

from . import views
from django.views.generic import TemplateView

from . import forms


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
# initial = {'1': {'department': 'IT', 'department_office': 'Room ITE 404', 'department_phone': '111-111-1111', 'course_number': '101', 'course_name':'Intro', 'semester':'Summer', 'year':'2021', 'course_acronym': 'IS'},
                    # '2': {'instructor_name':'Gerson', 'instructor_phone':'111-111-1111', 'instructor_email':'gkroiz1@umbc.edu', 'instructor_fax':'', 'instructor_website':'', 'instructor_course_delivery_site':'Blackboard', 'instructor_office_hours':'M/W 4'}}
urlpatterns = [
    path('wizard/', views.Wizard.as_view(FORMS,)),
    path('wizard/', views.Wizard),
    path('', views.wizardWelcome)
]

