from django.contrib import admin
from .models import Aluno, Turma, Professor
from .forms import AlunoForm, TurmaForm, ProfessorForm

admin.site.register(Aluno)
admin.site.register(Turma)
admin.site.register(Professor)

# Crie classes que herdam de admin.ModelAdmin para personalizar o painel de administração de cada modelo. Register your models here.
class AlunoAdmin(admin.ModelAdmin):
      form = AlunoForm

class TurmaAdmin(admin.ModelAdmin):
      form = TurmaForm 

class ProfessorAdmin(admin.ModelAdmin):
      form = ProfessorForm