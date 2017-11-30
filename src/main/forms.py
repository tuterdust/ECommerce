from django import forms
from django.core.validators import MinLengthValidator

class SignUpForm(forms.Form):
    firstname = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=25, validators=[MinLengthValidator(8)])
    address = forms.CharField(max_length=2000)
