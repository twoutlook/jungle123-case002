from django.db import models

class Data1(models.Model):
    date1 = models.DateField()
    place = models.CharField(max_length=100)
    worker = models.CharField(max_length=100)
    thing = models.CharField(max_length=100)

class Data2(models.Model):
    name = models.CharField(max_length=32)
    member =  models.CharField(max_length=6)
    date1 = models.DateField()
    role = models.CharField(max_length=32)
    points = models.IntegerField(default=0)
    class Meta:
        unique_together = ('name', 'date1','member',)

class Best(models.Model):
    date1 = models.DateField()
    title = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    class Meta:
        unique_together = ( 'date1','title')