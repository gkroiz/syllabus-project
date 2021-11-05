from django.db import models

from django import forms
# Create your models here.

class Course(models.Model):
    className = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def getCourseName(self):
        return self.className

    def getProfessor(self):
        return self.professor
    
    def getLocation(self):
        return self.location