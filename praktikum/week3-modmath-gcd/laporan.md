# Laporan Praktikum Kriptografi
Minggu ke-: 3
Topik: [Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit)]  
Nama: [Ramzi Selpora Widiyanto]  
NIM: [230202776]  
Kelas: [5IKKA]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:
1. Menyelesaikan operasi aritmetika modular.
2. Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
3. Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.
---

## 2. Dasar Teori
Aritmetika Modular adalah sistem operasi matematika yang bekerja berdasarkan sisa hasil bagi suatu bilangan terhadap modulus tertentu. Dalam bentuk umum, dua bilangan a dan b dikatakan kongruen terhadap modulus n jika 
a≡b(modn), artinya n membagi selisih (a−b). Aritmetika ini digunakan dalam berbagai bidang seperti kriptografi, teori bilangan, dan komputasi karena memungkinkan perhitungan besar menjadi lebih efisien dengan hanya memperhatikan sisanya.

GCD (Greatest Common Divisor) atau FPB (Faktor Persekutuan Terbesar) dari dua bilangan adalah bilangan bulat terbesar yang dapat membagi keduanya tanpa sisa. Konsep GCD erat kaitannya dengan aritmetika modular, misalnya dalam mencari inverse modulo, di mana invers suatu bilangan a terhadap modulus n hanya ada jika gcd(a,n)=1. Perhitungan GCD umumnya dilakukan dengan algoritma Euclidean, yang sangat efisien dan sering digunakan dalam sistem kriptografi seperti RSA.

Bilangan Prima adalah bilangan yang hanya memiliki dua faktor, yaitu 1 dan dirinya sendiri. Bilangan prima menjadi dasar dari banyak algoritma dalam keamanan komputer karena sifat faktorisasi yang sulit (contohnya dalam RSA dan Diffie-Hellman). Salah satu aplikasi lanjutannya adalah logaritma diskrit, yaitu mencari eksponen x dalam persamaan ax≡b(modp), yang merupakan masalah sulit untuk diselesaikan ketika p adalah bilangan prima besar—menjadi dasar keamanan banyak sistem kriptografi modern.
---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
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
