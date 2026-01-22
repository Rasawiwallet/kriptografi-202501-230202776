# Laporan Praktikum Kriptografi
Minggu ke-: 15
Topik: [Proyek Kelompok – TinyCoin ERC20]  
Nama: [Ramzi Selpora Widiyanto]  
NIM: [230202776]  
Kelas: [5IKKA]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:
1. Mengembangkan proyek sederhana berbasis algoritma kriptografi.
2. Mendokumentasikan proses implementasi proyek ke dalam repository Git.
3. Menyusun laporan teknis hasil proyek akhir.

---

## 2. Dasar Teori
ERC-20 merupakan standar token pada blockchain Ethereum yang mendefinisikan aturan dan fungsi dasar agar sebuah token dapat beroperasi secara kompatibel dengan berbagai wallet aplikasi terdesentralisasi dan exchange TinyCoin ERC-20 adalah implementasi token sederhana yang mengikuti standar ini untuk tujuan pembelajaran sehingga pengguna dapat memahami bagaimana aset digital diciptakan dikelola dan dipindahkan tanpa otoritas terpusat.

Standar ERC-20 menyediakan fungsi inti seperti pengecekan saldo transfer token serta mekanisme persetujuan penggunaan token oleh pihak lain Dengan mengikuti standar ini TinyCoin dapat berinteraksi dengan ekosistem Ethereum secara luas Setiap transaksi TinyCoin diproses melalui smart contract dan divalidasi oleh jaringan Ethereum sehingga bersifat transparan aman dan tercatat permanen di blockchain.

Meskipun mudah diimplementasikan keamanan TinyCoin ERC-20 sangat bergantung pada kualitas smart contract Kesalahan logika atau bug dapat menimbulkan risiko Oleh karena itu praktik seperti penggunaan library standar pengujian di testnet dan audit kode sangat penting untuk memastikan token berjalan dengan aman dan andal.

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)

---

## 4. Langkah Percobaan
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
