from django.db import models

class Fabricante(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome