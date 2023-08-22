from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms. EmailField()

    class Meta: #specify configurations of the model
        model = User
        fields = ['username', 'email', 'password1', 'password2'] #fields shown in the form
    

class DonateForm(UserCreationForm):
    email = forms. EmailField()

    class Meta: #specify configurations of the model
        model = User
        fields = ['username', 'email', 'password1', 'password2'] #fields shown in the form