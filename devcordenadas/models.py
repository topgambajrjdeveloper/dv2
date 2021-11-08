from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
"""Modelo de la pag de Auth"""
class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"

    def __str__(self):
        return self.email

"""Modelo de la pag de conoceme"""
class AboutPage(models.Model):
    title=models.CharField(verbose_name=_("titulo"), max_length=255)
    description_p1=models.CharField(verbose_name=_("desc parrafo1"), max_length=255)
    description_p2=models.CharField(verbose_name=_("desc parrafo2"), max_length=255)
    description_p3=models.CharField(verbose_name=_("desc parrafo3"), max_length=255)
    
    class Meta:
        verbose_name:_("SobreMi")
        verbose_name_plural:_("SobreMis")
    
    def __str__(self):
        return self.title

class ImagePilaAbout(models.Model):
    about=models.ForeignKey(AboutPage, on_delete=models.CASCADE, related_name="about_image")
    image=models.ImageField(verbose_name=_("imagen de habilidades"),default="about/default.png",upload_to="about/",)
    alt_text=models.CharField(verbose_name=_("titulo"), max_length=255)

"""Modelo de la pag de proyectos"""
class ProjectsPage(models.Model):
    title=models.CharField(verbose_name=_("titulo"), max_length=255)
    link=models.URLField(verbose_name=_("URL de la empresa"))
    
    class Meta:
        verbose_name:_("Proyecto")
        verbose_name_plural:_("Proyectos")
    
    def __str__(self):
        return self.title

class ImageProjects(models.Model):
    project=models.ForeignKey(ProjectsPage, on_delete=models.CASCADE, related_name="project_image")
    image=models.ImageField(verbose_name=_("imagen de habilidades"),default="project/default.png",upload_to="project/",)
    alt_text=models.CharField(verbose_name=_("titulo"), max_length=255)

"""Modelo de la pag de experiencias"""
class ExperiencePage(models.Model):
    title=models.CharField(verbose_name=_("titulo"), max_length=255)
    company=models.CharField(verbose_name=_("compañia"), max_length=255)
    desde=models.DateField(verbose_name=_("año en el que empezaste"))
    hasta=models.DateField(verbose_name=_("año en el que terminaste"))
    companyLink=models.URLField(verbose_name=_("URL de la empresa"))
    desc=models.CharField(verbose_name=_("descripcion de las tareas realizadas"), max_length=255)

    class Meta:
        verbose_name:_("Experiencia")
        verbose_name_plural:_("Experiencias")

    def __str__(self):
        return self.title