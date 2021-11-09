from rest_framework.routers import DefaultRouter

from devcordenadas.views import AboutsModelViewSet, ProjectsModelViewSet, ExperiencesModelViewSet

router_about=DefaultRouter()
router_about.register(
    prefix='sobre-mi', basename='sobre-mi', viewset=AboutsModelViewSet)
router_project=DefaultRouter()
router_project.register(
    prefix='proyecto', basename='proyecto', viewset=ProjectsModelViewSet)
router_experience=DefaultRouter()
router_experience.register(prefix='experiencia', basename='experiencia', viewset=ExperiencesModelViewSet)