# teachers/models.py
from django.db import models
from django.contrib.auth.models import User

class Professor(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        verbose_name="User"
    )

    name = models.CharField( 
        max_length=100, 
        verbose_name="Name", 
        blank=True, 
        null=True 
    )
    
    phone = models.CharField( 
        max_length=20, 
        verbose_name="Phone", 
        blank=True, 
        null=True 
    )
    
    # NOVO CAMPO ADICIONADO AQUI
    city = models.CharField( 
        max_length=100, 
        verbose_name="City", 
        blank=True, 
        null=True 
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name="Is active?"
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"