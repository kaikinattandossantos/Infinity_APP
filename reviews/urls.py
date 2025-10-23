from django.urls import path
from .views import ReviewPostCreateView, review_success

urlpatterns = [
    path('add/', ReviewPostCreateView.as_view(), name='review_create'),
    path('success/', review_success, name='review_success'),

]