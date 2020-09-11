from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class DoctorUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    gender_of_user = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Rather Not Say', 'Rather Not Say')
    ]
    phone_number = models.CharField(max_length=15,default='Enter Number')
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
    # #Personal Information
    address = models.TextField(max_length=200, default='Enter Address')
    phone_number = models.CharField(max_length=15,default='Enter Number')
    date_of_birth = models.CharField(max_length=30, default='day/month/year')
    age = models.IntegerField(default=20)
    health_card_number = models.CharField(max_length=15, default='Enter Number')
    height = models.IntegerField(default=10)
    weight = models.IntegerField(default=10)
    # #Emergency Contact Information
    emergency_contact = models.CharField(max_length=100, default='Enter Name')
    emergency_relation = models.CharField(max_length=50, default='Enter Relationship')
    emergency_number = models.CharField(max_length=15,default='Enter Number')


    def __str__(self):
        return f'{self.user}'


class Proscriptions(models.Model):
  patient = models.ForeignKey(PatientUserProfile,on_delete=models.CASCADE)
  proscribed = models.DateTimeField()
  duration = models.DateTimeField()
  reason = models.CharField(max_length=255)
  additional_information = models.CharField(max_length=100)


class DoctorPatient(models.Model):
  doctor = models.ForeignKey(DoctorUserProfile,on_delete=models.CASCADE)
  patient = models.ForeignKey(PatientUserProfile,on_delete=models.CASCADE)

class Role(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  name = models.CharField(max_length=10)

class PatientNote(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField(max_length=500)
    dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.note}'

class Event(models.Model):
    day = models.DateField(u'Day of the event', help_text=u'Day of the event')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Final time', help_text=u'Final time')
    notes = models.TextField(u'Appointment details', help_text=u'Appointment details', blank=True, null=True)
    doctor = models.ForeignKey(DoctorUserProfile,on_delete=models.CASCADE, blank=True)
    patient = models.ForeignKey(PatientUserProfile,on_delete=models.CASCADE, blank=True)
    class Meta:
        verbose_name = u'Apopointment'
        verbose_name_plural = u'Appointments'

    def __str__(self):
        return f'{self.patient} has an appointment with Dr. {self.doctor}, on {self.day} from {self.start_time} to {self.end_time}'
