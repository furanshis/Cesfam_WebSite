from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),

    #carrito
    path('carrito', carrito_compras, name="carrito_compras"),
    path('agregar/<int:producto_id>/', agregar_remedio, name="agregar_remedio"),
    path('eliminar/<int:producto_id>/', eliminar_remedio, name="eliminar_remedio"),
    path('restar/<int:producto_id>/', restar_remedio, name="restar_remedio"),
    path('limpiar/', limpiar_carrito, name="limpiar_carrito")
    
]