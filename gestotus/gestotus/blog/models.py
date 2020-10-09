from django.contrib.auth.models import User
from django.db import models


class Artigo(models.Model):
    titulo = models.CharField(max_length=255)
    resumo = models.TextField()
    imagem = models.ImageField()
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.PROTECT, related_name="artigos")

    def __str__(self):
        return self.titulo
