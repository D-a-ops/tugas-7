cache-coherence-simulator
🧠 Multi-threaded Cache Simulator with and without Coherence Protocol
Simulasi ini menunjukkan bagaimana cache bekerja dalam sistem multi-prosesor, dengan perbandingan performa antara penggunaan protokol koherensi (MSI) dan tanpa koherensi.

🔍 Deskripsi
Proyek ini mensimulasikan:

Beberapa prosesor (thread) yang membaca dan menulis data.
Cache lokal untuk setiap prosesor.
Protokol koherensi sederhana (MSI - Modified, Shared, Invalid).
Traffic cache: hit, miss, invalidasi, writeback.
Perbandingan performa dengan dan tanpa protokol koherensi.
Penjelasan Proyek Cache Simulator
Apa itu Cache? Cache adalah memori kecil dan cepat yang menyimpan salinan data dari memori utama untuk mempercepat akses oleh prosesor.

⚠️ Masalah Cache di Sistem Multi-Core Ketika banyak prosesor (atau thread) memiliki cache sendiri, bisa terjadi masalah inkonsistensi data. Misalnya:

Prosesor 1 menulis data ke cache-nya.

Prosesor 2 masih membaca data lama dari cache-nya.

Ini menyebabkan race condition dan data tidak sinkron.

Protokol Koherensi Cache: MSI
Untuk menghindari inkonsistensi, digunakan protokol seperti MSI yang mengatur status setiap blok data di cache:

State	Nama	Arti
M	Modified	Cache memiliki data yang sudah dimodifikasi. Data ini berbeda dari memori utama.
S	Shared	Data masih sama dengan memori utama. Bisa dibaca oleh banyak cache.
I	Invalid	Data tidak valid (harus diambil ulang dari cache lain atau memori).
Contoh Sederhana:

P1 baca A → load dari memori → status S

P2 tulis A → invalidasi A di P1 → P2 simpan A sebagai M

📊 Perbandingan: Dengan vs Tanpa Koherensi
Aspek	Dengan Koherensi (MSI)	Tanpa Koherensi
✅ Konsistensi Data	Terjaga (lewat invalidasi, sinkronisasi)	Tidak terjaga (data bisa berbeda antar cache)
🔄 Overhead Komunikasi	Tinggi (karena invalidasi dan sinkronisasi antar cache)	Rendah (tidak ada sinkronisasi)
⏱️ Kecepatan Simulasi	Lebih lambat	Lebih cepat
💥 Resiko Race Condition	Sangat rendah	Sangat tinggi (data tidak akurat)
🧪 Akurasi Sistem Riil	Mirip sistem komputer nyata	Tidak realistis, hanya cocok untuk eksperimen awal
🔚 Kesimpulan
Tanpa koherensi, data bisa cepat diakses tapi berisiko inkonsistensi.

Dengan koherensi, sistem lebih kompleks tapi data tetap konsisten dan benar.

Proyek ini membantu memahami pentingnya koherensi dalam sistem multiprosesor.
