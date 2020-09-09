from django.contrib import admin
from .models import DoctorUserProfile, PatientUserProfile, Role, DoctorPatient
# Register your models here.
admin.site.register(DoctorUserProfile)

admin.site.register(PatientUserProfile)

admin.site.register(Role)

admin.site.register(DoctorPatient)
