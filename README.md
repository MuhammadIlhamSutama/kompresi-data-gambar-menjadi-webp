# 🖼️ Image Watcher & Supabase Uploader

Skrip Python ini secara otomatis:
1. Mendeteksi file gambar baru di folder `images/`,
2. Mengonversi gambar tersebut ke format `.webp` dengan ukuran dan kualitas yang diatur,
3. Mengunggah gambar ke **Supabase Storage**, dan
4. Menyimpan data metadata (nama, tanggal, jam, dan URL gambar) ke **tabel Supabase** bernama `fotos`.

---

## 🔧 Fitur Utama

- 🔄 **Pemantauan Folder**: Otomatis mendeteksi gambar baru yang ditambahkan.
- 🗜️ **Konversi ke WebP**: Mengubah format gambar menjadi `.webp` dengan kualitas dan ukuran lebih kecil.
- ☁️ **Upload ke Supabase**: Gambar dikirim ke bucket Supabase Storage.
- 🧾 **Simpan Metadata**: Informasi gambar dicatat ke dalam tabel database Supabase.

---

## 📁 Struktur Folder

```
project-folder/
│
├── images/                  # Folder tempat menambahkan gambar
│   └── output/              # Hasil konversi gambar .webp
│
├── main.py                  # Skrip utama (kode Python)
└── README.md                # Dokumentasi proyek
```

---

## 💡 Format Nama Gambar

Agar metadata dapat diambil otomatis, gambar harus dinamai dengan format seperti berikut:

```
Nama_Tanggal_Jam.jpg
Contoh: Ilham_2025-05-06_18-30-26.jpg
```

Skrip akan mengekstrak:
- **Nama**: Ilham
- **Tanggal**: 2025-05-06
- **Jam**: 18:30:26

Jika nama file tidak mengikuti format, maka data tanggal dan jam akan kosong.

---

## 🧰 Instalasi Dependensi

Sebelum menjalankan skrip, pastikan Python telah terinstal, lalu install modul yang dibutuhkan:

```bash
pip install pillow watchdog supabase
```

---

## ⚙️ Konfigurasi Supabase

Ganti kredensial di `main.py` dengan URL dan API Key dari proyek Supabase kamu:

```python
SUPABASE_URL = 'https://<project>.supabase.co'
SUPABASE_KEY = '<your-key>'
BUCKET_NAME = 'testfield'
```

### ✅ Struktur Tabel `fotos`

Pastikan kamu telah membuat tabel bernama `fotos` di Supabase dengan kolom berikut:

- `name` (text)
- `tanggal` (text)
- `jam` (text)
- `url` (text)

---

## ▶️ Menjalankan Skrip

```bash
python main.py
```

Setelah itu, cukup tambahkan gambar ke dalam folder `images/`. Gambar akan otomatis dikonversi dan diunggah.

---

## 📬 Lisensi

Proyek ini bebas digunakan untuk keperluan pribadi dan pembelajaran. Gunakan dengan bijak.
