from django.shortcuts import render
from .models import Acomodacao

def home(request): 
    return render(request, 'home.html')

def suite_luxo(request):
    acomodacao = Acomodacao.objects.get(id=1)
    return render(request, 'suite-luxo.html', {'acomodacao': acomodacao})

def accomodations(request):
    return render(request, 'accomodations.html')

def reserva(request): 
    return render(request, 'reserva.html')
