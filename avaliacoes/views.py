from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class AvaliacaoPostCreateView(LoginRequiredMixin, CreateView):
    