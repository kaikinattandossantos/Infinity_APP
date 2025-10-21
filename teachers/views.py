# docentes/views.py
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from .models import Professor
from .forms import ProfessorForm 



class ProfessorListView(ListView):
    """Lista todos os professores ativos."""
    model = Professor
    template_name = 'docentes/professor_list.html'
    context_object_name = 'professores'
   
    def get_queryset(self):
        return Professor.objects.filter(esta_ativo=True).select_related('user')
       

class ProfessorDetailView(DetailView):
    """Exibe os detalhes de um professor específico."""
    model = Professor
    template_name = 'docentes/professor_detail.html'
    context_object_name = 'professor'



class ProfessorCreateView(CreateView):
   
    model = Professor
    form_class = ProfessorForm
    template_name = 'docentes/professor_form.html'
    
    success_url = reverse_lazy('professor_list') 

class ProfessorUpdateView(UpdateView):
    
    model = Professor
    form_class = ProfessorForm
    template_name = 'docentes/professor_form.html'
    context_object_name = 'professor'
    success_url = reverse_lazy('professor_list')

class ProfessorDeleteView(DeleteView):
   
    model = Professor
    template_name = 'docentes/professor_confirm_delete.html'
    context_object_name = 'professor'
    
    success_url = reverse_lazy('professor_list')