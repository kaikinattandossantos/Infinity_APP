from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    # Adicionando um campo para a "aula" (classe) que não está no modelo Review,
    # mas pode ser útil para o contexto da avaliação, se necessário.
    # Se a "aula" for a classe do aluno, ela já está no modelo Student (se o aluno for o User).
    # Aqui, vamos focar nos campos do Review e garantir que o monitor seja selecionável.
    
    class Meta:
        model = Review
        fields = ['teacher', 'teaching_score', 'punctuality_score', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # O queryset para 'teacher' (monitor) será definido na View,
        # mas podemos adicionar um placeholder aqui.
        self.fields['teacher'].empty_label = "Selecione o Monitor"