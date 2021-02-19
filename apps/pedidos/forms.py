from django import forms

from .models import Pedido, Item


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'data',
            'cliente',
            'total',
        ]

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'produto',
            'quantidade',
            'valor_base',
        ]
