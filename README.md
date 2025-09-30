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
2. Menambahkan Arsip Surat
   <img width="1919" height="928" alt="Cuplikan layar 2025-09-30 154340" src="https://github.com/user-attachments/assets/c6e4dfda-e9ae-4144-87b0-84ba4e49b845" />
3. Mencari Arsip Surat
   <img width="1919" height="927" alt="Cuplikan layar 2025-09-30 154306" src="https://github.com/user-attachments/assets/36568221-f6e9-4125-b6b8-6807e56fefa5" />
4. Melihat isi surat
   <img width="1919" height="926" alt="Cuplikan layar 2025-09-30 154405" src="https://github.com/user-attachments/assets/787dca22-d44c-4f65-90b5-eb111c16c171" />
5. Mengunduh Arsip
   <img width="1919" height="933" alt="Cuplikan layar 2025-09-30 154424" src="https://github.com/user-attachments/assets/ddac6251-eb8e-4126-8215-89d877388a2a" />
6. Menghapus Arsip
   <img width="1919" height="930" alt="Cuplikan layar 2025-09-30 154443" src="https://github.com/user-attachments/assets/5d71fb13-3747-4856-855a-1b4f64c7f489" />
   <img width="1919" height="926" alt="Cuplikan layar 2025-09-30 154454" src="https://github.com/user-attachments/assets/c208443f-fda7-4c65-abae-12daf3943e85" />
7. Menampilkan halaman kategori
   <img width="1919" height="929" alt="Cuplikan layar 2025-09-30 154505" src="https://github.com/user-attachments/assets/25f44ace-2535-421b-942c-fa87bcdac24a" />
8. Menambahkan Kategori
   <img width="1919" height="928" alt="Cuplikan layar 2025-09-30 154546" src="https://github.com/user-attachments/assets/3689a0b7-8cba-4442-9733-822f7f7cce0b" />
   <img width="1919" height="930" alt="Cuplikan layar 2025-09-30 154600" src="https://github.com/user-attachments/assets/b134ddce-63b3-42ad-84ed-2c4eda6e99b7" />
9. Menghapus kategori
    <img width="1919" height="927" alt="Cuplikan layar 2025-09-30 154624" src="https://github.com/user-attachments/assets/15ddf153-cebf-4357-ab06-21fb02055b9b" />






 



