from django.shortcuts import render, HttpResponse # Aula 01

# Create your views here.

def hello(request, nome, idade): # Aula 01
    return HttpResponse(f'<h1>Hello {nome}! You are {idade} years old.</h1>')