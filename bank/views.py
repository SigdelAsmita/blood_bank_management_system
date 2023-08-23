from django.shortcuts import render 
from .models import *
from users.models import *
from django.db.models import Q
from django.shortcuts import render, redirect


#handle routes

def home(request):
    context ={
        'posts': BankPost.objects.all()
    }
    return render(request, 'bank/home.html',context=context)

def about(request):
    return render (request, 'bank/about.html', {'title': 'About'})

def bloodbank(request):
    cards=[]
    blood_bank_list=BloodBank.objects.all()
    return render(request, 'bank/bloodbank.html', context={"blood_bank":blood_bank_list, 'title':'BloodBanks'})


def event(request):
    cards=[]
    event_list=Events.objects.all()
    return render(request, 'bank/events.html', context={"event":event_list, 'title':'Events'})

def search(request):
    if request.method =="POST":
        searched = request.POST['searched']
        banks = BloodBank.objects.filter(Q(blood_bank_name__icontains= searched)).distinct()
        return render (request, 'bank/search.html', context={'title': 'Search','searched':searched, "bank": banks})
    else:
        return render (request, 'bank/search.html', {'title': 'Search'})

def donate(request):
    if request.method =='POST':
        form = DonateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('thanks')
    else:
            form = DonateForm()

    return render(request, "donate.html", {'form': form})

def request(request):
    if request.method =='POST':
        form = RequestForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('requestProcess')
    else:
            form = RequestForm()

    return render(request, "request.html", {'form': form})

def thanks(request):
    return render (request, 'bank/thanks.html', {'title': 'Thanks'})

def requestProcess(request):
    return render (request, 'bank/requestProcess.html', {'title': 'requestProcess'})