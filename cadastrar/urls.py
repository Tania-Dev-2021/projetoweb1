from django.urls import path
from .views import *

urlpatterns = [
    path('clientes/listar', listar_clientes, name='listar_clientes'),
    path('clientes/listar/<int:id>', listar_clientes_id, name='listar_clientes_id'),
    path('clientes/inserir', inserir_clientes, name='inserir_clientes'),
    path('clientes/editar/<int:id>', editar_cliente, name='editar_cliente'),
    path('clientes/remover/<int:id>', remover_cliente, name='remover_cliente'),
    path('produtos/listar', listar_produtos, name='listar_produtos'),
    path('produtos/listar/<int:id>', listar_produto_id, name='listar_produtos_id'),
    path('produtos/inserir', inserir_produtos, name='inserir_produtos'),
    path('produtos/editar/<int:id>', editar_produto, name='editar_produto'),
    path('produtos/remover/<int:id>', remover_produto, name='remover_produto'),
    path('pedidos/listar', listar_pedidos, name='listar_pedidos'),
    path('pedidos/listar/<int:id>', listar_pedido_id, name='listar_pedido_id'),
    path('pedidos/inserir', inserir_pedidos, name='inserir_pedidos'),
    path('pedidos/editar/<int:id>', editar_pedido, name='editar_pedido'),
    path('pedidos/remover/<int:id>', remover_pedido, name='remover_pedido'),
]    