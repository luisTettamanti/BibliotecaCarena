from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=30, help_text="Apellido y nombres del autor", verbose_name="Apellido y Nombres")
    nacionalidad = models.CharField(max_length=30, help_text="Nacionalidad del autor", blank=True, null=True)
    fecNacimiento = models.DateField(help_text="Fecha de nacimiento del autor", blank=True, null=True)
    fecDefuncion = models.DateField(help_text="Fecha de defunción del autor", blank=True, null=True)
    comentarios = models.TextField(help_text="Comentarios referidos al autor", blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']

class Libro(models.Model):
    titulo = models.CharField(max_length=40, help_text="Título del libro", verbose_name="Apellido y Nombres")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.CharField(max_length=30, help_text="Editorial del libro", blank=True, null=True)
    anioPub = models.IntegerField(help_text="Año de publicación", blank=True, null=True)
    comentarios = models.TextField(help_text="Comentarios referidos al libro", blank=True, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['titulo']