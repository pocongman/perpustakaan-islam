from django.contrib import admin
from .models import *
# Register your models here.

class BukuAdmin(admin.ModelAdmin):
    list_display = ('judul', 'pengarang', 'penerbit', 'halaman', 'kategori', 'date')

admin.site.register(Kategori)
admin.site.register(Buku, BukuAdmin)