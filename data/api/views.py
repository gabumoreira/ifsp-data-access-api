from rest_framework import authentication, permissions, viewsets

from .models import Areas, Base, Curso, Docentes, Infra
from .serializers import AreasSerializer, BaseSerializer, CursoSerializer, DocentesSerializer, InfraSerializer
from .filters import AreasFilter

class AreasViewSet(viewsets.ModelViewSet):
    queryset = Areas.objects.order_by('id_area')
    serializer_class = AreasSerializer

    filter_class = AreasFilter
    filter_fields  = ('sigla_area','area_atua','equi_area',)
    search_fields = ('obs_area')
    ordering_fields = ('id_area')

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