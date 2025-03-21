'''Ótimo! Vamos começar a deixar seu models.py mais completo e funcional.

1. Adicionando mais campos ao modelo Aluno:

Vamos adicionar os campos que discutimos anteriormente para representar melhor um aluno:'''
from django.db import models
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.nome
    
    