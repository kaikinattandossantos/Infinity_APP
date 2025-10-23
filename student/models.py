from django.db import models
from django.urls import reverse 

class Student(models.Model):
    name = models.CharField(max_length=100) 
    student_class = models.CharField(max_length=50) 
    
    phone = models.CharField(
        max_length=20, 
        blank=True, 
        null=True, 
        verbose_name="Telefone"
    )
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('student_list')