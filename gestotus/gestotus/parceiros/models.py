from django.db import models


class Parceiro(models.Model):
    nome = models.CharField(max_length=255)
    imagem = models.ImageField()
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
