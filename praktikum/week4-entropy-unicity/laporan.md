# Laporan Praktikum Kriptografi
Minggu ke-: 4
Topik: [Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)]  
Nama: [Ramzi Selpora Widiyanto ]  
NIM: [230202776]  
Kelas: [5 IKKA]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

1. Menyelesaikan perhitungan sederhana terkait entropi kunci.
2. Menggunakan teorema Euler pada contoh perhitungan modular & invers.
3. Menghitung unicity distance untuk ciphertext tertentu.
4. Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
5. Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.

---

## 2. Dasar Teori
Entropy dalam kriptografi menggambarkan tingkat ketidakpastian atau keacakan dari sebuah kunci. Semakin tinggi nilai entropi, semakin sulit bagi penyerang untuk menebak atau memprediksi kunci tersebut. Entropi diukur dalam bit, dan kunci dengan entropi n bit berarti ada 2n kemungkinan kombinasi. Misalnya, kunci 128-bit memiliki 2 ^128 kemungkinan, yang membuat serangan brute force (mencoba semua kombinasi) secara praktis mustahil dengan teknologi saat ini. Oleh karena itu, entropi menjadi ukuran utama untuk menilai kekuatan suatu sistem kriptografi terhadap penebakan kunci.

Unicity Distance adalah konsep yang menunjukkan berapa banyak data terenkripsi (ciphertext) yang dibutuhkan agar penyerang dapat secara unik menentukan kunci yang digunakan. Nilai ini bergantung pada panjang kunci dan redundansi informasi dari pesan asli. Jika ciphertext yang tersedia lebih panjang dari unicity distance, maka secara teoritis kunci dapat ditemukan dengan analisis statistik, bukan hanya brute force.

Dalam konteks evaluasi kekuatan kunci, kombinasi antara entropi tinggi dan unicity distance yang besar memastikan sistem lebih tahan terhadap serangan. Kunci dengan entropi rendah mudah ditebak, sedangkan sistem dengan unicity distance kecil dapat dipecahkan dengan sedikit ciphertext. Oleh karena itu, pemilihan panjang kunci yang memadai dan algoritma dengan distribusi keacakan yang baik sangat penting untuk menjaga keamanan kriptografi modern.
---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan

1. Membuat file masing-masing source `entropy_unicity.py` di folder `praktikum/week3-modmath-gcd/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program masing-masing source dengan perintah `entropy_unicity.py`.
---

## 5. Source Code

```python
import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")
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
