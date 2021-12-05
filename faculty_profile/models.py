from django.db import models


# Create your models here.

# model: Faculty Profile
# attributes: ID, name, email, office phone, office location
class Profile(models.Model):
    ID = models.CharField(max_length=50, primary_key=True)
    location = models.CharField(max_length=100, default='None')
    phone = models.CharField(max_length=20, default='+1 (000) 000-0000')
