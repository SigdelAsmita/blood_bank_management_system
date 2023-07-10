from django.shortcuts import render 
from .models import Post

#handle routes

def home(request):
    context ={
        'posts': Post.objects.all()
    }
    return render(request, 'bank/home.html',context)

def about(request):
    return render (request, 'bank/about.html', {'title': 'About'})

