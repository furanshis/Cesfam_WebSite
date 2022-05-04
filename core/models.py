from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombreUsuario = models.CharField(primary_key=True, max_length=20, verbose_name="Nombre de usuario")
    contrasenaUsuario = models.CharField(max_length=15, verbose_name="Contraseña de usuario")

    def __str__(self):
        return self.nombreUsuario


class Producto(models.Model):
    objects = None
    idProducto = models.IntegerField(primary_key=True, verbose_name="Id del producto")
    nombreProducto = models.CharField(max_length=50, verbose_name="Nombre del producto")
    descripcionProducto = models.CharField(max_length=200, verbose_name="Descripción del producto")
    precioProducto = models.IntegerField(verbose_name="Precio del producto")

    def __str__(self):
        return f'{self.nombreProducto} -> {self.precioProducto}'

class Remedio(models.Model):
    idRemedio = models.IntegerField(primary_key=True,verbose_name="Id del remedio")
    nombreRemedio = models.CharField(max_lenght=50, verbose_name="Nombre del remedio")
    descripcionRemedio = models.CharField(max_lenght=120, verbose_name="Descripción del remedio")

class CategoriaRemedio(models.Model):
    idCategoriaRemedio = models.IntegerField()