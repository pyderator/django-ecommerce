from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



# REF: https://www.crunchydata.com/blog/building-a-user-registration-form-with-djangos-built-in-authentication
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='First Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')

    class Meta:
        model = User
        fields = ["first_name", "last_name","username", "password1", "password2",  "email"]
