from django.contrib import admin
from .models import DoctorUserProfile, PatientUserProfile, Role, DoctorPatient, Event
# Register your models here.
admin.site.register(DoctorUserProfile)

admin.site.register(PatientUserProfile)

admin.site.register(Role)

admin.site.register(DoctorPatient)

admin.site.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['day', 'start_time', 'end_time', 'patient', 'doctor','notes']
