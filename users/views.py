from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import DonateForm
from .forms import RequestForm
# decorators add functionalities to existing function
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid(): 
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You can now login!')
            form.save()
            return redirect ('login')
        
    else:
        form = UserRegisterForm()
    
    return render(request,'users/register.html',{'form':form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


# def donate(request):
#     if request.method == 'POST':
#         form = DonateForm(request.POST)
#         if form.is_valid(): 
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Your donation request has been submitted.')
#             form.save()
#             return redirect ('thanks')       
#     else:
#         form = DonateForm()
#     return render(request,'users/donate.html',{'form':form})

# @login_required
# def profile(request):
#     return render(request, 'users/profile.html')


# def request(request):
#     if request.method == 'POST':
#         form = RequestForm(request.POST)
#         if form.is_valid(): 
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Your request has been submitted.')
#             form.save()
#             return redirect ('requestProcess')
#     else:
#         form = DonateForm()
#     return render(request,'users/request.html',{'form':form})


# @login_required
# def profile(request):
#     return render(request, 'users/profile.html')