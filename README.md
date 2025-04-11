# 🖼️ Auto Image to WebP Converter with Watchdog

Sebuah script Python yang secara otomatis mengkonversi file gambar (`.jpg`, `.jpeg`, `.png`) menjadi format `.webp` saat file baru ditambahkan ke folder tertentu. Gambar hasil konversi disimpan di subfolder `output/`, dan file asli akan dihapus setelah berhasil dikonversi.

## 🚀 Fitur

- Mendeteksi file baru secara **real-time** menggunakan `watchdog`.
- Mengkonversi gambar ke `.webp` dengan kualitas tinggi.
- Secara otomatis menghapus file asli setelah konversi.
- Dukungan file: `.jpg`, `.jpeg`, `.png` (case-insensitive).

## 📁 Struktur Folder


## ⚙️ Cara Pakai

1. **Clone/download** repositori ini.
2. Pastikan kamu sudah menginstall dependensi:
    ```bash
    pip install pillow watchdog
    ```
3. Jalankan script:
    ```bash
    python app.py
    ```
4. **Tambahkan gambar** (.jpg/.jpeg/.png) ke folder `images/`.
5. File akan otomatis:
    - Dikonversi ke `images/output/nama_file.webp`
    - File aslinya dihapus setelah sukses

## 🧠 Catatan

- File hasil akan disimpan di: `images/output/`
- Jangan taruh gambar baru di dalam folder `output`, karena folder ini tidak dimonitor.
- Hindari memberi nama file yang sama dengan file `.webp` yang sudah ada, agar tidak tertimpa.

## 📦 Dependencies

- [Pillow](https://pillow.readthedocs.io/)
- [Watchdog](https://python-watchdog.readthedocs.io/)

## 👨‍💻 Author

Made with ❤️ by Ilham

