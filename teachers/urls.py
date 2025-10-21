from django.urls import path
from .views import (
    ProfessorListView, 
    ProfessorDetailView, 
    ProfessorCreateView, 
    ProfessorUpdateView, 
    ProfessorDeleteView
)

urlpatterns = [
    path('', ProfessorListView.as_view(), name='professor_list'),
    path('adicionar/', ProfessorCreateView.as_view(), name='professor_create'),
    path('<int:pk>/', ProfessorDetailView.as_view(), name='professor_detail'),
    path('<int:pk>/editar/', ProfessorUpdateView.as_view(), name='professor_update'),
    path('<int:pk>/deletar/', ProfessorDeleteView.as_view(), name='professor_delete'),
]