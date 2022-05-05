from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('contacto/', contacto, name='contacto'),

    #carrito
    path('carrito', carrito_compras, name="carrito_compras"),
    path('agregar/<int:remedio_id>/', agregar_remedio, name="agregar_remedio"),
    path('eliminar/<int:remedio_id>/', eliminar_remedio, name="eliminar_remedio"),
    path('restar/<int:remedio_id>/', restar_remedio, name="restar_remedio"),
    path('limpiar/', limpiar_carrito, name="limpiar_carrito")
    
]