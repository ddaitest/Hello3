import datetime
from django.db import models
from django.utils import timezone


# Create your models here.

class Driver(models.Model):
    avatar = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    reg_date = models.DateTimeField('register at')

    def __str__(self):
        return self.name


class Task(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    start = models.CharField(max_length=200)
    end = models.CharField(max_length=200)
    quota = models.IntegerField(default=1)
    remarks = models.CharField(max_length=200)
    departure = models.DateTimeField('departure')

    def __str__(self):
        return self.start + self.end

    def my_departure(self):
        return datetime.timedelta(days=1)
