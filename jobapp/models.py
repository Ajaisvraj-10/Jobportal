from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Mainuser(AbstractUser):
    gender_choices = (
        ('gender','Gender'),
        ('male','Male'),
        ('female','Female')
    )
    phone = models.CharField(max_length=11)
    gender = models.CharField(max_length=50,choices=gender_choices)
    


