from django.contrib import admin
from .models import Aluno, Turma, Professores
from .forms import AlunoForm, TurmaForm, ProfessoresForm

class AlunoAdmin(admin.ModelAdmin):
    form = AlunoForm
    list_filter = ('data_nascimento', 'disciplinas_lecionadas')
    search_fields = ('nome', 'cpf', 'email')
    list_display = ('nome', 'cpf', 'email', 'data_nascimento')

class TurmaAdmin(admin.ModelAdmin):
    form = TurmaForm
    list_filter = ('serie', 'professor_responsavel')
    search_fields = ('nome', 'serie', 'professor_responsavel__nome_completo')
    list_display = ('nome', 'serie', 'professor_responsavel')
    related_lookup_fields = {
        'professor_responsavel': ('nome_completo',),
    }

class ProfessorAdmin(admin.ModelAdmin):
    form = ProfessoresForm
    list_filter = ('formacao_academica', 'disciplinas_lecionadas')
    search_fields = ('nome_completo', 'cpf', 'email')
    list_display = ('nome_completo', 'cpf', 'email', 'formacao_academica')

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Professores, ProfessorAdmin)