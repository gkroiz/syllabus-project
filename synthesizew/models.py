from django.db import models


# Create your models here.
class Syllabus(models.Model):
    syllabus_file = models.FileField(upload_to='syllabi/', default='syllabus.pdf')
    title = models.CharField(max_length=9, default='TUFF 101', primary_key=True)
    instructor_name = models.TextField(default='Dr. Hrabowski')
    instructor_phone = models.CharField(max_length=14, default='(410) 455-1000')
    instructor_email = models.CharField(max_length=41, default='noreply@umbc.edu')
    ta_name = models.TextField(default='Philip Rous')
    ta_email = models.CharField(max_length=41, default='UMBCHelp@rt.umbc.edu')
    course_site = models.TextField(default='https://blackboard.umbc.edu')
    office_hours = models.TextField(default='2-3am')
    course_time = models.TextField(default='9am-5pm')
    course_description = models.TextField(default='A course that didn\'t have one!')
    course_objectives = models.TextField(default='Just try your hardest!')
    prereqs = models.TextField(default='Admission to UMBC, a willingness to succeed, and a passion for more')
    textbook = models.TextField(default='Dune by Frank Herbert')
    instruct_methods = models.TextField(default='IRL talking')
    attendance_rule = models.TextField(default='Stick around!')
    class_preparation = models.TextField(default='Listen, learn, grow')
    course_requirements = models.TextField(default='See class preparation steps')
    grade_breakdown = models.TextField(default='If you try, you get 100%')
    quizzes = models.TextField(default='Also called \'bad news\'')
    exams = models.TextField(default='Those really tough days and situations')
    prog_assignments = models.TextField(default='Arguments and confrontations')
    participation = models.TextField(default='100% of your grade is being there')
    hands_on = models.TextField(default='See participation grade')
    assignments = models.TextField(default='Be the best you you can be')
    homework = models.TextField(default='Life has no homework (wish school was the same)')
    late_policy = models.TextField(default='Whenever it suits you')
    makeup_policy = models.TextField(default='There are no second chances')

    @staticmethod
    def is_created(self, syllabus, key_value):
        return hasattr(syllabus, key_value)
