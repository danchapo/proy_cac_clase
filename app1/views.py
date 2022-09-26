from django.http import HttpResponse
# OJO que esto no va: from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
def hola_mundo(request):
    return HttpResponse('Hola Mundo Django')

def saludar(request, nombre='RANDOM'):
    return HttpResponse(f"""
        <h1> Hola, cómo estas {nombre}?</h1>
        <p>"probando cositas"</p>
        """)

def ver_proyectos(request, mes, anio):
    return HttpResponse(f"""
        <h1> proyectos del - {mes}/{anio}?</h1>
        <p>Listado de proyectos</p>
        """)