from django.shortcuts import render, redirect

from core.carrito import Carrito
from core.models import Remedio

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

#carrito compras
def carrito_compras(request):
    remedios = Remedio.objects.all()
    return render(request, 'core/carrito_compras.html', {"remedios": remedios})


def agregar_remedio(request, remedio_id):
    carrito = Carrito(request)
    remedio = Remedio.objects.get(idRemedio=remedio_id)
    carrito.agregar(remedio)
    return redirect("carrito_compras")


def eliminar_remedio(request, remedio_id):
    carrito = Carrito(request)
    remedio = Remedio.objects.get(idRemedio=remedio_id)
    carrito.eliminar(remedio)
    return redirect("carrito_compras")


def restar_remedio(request, remedio_id):
    carrito = Carrito(request)
    remedio = Remedio.objects.get(idRemedio=remedio_id)
    carrito.restar(remedio)
    return redirect("carrito_compras")


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito_compras")


