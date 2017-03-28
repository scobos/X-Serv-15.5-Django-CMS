from django.shortcuts import render
from django.http import HttpResponse
from cms.models import Pages


# Create your views here.

def pagina(request, identificador):

    try:
        pag = Pages.objects.get(id = int(identificador))
        respuesta = pag.page
    except Pages.DoesNotExist:
        respuesta = "El nombre no está en la base de datos"
    return HttpResponse(respuesta)

def mostrar_Info(request):
    lista = Pages.objects.all()
    respuesta = "<ol>"
    for pag in lista:
        respuesta += '<li><a href="' + str(pag.id) + '">' + pag.name + '</a>'
    respuesta += "</ol>"
    return HttpResponse(respuesta)
