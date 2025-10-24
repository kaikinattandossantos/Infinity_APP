from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Review
from .forms import ReviewForm # Importa o novo formulário
from teachers.models import Professor 

class ReviewPostCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm 
    template_name = 'reviews/review_form.html'
    success_url = reverse_lazy('review_success') 

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Avaliar Monitor'
        return context

    def form_valid(self, form):

        form.instance.student = self.request.user
        return super().form_valid(form)
    
def review_success(request):
    return render(request, 'reviews/review_success.html', {'message': 'Sua avaliação foi enviada com sucesso!'})