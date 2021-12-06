from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from django.test import TestCase
from synthesizew.models import Syllabus
from django.test import LiveServerTestCase
import time


# tests search subdomain fully accessible
class ViewTests(TestCase):
    def test_lookup_view(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200)


class LookupCourseTests(LiveServerTestCase):
    # sets up Syllabus objects so search can occur
    # @classmethod
    # def setUpClass(cls):
    #     super().setUpClass()
    #     print("test A")
    #     cls.syllabus_1 =
    #     cls.syllabus_1.save()
    #     print("test B")

    # runs search for course title and gets results based on inputted db entry
    def test_search_for_course_title(self):
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
                                makeup_policy='There are no second chances').save()
        selenium = webdriver.Chrome(executable_path='chromedriver')
        selenium.get('%s%s' % (self.live_server_url, '/search/'))

        selenium.implicitly_wait(1000)

        query_type_select = Select(selenium.find_element_by_id("dropdown"))
        query_type_select.select_by_value("course_title")

        course_title_input = selenium.find_element_by_id("search_bar")
        course_title_input.send_keys("TUFF 101")

        submit_input = selenium.find_element_by_id("submit_click")
        submit_input.click()

        time.sleep(2)

        try:
            selenium.find_element_by_id("results_header")
        except NoSuchElementException:
            self.assertTrue(0)

        selenium.quit()

    # runs search for course instructor and gets results based on inputted db entry
    def test_search_for_instructor(self):
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
                                makeup_policy='There are no second chances').save()
        print(Syllabus.objects.filter(title__contains="TUFF"))
        selenium = webdriver.Chrome(executable_path='chromedriver')
        selenium.get('%s%s' % (self.live_server_url, '/search/'))

        selenium.implicitly_wait(1000)

        query_type_select = Select(selenium.find_element_by_id("dropdown"))
        query_type_select.select_by_value("instructor_name")

        course_title_input = selenium.find_element_by_id("search_bar")
        course_title_input.send_keys("Hrabowski")

        submit_input = selenium.find_element_by_id("submit_click")
        submit_input.click()

        time.sleep(2)

        try:
            selenium.find_element_by_id("results_header")
        except NoSuchElementException:
            self.assertTrue(0)

        selenium.quit()

    # runs search for course time and gets results based on inputted db entry
    def test_search_for_course_time(self):
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
                                makeup_policy='There are no second chances').save()
        selenium = webdriver.Chrome(executable_path='chromedriver')
        selenium.get('%s%s' % (self.live_server_url, '/search/'))

        selenium.implicitly_wait(1000)

        query_type_select = Select(selenium.find_element_by_id("dropdown"))
        query_type_select.select_by_value("course_time")

        course_title_input = selenium.find_element_by_id("search_bar")
        course_title_input.send_keys("5pm")

        submit_input = selenium.find_element_by_id("submit_click")
        submit_input.click()

        time.sleep(2)

        try:
            selenium.find_element_by_id("results_header")
        except NoSuchElementException:
            self.assertTrue(0)

        selenium.quit()
