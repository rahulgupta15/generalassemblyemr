from django.contrib import admin
from .models import DoctorUserProfile, PatientUserProfile
# Register your models here.
admin.site.register(DoctorUserProfile)

admin.site.register(PatientUserProfile)
