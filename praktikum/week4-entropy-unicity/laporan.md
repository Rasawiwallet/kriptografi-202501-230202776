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

### 1 — Perhitungan Entropi
Gunakan rumus:  
\[
H(K) = \log_2 |K|
\]  
dengan \(|K|\) adalah ukuran ruang kunci.  

Contoh implementasi Python:  
```python
import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")
```

### 2 — Menghitung Unicity Distance
Gunakan rumus:  
\[
U = \frac{H(K)}{R \cdot \log_2 |A|}
\]  
dengan:  
- \(H(K)\): entropi kunci,  
- \(R\): redundansi bahasa (misal bahasa Inggris \(R \approx 0.75\)),  
- \(|A|\): ukuran alfabet (26 untuk A–Z).  

Contoh implementasi Python:  
```python
def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

HK = entropy(26)
print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK))
```

### 3 — Analisis Brute Force
Simulasikan waktu brute force dengan asumsi kecepatan komputer tertentu.  

```python
def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")
```

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
- Pertanyaan 1:
Arti nilai entropy dalam konteks kekuatan kunci:
Nilai entropy menunjukkan tingkat keacakan atau ketidakpastian suatu kunci kriptografi. Semakin tinggi entropinya, semakin banyak kemungkinan kombinasi kunci yang harus dicoba oleh penyerang untuk menemukan kunci yang benar. Dengan kata lain, entropi tinggi berarti kunci lebih sulit ditebak dan lebih kuat terhadap serangan brute force. Misalnya, kunci dengan 128 bit entropi memiliki 
2 ^128 kemungkinan, sehingga hampir mustahil ditebak dengan teknologi komputasi saat ini.

- Pertanyaan 2:
Pentingnya unicity distance dalam menentukan keamanan cipher:
Unicity distance menunjukkan jumlah minimal ciphertext yang diperlukan agar kunci dapat ditentukan secara unik. Jika ciphertext yang diperoleh penyerang lebih banyak daripada nilai unicity distance, maka secara teoritis ia bisa menebak kunci dengan menganalisis pola atau redundansi dalam teks. Jadi, semakin besar unicity distance suatu cipher, semakin aman cipher tersebut karena membutuhkan lebih banyak data terenkripsi sebelum kunci bisa ditemukan.

- Pertanyaan 3:
Alasan brute force tetap menjadi ancaman meskipun algoritma kuat:
Meskipun algoritma modern seperti AES atau RSA sangat kuat secara matematis, brute force tetap menjadi ancaman jika kunci yang digunakan terlalu pendek atau dihasilkan dari sumber yang lemah (misalnya, kata sandi sederhana). Selain itu, perkembangan teknologi seperti komputasi paralel dan komputer kuantum berpotensi mempercepat pencarian kunci secara eksponensial. Oleh karena itu, keamanan kriptografi tidak hanya bergantung pada algoritmanya, tetapi juga pada panjang dan kualitas kunci yang digunakan.
)
---

## 8. Kesimpulan
Berdasarkan percobaan, terlihat bahwa entropy untuk ruang kunci kecil seperti Caesar Cipher (26 kemungkinan) sangat rendah, sehingga mudah ditebak melalui brute force. Sebaliknya, ruang kunci besar seperti AES-128 memiliki entropi yang sangat tinggi sehingga hampir mustahil dipecahkan dengan kekuatan komputasi saat ini. Nilai unicity distance Caesar Cipher juga kecil, menandakan cipher tersebut mudah dianalisis dan tidak aman dibandingkan algoritma modern.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log

```
commit week4-entropy-unicity
Author: Ramzi Selpora Widiyanto <rasawi46rsw@gmail.com>
Date:   2025-11-08

    week4-entrophy-unicity: Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)
```
