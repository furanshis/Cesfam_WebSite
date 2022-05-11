from ctypes.wintypes import PINT
from email import message
from django.shortcuts import render, redirect
from django.core.mail import send_mail


from core.carrito import Carrito
from core.models import Remedio

#rest
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters
from .serializers import *

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('full-name')
        correo = request.POST.get('email')
        telefono = request.POST.get('telefono')
        asunto = request.POST.get('subject')
        mensaje = request.POST.get('message')

        data= {
            'nombre' : nombre,
            'email' : correo,
            'telefono' : telefono,
            'subject' : asunto,
            'message' : mensaje

        }
        message = '''
        New message: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '',['matideus74@gmail.com'])

    return render(request, 'core/contacto.html')



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

def total_carrito(request, precio_remedio):
    carrito = Carrito(request)
    remedio = Remedio.objects.get(precioRemedio=precio_remedio)
    carrito.total_carrito(remedio)
    return redirect("carrito_compras")




#rest
class RemedioViewSet(viewsets.ModelViewSet):
    queryset = Remedio.objects.all().order_by('idRemedio')
    serializer_class = RemedioSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    search_fields = ['question_text']
    filter_backends = (filters.SearchFilter,)
    queryset = MarcaRemedio.objects.all().order_by('idMarcaRemedio')
    serializer_class = MarcaSerializer

