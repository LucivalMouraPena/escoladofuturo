from django.urls import path
from . import views
from alunos import views
urlpatterns = [
    path('', views.index, name='index'),
]