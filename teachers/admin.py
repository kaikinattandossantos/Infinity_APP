# teachers/admin.py
from django.contrib import admin
from .models import Professor

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'city', 'is_active')
    
    list_editable = ('is_active',)
    
    list_filter = ('is_active', 'city')
    
    search_fields = ('name', 'phone', 'city')

admin.site.register(Professor, TeacherAdmin)