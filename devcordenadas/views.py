from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from devcordenadas.models import User, AboutPage, ImagePilaAbout, ProjectsPage,ImageProjects, ExperiencePage
from devcordenadas.serializers import  ImagePilaAboutSerializers, AboutPageSerializers, ImageProjectsSerializers, ProjectsPageSerializers, ExperiencePageSerializers
from rest_framework import generics

# Create your views here.

"""Class ModelViewSet Abouts"""
class AboutsModelViewSet(ModelViewSet):
    queryset = AboutPage.objects.all()
    serializer_class = AboutPageSerializers

"""Class ModelViewSet Projects"""
class ProjectsModelViewSet(ModelViewSet):
    queryset = ProjectsPage.objects.all()
    serializer_class = ProjectsPageSerializers

"""Class ModelViewSet Experiences"""
class ExperiencesModelViewSet(ModelViewSet):
    queryset = ExperiencePage.objects.all()
    serializer_class = ExperiencePageSerializers
