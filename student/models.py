from django.db import models
from django.urls import reverse 

class Aluno(models.Model):
    
    nome_aluno = models.CharField(max_length=100) 
    
    
    turma = models.CharField(max_length=50) 
    
    
    curso = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.nome_aluno
        
    
    def get_absolute_url(self):
       
        return reverse('aluno_list') 

