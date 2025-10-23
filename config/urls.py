from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teachers/', include('teachers.urls')),
    path('students/', include('student.urls')),
    
    path('reviews/', include('reviews.urls')), 
]