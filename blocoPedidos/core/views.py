from decimal import Decimal

from django.shortcuts import render
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, FormView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect

from core.models import Pedido, PedidoProduto, Produto
from core.forms import PedidoForm, PedidoFormSet,NovoPedidoForm

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'home'
        context['pedidos_abertos'] = Pedido.objects.filter(finalizado=False)
        context['pedidos_finalizados'] = Pedido.objects.filter(finalizado=True)
        return context


class NovoPedidoFormView(FormView):
    template_name = 'novo-pedido.html'
    form_class = NovoPedidoForm
    pk = None
    ultimo_pedido = Pedido.objects.all().order_by("pk").last()

    def form_valid(self, form):
        if form.is_valid():
            novo_pedido = form.save()
            self.pk = novo_pedido.pk
            return super(NovoPedidoFormView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        if self.ultimo_pedido:
            kwargs['pk'] = self.ultimo_pedido.pk + 1
        else:
            kwargs['pk'] = 1
        kwargs['active_page'] = 'novo-pedido'
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse('novo-pedido', kwargs={'pk': self.pk})


class PedidoDetailView(DetailView):
    model = Pedido

    def get_template_names(self):
        return ["detalhe_pedido.html"]

    def get_context_data(self, **kwargs):
        kwargs['active_page'] = 'pedido'
        return super().get_context_data(**kwargs)


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
                                produtos=produtos,
                                active_page='itens-pedidos'))

    def get_success_url(self):
        import pdb; pdb.set_trace()
        return reverse("novo-pedido",  kwargs={'pk': self.get_object().pk})


class ProdutosListView(ListView):
    model = Produto
    paginate_by = 3
    context_object_name = 'lista_produtos'
    template_name = 'listagem-produtos.html'

    def get_context_data(self, **kwargs):
        kwargs['active_page'] = 'listagem-produtos'
        return super().get_context_data(**kwargs)



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


def finalizar_pedido(request):
    if request.POST:
        import pdb; pdb.set_trace()
        pk = request.POST["pk"]
        Pedido.objects.filter(pk=pk).update(finalizado=True)

        return HttpResponseRedirect(reverse("pedido", kwargs={'pk': pk}))