from django.db import models


class student(models.Model):
    sname = models.CharField(max_length=50)
    fee = models.IntegerField()
    course = models.CharField(max_length=50)
    mobile = models.BigIntegerField()


class feedbackdata(models.Model):
    name = models.CharField(max_length=50)
    rating = models.IntegerField()
    date = models.DateTimeField(max_length=50)
    feedback = models.CharField(max_length=200)


class servicedata(models.Model):
    course_no = models.IntegerField()
    course_name = models.CharField(max_length=50)
    timings = models.TimeField(max_length=50)
    starting_date = models.DateField(max_length=50)
    duration = models.CharField(max_length=50)
    fee = models.FloatField()
    trainer_name = models.CharField(max_length=50)


class Curddata(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField()
    course = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    assignment1 = models.IntegerField()
    assignment2 = models.IntegerField()
    assignment3 = models.IntegerField()
    assignment4 = models.IntegerField()
