from django.db import models

# Use 'python manage.py makemigrations syllabus' to create tables
# Use 'python manage.py shell' to make a shell


class User(models.Model):
    user_id = models.CharField(max_length=200, primary_key=True)
    role = models.CharField(max_length=15)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    date_created = models.DateTimeField('date created')

    def __str__(self):
        return self.user_id + ": " + self.role


class Syllabi(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # semester_held = SPRING
    semester_held = models.CharField(max_length=6)
    # semester_year = 2021
    semester_year = models.IntegerField()
    # class_dept = CMSC
    class_dept = models.CharField(max_length=4)
    # class_code = 447
    class_code = models.IntegerField()
    # class_id = CMSC447
    class_id = models.CharField(max_length=7, primary_key=True)
    professor_name = models.CharField(max_length=50)

    def __str__(self):
        return self.class_id


class Textbook(models.Model):
    class_id = models.ForeignKey(Syllabi, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

