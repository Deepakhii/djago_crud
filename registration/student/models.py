from django.db import models
from datetime import datetime
# Create your models here.

class StudentReg(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    name= models.CharField(max_length=200)
    email   = models.EmailField()
    mobile  = models.IntegerField()
    gender  = models.CharField(max_length=6, choices=GENDER_CHOICES)
    dob     = models.DateField()
    file    = models.FileField(upload_to='images/')
    password = models.CharField(max_length=200)
    time= models.DateTimeField(default=datetime.now(), blank=True)