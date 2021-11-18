from django import forms


class EditProfileForm(forms.Form):
    ID = forms.CharField(label='Enter an ID:', max_length=200)
    location = forms.CharField(label='Enter an Office Location:', max_length=200)
    phone = forms.CharField(label='Enter an Office Phone Number:', max_length=20)
    hours = forms.CharField(label='Enter Office Hours:', max_length=200)
