'''Ótimo! Vamos começar a deixar seu models.py mais completo e funcional.

1. Adicionando mais campos ao modelo Aluno:

Vamos adicionar os campos que discutimos anteriormente para representar melhor um aluno:'''
from django.db import models
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True) # CPF com máscara e único 
    endereco = models.CharFieldField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    disciplinas_lecionadas = models.CharField(max_length=100)

    
    def __str__(self):
        return self.nome
    
    