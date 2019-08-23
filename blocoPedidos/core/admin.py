from django.contrib import admin

from .models import Produto, Pedido, PedidoProduto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    pass

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    pass

@admin.register(PedidoProduto)
class PedidoProdutoAdmin(admin.ModelAdmin):
    pass