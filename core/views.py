from django.shortcuts import render, redirect

from core.carrito import Carrito
from core.models import Remedio

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')

#carrito compras
def carrito_compras(request):
    remedios = Remedio.objects.all()
    return render(request, 'core/carrito_compras.html', {"remedios": remedios})


def agregar_remedio(request, producto_id):
    carrito = Carrito(request)
    producto = Remedio.objects.get(idProducto=producto_id)
    carrito.agregar(producto)
    return redirect("carrito_compras")


def eliminar_remedio(request, producto_id):
    carrito = Carrito(request)
    producto = Remedio.objects.get(idProducto=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito_compras")


def restar_remedio(request, producto_id):
    carrito = Carrito(request)
    producto = Remedio.objects.get(idProducto=producto_id)
    carrito.restar(producto)
    return redirect("carrito_compras")


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito_compras")


