# Laporan Praktikum Kriptografi
Minggu ke-: 10  
Topik: [Public Key Infrastructure (PKI & Certificate Authority)]  
Nama: [Ramzi Selpora Widiyanto]  
NIM: [230202776 ]  
Kelas: [5 IKKA]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:
1. Membuat sertifikat digital sederhana.
2. Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.
3. Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).

---

## 2. Dasar Teori
Public Key Infrastructure (PKI) adalah kerangka kerja keamanan yang mengelola penggunaan kriptografi kunci publik untuk menjamin keaslian, kerahasiaan, integritas, dan non-repudiation dalam komunikasi digital. PKI mencakup kebijakan, prosedur, perangkat keras, perangkat lunak, serta peran-peran tertentu yang mengatur pembuatan, distribusi, penyimpanan, penggunaan, dan pencabutan kunci kriptografi beserta sertifikat digital. Komponen utama PKI meliputi Certificate Authority (CA), Registration Authority (RA), sertifikat digital, serta mekanisme manajemen siklus hidup sertifikat.

Certificate Authority (CA) adalah entitas tepercaya dalam PKI yang bertugas memverifikasi identitas pemilik kunci publik dan menerbitkan sertifikat digital. Sertifikat ini mengikat identitas (pengguna, organisasi, atau server) dengan kunci publik tertentu dan ditandatangani secara digital oleh CA. Dengan tanda tangan CA, pihak lain dapat memverifikasi keaslian sertifikat dan mempercayai kunci publik yang digunakan, misalnya pada HTTPS, email terenkripsi, dan tanda tangan dokumen elektronik.

Dalam sistem modern, PKI juga menyediakan mekanisme pencabutan sertifikat melalui Certificate Revocation List (CRL) atau Online Certificate Status Protocol (OCSP) untuk memastikan sertifikat yang sudah tidak valid tidak lagi dipercaya. Dengan adanya PKI dan CA, komunikasi digital dapat berlangsung secara aman dan tepercaya meskipun dilakukan melalui jaringan publik seperti internet.
---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan cryptography pyopenssl

---

## 4. Langkah Percobaan
1. Membuat file `pki_cert.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python oki_cert.py`.
---

## 5. Source Code

```python
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta

# Generate key pair
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Buat subject & issuer (CA sederhana = self-signed)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"example.com"),
])

# Buat sertifikat
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(datetime.utcnow() + timedelta(days=365))
    .sign(key, hashes.SHA256())
)

# Simpan sertifikat
with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Sertifikat digital berhasil dibuat: cert.pem")
```

- Memverifikasi Sertifikat

Verifikasi sertifikat dilakukan dengan memeriksa tanda tangan digital pada sertifikat menggunakan public key milik Certificate Authority (CA). Pada kode di atas, sertifikat bersifat self-signed, artinya issuer dan subject sama, sehingga verifikasi dilakukan menggunakan public key dari sertifikat itu sendiri. Jika tanda tangan valid dan periode berlaku masih aktif, maka sertifikat dianggap sah secara kriptografis.

Dalam PKI nyata, CA berperan sebagai pihak tepercaya yang menandatangani sertifikat milik pengguna atau server. Ketika sebuah sertifikat diterima, sistem akan menggunakan public key CA (yang sudah dipercaya dan tersimpan di sistem/browsers) untuk memverifikasi tanda tangan sertifikat tersebut. Dengan demikian, keaslian sertifikat dijamin karena hanya CA yang sah yang memiliki private key untuk membuat tanda tangan tersebut.

- Analisis PKI (Kasus Nyata)

1. Bagaimana browser memverifikasi sertifikat HTTPS?
Browser memeriksa sertifikat server dengan cara:

- Memvalidasi rantai kepercayaan (certificate chain) dari sertifikat server hingga Root CA tepercaya.
- Memeriksa tanda tangan digital pada setiap sertifikat menggunakan public key CA terkait.
- Memastikan masa berlaku, nama domain, serta status pencabutan sertifikat (CRL/OCSP).
Jika semua valid, koneksi HTTPS dianggap aman dan tepercaya.

