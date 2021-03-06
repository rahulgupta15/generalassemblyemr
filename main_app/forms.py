from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import DoctorUserProfile, PatientUserProfile, PatientNote

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class DoctorUserProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorUserProfile
        type = 'Doctor'
        fields = ('gender','phone_number','education')

class PatientUserProfileForm(forms.ModelForm):
    class Meta:
        model = PatientUserProfile
        fields = ('gender','date_of_birth','address','phone_number','age','health_card_number','height','weight','emergency_contact','emergency_relation','emergency_number')

class PatientNoteForm(forms.ModelForm):
    class Meta:
        model = PatientNote
        fields = ('note',)
