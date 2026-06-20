from django.shortcuts import render
from .models import Education

# Education view - fetches all education records
def education_view(request):
    educations = Education.objects.all()
    return render(request, 'index.html', {'educations': educations})