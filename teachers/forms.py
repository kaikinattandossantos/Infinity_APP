# teachers/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Professor

class TeacherRegistrationForm(forms.ModelForm):
    
    username = forms.CharField(label='Username', max_length=150)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Professor
        
        fields = ['name', 'phone', 'city', 'is_active']