# Laporan Praktikum Kriptografi
Minggu ke-: 7  
Topik: [Diffie-Hellman Key Exchange]  
Nama: [Ramzi Selpora Widiyanto]  
NIM: [230202776]  
Kelas: [5 IKKA]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:
1. Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).

---

## 2. Dasar Teori
Diffie–Hellman Key Exchange (DHKE) adalah sebuah protokol kriptografi yang memungkinkan dua pihak bertukar secret key melalui kanal komunikasi yang tidak aman tanpa perlu saling berbagi kunci sebelumnya. Inti dari protokol ini adalah pemanfaatan operasi matematika pada aritmetika modulo, khususnya konsep discrete logarithm problem (DLP) yang sulit dipecahkan. Dua pihak sepakat memilih sebuah bilangan prima besar 
p dan sebuah generator g. Masing-masing pihak kemudian memilih bilangan rahasia secara acak, melakukan perpangkatan g^a mod p dan g^b mod p, lalu bertukar hasil tersebut secara publik.

Keamanan DHKE terletak pada fakta bahwa meskipun nilai publik 
g^amod p dan g^bmod dapat dilihat oleh pihak lain, menghitung nilai rahasia a atau b dari informasi itu sangat sulit karena masalah DLP. Setelah pertukaran nilai publik, kedua pihak dapat menghitung shared secret yang sama yaitu g^abmod  p, tetapi pihak luar tidak bisa mendapatkannya secara praktis. Dengan kunci bersama ini, kedua pihak dapat melakukan enkripsi simetris dengan aman.

Meski aman dari penyadapan pasif, Diffie–Hellman rentan terhadap serangan man-in-the-middle jika tidak digabungkan dengan autentikasi, misalnya sertifikat digital atau tanda tangan digital. Karena itu, di protokol modern seperti TLS, DH biasanya digunakan bersama mekanisme autentikasi untuk memastikan bahwa kunci yang dinegosiasikan benar-benar berasal dari pihak yang sah.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan

1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.

---

## 5. Source Code

```python

```


---

## 6. Hasil dan Pembahasan

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1:

- Pertanyaan 2:  
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
