from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Shoot_Plan
from django.forms import fields
from django.utils.translation import gettext_lazy as _

class ShootPlanForm(forms.ModelForm):
    class Meta:
        model=Shoot_Plan
        fields = ["shoot_type","album_type","num_of_concept"]