from django.db import models
from django.urls import reverse

# Create your models here.
class Genero(models.Model):
    nombre = models.CharField(max_length=200, help_text="Ingresa un genero de libro (ej. Ciencia Ficción)")
    
    def __str__(self):
        return self.nombre
    
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null =True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"    
    
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField(max_length=1000, help_text="Ingresa una breve descripción del Libro (max: 1000 caracteres)")
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text="Ingresa un ISBN de máximo 13 números")
    genero = models.ManyToManyField(Genero, help_text="Selecciona un genero para este libro")

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse("detalle_libro", args=[str(self.id)])

class LibroInstancia(models.Model):
    libro = models.ForeignKey('Libro', on_delete=models.SET_NULL, null=True)
    impresiones = models.CharField(max_length=200)
    fecha_devolucion = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(max_length=20, default="Disponible", help_text="Libro disponible")

    def __str__(self):
        return f'{self.id} ({self.libro.titulo})'