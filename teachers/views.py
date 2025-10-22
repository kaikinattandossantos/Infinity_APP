from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Professor
from .forms import TeacherRegistrationForm 

class TeacherCreateView(CreateView):
    model = Professor
    form_class = TeacherRegistrationForm 
    template_name = 'teachers/teacher_form.html'
    success_url = reverse_lazy('teacher_list')