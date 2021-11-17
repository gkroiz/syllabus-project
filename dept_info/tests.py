from django.test import TestCase


# Test for URL routes and Views
class ViewTests(TestCase):

    def test_dept_view(self):
        response = self.client.get('/dept')
        self.assertEqual(response.status_code, 200)
