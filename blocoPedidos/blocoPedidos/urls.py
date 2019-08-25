"""blocoPedidos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import (
    PedidoDetailView, PedidoUpdateView, delete_item_pedido,
    lancar_desconto, HomeView, NovoPedidoFormView, finalizar_pedido
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('novo-pedido/', NovoPedidoFormView.as_view(), name='inicio-novo-pedido'),
    path('novo-pedido/<int:pk>/', PedidoUpdateView.as_view(), name='novo-pedido'),
    path('pedido/remover-item/', delete_item_pedido, name='remover-pedidos'),
    path('pedido/lancar-desconto/', lancar_desconto, name='lancar-desconto'),
    path('pedido/finalizar/', finalizar_pedido, name='finalizar-pedido'),
    path('pedido/<int:pk>/', PedidoDetailView.as_view(), name='pedido'),
]
