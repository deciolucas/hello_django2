# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse


def index(request):    
    return render(request, 'index.html')


def contato(request):    
    return render(request, 'contato.html')


def produto(request):
    return render(request, 'produto.html')


def lista_produtos(request):
    return render(request, 'lista_produtos.html')
