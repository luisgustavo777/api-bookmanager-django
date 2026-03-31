from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    descricao = models.TextField()
    genero = models.CharField(
        max_length=50,
        choices=[
            ('Ficção', 'Ficção'),
            ('Não Ficção', 'Não Ficção'),
            ('Tecnologia', 'Tecnologia'),
            ('Ciência', 'Ciência'),
            ('História', 'História'),
        ]
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('Disponível', 'Disponível'),
            ('Emprestado', 'Emprestado'),
            ('Lido', 'Lido'),
        ],
        default='Disponível'
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'