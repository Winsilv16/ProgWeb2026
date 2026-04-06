from django.db import models

class Fabricante(models.Model):
    nome = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    destaque = models.BooleanField(default=True)
    promocao = models.BooleanField(default=False)
    msg_promocao = models.CharField(max_length=100, null=True, blank=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.SET_NULL, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nome