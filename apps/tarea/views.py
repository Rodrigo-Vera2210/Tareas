from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework import status, permissions

from .models import Tarea
from .serializers import TareaSerializer
from .pagination import *
from rest_framework.parsers import MultiPartParser, FormParser

class TareaListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
        
class CrearTareaApiView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = TareaSerializer
    queryset = Tarea.objects.all()

class ActualizarTarea(UpdateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = TareaSerializer
    queryset = Tarea.objects.all()

class EliminarTarea(DestroyAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = Tarea
    queryset = Tarea.objects.all()