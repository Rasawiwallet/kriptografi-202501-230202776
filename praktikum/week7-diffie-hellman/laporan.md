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

1. Membuat file `diffie_hellman.py` di folder `praktikum/week7-diffie-hellman/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python diffie_hellman.py`.

---

## 5. Source Code

```python
import random

# parameter umum (disepakati publik)
p = 23  # bilangan prima
g = 5   # generator

# private key masing-masing pihak
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob

# public key
A = pow(g, a, p)
B = pow(g, b, p)

# exchange public key
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("Kunci bersama Alice :", shared_secret_A)
print("Kunci bersama Bob   :", shared_secret_B)
```


---

## 6. Hasil dan Pembahasan

![Hasil DIFFIE HELLMAN](screenshots/hasil_output_diffiehellman.png)


---

## 7. Jawaban Pertanyaan
 
- Pertanyaan 1:
Diffie-Hellman aman di saluran publik karena menggunakan masalah "discrete logarithm" yang sangat sulit dipecahkan. Dua pihak bertukar nilai publik seperti g^a mod p dan g^b mod p. Walaupun penyadap melihat nilai tersebut, dia tidak bisa menghitung kunci rahasia g^(ab) mod p tanpa mengetahui nilai a atau b, dan mencari nilai itu secara langsung hampir mustahil untuk bilangan besar.
- Pertanyaan 2:  
Kelemahan utamanya adalah tidak ada autentikasi. Diffie-Hellman hanya menghasilkan kunci bersama, tetapi tidak memverifikasi identitas lawan komunikasi. Karena itu, protokol ini rentan terhadap serangan Man-in-the-Middle (MITM), di mana penyerang bisa menyisipkan diri dan membuat dua kunci berbeda dengan masing-masing pihak.
- Pertanyaan 3:
Untuk mencegah MITM, Diffie-Hellman harus digabung dengan autentikasi, misalnya:
-Menggunakan tanda tangan digital (contoh: RSA atau ECDSA) untuk menandatangani nilai pertukaran kunci.
-Menggunakan sertifikat digital (PKI), seperti pada protokol TLS.
-Menggunakan metode PAKE (Password-Authenticated Key Exchange) agar kedua pihak saling memverifikasi menggunakan password bersama.

---

## 8. Kesimpulan
Diffie-Hellman adalah protokol pertukaran kunci yang memungkinkan dua pihak membentuk kunci rahasia bersama meskipun berkomunikasi melalui saluran publik. Keamanannya bergantung pada sulitnya memecahkan masalah logaritma diskret, sehingga penyadap tidak dapat memperoleh kunci rahasia dari nilai publik yang dipertukarkan. Namun, protokol Diffie-Hellman murni tidak menyediakan autentikasi, sehingga rentan terhadap serangan Man-in-the-Middle. Untuk membuatnya aman, Diffie-Hellman harus dikombinasikan dengan mekanisme autentikasi seperti tanda tangan digital atau sertifikat.

---

## 9. Daftar Pustaka
  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.

---

## 10. Commit Log

```
commit week7-diffie-hellman
Author: Ramzi Selpora Widiyanto <rasawi46rsw@gmail.com>
Date:   2025-11-17

    week7-diffie-hellman: Diffie Hellman Key Exchange
```
