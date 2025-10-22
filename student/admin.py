from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_class', 'id') 
    search_fields = ('name', 'student_class')
    list_per_page = 25

admin.site.register(Student, StudentAdmin)