from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_class', 'course', 'id') 
    list_filter = ('student_class', 'course') 
    search_fields = ('name', 'student_class', 'course')
    list_per_page = 25

admin.site.register(Student, StudentAdmin)