'''Ótimo! Vamos começar a deixar seu models.py mais completo e funcional.

1. Adicionando mais campos ao modelo Aluno:

Vamos adicionar os campos que discutimos anteriormente para representar melhor um aluno:'''
from django.db import models
from localflavor.br.models import BRCPFField
from .validators import validate_telefone, validate_data_nascimento

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(validators=[validate_data_nascimento])
    cpf = BRCPFField(unique=True)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20, validators=[validate_telefone])
    email = models.EmailField(unique=True)
    disciplinas = models.ManyToManyField('Disciplina', related_name='alunos')

    def __str__(self):
        return self.nome

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=50)
    serie = models.CharField(max_length=20)
    professor_responsavel = models.ForeignKey('Professores', on_delete=models.SET_NULL, null=True, blank=True)
    horario_aula = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Professores(models.Model):
    nome_completo = models.CharField(max_length=100)
    cpf = BRCPFField(unique=True)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20, validators=[validate_telefone])
    email = models.EmailField(unique=True)
    formacao_academica = models.CharField(max_length=200)
    disciplinas = models.ManyToManyField('Disciplina', related_name='professores')
    data_nascimento = models.DateField(default='2000-01-01', validators=[validate_data_nascimento])

    class Meta:
        verbose_name_plural = 'Professores'

    def __str__(self):
        return self.nome_completo

    class Meta:
        verbose_name_plural = 'Professores'

    def __str__(self):
        return self.nome_completo

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    data_matricula = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.aluno.nome} - {self.turma.nome}'