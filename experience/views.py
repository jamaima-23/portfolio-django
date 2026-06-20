from django.shortcuts import render
from .models import Experience

# Experience view - fetches all experience records
def experience_view(request):
    experiences = Experience.objects.all()
    return render(request, 'index.html', {'experiences': experiences})