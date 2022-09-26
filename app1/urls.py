from django.urls import path
from . import views

urlpatterns = [
    path('hola_mundo',views.hola_mundo),
    path('saludar',views.saludar, name="saludar_por_defecto"),
    path('saludar/<str:nombre>',views.saludar, name="saludar"),
    path('proyectos/<int:mes>/<int:anio>', views.ver_proyectos, name="ver_proyectos"),
]