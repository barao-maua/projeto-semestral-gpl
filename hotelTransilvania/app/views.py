from django.shortcuts import render, redirect,  get_object_or_404
from .models import Acomodacao, Usuario, Reserva, AvaliacaoUsuario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm, LoginForm, AvaliacaoUsuarioForm, ReservaForm

def home(request): 
    return render(request, 'home.html')


@login_required
def minhas_reservas(request):
    usuario = request.user.usuario  
    reservas = Reserva.objects.filter(usuario=usuario).order_by('-data_inicio')

    reservas_detalhadas = []
    for reserva in reservas:
        total_preco = (reserva.data_fim - reserva.data_inicio).days * reserva.acomodacao.preco
  
        data_reserva_formatada = reserva.data_inicio.strftime('%d/%m/%Y')
        data_inicio_formatada = reserva.data_inicio.strftime('%d/%m/%Y')
        data_fim_formatada = reserva.data_fim.strftime('%d/%m/%Y')

        avaliacoes = AvaliacaoUsuario.objects.filter(usuario=usuario, acomodacao=reserva.acomodacao).order_by('-data_avaliacao')

        reservas_detalhadas.append({
            'acomodacao_nome': reserva.acomodacao.nome,
            'total_preco': f"R$ {total_preco:.2f}".replace('.', ','),
            'data_reserva': data_reserva_formatada,
            'periodo': f"{data_inicio_formatada} a {data_fim_formatada} ({(reserva.data_fim - reserva.data_inicio).days} noites)",
            'avaliacoes': avaliacoes 
        })
    return render(request, 'minhas-reservas.html', {'reservas': reservas_detalhadas})

def suite_luxo(request):
    return render(request, 'suite-luxo.html')

def accomodations(request):
    return render(request, 'accomodations.html')


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
            acomodacao = get_object_or_404(Acomodacao, id=3)
            avaliacao.acomodacao = acomodacao
            avaliacao.save()

            return redirect('suite_luxo')
    else:
        form = AvaliacaoUsuarioForm()
    return render(request, 'avaliar.html', {'form': form})

@login_required
def criar_reserva(request):
    usuario = get_object_or_404(Usuario, user=request.user)
    acomodacao = get_object_or_404(Acomodacao, id=3)  # ID fixo da acomodação

    data_ida = request.GET.get('data_ida', '')
    data_volta = request.GET.get('data_volta', '')

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = usuario
            reserva.acomodacao = acomodacao
            reserva.statusReserva = 'concluída'
            reserva.save()
            return redirect('minhas_reservas')  # Substitua pelo nome da sua URL de sucesso
    else:
        initial_data = {
            'data_inicio': data_ida,
            'data_fim': data_volta
        }
        form = ReservaForm(initial=initial_data)

    context = {
        'form': form,
        'acomodacao': acomodacao,
        'usuario': usuario
    }
    return render(request, 'reserva.html', context)

@login_required
def reserva_view(request):
    usuario = get_object_or_404(Usuario, user=request.user)
    return render(request, 'reserva.html', {'usuario': usuario})