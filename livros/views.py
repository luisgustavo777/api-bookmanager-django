from django.http import JsonResponse
from .models import Livro

def listar_livros(request):
    """Rota GET Geral - todos os livros"""
    livros = Livro.objects.all()
    data = list(livros.values())
    return JsonResponse(data, safe=False)

def listar_livros_disponiveis(request):
    """Rota GET Filtrada - apenas livros disponíveis"""
    livros = Livro.objects.filter(status='Disponível')
    data = list(livros.values())
    return JsonResponse(data, safe=False)