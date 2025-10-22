# teachers/forms.py
from django import forms
from .models import Professor

class TeacherRegistrationForm(forms.ModelForm):

    class Meta:
        model = Professor
        
        fields = ['name', 'phone', 'city', 'is_active']