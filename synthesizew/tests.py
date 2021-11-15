from django.test import TestCase
from synthesizew.models import Syllabus


# Create your tests here.
class SyllabusTestCase(TestCase):
    def setUp(self):
        # create two syllabus objects as a way of testing two scenarios - one with all data,
        # one missing some data
        Syllabus.objects.create(syllabus_file='syllabus.pdf',
                                title='TUFF 101',
                                instructor_name='Dr. Hrabowski',
                                instructor_phone='(410) 455-1000',
                                instructor_email='noreply@umbc.edu',
                                ta_name='Philip Rous',
                                ta_email='UMBCHelp@rt.umbc.edu',
                                course_site='https://blackboard.umbc.edu',
                                office_hours='2-3am',
                                course_time='9am-5pm',
                                course_description='A course that didn\'t have one!',
                                course_objectives='Just try your hardest!',
                                prereqs='Admission to UMBC, a willingness to succeed, and a passion for more',
                                textbook='Dune by Frank Herbert',
                                instruct_methods='IRL talking',
                                attendance_rule='Stick around!',
                                class_preparation='Listen, learn, grow',
                                course_requirements='See class preparation steps',
                                grade_breakdown='If you try, you get 100%',
                                quizzes='Also called \'bad news\'',
                                exams='Those really tough days and situations',
                                prog_assignments='Arguments and confrontations',
                                participation='100% of your grade is being there',
                                hands_on='See participation grade',
                                assignments='Be the best you you can be',
                                homework='Life has no homework (wish school was the same,',
                                late_policy='Whenever it suits you',
                                makeup_policy='There are no second chances')
        Syllabus.objects.create(syllabus_file='syllabus_CMSC104.pdf',
                                title='CMSC 104',
                                instructor_name='Dr. Jeremy Dixon',
                                instructor_email='jdixon@umbc.edu',
                                course_site='https://blackboard.umbc.edu',
                                office_hours='2-3am',
                                course_time='9am-5pm',
                                course_description='A course that didn\'t have one!',
                                prereqs='Admission to UMBC and a willingness to fail',
                                textbook='Dune by Frank Herbert',
                                instruct_methods='IRL talking',
                                attendance_rule='100% attendance of all classes online and in-person',
                                course_requirements='None',
                                grade_breakdown='45% exams, 30% quizzes, 10% participation, 15% projects',
                                quizzes='Three short essay questions',
                                exams='10 short essay questions, 1 hour each',
                                prog_assignments='Linked lists and building an OS from scratch',
                                late_policy='No late assignments allowed',
                                makeup_policy='Email professor for details')

    def test_dictionary_setup_correctly(self):
        """ Syllabi that are complete should have all fields attached! (which is expected - even if blank) """
        syllabus_1 = Syllabus.objects.get(title="TUFF 101")
        syllabus_2 = Syllabus.objects.get(title="CMSC 104")
        keys = ['syllabus_file', 'title', 'instructor_name', 'instructor_email', 'ta_name', 'ta_email',
                'course_site', 'instructor_phone', 'office_hours', 'course_time', 'course_description',
                'course_objectives', 'prereqs', 'textbook', 'instruct_methods', 'attendance_rule',
                'class_preparation', 'course_requirements', 'grade_breakdown', 'quizzes', 'exams',
                'prog_assignments', 'participation', 'hands_on', 'assignments', 'homework', 'late_policy',
                'makeup_policy']
        for key in keys:
            # check each syllabus has all fields (even if empty)
            self.assertTrue(hasattr(syllabus_1, key))
            self.assertTrue(hasattr(syllabus_2, key))

    # both tests here confirm they are themselves and not cross-contaminating data (and that they have
    # the same number of fields)
    def test_fields_correct_syllabus_1(self):
        syllabus = Syllabus.objects.get(title="TUFF 101")
        self.assertEqual(syllabus.ta_name, "Philip Rous")
        self.assertEqual(syllabus.course_site, "https://blackboard.umbc.edu")
        self.assertNotEqual(syllabus.title, "CMSC 104")
        self.assertFalse(syllabus.title == Syllabus.objects.get(title="CMSC 104").ta_name)

    def test_fields_correct_syllabus_2(self):
        syllabus = Syllabus.objects.get(title="CMSC 104")
        self.assertEqual(syllabus.ta_name, "Philip Rous")
        self.assertEqual(syllabus.course_site, "https://blackboard.umbc.edu")
        self.assertNotEqual(syllabus.title, "TUFF 101")
        self.assertEqual(Syllabus.objects.get(title="CMSC 104")._meta.get_fields(),
                         Syllabus.objects.get(title="TUFF 101")._meta.get_fields())
