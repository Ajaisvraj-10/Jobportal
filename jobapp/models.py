from typing import AbstractSet
from unittest import result
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save

# Create your models here.


class Mainuser(AbstractUser):
    gender_choices = (("gender", "Gender"), ("male", "Male"), ("female", "Female"))
    phone = models.CharField(max_length=11)
    gender = models.CharField(max_length=50, choices=gender_choices)


class Profile(AbstractBaseUser):
    name = models.CharField(max_length=15)
    domain = models.CharField(max_length=20)
    about = models.TextField(max_length=25)
    email = models.EmailField(max_length=20)
    profile = models.ImageField(upload_to="article_images/", null=True, blank=True)
    cv_upload = models.FileField(upload_to="article_images/", null=True, blank=True)



class User(AbstractUser):
    class Role(models.TextChoices):
     ADMIN = "ADMIN", "Admin"
    STUDENT = "STUDENT", "Student"
    TEACHER = "TEACHER", "Teacher"

    base_role = "ADMIN"

    role = models.CharField(max_length=50, choices=Role.choices, default=Role.base_role)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        return super().save(*args, **kwargs)

class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.STUDENT)


class Student(User):
    base_role = User.Role.STUDENT

    student = StudentManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for students"


class TeacherManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.TEACHER)


class Teacher(User):
    base_role = User.Role.TEACHER

    student = TeacherManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for teachers"
