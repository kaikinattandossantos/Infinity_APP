from django import forms
from .models import Professor

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['user', 'name', 'phone', 'is_active']