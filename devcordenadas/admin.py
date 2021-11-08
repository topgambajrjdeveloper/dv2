from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from devcordenadas.models import User, AboutPage,ImagePilaAbout, ProjectsPage,ImageProjects, ExperiencePage
# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass

class AboutImageInline(admin.TabularInline):
    model = ImagePilaAbout

@admin.register(AboutPage)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["title"]
    inlines=[AboutImageInline]

class ProjectsInline(admin.TabularInline):
    model = ImageProjects

@admin.register(ProjectsPage)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ["title"]
    inlines=[ProjectsInline]


@admin.register(ExperiencePage)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["title"]
    