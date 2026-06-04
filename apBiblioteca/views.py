from django.shortcuts import render, redirect, get_object_or_404
from apBiblioteca.models import Autor

def index(request):
    return render(request, 'apBiblioteca/index.html')


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

    autor = get_object_or_404(Autor, id=id)

    autor.delete()

    return redirect('index2')


def autorBorrar2(request, id):

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