from django.core.exceptions import ValidationError
import re
from datetime import date

def validate_telefone(value):
    """Valida o formato do telefone."""
    padrao = re.compile(r'^\(\d{2}\) \d{4,5}-\d{4}$')
    if not padrao.match(value):
        raise ValidationError('Telefone inválido. Use o formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX.')

def validate_data_nascimento(value):
    """Valida a data de nascimento e a idade."""
    hoje = date.today()
    idade = hoje.year - value.year - ((hoje.month, hoje.day) < (value.month, value.day))
    if idade < 18:  # Idade mínima de 18 anos
        raise ValidationError('A idade mínima é de 18 anos.')
    elif idade > 100:  # Idade máxima de 100 anos
        raise ValidationError('A idade máxima é de 100 anos.')
