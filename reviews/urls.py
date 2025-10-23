from django.urls import path
from .views import ReviewPostCreateView, review_success

urlpatterns = [
    # URL para o aluno cadastrar a avaliação
    path('new/', ReviewPostCreateView.as_view(), name='review_create'),
    # URL de sucesso após o envio do formulário
    path('success/', review_success, name='review_success'),
]