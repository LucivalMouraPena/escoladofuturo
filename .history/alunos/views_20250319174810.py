from django.shortcuts import render
from django.utils.translation import gettext as _
# Create your views here.
def index(request):
    mensagem = _("Bem-vindo ao aplicativo Alunos!")
    return render(request, 'alunos/index.html', {'mensagem': mensagem})