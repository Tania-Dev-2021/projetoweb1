from django.shortcuts import render, redirect
from .models import Dclientes, Dpedidos, Dprodutos
from .forms import ClienteForm, PedidoForm, ProdutoForm

# Funções da tabela Dclientes:
def listar_clientes(request):
    clientes = Dclientes.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})

def listar_clientes_id(request, id):
    cliente = Dclientes.objects.get(id=id)
    return render(request, 'lista_cliente.html',{'cliente' : cliente})

def inserir_clientes(request):
    if request.method=='POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'inserir_clientes.html', {'form':form})

def editar_cliente(request, id):
    cliente=Dclientes.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance =cliente )
    if form.is_valid():
        form.save()
        return redirect('listar_clientes')
    return render(request,'inserir_clientes.html', {'form':form})

def remover_cliente(request, id):
    cliente=Dclientes.objects.get(id=id)
    if request.method =='POST':
        cliente.delete()
        return redirect ('listar_clientes')
    return render(request, 'remover_clientes.html', {'cliente':cliente})

#Funçoes da tabela Dprodutos:
def listar_produtos(request):
    produtos = Dprodutos.objects.all()
    return render(request, 'listar_produtos.html', {'produtos': produtos})

def listar_produto_id(request, id):
    produto = Dprodutos.objects.get(id=id)
    return render(request, 'lista_produto.html',{'produto' : produto})

def inserir_produtos(request):
    if request.method=='POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'inserir_produtos.html', {'form':form})

def editar_produto(request, id):
    produto=Dprodutos.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance =produto )
    if form.is_valid():
        form.save()
        return redirect('listar_produtos')
    return render(request,'inserir_produtos.html', {'form':form})

def remover_produto(request, id):
    produto=Dprodutos.objects.get(id=id)
    if request.method =='POST':
        produto.delete()
        return redirect ('listar_produtos')
    return render(request, 'remover_produtos.html', {'produto':produto})

#Funçoes da tabela Dpedidos
def listar_pedidos(request):
    pedidos = Dpedidos.objects.all()
    return render(request, 'listar_pedidos.html', {'pedidos': pedidos})

def listar_pedido_id(request, id):
    pedido = Dpedidos.objects.get(id=id)
    return render(request, 'lista_pedido.html',{'pedido' : pedido})

def inserir_pedidos(request):
    if request.method=='POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'inserir_pedidos.html', {'form':form})

def editar_pedido(request, id):
    pedido=Dpedidos.objects.get(id=id)
    form = PedidoForm(request.POST or None, instance =pedido )
    if form.is_valid():
        form.save()
        return redirect('listar_pedidos')
    return render(request,'listar_pedidos.html', {'form':form})

def remover_pedido(request, id):
    pedido=Dpedidos.objects.get(id=id)
    if request.method =='POST':
        pedido.delete()
        return redirect ('listar_pedidos')
    return render(request, 'remover_pedidos.html', {'pedido':pedido})



    



