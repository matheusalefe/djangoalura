from django.shortcuts import render
from .models import Receitas
# Create your views here.

def index(request):
    

    return render(request,'index.html')

def receitas(request):
    receitas = Receitas.objects.all()

    dados = {
        'receitas': receitas
    }

    return render(request, 'receitas.html',dados)

def receita_cont(request):

    return render(request, receita_cont)