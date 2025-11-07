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
Contoh format:
1. Membuat file masing-masing source `.py` di folder `praktikum/week3-modmath-gcd/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program masing-masing source dengan perintah `.py`.
4. Program Python (src/) berisi implementasi:
~Modular arithmetic (add, sub, mul, exp).
~GCD & Euclidean Algorithm.
~Extended Euclidean & modular inverse.
~Discrete log sederhana.


---

## 5. Source Code

### 1 — Aritmetika Modular
Fungsi untuk menghitung operasi modular dasar.  
```python
def mod_add(a, b, n): return (a + b) % n
def mod_sub(a, b, n): return (a - b) % n
def mod_mul(a, b, n): return (a * b) % n
def mod_exp(base, exp, n): return pow(base, exp, n)  # eksponensiasi modular

print("7 + 5 mod 12 =", mod_add(7, 5, 12))
print("7 * 5 mod 12 =", mod_mul(7, 5, 12))
print("7^128 mod 13 =", mod_exp(7, 128, 13))
```
### 2 — GCD & Algoritma Euclidean
Fungsi GCD dengan algoritma Euclidean.  
```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("gcd(54, 24) =", gcd(54, 24))
```
### 3 — Extended Euclidean Algorithm
Tambahkan fungsi untuk mencari invers modular.  
```python
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        return None
    return x % n

print("Invers 3 mod 11 =", modinv(3, 11))  # hasil: 4
```
### 4 — Logaritma Diskrit (Discrete Log)
Simulasikan logaritma diskrit sederhana: mencari `x` sehingga `a^x ≡ b (mod n)`.  
```python
def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None

print("3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))  # hasil: 4
```

---

## 6. Hasil dan Pembahasan
## Hasil Langkah -Langkah
[Memiliki hasil 6] (screenshots/eksekusi-langkah1.png)
[Memiliki hasil 6] (screenshots/eksekusi-langkah2.png)
[Memiliki hasil 4] (screenshots/eksekusi-langkah3.png)
[Memiliki hasil 4] (screenshots/eksekusi-langkah4.png)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi 
- Pertanyaan 1:
Peran aritmetika modular dalam kriptografi modern
Aritmetika modular adalah dasar dari hampir semua sistem kriptografi modern, terutama yang berbasis pada bilangan bulat.
Dalam kriptografi, operasi seperti enkripsi, dekripsi, dan pembuatan tanda tangan digital sering dilakukan menggunakan operasi modulo (misalnya a^b mod n).
Fungsi utama aritmetika modular adalah:
Membuat hasil perhitungan tetap dalam rentang tertentu, mencegah bilangan menjadi terlalu besar.
Menyediakan struktur matematika yang sulit dibalik (misalnya mencari eksponen atau akar modulo n tidak mudah).
Contoh penerapannya: RSA, Diffie-Hellman, dan ECC semuanya bergantung pada aritmetika modular.

- Pertanyaan 2:
Pentingnya invers modular dalam algoritma kunci publik (misalnya RSA)
Invers modular digunakan untuk mengembalikan operasi enkripsi menjadi dekripsi.
Pada RSA, jika e adalah kunci publik dan d adalah kunci privat, maka:
d≡e−1 (mod φ(n))−1
Artinya d adalah invers modular dari e terhadap φ(n).
Tanpa invers modular, tidak ada cara untuk menghitung kunci privat yang bisa mendekripsi pesan yang dienkripsi.
Jadi, invers modular menjamin bahwa proses enkripsi dan dekripsi saling membatalkan secara matematis dalam sistem kunci publik.

- Pertanyaan 3:
Masalah logaritma diskrit adalah:
diberikan 
gx(pangkat)≡y (mod p) cari nilai x.
Untuk modulus besar (misalnya ratusan atau ribuan bit), tidak ada algoritma efisien yang bisa menyelesaikannya dengan cepat.
Kesulitannya berasal dari:
Pertumbuhan eksponensial dari waktu komputasi terhadap ukuran modulus.
Tidak adanya pola matematis sederhana untuk membalikkan operasi eksponen modulo.
Inilah yang membuat algoritma seperti Diffie-Hellman dan ElGamal aman — karena logaritma diskrit sangat sulit dipecahkan jika modulus cukup besar.
)
---

## 8. Kesimpulan
[Memiliki hasil 6] pada langkah 1
[Memiliki hasil 6] pada langkah 2
[Memiliki hasil 4] pada langkah 3
[Memiliki hasil 4] pada langkah 4

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
commit week3-modmath-gcd
Author: Ramzi Selpora Widiyanto <rasawi46rsw@gmail.com>
Date:   2025-11-07

    week3-modmath-gcd: Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit)
```
