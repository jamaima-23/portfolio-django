from django.contrib import admin
from .models import Experience

# Register Experience model in admin panel
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('organization', 'position', 'duration')