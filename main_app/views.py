from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import ExtendedUserCreationForm, DoctorUserProfileForm, PatientUserProfileForm
# Create your views here.

def index(request):
    return render(request, 'main_app/index.html')

def doctor_register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = DoctorUserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('index')
    else:
        form = ExtendedUserCreationForm()
        profile_form = DoctorUserProfileForm()

    context = {
    'form' : form,
    'profile_form' : profile_form
    }
    return render(request, 'registration/doctor_register.html', context)

def patient_register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = PatientUserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('index')
    else:
        form = ExtendedUserCreationForm()
        profile_form = PatientUserProfileForm()

    context = {
    'form' : form,
    'profile_form' : profile_form
    }
    return render(request, 'registration/patient_register.html', context)

#Doctor log in portal
def doctor(request):
  if request.method =='GET':
    try:
      return render(request, 'doctor/doctor.html')
    except Exception as e:
      return HttpResponse({e})

#Doctor profile portal
def doctors_profile(request):
  return render(request, 'doctor/profile.html')

#Doctor schedule
def doctors_schedule(request):
  return render(request, 'doctor/schedule.html')