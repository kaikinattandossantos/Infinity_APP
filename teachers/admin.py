# teachers/admin.py
from django.contrib import admin
from .models import Professor

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_email', 'phone', 'city', 'is_active')
    
    list_editable = ('is_active',)
    
    list_filter = ('is_active', 'city')
    
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'user__email', 'phone', 'city')
    
    @admin.action(description='Email')
    def get_email(self, obj):
        return obj.user.email

admin.site.register(Professor, TeacherAdmin)