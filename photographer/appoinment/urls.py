from django.urls import path
from . import views

urlpatterns = [
    path("appoinment/", views.appoinment, name="appoinment"),
    path("appoinment/data/", views.appoinment_data, name="appoinment_data"),
]