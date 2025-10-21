from django.urls import path
from .views import (
    StudentListView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView
)

urlpatterns = [
    
    path('', StudentListView.as_view(), name='aluno_list'), 
    
    
    path('adicionar/', StudentCreateView.as_view(), name='aluno_create'), 
    
    
    path('<int:pk>/', StudentDetailView.as_view(), name='aluno_detail'), 
    
    
    path('<int:pk>/editar/', StudentUpdateView.as_view(), name='aluno_update'), 
    
    
    path('<int:pk>/deletar/', StudentDeleteView.as_view(), name='aluno_delete'),
]