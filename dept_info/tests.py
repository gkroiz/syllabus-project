from django.test import TestCase
from selenium import webdriver
from selenium.webdriver import Keys
from django.test import TestCase
from django.test import LiveServerTestCase
import time


# Test for URL routes and Views
class ViewTests(TestCase):

    def test_dept_view(self):
        response = self.client.get('/dept_info/')
        self.assertEqual(response.status_code, 200)

    # test the signup view
    def test_dept_submitted_view(self):
        response = self.client.get('/dept_info/submitted')
        self.assertEqual(response.status_code, 200)


class DepartmentSeleniumTests(LiveServerTestCase):

    # test just filling in the default boxes and submitting
    def test_info_submit(self):
        selenium = webdriver.Chrome('chromedriver')

        # Goes to signup page
        selenium.get('http://127.0.0.1:8000/dept_info')

        # Finds the fields
        dept = selenium.find_element_by_name('dept_info')

        # tests if you can add items
        dept.send_keys("Did you ever hear the tragedy of Darth Plagueis The Wise?")

        button = selenium.find_element_by_name('Update')
        button.click()
        self.assertEqual(selenium.current_url, 'http://127.0.0.1:8000/dept_info/submitted')

    def test_go_back(self):
        selenium = webdriver.Chrome('chromedriver')
        selenium.get('http://127.0.0.1:8000/dept_info/submitted')
        button = selenium.find_element_by_name('go_back')
        button.click()
        self.assertEqual(selenium.current_url, 'http://127.0.0.1:8000/dept_info/')


