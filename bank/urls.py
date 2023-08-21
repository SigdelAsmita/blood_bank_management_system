from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='bank-home'),
    path('about/', views.about, name ='bank-about'),
    path('search', views.search, name ='bank-search'),
    path('bloodbanks/', views.bloodbank, name ='bank-bloodbank'),
]
