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
        fields = ["first_name","last_name","email", "phone","password1", "password2"]
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'email': _('E-mail'),
            'phone': _('Phone'),
            'password1': _('Password'),
            'password2': _('Password Check'),
        }

class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ["password1"]
        labels = {
            'username': _('E-mail'),
        }
        
#Profile means Address
class PartialProfileForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ["name","city","district","neighbourhood","street_name","building_num","flat_num","address_instructions"]
        labels = {
            'name': _('Adsress Name'),
            'city': _('City'),
            'district': _('District'),
            'neighbourhood': _('Neighbourhood'),
            'street_name': _('Street'),
            'building_num': _('Building Number'),
            'flat_num': _('Flat Number'),
            'address_instructions': _('Address Instructions'),
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
        fields = ["first_name","last_name","phone","email"]
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last name'),
            'email': _('E-mail'),
            'phone': _('Phone'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields["slug"].disabled = True
        # Or to set READONLY
        self.fields["email"].widget.attrs["readonly"] = True
        