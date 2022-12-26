from django.urls import path, include
from .views import *

urlpatterns = [
    
    path('', dashboard, name='dashboard'),
    path('buku/', buku, name='tabel_buku'),
    path('tambah_buku/tambah', tambah_buku, name='tambah_buku'),
    path('buku/lihat/<str:id>', lihat_buku, name='lihat_buku'),
    path('buku/edit/<str:id>', edit_buku, name='edit_buku'),
    path('buku/hapus/<str:id>', hapus_buku, name='hapus_buku'),
    
    path('users/', users, name='tabel_user'),
]