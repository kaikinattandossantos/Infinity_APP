from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        
        fields = ['nome_aluno', 'turma', 'curso'] 
    