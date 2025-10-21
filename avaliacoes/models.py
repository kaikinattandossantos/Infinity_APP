# avaliacoes/models.py
from django.db import models
from django.contrib.auth.models import User
from teachers.models import Professor 

class Avaliacao(models.Model):
    # Quem foi avaliado:
    professor = models.ForeignKey(
        Professor, 
        on_delete=models.CASCADE, # Se o prof for deletado, suas avaliações somem
        related_name="avaliacoes",
        verbose_name="Professor"
    )
    
    # Quem avaliou (o Aluno):
    # Por enquanto, vamos linkar ao Usuário padrão do Django.
    # Depois, no app 'usuarios', podemos garantir que ele é um aluno.
    aluno = models.ForeignKey(
        User,
        on_delete=models.SET_NULL, # Se o aluno for deletado, a avaliação fica (anônima)
        null=True, 
        blank=True,
        verbose_name="Aluno"
    )
    
    # Os campos da avaliação:
    nota_didatica = models.PositiveSmallIntegerField(verbose_name="Nota de Didática (1-5)", default=0)
    nota_pontualidade = models.PositiveSmallIntegerField(verbose_name="Nota de Pontualidade (1-5)", default=0)
    
    comentario = models.TextField(
        verbose_name="Comentário",
        blank=True, 
        null=True
    )
    
    data_criacao = models.DateTimeField(
        auto_now_add=True, # Define a data/hora automaticamente quando é criado
        verbose_name="Data da Avaliação"
    )

    def __str__(self):
        return f"Avaliação de {self.aluno.username} para {self.professor}"
        
    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        ordering = ['-data_criacao'] # Mostra as mais recentes primeiro