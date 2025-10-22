# teachers/models.py
from django.db import models

class Professor(models.Model):
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
        return self.name

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"