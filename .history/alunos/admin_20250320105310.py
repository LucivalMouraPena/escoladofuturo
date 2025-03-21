from django.contrib import admin
from .models import Aluno, Turma, Professor
from .forms import AlunoForm, TurmaForm, ProfessorForm

class AlunoAdmin(admin.ModelAdmin):
    form = AlunoForm

class TurmaAdmin(admin.ModelAdmin):
    form = TurmaForm

class ProfessorAdmin(admin.ModelAdmin):
    form = ProfessorForm

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Professor, ProfessorAdmin)