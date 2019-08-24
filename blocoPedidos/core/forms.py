from django import forms
from .models import Pedido, PedidoProduto, Produto
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

# class PedidoFormSet(BasePedidoFormSet):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.form._meta.fields['produto'].choices = Produto.objects.all()