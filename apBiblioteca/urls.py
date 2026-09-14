from django.urls import path
from . import views
from .views import (LibrosLista, LibroDetalle, LibroAgregar, LibroModificar, LibroBorrar,
                    AutoresLista, AutorDetalle, AutorAgregar, AutorModificar, AutorBorrar)

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.index2, name='index2'),
    # path('saludo/', views.saludo, name='saludo'),
    # path('mensaje/', views.mensaje, name='mensaje'),

    # path('autoragregarclase/', AutorCreateView.as_view(), name='autoragregarclase'),
    # path('autormodificarclase/<int:pk>/', AutorUpdateView.as_view(), name='autormodificarclase'),
    # path('autorborrarclase/<int:pk>/', AutorDeleteView.as_view(), name='autorborrarclase'),

    path('autoreslista/', AutoresLista.as_view(), name='autoreslista'),
    path('autordetalle/<int:pk>/', AutorDetalle.as_view(), name='autordetalle'),
    path('autoragregar/', AutorAgregar.as_view(), name='autoragregar'),
    path('autormodificar/<int:pk>/', AutorModificar.as_view(), name='autormodificar'),
    path('autorborrar/<int:pk>/', AutorBorrar.as_view(), name='autorborrar'),

    path('libroslista/', LibrosLista.as_view(), name='libroslista'),
    path('librodetalle/<int:pk>/', LibroDetalle.as_view(), name='librodetalle'),
    path('libroagregar/', LibroAgregar.as_view(), name='libroagregar'),
    path('libromodificar/<int:pk>/', LibroModificar.as_view(), name='libromodificar'),
    path('libroborrar/<int:pk>/', LibroBorrar.as_view(), name='libroborrar'),

]