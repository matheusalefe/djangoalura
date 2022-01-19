from django.shortcuts import render

# Create your views here.

def index(request):
    

    return render(request,'index.html')

def receitas(request):
    receitas = {
        1: 'Bolinho de chuva',
        2: 'Omelete',
        3: 'Carne moída',
        4: 'Frango a passarinho'
    }
    dados = {
        'nome_das_receitas': receitas
    }

    return render(request, 'receitas.html',dados)