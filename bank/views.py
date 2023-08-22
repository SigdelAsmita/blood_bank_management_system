from django.shortcuts import render 
from .models import *
from users.models import *
from django.db.models import Q

#handle routes

def home(request):
    context ={
        'posts': BankPost.objects.all()
    }
    return render(request, 'bank/home.html',context)

def about(request):
    return render (request, 'bank/about.html', {'title': 'About'})

def bloodbank(request):
    cards=[]
    blood_bank_list=BloodBank.objects.all()
    return render(request, 'bank/bloodbank.html', context={"blood_bank":blood_bank_list, 'title':'BloodBanks'})

def search(request):
    if request.method =="POST":
        searched = request.POST['searched']
        banks = BloodBank.objects.filter(Q(blood_bank_name__icontains= searched)).distinct()
        return render (request, 'bank/search.html', context={'title': 'Search','searched':searched, "bank": banks})
    else:
        return render (request, 'bank/search.html', {'title': 'Search'})

def donate(request):
    return render (request, 'bank/donate.html', {'title': 'Donate'})

def request(request):
    return render (request, 'bank/request.html', {'title': 'Request'})