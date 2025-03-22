from django.contrib import admin

from .models import Aluno, Turma, Professores, Disciplina, Matricula

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'cpf', 'email')
    list_filter = ['nome', 'disciplinas'] # Modificação aqui
    search_fields = ('nome', 'cpf', 'email')

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'serie', 'professor_responsavel', 'horario_aula')
    list_filter = ['nome', 'serie', 'professor_responsavel']
    search_fields = ('nome', 'serie')
    related_lookup_fields = {
        'fk': ['professor_responsavel'],
    }

@admin.register(Professores)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'email', 'formacao_academica')
    list_filter = ['nome_completo', 'disciplinas'] # Modificação aqui
    search_fields = ('nome_completo', 'cpf', 'email')

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'turma', 'data_matricula')
    list_filter = ['turma']
    search_fields = ['aluno__nome', 'turma__nome']
    related_lookup_fields = {
        'fk': ['aluno', 'turma'],
    }