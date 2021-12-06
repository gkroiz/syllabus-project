from django.db import models


# Create your models here.

# model: Faculty Profile
# attributes: ID, name, email, office phone, office location
class Profile(models.Model):
    faculty_id = models.CharField(max_length=50, primary_key=True)
    location = models.CharField(max_length=100, default='None')
    phone = models.CharField(max_length=20, default='+1 (000) 000-0000')

    def __str__(self):
        return self.faculty_id


class OfficeHours(models.Model):
    faculty_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_time = models.CharField(max_length=100)

    class Meta:
        ordering = ['faculty_id']
