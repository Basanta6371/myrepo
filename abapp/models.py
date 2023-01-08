from django.db import models


class CoomonData(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    class Meta:
        abstract = True


class Student(CoomonData):
    marks = models.IntegerField()


class Employee(CoomonData):
    salary = models.IntegerField()


class Coustomer(CoomonData):

    sales = models.IntegerField()