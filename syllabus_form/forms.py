from django import forms
from .models import Course
from django.db import models

class WelcomeForm(forms.Form):
    course = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ex: CMSC 101'}), label='', max_length=100, required=False)

#department info
class CourseForm1(forms.ModelForm):
    department = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Department', max_length=200)#, attrs={'class': 'form-control'})
    department_office = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ex: Room ITE 404'}), label='Department Office')
    department_phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ex: 111-111-1111'}), label='Department Phone')
    course_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ex: 101'}), label='Course Number')
    course_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Course Name')
    semester = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=(('1', 'Spring'), ('2', 'Summer'), ('3', 'Fall'), ('4','Winter')), label='Semester')
    year = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=(('1', '2021'), ('2', '2022'), ('3', '2023'), ('4','2024')), label='Year')
    course_acronym = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ex: CMSC'}), label='Course Acronym')

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

#general course information
class CourseForm4(forms.Form):
    textbook = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Textbook')
    course_description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Ex: Include catalog description and a statement about the course place in the curriculum or relevance to the discipline'}), label = 'Course Description')
    num_credits = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4','4')), label = 'Number of Credits')
    prerequisites = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Prerequisites')

#course-objectives is a bulleted list, should be dynamic
class CourseForm5(forms.Form):
    course_objectives = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label='')

#instructional methods
class CourseForm6(forms.Form):
    instructional_methods = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label = '')

#attendance and participation
class CourseForm7(forms.Form):
    attendance_participation = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label='Attendance and Participation')

#class preparation and student success
class CourseForm8(forms.Form):
    class_pre_and_student_success = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label='Class Preparation and Student Success')

#course requirements
class CourseForm9(forms.Form):
    course_requirements = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label='Course Requirements')

#grade apportionment
#need to add grading split, and description about each portion of the grade split
class CourseForm10(forms.Form):
    grade_apportionment = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Ex: Homeworks = 15%\nProject = 30%\nExam = 20%\nQuizzes = 15%\nFinal = 20%'}), label='Grade Apportionment')
    descriptions = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Enter information about each different assignment type. For each assignment type, separate with blank line and start with the kind of assignment.'\
     '\n\nFor example:' 
     '\n\nHomeworks: There will be 5 homeworks. Each homework will be assigned 2 weeks before the due date. Collaboration is allowed, but you cannot submit the same work...'\
     '\n\nExams: There will be 2 Exams. You may not use calculators for exams. You must bring picture ID...'}), label='Grade Type Descriptions')
#grading standards  
class CourseForm11(forms.Form):
    grading_standards = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label='Grading Standards')

#due dates
class CourseForm12(forms.Form):
    due_dates = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label='Due Dates')

#make up policy
class CourseForm13(forms.Form):
    make_up_policy = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label='Make-up Policy')

#academic integrity
class CourseForm14(forms.Form):
    academic_integrity = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label='Academic Integrity')

#accommodations
class CourseForm15(forms.Form):
    accommodations = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label='Accommodations')

#course_schedule
class CourseForm16Full(forms.Form):
    #16 weeks worth of fields
    lecture0 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ex: Week 1'}), label='lecture',required=False, max_length=50)
    material0 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Ex: Syllabus Review'}), label='material',required=False, max_length=50)
    due0 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ex: Due: Homework 0'}), label='due', required=False, max_length=50)
    lecture1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Week 2'}), label='lecture',required=False, max_length=50)
    material1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='material',required=False, max_length=50)
    due1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='due', required=False, max_length=50)
    lecture2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Week 3'}), label='lecture',required=False, max_length=50)
    material2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='material',required=False, max_length=50)
    due2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='due', required=False, max_length=50)
    lecture3 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Week 4'}), label='lecture',required=False, max_length=50)
    material3 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='material',required=False, max_length=50)
    due3 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='due', required=False, max_length=50)
    lecture4 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Week 5'}), label='lecture',required=False, max_length=50)
    material4 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='material',required=False, max_length=50)
    due4 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='due', required=False, max_length=50)
    lecture5 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Week 6'}), label='lecture',required=False, max_length=50)
    material5 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='material',required=False, max_length=50)
    due5 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='due', required=False, max_length=50)
    lecture6 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Week 7'}), label='lecture',required=False, max_length=50)
    material6 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='material',required=False, max_length=50)
    due6 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='due', required=False, max_length=50)
    lecture7 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Week 8'}), label='lecture',required=False, max_length=50)
    material7 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='material',required=False, max_length=50)
    due7 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='due', required=False, max_length=50)
    lecture8 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Week 9'}), label='lecture',required=False, max_length=50)
    material8 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='material',required=False, max_length=50)
    due8 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='due', required=False, max_length=50)
    lecture9 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Week 10'}), label='lecture',required=False, max_length=50)
    material9 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='material',required=False, max_length=50)
    due9 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='due', required=False, max_length=50)
    lecture10 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Week 11'}), label='lecture',required=False, max_length=50)
    material10 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='material',required=False, max_length=50)
    due10 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='due', required=False, max_length=50)
    lecture11 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Week 12'}), label='lecture',required=False, max_length=50)
    material11 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='material',required=False, max_length=50)
    due11 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='due', required=False, max_length=50)
    lecture12 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Week 13'}), label='lecture',required=False, max_length=50)
    material12 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='material',required=False, max_length=50)
    due12 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='due', required=False, max_length=50)
    lecture13 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Week 14'}), label='lecture',required=False, max_length=50)
    material13 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='material',required=False, max_length=50)
    due13 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='due', required=False, max_length=50)
    lecture14 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Week 15'}), label='lecture',required=False, max_length=50)
    material14 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='material',required=False, max_length=50)
    due14 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='due', required=False, max_length=50)
    lecture15 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Week 16'}), label='lecture',required=False, max_length=50)
    material15 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='material',required=False, max_length=50)
    due15 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='due', required=False, max_length=50)

#inclement weather
class CourseForm17(forms.Form):
    inclement_weather = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder': ''\
        'Any work or test due on a class date that has been canceled due to inclement weather will be due the next class meeting.'\
    '(If the semester\'s last exam is postponed, it will be given during the time period assigned during the University\'s official Final Exam week.'}),
     label = 'Inclement Weather')
