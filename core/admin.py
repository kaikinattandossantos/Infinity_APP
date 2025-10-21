# docentes/admin.py
from django.contrib import admin
from .models import Professor

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_email', 'telefone', 'esta_ativo')
    
    list_editable = ('esta_ativo',)
    list_filter = ('esta_ativo',)
    
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'user__email', 'telefone')
    
    readonly_fields = ('user',)

    @admin.action(description='Email')
    def get_email(self, obj):
        return obj.user.email

admin.site.register(Professor, ProfessorAdmin)