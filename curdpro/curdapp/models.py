from django.db import models

class StudentsData(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField()
    course = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    assigment1 = models.IntegerField()
    assigment2 = models.IntegerField()
    assigment3 = models.IntegerField()
    assigment4 = models.IntegerField()
