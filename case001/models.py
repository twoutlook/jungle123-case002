from django.db import models

class Data1(models.Model):
    date1 = models.DateField()
    place = models.CharField(max_length=100)
    worker = models.CharField(max_length=100)
    thing = models.CharField(max_length=100)