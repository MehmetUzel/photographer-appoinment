from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("profileaddress/", views.profileaddress, name="profileaddress"),
    path("userprofile/", views.userprofile, name="userprofile"),
]