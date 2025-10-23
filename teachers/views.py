from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Professor

# Lista todos os professores
class TeacherListView(ListView):
    model = Professor
    template_name = 'teachers/teacher_list.html'
    context_object_name = 'teachers'

# Mostra detalhes de um professor específico
class TeacherDetailView(DetailView):
    model = Professor
    template_name = 'teachers/teacher_detail.html'
    context_object_name = 'teacher'

# Cria novo professor
class TeacherCreateView(CreateView):
    model = Professor
    template_name = 'teachers/teacher_form.html'
    fields = ['name', 'city'] 
    success_url = reverse_lazy('teacher_list')

# Atualiza dados de um professor existente
class TeacherUpdateView(UpdateView):
    model = Professor
    template_name = 'teachers/teacher_form.html'
    fields = ['name', 'city']
    success_url = reverse_lazy('teacher_list')

# Deleta um professor
class TeacherDeleteView(DeleteView):
    model = Professor
    template_name = 'teachers/teacher_confirm_delete.html'
    success_url = reverse_lazy('teacher_list')
