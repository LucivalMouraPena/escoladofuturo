from django.urls import path
from . import views
from alunos.views import index # Importa apenas a função index
urlpatterns = [
    path('', views.index, name='index'),
]