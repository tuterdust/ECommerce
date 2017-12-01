from django import forms
from django.core.validators import MinLengthValidator

class ProductDetailForm(forms.Form):
    amount = forms.IntegerField()

class SignInForm(forms.Form):
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=25, validators=[MinLengthValidator(8)])

class SignUpForm(forms.Form):
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=25, validators=[MinLengthValidator(8)])
    confirm_password = forms.CharField(max_length=25, validators=[MinLengthValidator(8)])
    firstname = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    address = forms.CharField(max_length=2000)
