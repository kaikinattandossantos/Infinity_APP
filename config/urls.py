from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core.views import home


urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    # Login / Logout
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    # Apps
    path('teachers/', include('teachers.urls')),
    path('students/', include('student.urls')),
    path('reviews/', include('reviews.urls')),
]
