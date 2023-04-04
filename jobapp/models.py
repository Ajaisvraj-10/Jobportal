from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser


# Create your models here.

class Mainuser(AbstractUser):
    gender_choices = (
        ('gender','Gender'),
        ('male','Male'), 
        ('female','Female')
    )
    phone = models.CharField(max_length=11)
    gender = models.CharField(max_length=50,choices=gender_choices)
    
class Profile(AbstractBaseUser):
    name = models.CharField(max_length=15)
    domain = models.CharField(max_length=20)
    about = models.TextField(max_length=25)
    email = models.EmailField(max_length=20)
    profile = models.ImageField(upload_to="article_images/", null=True, blank=True)
    cv_upload = models.FileField(upload_to="article_images/",null=True,blank=True)
    
    
    
    


    




