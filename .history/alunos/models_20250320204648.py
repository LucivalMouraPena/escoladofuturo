'''Ótimo! Vamos começar a deixar seu models.py mais completo e funcional.

1. Adicionando mais campos ao modelo Aluno:

Vamos adicionar os campos que discutimos anteriormente para representar melhor um aluno:'''
from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True) # CPF com máscara e único 
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    disciplinas_lecionadas = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=50)
    serie = models.CharField(max_length=20)
    professor_responsavel = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True, blank=True)
    horario_aula = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Professores(models.Model):
    nome_completo = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    formacao_academica = models.CharField(max_length=200)
    disciplinas_lecionadas = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = 'Professores' name

    def __str__(self):
        return self.nome_completo