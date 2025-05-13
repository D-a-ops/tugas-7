# main.py

from simulator import run_simulation, tampilkan_grafik

def main():
    time_with, msg_with = run_simulation(with_coherence=True)
    time_without, msg_without = run_simulation(with_coherence=False)

    print("=== HASIL SIMULASI ===")
    print(f"Dengan Koherensi   : Waktu = {time_with:.4f} detik, Pesan Koherensi = {msg_with}")
    print(f"Tanpa Koherensi    : Waktu = {time_without:.4f} detik, Pesan Koherensi = {msg_without}")

    tampilkan_grafik(time_with, msg_with, time_without, msg_without)

if __name__ == "__main__":
    main()
