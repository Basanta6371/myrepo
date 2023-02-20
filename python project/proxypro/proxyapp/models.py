from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    marks = models.IntegerField()


class StudentProxy(Student):

    class Meta:
        proxy = True
