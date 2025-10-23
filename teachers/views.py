from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Professor
from django.contrib.auth.mixins import UserPassesTestMixin


# Lista todos os professores
class TeacherListView(UserPassesTestMixin, ListView):
    model = Professor
    template_name = 'teachers/teacher_list.html'
    context_object_name = 'teachers'
    def test_func(self):
        return self.request.user.is_staff

# Mostra detalhes de um professor específico
class TeacherDetailView(UserPassesTestMixin, DetailView):
    model = Professor
    template_name = 'teachers/teacher_detail.html'
    context_object_name = 'teacher'
    def test_func(self):
        return self.request.user.is_staff

# Cria novo professor
class TeacherCreateView(UserPassesTestMixin, CreateView):
    model = Professor
    template_name = 'teachers/teacher_form.html'
    fields = ['name', 'city'] 
    success_url = reverse_lazy('teacher_list')

    def test_func(self):
        return self.request.user.is_staff

# Atualiza dados de um professor existente
class TeacherUpdateView(UserPassesTestMixin, UpdateView):
    model = Professor
    template_name = 'teachers/teacher_form.html'
    fields = ['name', 'city']
    success_url = reverse_lazy('teacher_list')
    def test_func(self):
        return self.request.user.is_staff

# Deleta um professor
class TeacherDeleteView(DeleteView):
    model = Professor
    template_name = 'teachers/teacher_confirm_delete.html'
    success_url = reverse_lazy('teacher_list')

    def test_func(self):
        return self.request.user.is_staff