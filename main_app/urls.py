from django.urls import path
from . import views

urlpatterns = [
    #Authentication route
    path('', views.index, name='index'),
    path('doctor_register', views.doctor_register, name='doctor_register'),
    path('patient_register', views.patient_register, name='patient_register'),

    #Doctor log in portal
    path('doctor/', views.doctor, name='doctor'),

    #Doctor profile page
    path('doctor/profile/', views.doctors_profile, name = 'dprofile'),

    #Doctor schedule page
    path('doctor/schedule/',views.doctors_schedule, name = 'dschedule'),

    #Doctor view of patient profile
    path('doctor/patient/<int:patient_id>', views.doctorpatient, name='doctorpatient'),

    #Doctor view of # NOTE
    path('doctor/patient/<int:patient_id>/<int:note_id>', views.patientnote, name='patientnote'),

    #Patient view of Doctor
    path('patient/doctor/<int:doctor_id>', views.patientdoctor, name='patientdoctor'),

    #Redirect to Admin page
    path('admin/', views.admin, name='admin'),
]
