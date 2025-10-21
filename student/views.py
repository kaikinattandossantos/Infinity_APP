from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Aluno
from .forms import AlunoForm

class AlunoCreateView(CreateView):
    model = Aluno
    form_class = AlunoForm 
    template_name = 'escola/aluno_form.html'
    
   

class AlunoListView(ListView):
    model = Aluno
    template_name = 'escola/aluno_list.html' 
    context_object_name = 'alunos' 


class AlunoDetailView(DetailView):
    model = Aluno
    template_name = 'escola/aluno_detail.html'
    context_object_name = 'aluno'


class AlunoUpdateView(UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'escola/aluno_form.html' 


class AlunoDeleteView(DeleteView):
    model = Aluno
    template_name = 'escola/aluno_confirm_delete.html' 
    success_url = reverse_lazy('aluno_list') 