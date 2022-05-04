from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),

    #carrito
    path('carrito', carrito_compras, name="carrito_compras"),
    path('agregar/<int:producto_id>/', agregar_producto, name="agregar_producto"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="eliminar_producto"),
    path('restar/<int:producto_id>/', restar_producto, name="restar_producto"),
    path('limpiar/', limpiar_carrito, name="limpiar_carrito")
    
]