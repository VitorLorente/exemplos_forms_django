from django.shortcuts import render
from django.urls import reverse

# Create your views here.

from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from core.models import Pedido, PedidoProduto
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
        return self.render_to_response(
            self.get_context_data(form=form,
                                items_form=items_form))

    def get_success_url(self):
        return reverse("pedido",  kwargs={'pk': 1})