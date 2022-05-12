from rest_framework import serializers
from core..models import *

class RemedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remedio
        fields = ('idRemedio', 'nombreRemedio', 'descripcionRemedio', 'precioRemedio', 'stockRemedio', 'cantidadRemedio', 'imagenRemedio')

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarcaRemedio
        fields = ('idMarcaRemedio', 'nombreMarcaRemedio')