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
    #Personal Information
    #address = models.CharField(max_length=100)
    #date_of_birth = models.DateTimeField()
    #health_card_number = models.IntegerField()
    #height = models.IntegerField()
    #weight = models.IntegerField()
    #Emergency Contact Information
    #emergency_contact = models.CharField(max_length=100)
    #emergency_relation = models.CharField(max_length=15)
    #emergency_number = models.IntegerField()
    #Appointment History - in progress
    doctor = models.ForeignKey(DoctorUserProfile, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user}'

class Proscriptions(models.Model):
  patient = models.ForeignKey(PatientUserProfile,on_delete=models.CASCADE)
  proscribed = models.DateTimeField()
  duration = models.DateTimeField()
  reason = models.CharField(max_length=255)
  additional_information = models.CharField(max_length=100)

class Conditions(models.Model):
  patient = models.ForeignKey(PatientUserProfile,on_delete=models.CASCADE)
  condition = models.CharField(max_length=100)
  diagnosed = models.DateTimeField()

class Appointment(models.Model):
  patient = models.ForeignKey(PatientUserProfile,on_delete=models.CASCADE)
  date = models.DateTimeField()
  next_appointment = models.DateTimeField()

class Admin(models.Model):
    doctor = models.ForeignKey(DoctorUserProfile,on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientUserProfile,on_delete=models.CASCADE)