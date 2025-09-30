# arsip_surat/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import ListView
from django.contrib import messages
from django.db.models import Q

from .models import Surat, Kategori
from .forms import SuratForm, KategoriForm

import os
from django.conf import settings

# --- View Tambahan untuk About (Langkah 7) ---
def about(request):
    # Data baru sesuai permintaan Anda
    context = {
        'nama': 'BRIAN IGHTIARO MASYURA ALIFIANTO',
        'nim': '2331730143', 
        'tanggal_pembuatan': '29 September 2025', 
        # Pastikan Anda memiliki 'foto.jpg' di folder media/
        'foto_url': settings.MEDIA_URL + 'foto.jpg' 
    }
    return render(request, 'arsip_surat/about.html', context)


# --- Halaman Utama / Arsip Surat (Langkah 1) ---
class ArsipSuratListView(ListView):
    model = Surat
    template_name = 'arsip_surat/halaman_utama.html'
    context_object_name = 'daftar_surat'
    ordering = ['-waktu_pengarsipan'] 

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        
        # Ketentuan: Pencarian berdasarkan Judul Surat yang mengandung kata yang dicari [cite: 37, 41]
        if query:
            queryset = queryset.filter(Q(judul__icontains=query))
        return queryset

# --- Tambah/Ubah Arsip Surat (Langkah 2) ---
def arsipkan_surat(request):
    if request.method == 'POST':
        form = SuratForm(request.POST, request.FILES)
        if form.is_valid():
            kategori_nama = form.cleaned_data.pop('kategori_nama')
            
            # Ambil atau buat objek Kategori berdasarkan nama 
            try:
                kategori_obj = Kategori.objects.get(nama=kategori_nama)
            except Kategori.DoesNotExist:
                # Membuat kategori jika belum ada (meski seharusnya sudah dibuat di Langkah 5/6)
                kategori_obj = Kategori.objects.create(nama=kategori_nama)

            surat = form.save(commit=False)
            surat.kategori = kategori_obj
            surat.save()

            # Ketentuan: Munculkan pesan "Data berhasil disimpan" 
            messages.success(request, "Data berhasil disimpan")
            return redirect('halaman_utama')
    else:
        form = SuratForm()
    
    context = {'form': form, 'page_title': 'Form Arsip Surat'}
    return render(request, 'arsip_surat/form_surat.html', context)

# --- Hapus Surat (Langkah 3) ---
def hapus_surat(request, pk):
    surat = get_object_or_404(Surat, pk=pk)

    # Menangani konfirmasi penghapusan (mengacu pada Ketentuan Langkah 3)
    if request.method == 'POST':
        # Ketentuan: Hapus baik dari database maupun dari tabel (dan file) [cite: 41, 46]
        
        # 1. Hapus file PDF dari sistem file
        file_path = os.path.join(settings.MEDIA_ROOT, surat.file_pdf.name)
        if os.path.exists(file_path):
            os.remove(file_path)

        # 2. Hapus data dari database
        surat.delete()
        messages.success(request, f"Surat '{surat.judul}' berhasil dihapus.")
        return redirect('halaman_utama')
    
    # Menampilkan peringatan sebelum menghapus 
    context = {'surat': surat}
    return render(request, 'arsip_surat/konfirmasi_hapus.html', context)

# --- Lihat Detail Surat (Langkah 4) ---
def lihat_surat(request, pk):
    surat = get_object_or_404(Surat, pk=pk)
    context = {'surat': surat}
    return render(request, 'arsip_surat/lihat_surat.html', context)

# --- Unduh Surat (Langkah 1 & 4) ---
def unduh_surat(request, pk):
    surat = get_object_or_404(Surat, pk=pk)
    
    file_path = os.path.join(settings.MEDIA_ROOT, surat.file_pdf.name)
    
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            # Ketentuan: file PDF akan didownload/simpan [cite: 41, 46]
            response['Content-Disposition'] = f'attachment; filename="{surat.nomor_surat}_{surat.judul}.pdf"'
            return response
    
    raise Http404("File PDF tidak ditemukan.")

# --- Kategori (Langkah 5 & 6) ---
class KategoriListView(ListView):
    model = Kategori
    template_name = 'arsip_surat/kategori_list.html'
    context_object_name = 'daftar_kategori'

def kategori_form(request, pk=None):
    if pk:
        kategori = get_object_or_404(Kategori, pk=pk)
    else:
        kategori = None
        
    if request.method == 'POST':
        form = KategoriForm(request.POST, instance=kategori)
        if form.is_valid():
            form.save()
            messages.success(request, "Kategori berhasil disimpan.")
            return redirect('kategori_list')
    else:
        form = KategoriForm(instance=kategori)
        
    context = {'form': form, 'kategori': kategori}
    return render(request, 'arsip_surat/kategori_form.html', context)

def kategori_hapus(request, pk):
    kategori = get_object_or_404(Kategori, pk=pk)
    # Cek apakah kategori digunakan oleh surat lain
    if Surat.objects.filter(kategori=kategori).exists():
        messages.error(request, "Kategori tidak dapat dihapus karena masih digunakan oleh surat.")
        return redirect('kategori_list')

    kategori.delete()
    messages.success(request, "Kategori berhasil dihapus.")
    return redirect('kategori_list')