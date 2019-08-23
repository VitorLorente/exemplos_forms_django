from django import forms
from .models import Pedido, PedidoProduto
from django.forms.models import inlineformset_factory

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        exclude = ()

PedidoFormSet = inlineformset_factory(
    Pedido, PedidoProduto, form=PedidoForm, 
    fields=["quantidade", "produto"], extra=1,
    can_delete=True
)