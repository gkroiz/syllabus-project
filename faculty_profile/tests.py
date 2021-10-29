from django.test import TestCase
from .models import Profile


# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        Profile.objects.create(ID="123VT45", name="John Benson", email="jbenson1@umbc.edu", location="ILSB 420",
                               phone="+1 (123) 456-7891", hours="10-11 AM M/W")

    def test_database_object_was_created(self):
        benson = Profile.objects.get(ID="123VT45")
        self.assertEqual(benson.ID, "123VT45")
        self.assertEqual(benson.name, "John Benson")
        self.assertEqual(benson.email, "jbenson1@umbc.edu")
        self.assertEqual(benson.location, "ILSB 420")
        self.assertEqual(benson.phone, "+1 (123) 456-7891")
        self.assertEqual(benson.hours, "10-11 AM M/W")
