from django.db import models
from decimal import *

class Produto(models.Model):
    nome = models.CharField("Nome", max_length=30)
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.nome}"

class Cliente(models.Model):
    nome = models.CharField("Nome", max_length=50)
    rg = models.CharField("R.G", max_length=12)

    def __str__(self):
        return f"Nome: {self.nome} - R.G.: {self.rg}"

class Pedido(models.Model):
    data = models.DateTimeField(auto_now=True)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    finalizado = models.BooleanField(default=False)

    @property
    def total(self):
        getcontext().prec = 4
        total = sum(
            [item.valor_final for item in self.pedidoproduto_set.all()]
        )
        descontado = Decimal(0.0)
        if self.desconto > 0:
            descontado = Decimal((self.desconto / 100) * total)

        return Decimal(total - descontado)

    @property
    def numero(self):
        return f"#{self.pk}"


class PedidoProduto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()

    @property
    def valor_final(self):
        return self.quantidade * self.produto.preco