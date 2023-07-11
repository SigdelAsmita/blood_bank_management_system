from django.shortcuts import render 
from .models import *
from users.models import *

#handle routes

def home(request):
    context ={
        'posts': BankPost.objects.all()
    }
    return render(request, 'bank/home.html',context)

def about(request):
    return render (request, 'bank/about.html', {'title': 'About'})

