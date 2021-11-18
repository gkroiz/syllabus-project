from django import forms
from .models import Course
from django.db import models

#department info
class CourseForm1(forms.Form):
    department = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Department', max_length=200)#, attrs={'class': 'form-control'})
    department_office = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Room ITE 404'}), label='Department Office')
    department_phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'111-111-1111'}), label='Department Phone')
    course_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'101'}), label='Course Number')
    course_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Course Name')
    semester = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=(('1', 'Spring'), ('2', 'Summer'), ('3', 'Fall'), ('4','Winter')), label='Semester')
    year = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=(('1', '2021'), ('2', '2022'), ('3', '2023'), ('4','2024')), label='Year')
    course_acronym = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'CMSC'}), label='Course Acronym')

#class info
class CourseForm2(forms.Form):
    instructor_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Name')
    instructor_phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Number')
    instructor_email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}), label='E-mail')
    instructor_fax = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Fax', required=False)
    instructor_website = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Website', required=False)
    instructor_course_delivery_site = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Course Delivery Site')
    instructor_office_hours = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Office Hours')

# meeting times should be dynamic for both lecture and discussion
class CourseForm3(forms.Form):
    meeting_times = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label='')


class CourseForm4(forms.Form):
    textbook = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Textbook')
    course_description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Include catalog description and a statement about the course place in the curriculum or relevance to the discipline'}), label = 'Course Description')
    num_credits = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4','4')), label = 'Number of Credits')
    prerequisites = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Prerequisites')

#course-objectives is a bulleted list, should be dynamic
class CourseForm5(forms.Form):
    course_objectives = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label='')


class CourseForm6(forms.Form):
    instructional_methods = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label = 'Instruction Methods')

class CourseForm7(forms.Form):
    attendance_participation = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label='Attendance and Participation')

class CourseForm8(forms.Form):
    class_pre_and_student_success = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label='Class Preparation and Student Success')

class CourseForm9(forms.Form):
    course_requirements = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label='Course Requirements')

#need to add grading split, and description about each portion of the grade split
class CourseForm10(forms.Form):
    grade_apportionment = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Homeworks = 15%\nProject = 30%\nExam = 20%\nQuizzes = 15%\nFinal = 20%'}), label='Grade Apportionment')


class CourseForm11(forms.Form):
    grading_standards = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label='Grading Standards')
    
class CourseForm12(forms.Form):
    due_dates = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label='Due Dates')

class CourseForm13(forms.Form):
    make_up_policy = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label='Make-up Policy')

class CourseForm14(forms.Form):
    academic_integrity = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label='Academic Integrity')

class CourseForm15(forms.Form):
    accomodations = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label='Accomodations')

#course_schedule
class CourseForm16(forms.Form):
    course_schedule = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'This part is incomplete and will be revised.'}), label='course_schedule')
    # course_schedule = ...

class CourseForm17(forms.Form):
    inclement_weather = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label = 'Inclement Weather')