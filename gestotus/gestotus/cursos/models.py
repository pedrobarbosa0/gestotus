from django.db import models


class Curso(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    imagem = models.ImageField()
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo
