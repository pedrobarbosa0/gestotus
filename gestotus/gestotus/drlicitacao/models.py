from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Link(models.Model):
    titulo = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="links")

    def __str__(self):
        return f"{self.categoria}: {self.url}"
