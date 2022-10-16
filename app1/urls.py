from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name = 'inicio'),
    path('quienessomos/', views.quienes_somos, name = 'quienes_somos'),
    path('proyectos/', views.ver_proyectos, name='proyectos'),
    path('cursos/', views.ver_cursos, name='cursos'),

    path('hola_mundo', views.hola_mundo),
    path('saludar', views.saludar, name="saludar_por_defecto"),
    path('saludar/<str:nombre>', views.saludar, name="saludar"),
    #path('proyectos/2022/07',views.ver_proyectos_2022_07),
    #path('proyectos/<int:mes>/<int:anio>', views.ver_proyectos, name="ver_proyectos"),
        # con el re_path vamos a especificar que el anio sea un caracter numérico (d) de entre 2 a 4 caracteres. 
    #re_path(r'^proyectos/(?P<anio>\d{2,4})', views.ver_proyectos_anio),
    #path('cursos/detalle/<slug:nombre_curso>', views.cursos_detalle, name= "curso_detalle"),
        # la fc 're_path' es mas compleja: incluye metacaracteres (w,+) para definir cosas.
    #re_path(r'^cursos/(?P<nombre>\w+)/$', views.cursos, name="cursos"),
]