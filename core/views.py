from django.shortcuts import render, redirect

from core.carrito import Carrito
from core.models import Producto

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')

#carrito compras
def carrito_compras(request):
    productos = Producto.objects.all()
    return render(request, 'core/carrito_compras.html', {"productos": productos})


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.agregar(producto)
    return redirect("index")


def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.eliminar(producto)
    return redirect("index")


def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.restar(producto)
    return redirect("index")


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("index")


