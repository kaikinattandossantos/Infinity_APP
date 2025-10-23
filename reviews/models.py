# reviews/models.py
from django.db import models
from django.contrib.auth.models import User
from teachers.models import Professor 

class Review(models.Model):
    teacher = models.ForeignKey(
        Professor, 
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Teacher"
    )
    
    student = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, 
        blank=True,
        verbose_name="Student"
    )

    class_name = models.CharField(  # <-- NOVO CAMPO
        max_length=100,
        verbose_name="Class (Aula)"
    )
    
    teaching_score = models.PositiveSmallIntegerField(verbose_name="Teaching Score (1-5)", default=0)
    punctuality_score = models.PositiveSmallIntegerField(verbose_name="Punctuality Score (1-5)", default=0)
    
    comment = models.TextField(
        verbose_name="Comment",
        blank=True, 
        null=True
    )
    
    creation_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Review Date"
    )

    def __str__(self):
        student_name = self.student.username if self.student else "Anonymous"
        return f"Review from {student_name} for {self.teacher}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ['-creation_date']
