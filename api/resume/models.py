from django.db import models

# Create your models here.
class Keys(models.Model):
    name = models.CharField(max_length=250)
    key = models.CharField(max_length=250)
class Summary(models.Model):
    name = models.CharField(max_length=250)
    currentPosition = models.CharField(max_length=100)
    summary = models.TextField()

class PersonalData(models.Model):
    fieldName = models.CharField(max_length=250)
    fieldValue = models.CharField(max_length=250)

class Degree(models.Model):
    name = models.CharField(max_length=250)
    institution = models.CharField(max_length=250)
    degree = models.CharField(max_length=250)
    date = models.CharField(max_length=100)

class Language(models.Model):
    name = models.CharField(max_length=100)
    written = models.IntegerField()
    reading = models.IntegerField()
    spoken = models.IntegerField()

class Certifications(models.Model):
    name = models.CharField(max_length=250)
    institution = models.CharField(max_length=250)
    date = models.CharField(max_length=100)