import time
from selenium import webdriver
from selenium.webdriver import Keys
from django.test import TestCase
from django.test import LiveServerTestCase


# Create your tests here.
from selenium.webdriver.common import keys


class LoginTest(TestCase):
    # test the login view
    def test_login_view(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    # test the signup view
    def test_signup_view(self):
        response = self.client.get('/login/signup/')
        self.assertEqual(response.status_code, 200)

    # test the forgotPassword view
    def test_forgot_password_view(self):
        response = self.client.get('/login/password_reset/')
        self.assertEqual(response.status_code, 200)

    # test the sent email view
    def test_password_reset_email_sent_view(self):
        response = self.client.get('/password_reset/done/')
        self.assertEqual(response.status_code, 200)

    # test the password Change view
    def test_password_change_view(self):
        response = self.client.get('/reset/MjU/set-password/')
        self.assertEqual(response.status_code, 200)

    # test the password reset done view
    def test_password_reset_dont_view(self):
        response = self.client.get('/reset/done/')
        self.assertEqual(response.status_code, 200)


class CourseFormSeleniumTests(LiveServerTestCase):

    # test just filling in the default boxes and submitting
    def testSignupform(self):
        selenium = webdriver.Chrome('/Users/deepmistry/bin/chromedriver')
        # Goes to signup page
        selenium.get('http://127.0.0.1:8000/login/signup')

        # Finds the fields
        email = selenium.find_element_by_name('email')
        first_name = selenium.find_element_by_name('first_name')
        last_name = selenium.find_element_by_name('last_name')
        password1 = selenium.find_element_by_name('password1')
        password2 = selenium.find_element_by_name('password2')
        submit = selenium.find_element_by_tag_name('button')
        dropdown = selenium.find_element_by_name('user_type')

        # adds the value in fields
        email.send_keys("user@umbc.edu")
        first_name.send_keys("Test")
        last_name.send_keys("User")
        password1.send_keys("Password@1")
        password2.send_keys("Password@1")

        # selects the department
        for option in dropdown.find_elements_by_tag_name('option'):
            if option.text == 'Faculty':
                option.click()

        time.sleep(5)
        submit.send_keys(Keys.RETURN)
        time.sleep(5)


    def testLoginForm(self):
        selenium = webdriver.Chrome('/Users/deepmistry/bin/chromedriver')
        # Goes to signup page
        selenium.get('http://127.0.0.1:8000/login')

        email = selenium.find_element_by_name('email')
        password1 = selenium.find_element_by_name('password')
        submit = selenium.find_element_by_tag_name('button')

        email.send_keys("user@umbc.edu")
        password1.send_keys("Password@1")
        time.sleep(5)
        submit.send_keys(Keys.RETURN)
        time.sleep(5)

    def testForgotPasswordForm(self):
        selenium = webdriver.Chrome('/Users/deepmistry/bin/chromedriver')
        # Goes to signup page
        selenium.get('http://127.0.0.1:8000/login/password_reset')

        email = selenium.find_element_by_name('email')
        submit = selenium.find_element_by_tag_name('button')

        email.send_keys("user@umbc.edu")
        time.sleep(5)
        submit.send_keys(Keys.RETURN)
        time.sleep(5)

    def testDropDown(self):
        selenium = webdriver.Chrome('chromedriver')
        selenium.get('http://127.0.0.1:8000/login/signup')
        dropdown = selenium.find_element_by_name('user_type')
        self.assertTrue(dropdown.is_displayed())
        # selects the department
        for option in dropdown.find_elements_by_tag_name('option'):
            if option.text == 'Department':
                option.click()

