from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse
# OJO que esto no va: from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from django.template import loader
# Create your views here.

def index(request):
    if (request.method == 'GET'):
        titulo = 'titulo cuado se accede con GET'
    else:
        titulo = f'titulo cuando se accede con otro metodo: {request.method}'
    # lo siguiente muestra como obtener por GET los parametros que se puedan ingresar por url
    parameters_get = request.GET.get('param1')
        #ya no usaremos las vistas -> usaremos los templates
    # return HttpResponse(f"""
    #     <h1>{titulo}</h1>
    #     <p>valor de param1: {parameters_get}</p>
    #     """)
        # con el dicc que pasamos como param a 'render' indicamos qué variables estarán disponibles.
    listado_cursos = [
        {
            'nombre':'Fullstack Java',
            'descripcion':'Curso de Fullstack',
            'categoria':'Programacion'
        },
        {
            'nombre':'diseño UX',
            'descripcion':'Curso de Diseño',
            'categoria':'diseño'
        },
        {
            'nombre':'Big data',
            'descripcion':'analisis de datos',
            'categoria':'ciencia de datos'
        }
    ]
    return render(request, 'app1/index.html', {
                                        'titulo_nombre': titulo, 
                                        'cursos': listado_cursos,
                                        'parametros': parameters_get,
                                        'hoy': datetime.now})

def quienes_somos(request):
        # redirige a la url(path) con el name 'saludar_por_defecto' 
    # return redirect('saludar_por_defecto')
        # el redirect de abajo accede a la url con name 'saludar' y asigna 'Panchito' al str 'nombre'.
    #return redirect(reverse('saludar', kwargs={'nombre': 'Panchito'}))
        #ahora vamos a ver otra forma de renderizar diferente a la de index:
    template = loader.get_template('app1/quienes_somos.html')
    context = {'titulo':'codo a codo - quienes somos'}
    return HttpResponse(template.render(context, request))

def ver_proyectos(request, anio=2022, mes=1):
    proyectos = []
    return render(request, 'app1/proyectos.html', {'proyectos':proyectos})

def ver_cursos(request):   
    listado_cursos = [
        {
            'nombre':'Fullstack Java',
            'descripcion':'Curso de Fullstack',
            'categoria':'Programacion'
        },
        {
            'nombre':'diseño UX',
            'descripcion':'Curso de Diseño',
            'categoria':'diseño'
        },
        {
            'nombre':'Big data',
            'descripcion':'analisis de datos',
            'categoria':'ciencia de datos'
        }
    ]
    return render(request, 'app1/cursos.html', {'cursos': listado_cursos})
    

def hola_mundo(request):
    return HttpResponse('Hola Mundo Django')

def saludar(request, nombre='RANDOM'):
    return HttpResponse(f"""
        <h1> Hola, cómo estas {nombre}?</h1>
        <p>"probando cositas"</p>
        """)

def ver_proyectos_2022_07(request):
    return HttpResponse(f"""
        <h1>Proyectos del mes 7 del año 2022</h1>
        <p>Listado de proyectos</p>
    """) 

def ver_proyectos_anio(request, anio):
    return HttpResponse(f"""
        <h1> proyectos del {anio}</h1>
        <p>Listado de proyectos</p>
        """)

def cursos_detalle(request, nombre_curso):
    return HttpResponse(f"""
    <h1>{nombre_curso}</h1>
    """)

def cursos(request, nombre):
    return HttpResponse(f"""
    <h2>{nombre}</h2>
    """)