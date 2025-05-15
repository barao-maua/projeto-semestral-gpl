from django.shortcuts import render, redirect,  get_object_or_404
from .models import Acomodacao, Usuario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm, LoginForm, AvaliacaoUsuarioForm

def home(request): 
    return render(request, 'home.html')

def suite_luxo(request):
    acomodacao = Acomodacao.objects.get(id=1)
    return render(request, 'suite-luxo.html', {'acomodacao': acomodacao})

def accomodations(request):
    return render(request, 'accomodations.html')


def reserva(request): 
    return render(request, 'reserva.html')

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)

            usuario = form.save(commit=False)
            usuario.user = user
            usuario.save()

            return redirect('login')  # Redireciona após cadastro bem-sucedido
    else:
        form = UsuarioForm()
    return render(request, 'cadastro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if usuario is not None:
                login(request, usuario)
                return redirect('home')  # Redireciona para a página inicial
            else:
                form.add_error(None, 'Usuário ou senha inválidos.')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def logout_usuario(request):
    logout(request)
    return redirect('home')


@login_required
def criar_avaliacao(request):
    if request.method == 'POST':
        form = AvaliacaoUsuarioForm(request.POST)
        if form.is_valid():
            
            avaliacao = form.save(commit=False)
            
            user = request.user
            usuario = get_object_or_404(Usuario, user = user)
            avaliacao.usuario = usuario
            acomodacao = get_object_or_404(Acomodacao, id=1)
            avaliacao.acomodacao = acomodacao
            avaliacao.save()

            return redirect('suite_luxo')
    else:
        form = AvaliacaoUsuarioForm()
    return render(request, 'avaliar.html', {'form': form})