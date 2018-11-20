from rest_framework.routers import DefaultRouter

from . import views

# Recursos diretos e listagens
router 		= DefaultRouter()
router.register('areas', views.AreasViewSet)
router.register('base', views.BaseViewSet)
router.register('curso', views.CursoViewSet)
router.register('docentes', views.DocentesViewSet)
router.register('infra', views.InfraViewSet)