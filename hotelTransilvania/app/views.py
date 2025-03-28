from django.shortcuts import render

def home(request): 
    return render(request, 'home.html')

def suite_luxo(request):
    return render(request, 'suite-luxo.html')

def accomodations(request):
    return render(request, 'accomodations.html')
