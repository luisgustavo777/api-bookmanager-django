# BookManager - API REST para Gerenciamento de Biblioteca

## Sobre o projeto
API REST simples desenvolvida com Django para gerenciar o acervo de uma biblioteca pessoal/universitária.

## Respostas do trabalho
- **Qual é o tema do seu sistema?**  
  Gerenciamento de Biblioteca Pessoal (BookManager).

- **Quais são as funcionalidades esperadas?**  
  - Listagem de todos os livros cadastrados.  
  - Listagem filtrada de livros por status (Disponível).

- **Quais serão os dados armazenados?**  
  Título, autor, descrição, gênero (categoria) e status do livro.

## Exemplo de README consultado
Inspirado no projeto “django_livraria”:  
https://github.com/fgsantosti/django_livraria

## Tecnologias
- Python
- Django
- Django REST Framework (instalado conforme exigido)
- SQLite (banco padrão)

## Como rodar o projeto localmente
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
