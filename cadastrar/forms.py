from django import forms
from .models import Dclientes, Dprodutos, Dpedidos

class ClienteForm(forms.ModelForm):
        class Meta:
                model = Dclientes
                fields = ['nomec', 'cpf', 'endereco', 'tipo']
                

class ProdutoForm(forms.ModelForm):
        class Meta:
                model = Dprodutos
                fields = ['nomep', 'valor_produto']  

class PedidoForm(forms.ModelForm):
        class Meta:
                model = Dpedidos
                fields=['numero_pedido', 'valor_pedido', 'cliente', 'produto', 'status', 'quantidade_pedido']
