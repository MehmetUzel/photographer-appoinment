from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Shoot_Plan
from django.forms import fields
from django.utils.translation import gettext_lazy as _

class DateInput(forms.DateInput):
    input_type = 'date'

class ShootPlanForm(forms.ModelForm):
    birth_date = forms.DateField(
        input_formats=["%d/%m/%Y"],
        widget=DateInput(attrs={'placeholder':'dd/mm/yyyy', 'min':'1997/01/01', 'max':'2030/12/31','class': 'datepicker'}, format="%d/%m/%Y"),
    )
    class Meta:
        model=Shoot_Plan
        fields = ["shoot_type","album_type","num_of_concept","payment_choice","birth_date"]
        labels = {
            'shoot_type': _('Shoot Type'),
            'album_type': _('Album Type'),
            'num_of_concept': _('Number of Concept'),
            'birth_date': _('Birth Date of Child'),
            'payment_choice': _('Payment Type'),
        }
