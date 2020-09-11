from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import ExtendedUserCreationForm, DoctorUserProfileForm, PatientUserProfileForm, PatientNoteForm
from .models import Role, PatientNote
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request, 'main_app/index.html')

def admin(request):
    return redirect('/admin')

def doctor_register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = DoctorUserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            role = Role(name='Doctor')
            role.user = user
            role.save()

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
            role = Role(name='Patient')
            role.user = user
            role.save()

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

def doctorpatient(request, patient_id):
    patient = User.objects.get(id=patient_id)
    notes = PatientNote.objects.filter(patient=patient)
    # print(PatientNote.objects.filter(patient=patient))
    if request.method == 'POST':
        note_Form = PatientNoteForm(request.POST)

        if note_Form.is_valid():
            note = note_Form.save(commit=False)
            note.patient = patient
            note.save()

            return redirect('doctorpatient', patient_id)
    else:
        note_Form = PatientNoteForm()



    context = {
        'patient':patient,
        'note_Form':note_Form,
        'notes':notes,
    }
    return render(request, 'main_app/doctorpatient.html', context)

def patientdoctor(request, doctor_id):
    doctor = User.objects.get(id=doctor_id)
    return render(request, 'main_app/patientdoctor.html', {'doctor':doctor})

def patientnote(request, patient_id, note_id):
    patient = User.objects.get(id=patient_id)
    note = PatientNote.objects.get(id=note_id)
    # print(note)
    context = {
        'patient':patient,
        'note':note
    }
    return render(request, 'main_app/patientnote.html', context)


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
