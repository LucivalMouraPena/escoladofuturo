from django import forms
from .models import Aluno, Turma, Professor

class AlunoForm(forms.ModelForm):
    class Meta : 
        model = Aluno
        fields = '__all__'

class TurmaForm(forms.ModelForm):
    class Meta :
        model = Turma
        fields = '__all__'

class ProfessorForm(forms.ModelForm):
    class Meta :
        model = Professor
        fields = '__all__'