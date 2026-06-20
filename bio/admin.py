from django.contrib import admin
from .models import Bio

# Register Bio model in admin panel
@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    # Columns shown in admin list view
    list_display = ('name', 'job_title')