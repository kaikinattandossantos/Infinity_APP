from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from .models import Professor
from .forms import TeacherForm 

class TeacherListView(ListView):
    model = Professor
    template_name = 'teachers/teacher_list.html'
    context_object_name = 'teachers'
    
    def get_queryset(self):
        return Professor.objects.filter(is_active=True).select_related('user')
        
class TeacherDetailView(DetailView):
    model = Professor
    template_name = 'teachers/teacher_detail.html'
    context_object_name = 'teacher'

class TeacherCreateView(CreateView):
    model = Professor
    form_class = TeacherForm
    template_name = 'teachers/teacher_form.html'
    success_url = reverse_lazy('teacher_list') 

class TeacherUpdateView(UpdateView):
    model = Professor
    form_class = TeacherForm
    template_name = 'teachers/teacher_form.html'
    context_object_name = 'teacher'
    success_url = reverse_lazy('teacher_list')

class TeacherDeleteView(DeleteView):
    model = Professor
    template_name = 'teachers/teacher_confirm_delete.html'
    context_object_name = 'teacher'
    success_url = reverse_lazy('teacher_list')