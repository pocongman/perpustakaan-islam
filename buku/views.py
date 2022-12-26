from re import template
import re
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
import requests
from django.http import HttpResponse

from .models import Buku, Kategori

# Create your views here.

def is_administrator(user):
    if user.groups.filter(name='Administrator').exists():
        return True
    else:
        return False

@login_required
def dashboard(request):
    if request.user.groups.filter(name='Administrator').exists():
        request.session['is_administrator'] = 'administrator'
       
    template_name = "back/dashboard.html"
    context = {
        'title':'Dashboard'
    }   
    return render(request, template_name, context)

@login_required

def buku(request) :
    URL = "https://buku-islam-api.vercel.app/books/category/ushul-fiqih"
    book = requests.get(url=URL)
    data = book.json()
    
    context ={
        "data" : data
    }
    return render(request, 'back/tabel_buku.html', context)
#def buku(request):
#    template_name = "back/tabel_buku.html"
#    buku = Buku.objects.all()
#    print(buku)
#    context = {
#        'title':'Data Buku',
#        'buku' : buku,
#    }
#    return render(request, template_name, context)

@login_required
def tambah_buku(request):
    template_name = "back/tambah_buku.html"
    kategori = Kategori.objects.all()
    print(kategori)
    if request.method == "POST":
        judul = request.POST.get('judul')
        pengarang = request.POST.get('pengarang')
        penerbit = request.POST.get('penerbit')
        halaman = request.POST.get('halaman')
        kategori = request.POST.get('kategori')
        kat = Kategori.objects.get(nama=kategori)
        Buku.objects.create(
            judul = judul,
            pengarang = pengarang,
            penerbit = penerbit,
            halaman = halaman,
            kategori = kat,
        )
        return redirect(buku)
    context = {
        'title': 'Tambah Buku',
        'kategori' : kategori,
    }
    return render(request, template_name, context)

@login_required
def lihat_buku(request, id):
    template_name = "back/lihat_buku.html"
    buku = Buku.objects.get(id=id)
    context = {
        'title' : 'Detail Buku',
        'buku' : buku,
    }
    return render(request, template_name, context)

@login_required
def edit_buku(request, id):
    template_name = "back/edit_buku.html"
    a = Buku.objects.get(id=id)
    kategori = Kategori.objects.all()
    if request.method == "POST":
        judul = request.POST.get("judul")
        pengarang = request.POST.get("pengarang")
        penerbit = request.POST.get("penerbit")
        halaman = request.POST.get("halaman")
        kategori = request.POST.get("kategori")
        kat = Kategori.objects.get(nama=kategori)
        a.judul = judul
        a.pengarang = pengarang
        a.penerbit = penerbit
        a.halaman = halaman
        a.kategori = kat
        a.save()
        return redirect(buku)
    context = {
        'title' : 'Edit Buku',
        'buku' : a,
        'kategori' : kategori
    }
    return render(request, template_name, context)

@login_required
def hapus_buku(request, id):
    Buku.objects.get(id=id).delete()
    return redirect(buku)

@login_required
@user_passes_test(is_administrator)
def users(request):
    template_name = "back/tabel_user.html"
    users = User.objects.all()
    context = {
        'title':'tabel user',
        'users' : users
    }
    return render(request, template_name, context)