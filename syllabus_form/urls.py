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
         ('16', forms.CourseForm16),
         ('17', forms.CourseForm17),
         ]

urlpatterns = [
    path('wizard/', views.Wizard.as_view(FORMS, ))
]

