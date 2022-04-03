from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User,Address
from django.forms import fields
from django.utils.translation import gettext_lazy as _

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["email", "phone","password1", "password2"]

class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ["password1"]
        
class PartialProfileForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ["name","city","district","neighbourhood","street_name","building_num","flat_num","address_instructions"]
        labels = {
            'name': _('Address Name'),
            'city': _('Şehir'),
        }

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = '__all__'

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'

class PartialUserProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["phone","email"]
        