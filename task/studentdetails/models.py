from django.db import models

# Create your models here.
class student (models.Model):
    rollno=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=100)


