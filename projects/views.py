from django.shortcuts import render
from .models import Project

# Projects view - fetches all projects
def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})