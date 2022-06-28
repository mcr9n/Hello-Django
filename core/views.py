from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>hello {} de {} anos</h1>'.format(nome, idade))
def soma(request, numero1, numero2):
    return HttpResponse(f'<h1>A soma vale {numero1 + numero2}</h1>')
def multiplicacao(request, numero1, numero2):
    return HttpResponse(f'<h1>A multiplicacao vale {numero1 * numero2}</h1>')
def divisao(request, numero1, numero2):
    return HttpResponse(f'<h1>A divisao vale {numero1 / numero2}</h1>')
def subtracao(request, numero1, numero2):
    return HttpResponse(f'<h1>A subtracao vale {numero1 - numero2}</h1>')
