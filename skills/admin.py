from django.contrib import admin
from .models import Skill

# Register Skill model in admin panel
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')