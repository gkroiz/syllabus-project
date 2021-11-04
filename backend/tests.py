from django.test import TestCase

from .models import *
import datetime

class ModelTest(TestCase):

    user_id = "test"
    role = "student"
    password = "insecure"
    email = "test@email.com"
    date = datetime.date.today()
    year = 123


    def setUp(self):
        User.objects.create(
            user_id=self.user_id,
            role=self.role,
            password=self.password,
            email=self.email,
            date_created=self.date
        )
        Syllabi.objects.create(
            user_id=User.objects.get(user_id="test"),
            semester_held=self.role,
            semester_year=self.year,
            class_dept=self.role,
            class_code=self.year,
            class_id=self.role,
            professor_name=self.role
        )

        Textbook.objects.create(
            class_id=Syllabi.objects.get(class_id=self.role),
            title=self.role,
            author=self.role
        )

    def test_user_string_representation(self):
        user = User.objects.get(user_id="test")
        str_rep = "test: student"
        self.assertEqual(str(user), str_rep)

    def test_user_object_defined(self):
        user = User.objects.get(user_id="test")

        self.assertEqual(user.user_id, self.user_id)
        self.assertEqual(user.password, self.password)
        self.assertEqual(user.role, self.role)
        self.assertEqual(user.email, self.email)

    def test_syllabi_string_representation(self):
        syllabi = Syllabi.objects.get(user_id="test")
        self.assertEqual(str(syllabi), self.role)

    def test_syllabi_object_defined(self):
        syllabi = Syllabi.objects.get(user_id="test")

        self.assertEqual(syllabi.user_id, User.objects.get(user_id="test"))
        self.assertEqual(syllabi.class_id, self.role)
        self.assertEqual(syllabi.class_dept, self.role)
        self.assertEqual(syllabi.class_code, self.year)
        self.assertEqual(syllabi.semester_held, self.role)
        self.assertEqual(syllabi.semester_year, self.year)
        self.assertEqual(syllabi.professor_name, self.role)

    def test_textbook_object_defined(self):
        textbook = Textbook.objects.get(id=1)

        self.assertEqual(textbook.title,self.role)
        self.assertEqual(textbook.author,self.role)
