from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms. EmailField()

    class Meta: #specify configurations of the model
        model = User
        fields = ['username', 'email', 'password1', 'password2'] #fields shown in the form
    

# class DonateForm(UserCreationForm):
#     email = forms. EmailField()

#     class Meta: #specify configurations of the model
#         model = User
#         fields = ['username', 'email', 'password1', 'password2'] #fields shown in the form


class DonateForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    address = forms.CharField(required=True)
    blood_group_choices = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    blood_group = forms.ChoiceField(choices= blood_group_choices)
    medication = forms.CharField(required=False)
    class Meta:
        model = ''
        fields = ['name', 'address', 'blood_group','medication']

class RequestForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    address = forms.CharField(required=True)
    blood_group_choices = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    blood_group = forms.ChoiceField(choices= blood_group_choices, required = True)
    medication = forms.CharField(required=False)
    class Meta:
        model = 'request_form'
        fields = ['name', 'address', 'blood_group','medication']
