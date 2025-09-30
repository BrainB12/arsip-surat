# arsip_surat/models.py
from django.db import models

# Ketentuan Khusus: ID Kategori harus otomatis [cite: 51]
class Kategori(models.Model):
    # ID otomatis (pk) sudah dibuat default oleh Django
    nama = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nama

class Surat(models.Model):
    # ID Surat (pk) otomatis dibuat oleh Django

    # Kategori Surat (Foreign Key)
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True, verbose_name="Kategori Surat")

    nomor_surat = models.CharField(max_length=100, unique=True)
    judul = models.CharField(max_length=255)

    # File yang diupload harus berupa PDF. Disimpan di folder media/surat/
    file_pdf = models.FileField(upload_to='surat/')
    
    # Waktu Pengarsipan (otomatis)
    waktu_pengarsipan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul