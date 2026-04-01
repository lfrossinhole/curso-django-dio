from django.shortcuts import render, HttpResponse # Aula 01

# Create your views here.

def hello(request, nome, idade): # Aula 01
    return HttpResponse(f'<h1>Olá {nome}! Você tem {idade} anos de idade.</h1>')

def soma(request, num1, num2): # Aula 01-EX
    resultado = num1 + num2
    return HttpResponse(f'<h1>A soma de {num1} e {num2} é {resultado}.</h1>')

def subtracao(request, num1, num2): # Aula 01-EX
    resultado = num1 - num2
    return HttpResponse(f'<h1>A subtração de {num1} e {num2} é {resultado}.</h1>')

def multiplicacao(request, num1, num2): # Aula 01-EX
    resultado = num1 * num2
    return HttpResponse(f'<h1>A multiplicação de {num1} e {num2} é {resultado}.</h1>')

def divisao(request, num1, num2): # Aula 01-EX
    if num2 != 0:
        resultado = num1 / num2
        return HttpResponse(f'<h1>A divisão de {num1} por {num2} é {resultado}.</h1>')
    else:
        return HttpResponse('<h1>Erro: Divisão por zero não é permitida.</h1>')