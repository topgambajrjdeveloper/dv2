from rest_framework.serializers import ModelSerializer

from devcordenadas.models import User, AboutPage, ImagePilaAbout, ProjectsPage,ImageProjects, ExperiencePage

"""Class Serialiezers Abouts"""
class ImagePilaAboutSerializers(ModelSerializer):
    class Meta:
        model=ImagePilaAbout
        fields=[
            'image',
            'alt_text'
        ]

class AboutPageSerializers(ModelSerializer):
    about_image = ImagePilaAboutSerializers(many=True, read_only=True)
    class Meta:
        model=AboutPage
        fields=[
            'title',
            'description_p1',
            'description_p2',
            'description_p3',
            'about_image'
        ]

"""Class Serialiezers Projects"""
class ImageProjectsSerializers(ModelSerializer):
    class Meta:
        model=ImageProjects
        fields=[
            'image',
            'alt_text'
        ]
class ProjectsPageSerializers(ModelSerializer):
    project_image=ImageProjectsSerializers(many=True, read_only=True)
    class Meta:
        model=ProjectsPage
        fields=[
            'id',
            'title',       
            'link',
            'project_image'
        ]

"""Class Serialiezers Projects"""
class ExperiencePageSerializers(ModelSerializer):
    class Meta:
        model=ExperiencePage
        fields=[
            'id',
            'title',
            'company',
            'desde',
            'hasta',
            'companyLink',
            'desc'
        ]