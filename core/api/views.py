from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from core.models import Remedio
from core.api.serializers import RemedioSerializer

@api_view(['GET', ])
def api_detail_remedio_view(request, slug):
    try:
    except Remedio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)