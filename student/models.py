from django.db import models
from django.urls import reverse 

class Student(models.Model):
    name = models.CharField(max_length=100) 
    student_class = models.CharField(max_length=50) 
    course = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('student_list')