# Laporan Minggu 1 - Intro CIA

# Ringkasan Sejarah Kriptografi
--Era Kriptografi Klasik: Seni Kerahasiaan Manual--

Kriptografi klasik merujuk pada metode-metode enkripsi yang digunakan sebelum era komputer. Ciri utamanya adalah penggunaan algoritma yang relatif sederhana dan dapat dihitung dengan tangan. Metode-metode ini umumnya bekerja pada tingkat substitusi (mengganti huruf) atau transposisi (mengubah urutan huruf).

Salah satu contoh paling terkenal dari era ini adalah Caesar Cipher, yang konon digunakan oleh Julius Caesar untuk melindungi komunikasi militernya. Dalam sandi ini, setiap huruf dalam teks asli digeser sejumlah posisi tertentu dalam alfabet. Misalnya, dengan pergeseran tiga, 'A' akan menjadi 'D', 'B' menjadi 'E', dan seterusnya. Meskipun efektif pada masanya, sandi ini sangat mudah dipecahkan dengan analisis frekuensi huruf.

Contoh lain yang lebih kompleks adalah Vigenère Cipher. Sandi ini menggunakan kata kunci untuk melakukan serangkaian pergeseran Caesar yang berbeda pada huruf-huruf dalam pesan. Hal ini membuatnya jauh lebih tahan terhadap analisis frekuensi sederhana dibandingkan Caesar Cipher dan sempat dianggap "tidak terpecahkan" selama berabad-abad. Namun, kelemahannya terletak pada sifat perulangan kata kuncinya, yang pada akhirnya dapat dieksploitasi untuk memecahkan sandi.

--Perkembangan Kriptografi Modern: Kekuatan Komputasi dan Kunci--

Revolusi komputer membawa kriptografi ke era modern. Algoritma-algoritma yang dikembangkan pada periode ini jauh lebih kompleks dan dirancang untuk menahan serangan dari mesin-mesin komputasi yang kuat. Dua kategori utama mendominasi kriptografi modern:

Kriptografi Kunci Simetris, di mana kunci yang sama digunakan untuk proses enkripsi dan dekripsi. Contoh paling menonjol adalah Advanced Encryption Standard (AES). AES beroperasi pada blok data dengan ukuran tetap dan menggunakan kunci dengan panjang yang bervariasi (128, 192, atau 256 bit). Kecepatan dan efisiensinya membuat AES menjadi standar global untuk mengamankan berbagai jenis data, mulai dari file di hard drive hingga komunikasi online. Tantangan utamanya adalah bagaimana cara mendistribusikan kunci rahasia dengan aman kepada pihak yang berwenang.

Kriptografi Kunci Asimetris (atau Kunci Publik), yang menggunakan sepasang kunci: kunci publik dan kunci privat. Kunci publik dapat dibagikan secara luas dan digunakan untuk mengenkripsi pesan, sementara hanya pemilik kunci privat yang dapat mendekripsi pesan tersebut. RSA (Rivest-Shamir-Adleman) adalah algoritma kunci asimetris yang paling terkenal. RSA menjadi dasar bagi banyak protokol keamanan internet, seperti SSL/TLS yang mengamankan koneksi HTTPS, tanda tangan digital, dan pertukaran kunci yang aman.

--Evolusi Menuju Kriptografi Kontemporer: Desentralisasi dan Aplikasi Baru--

Era kontemporer ditandai dengan penerapan kriptografi pada skala yang lebih luas dan dalam konteks yang sama sekali baru, terutama didorong oleh munculnya internet dan kebutuhan akan sistem yang terdesentralisasi dan dapat dipercaya.

Contoh paling signifikan dari evolusi ini adalah blockchain dan cryptocurrency seperti Bitcoin. Teknologi blockchain pada dasarnya adalah buku besar digital yang didistribusikan dan diamankan menggunakan prinsip-prinsip kriptografi. Beberapa konsep kriptografi kunci yang digunakan meliputi:

~ Fungsi Hash Kriptografis: Setiap blok dalam rantai berisi hash kriptografis dari blok sebelumnya, menciptakan hubungan yang tidak dapat diubah dan memastikan integritas data.

