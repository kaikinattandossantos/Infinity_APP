# avaliacoes/admin.py
from django.contrib import admin
from .models import Avaliacao

class AvaliacaoAdmin(admin.ModelAdmin):
    # Colunas que a Gerência verá na lista
    list_display = (
        'professor', 
        'get_aluno_nome', 
        'nota_didatica', 
        'nota_pontualidade', 
        'data_criacao'
    )
    
    # Filtros laterais
    list_filter = ('professor', 'data_criacao')
    
    # Barra de busca
    search_fields = (
        'professor__user__first_name', 
        'professor__user__last_name', 
        'aluno__username',
        'comentario'
    )
    
    # Campos que a Gerência NÃO PODE editar (para manter a integridade)
    # Ela não deve poder trocar o aluno ou o professor de uma avaliação.
    readonly_fields = ('professor', 'aluno', 'data_criacao')
    
    # Função para pegar o nome do aluno (igual fizemos com email)
    @admin.action(description='Aluno')
    def get_aluno_nome(self, obj):
        if obj.aluno:
            return obj.aluno.username
        return "Anônimo" # Caso o aluno tenha sido deletado

# Registra o modelo Avaliacao e usa a personalização acima
admin.site.register(Avaliacao, AvaliacaoAdmin)