from django import forms
from .models import Autor, Libro

class AutorForm(forms.ModelForm):

    class Meta:
        model = Autor

        fields = (
            'nombre',
            'nacionalidad',
            'fecNacimiento',
            'fecDefuncion',
            'comentarios',
            'activo',
        )

        labels = {
            'nombre': 'Apellido y nombres',
            'nacionalidad': 'Nacionalidad',
            'fecNacimiento': 'Fecha de nacimiento',
            'fecDefuncion': 'Fecha de defunción',
            'comentarios': 'Comentarios',
            'activo': 'Activo',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'nacionalidad': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'fecNacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'fecDefuncion': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'comentarios': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),

            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }


class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro

        fields = (
            'titulo',
            'autor',
            'editorial',
            'anioPub',
            'comentarios',
        )

        labels = {
            'anioPub': 'Año de publicación',
        }

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'autor': forms.Select(attrs={
                'class': 'form-select'
            }),

            'editorial': forms.DateInput(attrs={
                'class': 'form-control',
            }),

            'anioPub': forms.DateInput(attrs={
                'class': 'form-control',
            }),

            'comentarios': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
        }