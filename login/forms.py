import self as self
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField


class CreateUserForm(UserCreationForm):
    email = forms.EmailInput()

    class Meta:
        model = User
        fields = ['email','first_name', 'last_name', 'password1','password2', ]


class LoginUser(AuthenticationForm):
    #email = forms.EmailInput(label=("Email address"),widget=forms.EmailInput(attrs={'autofocus': True}))
    username = UsernameField(
        label='Email',
        widget=forms.TextInput(attrs={'autofocus': True}))