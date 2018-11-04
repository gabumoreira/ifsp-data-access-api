from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import NestedRouterMixin

from . import views

class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    """ Foo de configuração para roteamento aninhado na URL """
    pass

# Recursos diretos e listagens
router 		= NestedDefaultRouter()
router.register('areas', views.AreasViewSet)
router.register('base', views.BaseViewSet)
router.register('curso', views.CursoViewSet)
router.register('docentes', views.DocentesViewSet)
router.register('infra', views.InfraViewSet)