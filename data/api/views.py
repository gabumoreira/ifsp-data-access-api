from rest_framework import authentication, permissions, viewsets

from .models import Areas, Base, Curso, Docentes, Infra
from .serializers import AreasSerializer, BaseSerializer, CursoSerializer, DocentesSerializer, InfraSerializer

class AreasViewSet(viewsets.ModelViewSet):
    queryset = Areas.objects.order_by('id_area')
    serializer_class = AreasSerializer

class BaseViewSet(viewsets.ModelViewSet):
    queryset = Base.objects.order_by('id_base')
    serializer_class = BaseSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.order_by('id_curso')
    serializer_class = CursoSerializer
    
class DocentesViewSet(viewsets.ModelViewSet):
    queryset = Docentes.objects.order_by('id_docente')
    serializer_class = DocentesSerializer 
       
class InfraViewSet(viewsets.ModelViewSet):
    queryset = Infra.objects.order_by('id_infra')
    serializer_class = InfraSerializer