# docentes/models.py
from django.db import models
from django.contrib.auth.models import User

class Professor(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        verbose_name="Usuário"
    )
    
    # NOVO CAMPO ADICIONADO AQUI
    telefone = models.CharField(
        max_length=20, 
        verbose_name="Telefone", 
        blank=True,  # O campo é opcional no admin
        null=True    # O campo pode ser nulo no banco
    )
    
    esta_ativo = models.BooleanField(
        default=True,
        verbose_name="Está ativo?"
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professores"