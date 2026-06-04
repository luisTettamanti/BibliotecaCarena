from django.urls import path
from . import views

urlpatterns = [
    path('', views.index2, name='index2'),
    path('saludo/', views.saludo, name='saludo'),
    path('mensaje/', views.mensaje, name='mensaje'),
    path('autoragregar/', views.autorAgregar, name='autoragregar'),
    path('autormodificar/<int:id>/', views.autorModificar, name='autormodificar'),
    path('autorborrar/<int:id>/', views.autorBorrar2, name='autorborrar'),
]