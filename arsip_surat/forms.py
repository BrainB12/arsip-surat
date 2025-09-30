# arsip_surat/forms.py
from django import forms
from .models import Surat, Kategori
from django.core.exceptions import ValidationError

class SuratForm(forms.ModelForm):
    # Pilihan Kategori sesuai ketentuan: 'Undangan', 'Pengumuman', 'Nota Dinas', 'Pemberitahuan' 
    KATEGORI_CHOICES = [
        ('Undangan', 'Undangan'),
        ('Pengumuman', 'Pengumuman'),
        ('Nota Dinas', 'Nota Dinas'),
        ('Pemberitahuan', 'Pemberitahuan'),
    ]

    # Field kategori_nama digunakan di form dan di-mapping ke objek Kategori di view
    kategori_nama = forms.ChoiceField(
        choices=KATEGORI_CHOICES,
        label="Pilih Kategori",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Surat
        fields = ['nomor_surat', 'judul', 'file_pdf']
        widgets = {
            'nomor_surat': forms.TextInput(attrs={'class': 'form-control'}),
            'judul': forms.TextInput(attrs={'class': 'form-control'}),
            'file_pdf': forms.FileInput(attrs={'class': 'form-control'}),
        }
        
    def clean_file_pdf(self):
        # Ketentuan: File harus berupa PDF 
        uploaded_file = self.cleaned_data.get('file_pdf')
        if uploaded_file and not uploaded_file.name.lower().endswith('.pdf'):
            raise ValidationError("File yang diunggah harus berformat PDF.")
        return uploaded_file

class KategoriForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ['nama']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
        }