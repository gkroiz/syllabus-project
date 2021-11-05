import time
from selenium import webdriver
from selenium.webdriver import Keys
from django.test import TestCase
from django.test import LiveServerTestCase


# Create your tests here.


class SignupTests(TestCase):
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_signup_view(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)


class CourseFormSeleniumTests(LiveServerTestCase):

    # test just filling in the default boxes and submitting
    def testBasicform(self):
        selenium = webdriver.Chrome('/Users/deepmistry/bin/chromedriver')

        # choose url to use
        selenium.get('http://127.0.0.1:8000/signup')
        email = selenium.find_element_by_id('id_email')
        firstName = selenium.find_element_by_id('id_first_name')
        lastName = selenium.find_element_by_id('id_last_name')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')
        submit = selenium.find_element_by_name('submit')

        # adds the value in fields
        email.send_keys('user@umbc.edu')
        firstName.send_keys('user')
        lastName.send_keys('Last')
        password1.send_keys('Password@1')
        password2.send_keys('Password@1')
        time.sleep(5)

        # submit form
        submit.send_keys(Keys.RETURN)
        submit.send_keys(Keys.RETURN)
