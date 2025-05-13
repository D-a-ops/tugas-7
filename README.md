📦 cache-coherence-simulator
🧠 Multi-threaded Cache Simulator with and without Coherence Protocol

Simulasi ini menunjukkan bagaimana cache bekerja dalam sistem multi-prosesor,
dengan perbandingan performa antara penggunaan protokol koherensi (sederhana, seperti MSI)
dan tanpa koherensi.

🔍 Deskripsi
Program ini mensimulasikan:
- Beberapa prosesor (thread) yang membaca dan menulis data secara paralel.
- Cache lokal untuk setiap thread.
- Protokol koherensi sederhana (invalidate saat write).
- Traffic cache: valid/invalid, update bersama, dan pengaruh sinkronisasi.
- Perbandingan performa antara sistem dengan dan tanpa protokol koherensi.

💡 Apa Itu Cache?
Cache adalah memori kecil dan cepat yang menyimpan salinan data dari memori utama.
Cache membantu mempercepat akses data oleh prosesor.

⚠️ Masalah Cache di Sistem Multi-Core
Ketika setiap prosesor memiliki cache sendiri, bisa terjadi inkonsistensi:
- Thread 1 menulis ke cache-nya.
- Thread 2 masih membaca data lama dari cache-nya sendiri.
Hal ini menyebabkan race condition dan data menjadi tidak sinkron.

🔄 Protokol Koherensi Cache (Model Sederhana - mirip MSI)
Untuk mencegah inkonsistensi, digunakan protokol koherensi:
- Ketika satu thread melakukan penulisan, cache thread lain di-*invalidate*.
- Ini menimbulkan lalu lintas koherensi (pesan sinkronisasi antar thread).

Status data:
- ✅ Valid → Data sinkron
- ❌ Invalid → Perlu ambil ulang dari memori utama

Contoh Proses:
1. Thread A baca `x` → cache ambil dari memori → status valid
2. Thread B tulis `x` → update nilai, invalidate `x` di cache thread lain

📊 Perbandingan: Dengan vs Tanpa Koherensi
| Aspek                    | Dengan Koherensi         | Tanpa Koherensi          |
|--------------------------|---------------------------|---------------------------|
| ✅ Konsistensi Data      | Terjaga (sinkronisasi)   | Tidak terjaga             |
| 🔄 Overhead Komunikasi  | Tinggi (pesan invalidasi)| Rendah                    |
| ⏱️ Kecepatan Simulasi   | Lebih lambat             | Lebih cepat               |
| 💥 Risiko Race Condition| Rendah                   | Tinggi                    |
| 🧪 Akurasi Sistem Nyata | Mirip sistem riil        | Tidak akurat              |

📈 Output Simulasi
Program akan mencetak:
- Waktu eksekusi untuk kedua mode
- Jumlah pesan koherensi (invalidasi)
- Grafik perbandingan waktu vs traffic

🔚 Kesimpulan
Tanpa koherensi:
- Lebih cepat, tapi berisiko data tidak konsisten

Dengan koherensi:
- Lebih lambat, tapi menjamin konsistensi data

Simulasi ini memberikan gambaran penting tentang bagaimana protokol koherensi
berperan dalam menjaga keandalan sistem multiprosesor modern.
"""

