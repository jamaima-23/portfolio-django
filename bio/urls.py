from django.urls import path
from . import views

urlpatterns = [
    path('', views.bio_view, name='bio'),
]