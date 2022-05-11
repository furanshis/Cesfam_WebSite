from rest_framework import serializers
from .models import *

class RemedioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Remedio
        fields = ('idRemedio', 'nombreRemedio', 'descripcionRemedio', 'precioRemedio', 'stockRemedio', 'cantidadRemedio', 'imagenRemedio')

class MarcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MarcaRemedio
        fields = ('idMarcaRemedio', 'nombreMarcaRemedio')