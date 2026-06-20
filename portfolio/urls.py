from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Import all views directly for homepage
from bio.views import bio_view
from education.models import Education
from skills.models import Skill
from experience.models import Experience
from projects.models import Project
from django.shortcuts import render

# This single view loads ALL data for homepage
def home(request):
    # Fetch all data from database
    bio = bio_view  # we'll handle this differently
    from bio.models import Bio
    bio = Bio.objects.first()
    educations = Education.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    projects = Project.objects.all()

    # Send all data to template
    context = {
        'bio': bio,
        'educations': educations,
        'skills': skills,
        'experiences': experiences,
        'projects': projects,
    }
    return render(request, 'index.html', context)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Homepage shows everything
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)