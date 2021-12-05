from re import sub
from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create your tests here.
from .forms import CourseForm
from .models import Course



class CourseFormTests(TestCase):
    #test that homepage loads
    def test_formpage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    #test that model works with values
    #Note that className, Location, and Professor are all mandatory, hence, we do not need to test if these are empty
    def test_Course(self):
        Course.objects.create(className = 'CMSC 447', professor = 'Benjamin Johnson', location = 'online')
        course = Course.objects.get(className = 'CMSC 447')
        self.assertEqual(course.getCourseName(), 'CMSC 447')
        self.assertEqual(course.getProfessor(),'Benjamin Johnson')
        self.assertEqual(course.getLocation(),'online')

    #test that the model can make new fields
    def test_CourseFormWithExtraFields(self):
        form = CourseForm(data = {'className': 'CMSC 447',
                            'professor': 'Benjamin Johnson',
                            'location': 'online',
        })

        form.fields['extra_field_count']= 1
        form.fields['extra_field_0'] = 'Welcome to this course!'

        self.assertEqual(form.fields['extra_field_count'], 1)
        self.assertEqual(form.fields['extra_field_0'], 'Welcome to this course!')


class CourseFormSeleniumTests(LiveServerTestCase):

    #test just filling in the default boxes and submitting
    def testBasicform(self):
        selenium = webdriver.Chrome(executable_path='/Users/gersonkroiz/chromedriver')

        #choose url to use
        selenium.get('http://127.0.0.1:8000/')

        #find elements needed to submit form
        courseName = selenium.find_element_by_id('id_className')
        professor = selenium.find_element_by_id('id_professor')
        location = selenium.find_element_by_id('id_location')
        body0 = selenium.find_element_by_id('id_extra_field_0')

        submit = selenium.find_element_by_id('submit')

        #populate the form with data
        courseName.send_keys('CMSC 447')
        professor.send_keys('Benjamin Johnson')
        location.send_keys('Online')
        body0.send_keys('Welcome to this course!')

        time.sleep(1) 
        #submit form
        submit.send_keys(Keys.RETURN)

    #testing the save button and making sure it saves the values
    def testSaveButton(self):
        selenium = webdriver.Chrome(executable_path='/Users/gersonkroiz/chromedriver')

        #choose url to use
        selenium.get('http://127.0.0.1:8000/')

        #find elements needed to submit form
        courseName = selenium.find_element_by_id('id_className')
        professor = selenium.find_element_by_id('id_professor')
        location = selenium.find_element_by_id('id_location')
        body0 = selenium.find_element_by_id('id_extra_field_0')

        update = selenium.find_element_by_id('update')
        submit = selenium.find_element_by_id('submit')

        #populate the form with data
        courseName.send_keys('CMSC 447')
        professor.send_keys('Benjamin Johnson')
        location.send_keys('Online')
        body0.send_keys('Welcome to this course!')

        #update form
        update.send_keys(Keys.RETURN)

        #check result; page source looks at entire html document
        assert 'CMSC 447' in selenium.page_source
        assert 'Benjamin Johnson' in selenium.page_source
        assert 'Online' in selenium.page_source
        assert 'Welcome to this course!' in selenium.page_source

        #find elements needed to submit form again
        courseName = selenium.find_element_by_id('id_className')
        professor = selenium.find_element_by_id('id_professor')
        location = selenium.find_element_by_id('id_location')
        body0 = selenium.find_element_by_id('id_extra_field_0')

        update = selenium.find_element_by_id('update')
        submit = selenium.find_element_by_id('submit')

        time.sleep(1) 
        #submit form
        submit.send_keys(Keys.RETURN)

    #testing the add button to make a new field
    def testAddButton(self):
        selenium = webdriver.Chrome(executable_path='/Users/gersonkroiz/chromedriver')

        #choose url to use
        selenium.get('http://127.0.0.1:8000/')

        #find elements needed to submit form
        courseName = selenium.find_element_by_id('id_className')
        professor = selenium.find_element_by_id('id_professor')
        location = selenium.find_element_by_id('id_location')
        body0 = selenium.find_element_by_id('id_extra_field_0')

        add = selenium.find_element_by_id('add')
        submit = selenium.find_element_by_id('submit')

        #populate the form with data
        courseName.send_keys('CMSC 447')
        professor.send_keys('Benjamin Johnson')
        location.send_keys('Online')
        body0.send_keys('Welcome to this course!')

        #add body
        add.send_keys(Keys.RETURN)
        time.sleep(1) 

        #find elements needed to submit form again
        courseName = selenium.find_element_by_id('id_className')
        professor = selenium.find_element_by_id('id_professor')
        location = selenium.find_element_by_id('id_location')
        body0 = selenium.find_element_by_id('id_extra_field_0')
        body1 = selenium.find_element_by_id('id_extra_field_1')


        add = selenium.find_element_by_id('add')
        submit = selenium.find_element_by_id('submit')

        #populate the form with data
        body1.send_keys('Homeworks are worth 20%, Exam 1 is 20%, Final is 20%, Project is 20%, and Quizzes are 20%.')
        time.sleep(1) 

        #submit form
        submit.send_keys(Keys.RETURN)

    #testing the remove button to remove a new field
    def testRemoveButton(self):
        selenium = webdriver.Chrome(executable_path='/Users/gersonkroiz/chromedriver')

        #choose url to use
        selenium.get('http://127.0.0.1:8000/')

        #find elements needed to submit form
        courseName = selenium.find_element_by_id('id_className')
        professor = selenium.find_element_by_id('id_professor')
        location = selenium.find_element_by_id('id_location')
        body0 = selenium.find_element_by_id('id_extra_field_0')

        add = selenium.find_element_by_id('add')
        submit = selenium.find_element_by_id('submit')

        #populate the form with data
        courseName.send_keys('CMSC 447')
        professor.send_keys('Benjamin Johnson')
        location.send_keys('Online')
        body0.send_keys('Welcome to this course!')

        #add body
        add.send_keys(Keys.RETURN)
        time.sleep(1) 

        #find element to remove body
        remove = selenium.find_element_by_id('remove')

        #remove body
        remove.send_keys(Keys.RETURN)
        time.sleep(1) 

        #find elements needed to submit form again
        courseName = selenium.find_element_by_id('id_className')
        professor = selenium.find_element_by_id('id_professor')
        location = selenium.find_element_by_id('id_location')
        body0 = selenium.find_element_by_id('id_extra_field_0')


        add = selenium.find_element_by_id('add')
        remove = selenium.find_element_by_id('remove')
        submit = selenium.find_element_by_id('submit')


        #submit form
        submit.send_keys(Keys.RETURN)
