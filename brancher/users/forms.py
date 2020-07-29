from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class InfluencerRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(error_messages={'required': 'Please enter your first name'})
    last_name = forms.CharField(error_messages={'required': 'Please enter your last name'})

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class CompanyRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(error_messages={'required': 'Please enter your brand name'}, label='Brand Name')

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
