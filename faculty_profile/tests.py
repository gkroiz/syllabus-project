from django.test import TestCase

from .models import Profile, OfficeHours
from .forms import EditProfileForm


# Test for proper Profile database functionality
class ProfileTests(TestCase):

    def setUp(self):
        Profile.objects.create(faculty_id='123VT45', location='ILSB 420', phone='+1 (123) 456-7891')

    def test_database_object_was_created(self):
        benson = Profile.objects.get(faculty_id='123VT45')
        self.assertEqual(benson.faculty_id, '123VT45')
        self.assertEqual(benson.location, 'ILSB 420')
        self.assertEqual(benson.phone, '+1 (123) 456-7891')


# Test for proper Profile database functionality
class OfficeHoursTests(TestCase):

    def setUp(self):
        profile = Profile.objects.create(faculty_id='123VT45', location='ILSB 420', phone='+1 (123) 456-7891')
        OfficeHours.objects.create(faculty=profile, date_time='MWF 1-2PM')

    def test_database_object_was_created(self):
        benson = Profile.objects.get(faculty_id='123VT45')
        benson_oh = OfficeHours.objects.get(faculty='123VT45')
        self.assertEqual(benson.faculty_id, benson_oh.faculty.faculty_id)
        self.assertEqual(benson_oh.date_time, 'MWF 1-2PM')


# Test for proper Edit form functionality
class FormTests(TestCase):
    def test_good_form(self):
        form_data = {'faculty_id': '123UMBC', 'location': 'ILSB 106b', 'phone': '+1 (444) 555-3322',
                     'extra_field_count': 0}
        form = EditProfileForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_bad_phone(self):
        form_data = {'faculty_id': '1', 'location': 'ITE', 'phone': '+1 (444) 555-33221111111111111111111',
                     'extra_field_count': 0}
        form = EditProfileForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_missing_field(self):
        form_data = {'faculty_id': '1', 'location': 'ITE', 'phone': '+1 (444) 555-3322'}
        form = EditProfileForm(data=form_data)
        self.assertFalse(form.is_valid())
