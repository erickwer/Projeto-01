from django.shortcuts import render
from django.http import HttpResponse

class tarefa (object):

    def __init__(self,titulo,data):
        self.titulo=titulo
        self.data=data

    def __str__(self):
        return self.titulo

def home(request):
    return HttpResponse("Olá!")

def sobre(request):
    return HttpResponse("Erick Willames E. Rodrigues")

def tarefa(request,ano,mes,dia):
    return HttpResponse("Tarefa: "+ str(ano)+" - "+str(mes)+" - "+str(dia))


def contatos(request, telefone):
    return HttpResponse("Telefone: "+ str(telefone))
