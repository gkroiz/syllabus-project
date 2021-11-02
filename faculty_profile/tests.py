from django.test import TestCase
from .models import Profile


# Test for proper Profile database functionality
class ProfileTests(TestCase):

    def setUp(self):
        Profile.objects.create(ID="123VT45", location="ILSB 420", phone="+1 (123) 456-7891", hours="10-11 AM M/W")

    def test_database_object_was_created(self):
        benson = Profile.objects.get(ID="123VT45")
        self.assertEqual(benson.ID, "123VT45")
        self.assertEqual(benson.location, "ILSB 420")
        self.assertEqual(benson.phone, "+1 (123) 456-7891")
        self.assertEqual(benson.hours, "10-11 AM M/W")


# Test for URL routes and Views
class ViewTests(TestCase):

    def test_homepage_view(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)

    def test_edit_view(self):
        response = self.client.get('/profile/edit/')
        self.assertEqual(response.status_code, 200)

    def test_syllabus_view(self):
        response = self.client.get('/profile/syllabus/')
        self.assertEqual(response.status_code, 200)
