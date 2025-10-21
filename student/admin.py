from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    # MUDANÇA: O campo Aluno foi renomeado para nome
    list_display = ('nome', 'turma', 'curso', 'id') 
    
    list_filter = ('turma', 'curso') 
    
    search_fields = ('nome', 'turma', 'curso')
    
    list_per_page = 25

admin.site.register(Student)