~ Kriptografi Kunci Publik: Digunakan untuk mengotentikasi transaksi. Alamat dompet cryptocurrency adalah turunan dari kunci publik, dan transaksi yang dikirim dari dompet tersebut harus ditandatangani secara digital menggunakan kunci privat yang sesuai.

# Prinsip CIA
--Confidentiality (Kerahasiaan)
Aspek ini mengacu pada kebijakan dan teknologi yang digunakan untuk melindungi informasi dari akses atau pengungkapan yang tidak sah. Dalam konteks kerahasiaan, informasi hanya boleh diakses oleh pihak yang berwenang, sehingga informasi sensitif atau rahasia tetap terlindungi dari pihak yang tidak diinginkan.

--Integrity (Integritas)
Integritas berkaitan dengan keotentikan dan kebenaran informasi. Artinya, informasi harus tetap utuh dan tidak mengalami perubahan yang tidak sah selama penyimpanan, pengiriman, atau pemrosesan. Upaya menjaga integritas informasi melibatkan tindakan untuk mencegah modifikasi atau manipulasi yang tidak sah terhadap data.

--Availability (Ketersediaan)
Ketersediaan menunjukkan bahwa informasi harus tersedia dan dapat diakses oleh pihak yang berwenang ketika diperlukan. Ini berarti sistem dan infrastruktur harus dirancang dan dikelola sedemikian rupa sehingga dapat menanggapi permintaan akses informasi dengan cepat dan tanpa gangguan yang signifikan.

## QUIZ ##
1. Claude Elwood Shannon
2. RSA (Rivest-Shamir-Adleman) dan ECC (Kriptografi Kurva Eliptik)
3. 
Perbedaan Kriptografi Klasik dan Modern
1. Basis Operasi

    Klasik: Bekerja pada level karakter atau huruf (alfabet A-Z). Algoritma seperti Caesar Cipher hanya mengganti atau menggeser huruf.

    Modern: Bekerja pada level bit (data biner 0 dan 1). Semua data, termasuk kunci dan pesan, diubah menjadi format biner sebelum diolah. Ini memungkinkan operasi matematis yang jauh lebih kompleks dan efisien bagi komputer.

2. Kompleksitas Algoritma

    Klasik: Menggunakan algoritma yang sederhana dan dapat dihitung secara manual dengan pensil dan kertas. Teknik utamanya hanya substitusi (mengganti huruf) dan transposisi (mengubah urutan huruf).

    Modern: Menggunakan algoritma yang sangat kompleks secara matematis, seperti teori bilangan prima dan kurva eliptik. Algoritma ini mustahil dipecahkan dengan tangan dan dirancang untuk tahan terhadap serangan brute-force dari komputer yang kuat.

3. Pengelolaan Kunci

    Klasik: Hampir secara eksklusif menggunakan kriptografi simetris, di mana kunci yang sama dipakai untuk mengenkripsi dan mendekripsi pesan. Tantangan terbesarnya adalah bagaimana cara membagikan kunci rahasia ini dengan aman.

    Modern: Menggunakan dua jenis sistem kunci:

    ~ Kriptografi Simetris (contoh: AES): Seperti kriptografi klasik, tapi dengan kunci dan algoritma yang jauh lebih rumit.

    ~ Kriptografi Asimetris/Kunci Publik (contoh: RSA, ECC): Menggunakan sepasang kunci (publik dan privat). Kunci publik bisa dibagikan secara bebas untuk enkripsi, sementara hanya pemilik kunci privat yang bisa melakukan dekripsi. Ini memecahkan masalah distribusi kunci yang ada di era klasik.

4. Tingkat Keamanan

    Klasik: Sangat rentan terhadap analisis statistik, terutama analisis frekuensi kemunculan huruf. Sandi seperti Vigenère pun dapat dipecahkan dengan teknik modern.

    Modern: Keamanannya didasarkan pada kesulitan komputasi matematis. Misalnya, keamanan RSA bergantung pada betapa sulitnya komputer memfaktorkan bilangan prima yang sangat besar. Algoritma ini dirancang untuk membuat pola statistik pada data asli menjadi tidak terlihat.