# docentes/admin.py
from django.contrib import admin
from .models import Professor

class ProfessorAdmin(admin.ModelAdmin):
    # ADICIONE 'telefone' AQUI
    list_display = ('__str__', 'get_email', 'telefone', 'esta_ativo')
    
    list_editable = ('esta_ativo',)
    list_filter = ('esta_ativo',)
    
    # E ADICIONE 'telefone' AQUI TAMBÉM
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'user__email', 'telefone')
    
    # ... (o resto do arquivo)
    readonly_fields = ('user',)

    @admin.action(description='Email')
    def get_email(self, obj):
        return obj.user.email

admin.site.register(Professor, ProfessorAdmin)