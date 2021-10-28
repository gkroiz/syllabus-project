from django.db import models


# Create your models here.

# model: Faculty
# attributes: ID, name, email, office phone, office location, office hours
class Profile(models.Model):
    ID = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    office_phone = models.CharField(max_length=20)
    office_hours = models.CharField(max_length=200)
