from django.urls import path
from . import views

urlpatterns = [
    path("photoshoot/", views.photo_shoot, name="photo_shoot"),
]