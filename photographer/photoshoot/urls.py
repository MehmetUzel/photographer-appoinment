from django.urls import path
from . import views

urlpatterns = [
    path("photoshoot/", views.photo_shoot, name="photo_shoot"),
    path("photoshoot/concepts/", views.concept_photos, name="concept_photos"),
]