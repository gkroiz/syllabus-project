from django.test import TestCase


# Test for URL routes and Views
class ViewTests(TestCase):

    def test_homepage_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_search_view(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200)
