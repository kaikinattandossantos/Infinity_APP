from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Review

class ReviewPostCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['teacher', 'teaching_score', 'punctuality_score', 'comment']
    template_name = 'reviews/review_form.html'
    success_url = reverse_lazy('teacher_list') 
    
    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)