2. Apa yang terjadi jika CA palsu menerbitkan sertifikat?
Jika CA palsu atau CA yang dikompromikan menerbitkan sertifikat, penyerang dapat melakukan man-in-the-middle attack, menyamar sebagai server asli dan mencuri data sensitif. Oleh karena itu, sistem operasi dan browser hanya mempercayai Root CA tertentu, serta dapat mencabut kepercayaan terhadap CA yang terbukti bermasalah.

3. Mengapa PKI penting dalam komunikasi aman (misalnya transaksi online)?
PKI memastikan bahwa komunikasi dilakukan dengan pihak yang benar, data tidak diubah selama transmisi, dan informasi sensitif tetap aman. Dalam transaksi online, PKI melindungi data seperti password, nomor kartu kredit, dan identitas pengguna, sehingga mencegah pemalsuan, penyadapan, dan penipuan digital. Tanpa PKI, kepercayaan dalam komunikasi di internet tidak dapat terjamin.
---

## 6. Hasil dan Pembahasan
- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program pki_cert:

![Hasil Eksekusi](screenshots/hasil.png)


---

## 7. Jawaban Pertanyaan
 
1. Apa fungsi utama Certificate Authority (CA)?
Jawab :
Certificate Authority (CA) berfungsi sebagai pihak tepercaya yang memverifikasi identitas pemilik kunci publik dan menerbitkan sertifikat digital. CA mengikat identitas (domain, individu, atau organisasi) dengan kunci publik melalui tanda tangan digital, sehingga pihak lain dapat mempercayai bahwa kunci publik tersebut benar-benar milik entitas yang sah.

2. Mengapa self-signed certificate tidak cukup untuk sistem produksi?
Jawab :
Self-signed certificate tidak cukup untuk sistem produksi karena tidak ada pihak ketiga tepercaya yang memverifikasi identitas pemilik sertifikat. Akibatnya, browser atau klien akan menampilkan peringatan keamanan dan pengguna tidak dapat memastikan keaslian server. Self-signed certificate hanya cocok untuk pengujian atau lingkungan internal, bukan untuk layanan publik yang membutuhkan tingkat kepercayaan tinggi.

3. Bagaimana PKI mencegah serangan MITM dalam komunikasi TLS/HTTPS?
Jawab : 
PKI mencegah serangan Man-in-the-Middle (MITM) dengan memastikan bahwa sertifikat server diverifikasi melalui rantai kepercayaan CA. Browser memeriksa tanda tangan sertifikat, kesesuaian nama domain, dan status pencabutan sertifikat. Penyerang tidak dapat menyamar sebagai server asli karena tidak memiliki sertifikat valid yang ditandatangani CA tepercaya, sehingga koneksi TLS/HTTPS yang aman tetap terjaga.

---

## 8. Kesimpulan
Kesimpulan pada Kode:
Kode tersebut menunjukkan implementasi dasar Public Key Infrastructure (PKI) melalui pembuatan sertifikat digital self-signed menggunakan algoritma kriptografi kunci publik RSA. Proses ini mencakup pembuatan pasangan kunci, penentuan identitas (subject dan issuer), serta penandatanganan sertifikat menggunakan fungsi hash SHA-256 untuk menjamin keutuhan dan keaslian sertifikat secara kriptografis.

Meskipun sertifikat yang dihasilkan valid secara teknis, karena bersifat self-signed, sertifikat ini belum dapat dipercaya dalam lingkungan produksi. Hal ini menegaskan pentingnya peran Certificate Authority (CA) sebagai pihak tepercaya dalam PKI, di mana CA memverifikasi identitas dan menandatangani sertifikat agar dapat digunakan secara aman pada sistem nyata seperti TLS/HTTPS.
---

## 9. Daftar Pustaka

- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  
- Stallings (2017), Bab 14.
---

## 10. Commit Log

```
commit week10-pki
Author: Ramzi Selpora Widiyanto <rasawi46rsw@gmail.com>
Date:   2026-01-09

    week10-pki: Public Key Infrastructure (PKI & Certificate Authority)
```
