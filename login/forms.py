import self as self
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField


class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name']


class CreateUserForm(UserCreationForm):
    email = forms.EmailInput()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2', ]

