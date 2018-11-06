import django_filters

from .models import Areas

class AreasFilter(django_filters.FilterSet):
    class Meta:
        model = Areas
        fields = {
            'sigla_area': ['exact','icontains'],
            'area_atua': ['exact'],
            'equi_area': ['exact'],
            'obs_area': ['exact']
        }
