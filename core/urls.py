from django.urls import path, include
from .views import *

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'remedio', views.RemedioViewSet)
router.register(r'marca', views.MarcaViewSet)

urlpatterns = [

    #rest
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('inicio', index, name='index'),
    path('login/', login, name='login'),
    path('nosotros/', nosotros, name='nosotros'),


    #carrito
    path('carrito', carrito_compras, name="carrito_compras"),
    path('agregar/<int:remedio_id>/', agregar_remedio, name="agregar_remedio"),
    path('eliminar/<int:remedio_id>/', eliminar_remedio, name="eliminar_remedio"),
    path('restar/<int:remedio_id>/', restar_remedio, name="restar_remedio"),
    path('limpiar/', limpiar_carrito, name="limpiar_carrito"),
    path('total/<int:precio_remedio>', total_carrito, name="total_carrito")
    
    
    
]