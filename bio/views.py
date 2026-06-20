from django.shortcuts import render
from .models import Bio

# Bio view - fetches bio data
def bio_view(request):
    bio = Bio.objects.first()  # Get first bio entry
    return render(request, 'index.html', {'bio': bio})