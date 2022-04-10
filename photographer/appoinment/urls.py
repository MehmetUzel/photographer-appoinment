from django.urls import path
from . import views

urlpatterns = [
    path("appoinment/", views.appoinment, name="appoinment"),
    path("appoinment/data/", views.appoinment_data, name="appoinment_data"),
    path("appoinment/data/week", views.get_week_data, name="get_week_data"),
    path("appoinment/add/", views.add_or_delete_appoinment, name="appoinment_add"),
    path("appoinment/admin/", views.admin_edit, name="admin_edit"),
    path("appoinment/admin/offday/", views.add_or_delete_offday, name="add_offday"),
    path("appoinment/admin/users/", views.user_info_for_admin, name="user_info_for_admin"),
    path("appoinment/users/data/", views.user_app_info, name="user_app_info"),
    path("appoinment/admin/appoinment_info/", views.get_user_for_app, name="get_user_for_app"),
]