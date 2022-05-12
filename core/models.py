from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombreUsuario = models.CharField(primary_key=True, max_length=20, verbose_name="Nombre de usuario")
    contrasenaUsuario = models.CharField(max_length=15, verbose_name="Contraseña de usuario")

    def __str__(self):
        return self.nombreUsuario

class CategoriaRemedio(models.Model):
    idCategoriaRemedio = models.IntegerField(primary_key=True, verbose_name="Id de la categoria del remedio")
    nombreCategoriaRemedio = models.CharField(max_length=50, verbose_name="Nombre de la categoría del producto")

    def __str__(self):
        return self.nombreCategoriaRemedio

class MarcaRemedio(models.Model):
    idMarcaRemedio = models.IntegerField(primary_key=True, verbose_name="Marca del remedio")
    nombreMarcaRemedio = models.CharField(max_length=50, verbose_name="Nombre de la marca del remedio")

    def __str__(self):
        return self.nombreMarcaRemedio

class Remedio(models.Model):
    objects = None
    idRemedio = models.IntegerField(primary_key=True,verbose_name="Id del remedio")
    nombreRemedio = models.CharField(max_length=50, verbose_name="Nombre del remedio")
    marcaRemedio = models.ForeignKey(MarcaRemedio, on_delete=models.CASCADE)
    descripcionRemedio = models.CharField(max_length=300, verbose_name="Descripción del remedio")
    categoriaRemedio = models.ForeignKey(CategoriaRemedio, on_delete=models.CASCADE)
    precioRemedio = models.IntegerField(verbose_name="Precio del remedio")
    stockRemedio = models.IntegerField(verbose_name="Stock del remedio")
    cantidadRemedio = models.CharField(max_length=15 ,verbose_name="Cantidad de remedio en gr o mg")
    imagenRemedio = models.ImageField(verbose_name="Imagen del remedio")

    def __str__(self):
        return f'{self.nombreRemedio} -> {self.precioRemedio}'

