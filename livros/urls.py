from django.urls import path
from .views import listar_livros, listar_livros_disponiveis

urlpatterns = [
    path('api/livros/', listar_livros, name='listar_livros'),
    path('api/livros/disponiveis/', listar_livros_disponiveis, name='listar_disponiveis'),
]