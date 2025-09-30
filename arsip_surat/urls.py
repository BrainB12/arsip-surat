# arsip_surat/urls.py
from django.urls import path
from . import views
from .views import ArsipSuratListView, KategoriListView

urlpatterns = [
    # Halaman Utama (Langkah 1)
    path('', ArsipSuratListView.as_view(), name='halaman_utama'),
    
    # Tambah Surat (Langkah 2)
    path('arsip/tambah/', views.arsipkan_surat, name='arsipkan_surat'),
    
    # Hapus Surat (Langkah 3)
    path('arsip/hapus/<int:pk>/', views.hapus_surat, name='hapus_surat'),
    
    # Lihat Surat (Langkah 4)
    path('arsip/lihat/<int:pk>/', views.lihat_surat, name='lihat_surat'),
    
    # Unduh Surat (Langkah 1 & 4)
    path('arsip/unduh/<int:pk>/', views.unduh_surat, name='unduh_surat'),
    
    # Kategori (Langkah 5 & 6)
    path('kategori/', KategoriListView.as_view(), name='kategori_list'),
    path('kategori/tambah/', views.kategori_form, name='kategori_tambah'),
    path('kategori/edit/<int:pk>/', views.kategori_form, name='kategori_edit'),
    path('kategori/hapus/<int:pk>/', views.kategori_hapus, name='kategori_hapus'),
    
    # About (Langkah 7)
    path('about/', views.about, name='about'),
]