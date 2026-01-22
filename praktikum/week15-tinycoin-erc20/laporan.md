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
- Metamask
- REMIX IDE  
- Library tambahan 

---

## 4. Langkah Percobaan
# 1. Membuat file `index.html , style.css , script.js , Donation.sol` di folder `praktikum/week15-tinycoin-erc20/src/`.

# 2. Membuat Akun Metamask dan mendownload add on nya

# 3. Buka dan siapkan file `Donation.sol`untuk di simpan di dalam Remix IDE https://remix.ethereum.org 
(screenshots/remix1.png)

# 4. Masuk ke menu Solidity Compiler , lalu Compile and Run Script
(screenshots/remix2.png)

# 5. Jika sudah membuat dan memiliki Metamask, langkah selanjutnya adalah ganti netwok di metamask menjadi Sepolia. Kemudian copy dan paste wallet addres ke dalam web ini https://sepolia-faucet.pk910.de/#/
(screenshots/ether.png)
(screenshots/mining1.png)
(screenshots/mining2.png)
(screenshots/mining3.png)

# Lalu Start Mining, tunggu sampai koin melebihi minimum atau maximum claim

# 6. Langkah selanjutnya kembali ke Remix IDE untuk pengaturan Donate, Pilih Inject Provide- Metamask di dalam Environment dan Masukkan Wallet Addres Sepolia (otomatis mendeteksi account) , pastikan masih value 0 dan wei
(screenshots/remix4.png)

# Setelah ,
(screenshots/remix5.png)

# di bawahnya ganti wei menjadi gwei dan pilih berapa Value yang kita mau transaksikan..contoh: 1.000.000 gwei yang nantinya akan menjadi 0.001ETH 
(screenshots/remix6.png)
(screenshots/remix7.png)
(screenshots/remix8.png)
# 7. Buka link view etherscan yang muncul di terminal
(screenshots/remix9.png)
(screenshots/remix10.png)
---

## 5. Source Code Untuk Pembuatan Donate via Website
# index.html
```python
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <title>Luxury Web3 Donation</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <link rel="stylesheet" href="style.css">
  <script src="https://cdn.jsdelivr.net/npm/ethers@6.9.0/dist/ethers.min.js"></script>
</head>
<body>

<div class="bg-orb orb-1"></div>
<div class="bg-orb orb-2"></div>

<main class="card">
  <h1>Web3 Donation</h1>
  <p class="subtitle">Transparan • Aman • Terdesentralisasi</p>

  <div class="input-group">
    <span>ETH</span>
    <input type="number" id="amount" placeholder="0.01" step="0.001">
  </div>

  <button onclick="donate()">Donate Now</button>

  <div id="status"></div>

  <footer>
    Powered by Ethereum • Sepolia Testnet
  </footer>
</main>

<script src="script.js"></script>
</body>
</html>

```

# style.css
```python
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

* {
  box-sizing: border-box;
  font-family: 'Inter', sans-serif;
}

body {
  margin: 0;
  height: 100vh;
  background: radial-gradient(circle at top, #0f172a, #020617);
  display: flex;
  justify-content: center;
  align-items: center;
  color: #fff;
  overflow: hidden;
}

/* Background Orbs */
.bg-orb {
  position: absolute;
  width: 420px;
  height: 420px;
  border-radius: 50%;
  filter: blur(140px);
  opacity: 0.45;
}

.orb-1 {
  background: #f59e0b;
  top: -120px;
  left: -120px;
}

.orb-2 {
  background: #38bdf8;
  bottom: -120px;
  right: -120px;
}

/* Card */
.card {
  width: 380px;
  padding: 36px;
  border-radius: 22px;
  background: rgba(255,255,255,0.08);
  backdrop-filter: blur(18px);
  box-shadow: 0 25px 80px rgba(0,0,0,0.55);
  text-align: center;
  z-index: 1;
}

.card h1 {
  font-size: 28px;
  font-weight: 600;
  letter-spacing: 0.5px;
}

.subtitle {
  font-size: 14px;
  opacity: 0.75;
  margin-bottom: 28px;
}

/* Input */
.input-group {
  display: flex;
  align-items: center;
  background: rgba(255,255,255,0.12);
  border-radius: 14px;
  padding: 12px 14px;
  margin-bottom: 22px;
}

.input-group span {
  font-weight: 600;
  margin-right: 8px;
  opacity: 0.9;
}

.input-group input {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  color: #fff;
  font-size: 15px;
}

/* Button */
button {
  width: 100%;
  padding: 14px;
  border-radius: 14px;
  border: none;
  background: linear-gradient(135deg, #f59e0b, #ef4444);
  color: #fff;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: 0.35s;
}

button:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 30px rgba(245, 158, 11, 0.45);
}

/* Status */
#status {
  margin-top: 18px;
  font-size: 14px;
  min-height: 20px;
}

/* Footer */
footer {
  margin-top: 26px;
  font-size: 12px;
  opacity: 0.55;
}

.donation-stats {
  background: linear-gradient(135deg, #111, #1f1f1f);
  border-radius: 16px;
  padding: 24px;
  margin: 20px 0;
  text-align: center;
  box-shadow: 0 0 20px rgba(255, 215, 0, 0.2);
}

.donation-stats p {
  color: #aaa;
  letter-spacing: 1px;
  margin-bottom: 8px;
}

.donation-stats h2 {
  color: gold;
  font-size: 2.2rem;
}

.stats {
  margin-top: 20px;
  padding: 14px;
  background: rgba(255,255,255,0.08);
  border-radius: 14px;
}

.stats h3 {
  margin: 0;
  font-size: 13px;
  opacity: 0.7;
}

#total {
  font-size: 20px;
  font-weight: 600;
}

#history {
  margin-top: 18px;
  list-style: none;
  padding: 0;
  max-height: 120px;
  overflow-y: auto;
}

#history li {
  font-size: 12px;
  opacity: 0.75;
  margin-bottom: 6px;
}
```

# script.js
```python
const contractAddress = "0x8E6e34F439EedE36f4c8fB435511A6BD08E8a259";

const abi = [
  "function donate() payable",
  "function totalDonations() view returns (uint256)"
];

async function donate() {
  if (!window.ethereum) {
    alert("MetaMask tidak ditemukan");
    return;
  }

  const amount = document.getElementById("amount").value;
  if (!amount || amount <= 0) {
    alert("Masukkan jumlah ETH");
    return;
  }

  try {
    const provider = new ethers.BrowserProvider(window.ethereum);
    await provider.send("eth_requestAccounts", []);
    const signer = await provider.getSigner();

    const contract = new ethers.Contract(
      contractAddress,
      abi,
      signer
    );

    document.getElementById("status").innerText =
      "⏳ Menunggu konfirmasi MetaMask...";

    const tx = await contract.donate({
      value: ethers.parseEther(amount)
    });

    document.getElementById("status").innerText =
      "⛓️ Transaksi diproses di blockchain...";

    await tx.wait();

    document.getElementById("status").innerText =
      "✅ Donasi berhasil via Smart Contract! 🤍";

  } catch (err) {
    console.error(err);
    document.getElementById("status").innerText =
      "❌ Transaksi dibatalkan / gagal";
  }
}

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
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka 
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.
- https://ethereum.org/en/developers/docs/standards/tokens/erc-20/
- https://docs.openzeppelin.com/contracts/erc20 

---

## 10. Commit Log

```
commit week15-tinycoin-erc20
Author: Ramzi Selpora Widiyanto <rasawi46rsw@gmail.com>
Date:   2026-01-22

    week15-tinycoin-erc20: Proyek Kelompok – TinyCoin ERC20
```
