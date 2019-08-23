from django.db import models

class Produto(models.Model):
    nome = models.CharField("Nome", max_length=30)
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.nome} - R$ {self.preco}"

class Pedido(models.Model):
    data = models.DateTimeField(auto_now=True)

    @property
    def total(self):
        return sum(
            [item.valor_final for item in self.pedidoproduto_set.all()]
        )

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