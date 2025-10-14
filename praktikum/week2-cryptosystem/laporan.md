# Laporan Praktikum Kriptografi
Minggu ke-: 2  
Topik: [CRYPTOSYSTEM]  
Nama: [Ramzi Selpora Widiyanto]  
NIM: [230202776]  
Kelas: [5IKKA]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:
1. Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).
2. Menggambarkan proses enkripsi dan dekripsi sederhana.
3. Mengklasifikasikan jenis kriptosistem (simetris dan asimetris)

---

## 2. Dasar Teori
Cryptosystem atau sistem kriptografi adalah seperangkat algoritma yang digunakan untuk melakukan enkripsi dan dekripsi data dengan tujuan menjaga keamanan informasi. Secara umum, sebuah cryptosystem terdiri dari tiga komponen utama, yaitu plaintext (pesan asli), ciphertext (pesan terenkripsi), dan key (kunci). Proses enkripsi mengubah plaintext menjadi ciphertext menggunakan kunci tertentu agar tidak dapat dibaca oleh pihak yang tidak berwenang, sedangkan dekripsi mengembalikan ciphertext ke bentuk aslinya dengan menggunakan kunci yang sesuai.

Kriptosistem dapat dibedakan menjadi dua jenis utama: symmetric key cryptosystem dan asymmetric key cryptosystem. Pada sistem simetris, kunci yang digunakan untuk enkripsi dan dekripsi adalah sama, sedangkan pada sistem asimetris digunakan dua kunci berbeda, yaitu public key (kunci publik) dan private key (kunci privat). Penggunaan cryptosystem sangat penting dalam bidang keamanan data seperti pengiriman pesan digital, transaksi online, serta penyimpanan data sensitif untuk melindungi dari akses tidak sah dan serangan siber.

Cipher klasik merupakan teknik enkripsi sederhana yang digunakan untuk mengamankan pesan dengan cara mengganti huruf atau mengubah urutan karakter menggunakan aturan tertentu. Beberapa jenis cipher klasik yang umum digunakan antara lain Caesar Cipher, Vigenère Cipher, dan Transposition Cipher. Pada Caesar Cipher, setiap huruf pada teks asli digeser sejauh kunci tertentu dalam alfabet. Misalnya, dengan kunci 3, huruf “A” menjadi “D”. Teknik ini mudah diterapkan namun rentan terhadap serangan analisis frekuensi.

Konsep aritmetika modular menjadi dasar penting dalam proses enkripsi dan dekripsi cipher klasik. Dalam sistem ini, operasi seperti penjumlahan atau pengurangan dilakukan dengan mengacu pada modulus tertentu, misalnya 26 untuk alfabet Latin (A–Z). Contohnya, jika hasil penjumlahan melebihi 25, maka akan kembali ke awal alfabet (mod 26). Dengan konsep ini, cipher dapat menjaga hasil enkripsi tetap berada dalam rentang huruf yang valid.

Penerapan cipher klasik dan aritmetika modular tidak hanya penting untuk memahami dasar kriptografi, tetapi juga menjadi landasan bagi pengembangan algoritma modern seperti AES dan RSA. Meski tergolong sederhana, teori ini membantu memahami bagaimana proses pengamanan data bekerja dari tahap substitusi hingga transformasi matematis yang lebih kompleks.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
1. Membuat Skema Kriptosistem
1. Membuat file `simple_crypto.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python simple_crypto.py`.
4. Klasifikasi Simetris dan Asimetris

---

## 5. Source Code
def encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def decrypt(ciphertext, key):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift - key) % 26 + shift)
        else:
            result += char
    return result

if __name__ == "__main__":
    message = "<230202776><Ramzi Selpora Widiyanto>"
    key = 5

    enc = encrypt(message, key)
    dec = decrypt(enc, key)

    print("Plaintext :", message)
    print("Ciphertext:", enc)
    print("Decrypted :", dec)
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
- Pertanyaan 1: 
-Plaintext (Teks Asli)
-CipherText (Teks Terenkripsi)
-Algoritma Enkripsi
-Algoritma Dekripsi
                -Kunci (Key)
- Pertanyaan 2: 
Kelebihan Simetris :
-Proses lebih cepat dan efisien.
-Cocok untuk data besar.
-Kebutuhan Sumber daya rendah.
Kelemahan Simetris :
-Kunci Sulit dan beresiko penyadapan karena memiliki kunci yang sama.
-Kurang aman untuk autentikasi.

---

## 8. Kesimpulan
Dari hasil program:
-Enkripsi (encrypt) berhasil mengubah teks asli menjadi ciphertext yang tidak terbaca secara langsung.
-Dekripsi (decrypt) berhasil mengembalikan ciphertext menjadi plaintext semula, menunjukkan bahwa algoritma bekerja dengan benar.
(key=5 , benar melompati 5 huruf setelahnya)
---

## 9. Daftar Pustaka
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Ramzi Selpora Widiyanto <rasawi46rsw@gmail.com>
Date:   2025-10-14

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
