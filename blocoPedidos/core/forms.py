from django import forms
from .models import Pedido, PedidoProduto, Produto, Cliente
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

class NovoPedidoForm(forms.Form):
    cliente_nome = forms.CharField(max_length=50, required=True)
    cliente_rg = forms.CharField(max_length=12, required=True)

    def save(self, commit=True):
        cliente, created = Cliente.objects.get_or_create(
            nome=self.cleaned_data["cliente_nome"],
            rg=self.cleaned_data["cliente_rg"]
        )

        pedido = Pedido(
            cliente=cliente
        )

        if commit:
            pedido.save()
        return pedido

# class PedidoFormSet(BasePedidoFormSet):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.form._meta.fields['produto'].choices = Produto.objects.all()