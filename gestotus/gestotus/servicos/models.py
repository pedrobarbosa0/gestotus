from django.db import models


class Area(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    area = models.ForeignKey(Area, on_delete=models.PROTECT, related_name="categorias")

    def __str__(self):
        return f"{self.nome} - (Area: {self.area.nome})"


class Servico(models.Model):
    nome = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="servicos")

    def __str__(self):
        return f"{self.nome} - (Categoria: {self.categoria.nome})"
