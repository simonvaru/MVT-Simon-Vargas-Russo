from django.urls import path
from proyectoClase import views # from proyectoClase en lugar de home


urlpatterns = [
    path('', views.index),
    path('mi-template/', views.mi_template),
    path('mi-template/<str:nombre>', views.tu_template),
    path('prueba-template/', views.prueba_template),
    path('ver-personas/', views.ver_personas),
    path('crear-persona/<str:nombre>/<str:apellido>/', views.crear_persona),
    # path('hola/', hola),
    # path('fecha/', fecha),
]
