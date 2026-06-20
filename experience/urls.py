from django.urls import path
from . import views

urlpatterns = [
    path('', views.experience_view, name='experience'),
]