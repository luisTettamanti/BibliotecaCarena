from django.urls import path
from . import views
from .views import (AutorCreateView, AutorUpdateView, AutorDeleteView,
                    LibrosLista, LibroDetalle, LibroAgregar, LibroModificar, LibroBorrar)

urlpatterns = [
    # path('', views.index, name='bootstrap'),
    # path('', views.index2, name='index2'),
    path('saludo/', views.saludo, name='saludo'),
    path('mensaje/', views.mensaje, name='mensaje'),
    path('autoragregar/', views.autorAgregar2, name='autoragregar'),
    path('autormodificar/<int:id>/', views.autorModificar2, name='autormodificar'),
    path('autorborrar/<int:id>/', views.autorBorrar2, name='autorborrar'),

    path('autoragregarclase/', AutorCreateView.as_view(), name='autoragregarclase'),
    path('autormodificarclase/<int:pk>/', AutorUpdateView.as_view(), name='autormodificarclase'),
    path('autorborrarclase/<int:pk>/', AutorDeleteView.as_view(), name='autorborrarclase'),

    path('', LibrosLista.as_view(), name='libroslista'),
    path('librodetalle/<int:pk>/', LibroDetalle.as_view(), name='librodetalle'),
    path('libroagregar/', LibroAgregar.as_view(), name='libroagregar'),
    path('libromodificar/<int:pk>/', LibroModificar.as_view(), name='libromodificar'),
    path('libroborrar/<int:pk>/', LibroBorrar.as_view(), name='libroborrar'),

]