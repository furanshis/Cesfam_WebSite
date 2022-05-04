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


class CategoriaRemedio(models.Model):
    idCategoriaRemedio = models.IntegerField(primary_key=True, verbose_name="Id de la categoria del remedio")
    nombreCategoriaRemedio = models.CharField(max_length=50, verbose_name="Nombre de la categoría del producto")

    def __str__(self):
        return self.nombreCategoriaRemedio

class Remedio(models.Model):
    objects = None
    idRemedio = models.IntegerField(primary_key=True,verbose_name="Id del remedio")
    nombreRemedio = models.CharField(max_length=50, verbose_name="Nombre del remedio")
    descripcionRemedio = models.CharField(max_length=120, verbose_name="Descripción del remedio")
    categoriaRemedio = models.ForeignKey(CategoriaRemedio, on_delete=models.CASCADE)
    precioRemedio = models.IntegerField(verbose_name="Precio del remedio")

    def __str__(self):
        return f'{self.nombreRemedio} -> {self.precioRemedio}'