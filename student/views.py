from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm 
    template_name = 'student/student_form.html'
    
   

class StudentListView(ListView):
    model = Student
    template_name = 'student/student_list.html' 
    context_object_name = 'student' 


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student/student_detail.html'
    context_object_name = 'student'


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_form.html' 


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student/student_confirm_delete.html' 
    success_url = reverse_lazy('student_list') 