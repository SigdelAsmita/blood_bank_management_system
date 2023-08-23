from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Donate
from .models import Request

class UserRegisterForm(UserCreationForm):
    email = forms. EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] #fields shown in the form
    
class DonateForm(forms.ModelForm):
    class Meta:
        model = Donate 
        fields = ['name', 'address', 'blood_group', 'medication']
    widgets = {
        'address': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px; height: 30px;'}),
    }
    
class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['name', 'address', 'blood_group', 'medication']

