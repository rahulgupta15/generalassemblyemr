from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doctor_register', views.doctor_register, name='doctor_register'),
    path('patient_register', views.patient_register, name='patient_register'),
]
