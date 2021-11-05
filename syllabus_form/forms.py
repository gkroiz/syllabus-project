from django import forms
from .models import Course
from django.db import models

# class CourseForm(forms.Form):
#     # class Meta:
#     #     model = Course
#     #     fields = {  'className': forms.CharField(max_length=100, label='Course Name'),
#     #                 'professor' : forms.CharField(max_length=100, label='Professor'),
#     #                 'location' : forms.CharField(max_legnth=100, label='Class Location'),
#     #                 'body' : forms.CharField(widget=forms.Textarea, label='Body')
#         # }
#     className = forms.CharField(max_length=100, label='Course Name')
#     professor = forms.CharField(max_length=100, label='Professor')
#     location = forms.CharField(max_length=100, label='Class Location')
#     # body = forms.CharField(widget=forms.Textarea, label='Body 0')   
#     # extra_field_count = 0
#     def __init__(self, *args, **kwargs):
#             extra_fields = kwargs.pop('extra', 1)

#             super(CourseForm, self).__init__(*args, **kwargs)
#             self.fields['extra_field_count'].initial = extra_fields

#             for index in range(int(extra_fields)):
#                 # generate extra fields in the number specified via extra_fields
#                 self.fields['extra_field_{index}'.format(index=index)] = \
#                     forms.CharField(widget=forms.Textarea, label='Body ' + str(index), required=False)
#     extra_field_count = forms.CharField(widget=forms.HiddenInput(), label = '')

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = {  'className',
                    'professor',
                    'location',
        }

    #init finds number of extra fields, and makes CharFields accordingly
    def __init__(self, *args, **kwargs):
            extra_fields = kwargs.pop('extra', 1)

            super(CourseForm, self).__init__(*args, **kwargs)
            self.fields['extra_field_count'].initial = extra_fields

            for index in range(int(extra_fields)):
                # generate extra fields in the number specified via extra_fields
                self.fields['extra_field_{index}'.format(index=index)] = \
                    forms.CharField(widget=forms.Textarea, label='Body ' + str(index), required=False)
    extra_field_count = forms.CharField(widget=forms.HiddenInput(), label = '')