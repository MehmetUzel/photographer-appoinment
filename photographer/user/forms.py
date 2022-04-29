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
            'first_name': _('İsim'),
            'last_name': _('Soyisim'),
            'email': _('E-mail'),
            'phone': _('Telefon'),
            'password1': _('Parola'),
            'password2': _('Parola Onayı'),
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
            'name': _('Adres Adı'),
            'city': _('İl'),
            'district': _('İlçe'),
            'neighbourhood': _('Mahalle'),
            'street_name': _('Sokak'),
            'building_num': _('Apartman No'),
            'flat_num': _('Daire No'),
            'address_instructions': _('Adres Tarifi'),
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
            'first_name': _('İsim'),
            'last_name': _('Soyisim'),
            'email': _('E-mail'),
            'phone': _('Telefon'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields["slug"].disabled = True
        # Or to set READONLY
        self.fields["email"].widget.attrs["readonly"] = True
        