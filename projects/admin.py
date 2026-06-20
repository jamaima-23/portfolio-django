from django.contrib import admin
from .models import Project

# Register Project model in admin panel
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies')