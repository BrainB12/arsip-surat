# [JUDUL] Aplikasi Arsip Surat Kelurahan Karangduren

## Tujuan Aplikasi
Aplikasi ini dibuat untuk memenuhi kebutuhan Kelurahan Karangduren dalam mengarsipkan surat-surat resmi mereka dalam format PDF.

## Fitur Utama
1.  **Arsip Surat:** Melakukan operasi CRUD (Create, Read, Update, Delete) pada data surat dan file PDF yang diunggah.
2.  **Pencarian Cepat:** Mencari surat berdasarkan judul.
3.  **Pengelolaan Kategori:** Mengelola data kategori surat (Undangan, Pengumuman, dll.) yang digunakan untuk pengarsipan.
4.  **Fungsionalitas File:** Dapat mengunggah file PDF, melihat pratinjau, dan mengunduhnya.

## Cara Menjalankan Aplikasi
1.  **Klon Repository:** `git clone [link repo Anda]`
2.  **Setup Environment:**
    * Buat dan aktifkan virtual environment Python.
    * Install dependensi: `pip install django mysqlclient`
3.  **Setup Database:**
    * Pastikan MySQL Server berjalan.
    * Buat database kosong (`arsip_surat_db`).
    * Import file `arsip_surat_db.sql` ke database tersebut.
4.  **Konfigurasi Django:**
    * Edit `project_arsip/settings.py` dengan kredensial database MySQL Anda.
5.  **Jalankan Server:** `python manage.py runserver`

## Screenshot
1. Menampilkan halaman Arsip
   <img width="1919" height="927" alt="Cuplikan layar 2025-09-30 154319" src="https://github.com/user-attachments/assets/8e6aa244-f550-4561-a025-fe8c24c3a2e5" />
