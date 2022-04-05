from django.urls import path
from . import views

urlpatterns = [
    path("appoinment/", views.appoinment, name="appoinment"),
    path("appoinment/data/", views.appoinment_data, name="appoinment_data"),
    path("appoinment/data/week", views.get_week_data, name="get_week_data"),
    path("appoinment/add/", views.add_appoinment, name="appoinment_add"),
    path("appoinment/admin/", views.admin_edit, name="admin_edit"),
    path("appoinment/admin/offday/", views.add_offday, name="add_offday")
]