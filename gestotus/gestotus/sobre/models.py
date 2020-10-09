from django.db import models


class QuemSomos(models.Model):
    imagem = models.ImageField()
    descricao = models.TextField()

    def __str__(self):
        return "Quem somos"


class Membro(models.Model):
    nome = models.CharField(max_length=255)
    imagem = models.ImageField()
    cargo = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
