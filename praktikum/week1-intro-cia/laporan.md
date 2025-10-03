# Laporan Minggu 1 - Intro CIA

# Ringkasan Sejarah Kriptografi
-Era Kriptografi Klasik: Seni Kerahasiaan Manual

Kriptografi klasik merujuk pada metode-metode enkripsi yang digunakan sebelum era komputer. Ciri utamanya adalah penggunaan algoritma yang relatif sederhana dan dapat dihitung dengan tangan. Metode-metode ini umumnya bekerja pada tingkat substitusi (mengganti huruf) atau transposisi (mengubah urutan huruf).

Salah satu contoh paling terkenal dari era ini adalah Caesar Cipher, yang konon digunakan oleh Julius Caesar untuk melindungi komunikasi militernya. Dalam sandi ini, setiap huruf dalam teks asli digeser sejumlah posisi tertentu dalam alfabet. Misalnya, dengan pergeseran tiga, 'A' akan menjadi 'D', 'B' menjadi 'E', dan seterusnya. Meskipun efektif pada masanya, sandi ini sangat mudah dipecahkan dengan analisis frekuensi huruf.

Contoh lain yang lebih kompleks adalah Vigenère Cipher. Sandi ini menggunakan kata kunci untuk melakukan serangkaian pergeseran Caesar yang berbeda pada huruf-huruf dalam pesan. Hal ini membuatnya jauh lebih tahan terhadap analisis frekuensi sederhana dibandingkan Caesar Cipher dan sempat dianggap "tidak terpecahkan" selama berabad-abad. Namun, kelemahannya terletak pada sifat perulangan kata kuncinya, yang pada akhirnya dapat dieksploitasi untuk memecahkan sandi.

-Perkembangan Kriptografi Modern: Kekuatan Komputasi dan Kunci

Revolusi komputer membawa kriptografi ke era modern. Algoritma-algoritma yang dikembangkan pada periode ini jauh lebih kompleks dan dirancang untuk menahan serangan dari mesin-mesin komputasi yang kuat. Dua kategori utama mendominasi kriptografi modern:

Kriptografi Kunci Simetris, di mana kunci yang sama digunakan untuk proses enkripsi dan dekripsi. Contoh paling menonjol adalah Advanced Encryption Standard (AES). AES beroperasi pada blok data dengan ukuran tetap dan menggunakan kunci dengan panjang yang bervariasi (128, 192, atau 256 bit). Kecepatan dan efisiensinya membuat AES menjadi standar global untuk mengamankan berbagai jenis data, mulai dari file di hard drive hingga komunikasi online. Tantangan utamanya adalah bagaimana cara mendistribusikan kunci rahasia dengan aman kepada pihak yang berwenang.

Kriptografi Kunci Asimetris (atau Kunci Publik), yang menggunakan sepasang kunci: kunci publik dan kunci privat. Kunci publik dapat dibagikan secara luas dan digunakan untuk mengenkripsi pesan, sementara hanya pemilik kunci privat yang dapat mendekripsi pesan tersebut. RSA (Rivest-Shamir-Adleman) adalah algoritma kunci asimetris yang paling terkenal. RSA menjadi dasar bagi banyak protokol keamanan internet, seperti SSL/TLS yang mengamankan koneksi HTTPS, tanda tangan digital, dan pertukaran kunci yang aman.

-Evolusi Menuju Kriptografi Kontemporer: Desentralisasi dan Aplikasi Baru

Era kontemporer ditandai dengan penerapan kriptografi pada skala yang lebih luas dan dalam konteks yang sama sekali baru, terutama didorong oleh munculnya internet dan kebutuhan akan sistem yang terdesentralisasi dan dapat dipercaya.

Contoh paling signifikan dari evolusi ini adalah blockchain dan cryptocurrency seperti Bitcoin. Teknologi blockchain pada dasarnya adalah buku besar digital yang didistribusikan dan diamankan menggunakan prinsip-prinsip kriptografi. Beberapa konsep kriptografi kunci yang digunakan meliputi:

    Fungsi Hash Kriptografis: Setiap blok dalam rantai berisi hash kriptografis dari blok sebelumnya, menciptakan hubungan yang tidak dapat diubah dan memastikan integritas data.

    Kriptografi Kunci Publik: Digunakan untuk mengotentikasi transaksi. Alamat dompet cryptocurrency adalah turunan dari kunci publik, dan transaksi yang dikirim dari dompet tersebut harus ditandatangani secara digital menggunakan kunci privat yang sesuai.