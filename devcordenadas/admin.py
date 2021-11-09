from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from devcordenadas.models import User, AboutPage,ImagePilaAbout, ProjectsPage,ImageProjects, ExperiencePage

# Register your models here.

"""Admin User"""
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass

"""Admin About"""
class AboutImageInline(admin.TabularInline):
    model = ImagePilaAbout

@admin.register(AboutPage)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["title"]
    inlines=[AboutImageInline]

"""Admin Projects"""
class ProjectsInline(admin.TabularInline):
    model = ImageProjects

@admin.register(ProjectsPage)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ["title"]
    inlines=[ProjectsInline]

"""Admin Experience"""
@admin.register(ExperiencePage)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["title"]
    