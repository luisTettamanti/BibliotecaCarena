from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from apBiblioteca.models import Autor, Libro
from .forms import AutorForm, LibroForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.db.models import Q

def index(request):
    return render(request, 'apBiblioteca/bootstrap.html')


def index2(request):
    autores = Autor.objects.all()
    # autores = Autor.objects.all().order_by('nombre')
    #
    # autores = Autor.objects.filter(nombre='Borges Jorge Luis')
    # autores = Autor.objects.filter(nombre__icontains='Bo')
    # autores = Autor.objects.filter(activo=True)
    # autores = Autor.objects.filter(fecNacimiento__year__gt=1980)
    #
    # autores = Autor.objects.exclude(activo=False)
    #
    # autores = Autor.objects.get(id=3)

    q = request.GET.get('q')

    autores = Autor.objects.all()

    if q:
        autores = autores.filter(nombre__icontains=q)

    contexto = {
        'autores': autores,
        'q': q,
    }

    return render(request,
                  'apBiblioteca/index2.html',
                  contexto)


def saludo(request):
    nombre = request.GET.get('nombre')
    contexto = {
        'nombre': nombre
    }
    return render(request, 'apBiblioteca/saludo.html', contexto)


def mensaje(request):
    texto = ''
    if request.method == 'POST':
        texto = request.POST.get('mensaje')
    contexto = {
        'texto': texto
    }
    return render(request, 'apBiblioteca/mensaje.html', contexto)


def autorAgregar(request):
    # Agregar Autor Form en template.

    if request.method == 'POST':

        Autor.objects.create(
            nombre=request.POST.get('nombre'),
            nacionalidad=request.POST.get('nacionalidad') or None,
            fecNacimiento=request.POST.get('fecNacimiento') or None,
            fecDefuncion=request.POST.get('fecDefuncion') or None,
            comentarios=request.POST.get('comentarios') or None,
            activo=True if request.POST.get('activo') == 'on' else False
        )

        return redirect('index2')

    contexto = {
        'autor': None
    }

    return render(request, 'apBiblioteca/autorform.html', contexto)


def autorModificar(request, id):
    # Modificar Autor Form en template.

    autor = get_object_or_404(Autor, id=id)

    if request.method == 'POST':

        autor.nombre = request.POST.get('nombre')
        autor.nacionalidad = request.POST.get('nacionalidad') or None
        autor.fecNacimiento = request.POST.get('fecNacimiento') or None
        autor.fecDefuncion = request.POST.get('fecDefuncion') or None
        autor.comentarios = request.POST.get('comentarios') or None
        autor.activo = True if request.POST.get('activo') == 'on' else False

        autor.save()

        return redirect('index2')

    contexto = {
        'autor': autor
    }

    return render(request, 'apBiblioteca/autorform.html', contexto)


def autorBorrar(request, id):
    # Borrar Autor sin confirmación.

    autor = get_object_or_404(Autor, id=id)
    autor.delete()
    return redirect('index2')


def autorAgregar2(request):
    # Agregar Autor Form en Forms.py.

    if request.method == "POST":
        form = AutorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index2')

    else:
        form = AutorForm()

    return render(request, "apBiblioteca/autorform2.html", {
        "form": form
    })


def autorModificar2(request, id):
    # Modificar Autor Form en Forms.py.

    autor = get_object_or_404(Autor, id=id)

    if request.method == "POST":
        form = AutorForm(request.POST, instance=autor)

        if form.is_valid():
            form.save()
            return redirect('index2')

    else:
        form = AutorForm(instance=autor)

    return render(request, "apBiblioteca/autorform2.html", {
        "form": form
    })


def autorBorrar2(request, id):
    # Borrar Autor con confirmación.

    autor = get_object_or_404(Autor, id=id)

    if request.method == 'POST':
        autor.delete()
        return redirect('index2')

    contexto = {
        'autor': autor
    }

    return render(
        request,
        'apBiblioteca/autorconfborrado.html',
        contexto
    )


class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'apBiblioteca/autorform2.html'
    success_url = '/'


class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'apBiblioteca/autorform2.html'
    success_url = '/'


class AutorDeleteView(DeleteView):
    model = Autor
    form_class = AutorForm
    template_name = 'apBiblioteca/autorconfborrado.html'
    success_url = '/'


class LibrosLista(ListView):
    model = Libro
    template_name = 'apBiblioteca/libroslista.html'
    context_object_name = 'libros'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            # queryset = queryset.filter(Q(titulo__icontains=query))
            queryset = queryset.filter(
                Q(titulo__icontains=query) |
                Q(autor__nombre__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')  # Enviar el valor de la búsqueda al contexto
        return context


class LibroDetalle(DetailView):
    model = Libro
    template_name = 'apBiblioteca/librodetalle.html'
    context_object_name = 'libro'


class LibroAgregar(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'apBiblioteca/libroform.html'
    success_url = reverse_lazy('libroslista')


class LibroModificar(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'apBiblioteca/libroform.html'
    success_url = reverse_lazy('libroslista')


class LibroBorrar(DeleteView):
    model = Libro
    template_name = 'apBiblioteca/libroborrar.html'
    success_url = reverse_lazy('libroslista')