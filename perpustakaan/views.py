from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.http import HttpResponse
import requests

from buku.models import Buku

def home(request):
    template_name = 'front/home.html'
    context = {
        'title': 'Beranda'
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'front/about.html'
    context = {
        'title': 'Tentang Kami'
    }
    return render(request, template_name, context)

# def books(request):
#     template_name = 'front/books.html'
#     buku = Buku.objects.all()
#     context = {
#         'title': 'Daftar Buku',
#         'buku' : buku
#     }
#     return render(request, template_name, context)

def books(request) :
    URL = "https://buku-islam-api.vercel.app/books/category/ushul-fiqih"
    book = requests.get(url=URL)       
    data = book.json()  
    
    context ={
        "data" : data
    }
    
    
    return render(request, 'front/books.html', context)
     

def login_view(request):
    #if request.user.is_authenticated:
       # print('loged')
       # return redirect('home')
    
    template_name = "akun/login.html"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('username benar')
            auth_login(request, user)
            return redirect('dashboard')
        else:
            print('username salah')
    
    context = {
        'title' : 'login'
    }
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('home')