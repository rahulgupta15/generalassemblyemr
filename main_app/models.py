from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class DoctorUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    gender_of_user = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Rather Not Say', 'Rather Not Say')
    ]
    type = 'Doctor'
    gender = models.CharField(max_length=15, choices = gender_of_user)
    education = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.user}'

class PatientUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    gender_of_user = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Rather Not Say', 'Rather Not Say')
    ]
    gender = models.CharField(max_length=15, choices = gender_of_user)
    doctor = models.ForeignKey(DoctorUserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'
