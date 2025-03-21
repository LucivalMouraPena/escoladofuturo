from django import forms
from .models import Aluno, Turma, Professor

class AlunoForm(forms.ModelForm)
    class Meta : 
        model = Aluno