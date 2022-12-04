from django.db import models

class EmpData(models.Model):
    name = models.CharField(max_length=20)
    salary = models.IntegerField()
    company = models.CharField(max_length=20)
