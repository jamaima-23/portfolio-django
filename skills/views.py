from django.shortcuts import render
from .models import Skill

# Skills view - fetches all skills
def skills_view(request):
    skills = Skill.objects.all()
    return render(request, 'index.html', {'skills': skills})