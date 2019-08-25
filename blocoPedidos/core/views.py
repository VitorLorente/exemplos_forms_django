from decimal import Decimal

from django.shortcuts import render
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect

from core.models import Pedido, PedidoProduto, Produto
from core.forms import PedidoForm, PedidoFormSet

class PedidoDetailView(DetailView):

    model = Pedido

    def get_template_names(self):
        return ["detalhe_pedido.html"]


class PedidoUpdateView(UpdateView):
    model = Pedido
    form_class = PedidoFormSet
    template_name = "form_pedido.html"

    def get(self, request, *args, **kwargs):

        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        items = PedidoProduto.objects.filter(pedido=self.object).order_by('pk').values()

        items_form = PedidoFormSet(initial=items)

        produtos = Produto.objects.all()
        return self.render_to_response(
            self.get_context_data(form=form,
                                items_form=items_form,
                                produtos=produtos))

    def get_success_url(self):
        return reverse("novo-pedido",  kwargs={'pk': 1})


def delete_item_pedido(request):
    if request.POST:
        pk = request.POST["pk"]
        PedidoProduto.objects.filter(pk=pk).delete()
        return HttpResponseRedirect(reverse("novo-pedido", kwargs={'pk': 1}))


def lancar_desconto(request):
    if request.POST:
        pk = request.POST["pk"]
        desconto = Decimal(request.POST["desconto"].replace(",", ".").replace("%", ""))
        Pedido.objects.filter(pk=pk).update(desconto=desconto)

        return HttpResponseRedirect(reverse("novo-pedido", kwargs={'pk': pk}))