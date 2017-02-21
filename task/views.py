from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá!")

def sobre(request):
    return HttpResponse("Erick Willames E. Rodrigues")

def tarefa(request,ano,mes,dia):
    return HttpResponse("Tarefa: "+ str(ano)+" - "+str(mes)+" - "+str(dia))
