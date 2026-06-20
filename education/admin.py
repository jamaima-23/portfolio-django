from django.contrib import admin
from .models import Education

# Register Education model in admin panel
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institute', 'session')