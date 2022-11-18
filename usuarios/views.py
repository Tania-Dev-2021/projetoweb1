from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def cad_user(request):
    #cadastro do usuário da aplicação
    if request.method == 'POST':
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('index')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'cadastro.html', {'form_usuario':form_usuario})

def log_user(request):
    #fazer login na aplicação
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario =authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})

def index(request):
    return render(request, 'index.html')
        

