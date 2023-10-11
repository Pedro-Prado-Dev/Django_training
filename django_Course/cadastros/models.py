from django.db import models


# Create your models here.

class Pais(models.Model):
    nome = models.CharField(max_length=88)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'


class Estado(models.Model):
    nome = models.CharField(max_length=88)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    name = models.CharField(max_length=100, unique=True)
    capital = models.BooleanField(default=False)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, null=True, blank=False)

    def __str__(self):
        return self.name
