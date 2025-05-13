# simulator.py

import threading
import time
import random
import matplotlib.pyplot as plt

# Konfigurasi simulasi
NUM_THREADS = 4
ITERATIONS = 100

# Memori bersama
shared_memory = {'x': 0}
memory_lock = threading.Lock()

# Statistik
coherence_messages = 0

class Cache:
    def __init__(self):
        self.data = {}
        self.valid = {}

    def read(self, key):
        return self.data.get(key, None)

    def write(self, key, value):
        self.data[key] = value
        self.valid[key] = True

    def invalidate(self, key):
        if key in self.valid:
            self.valid[key] = False

    def is_valid(self, key):
        return self.valid.get(key, False)

def invalidate_other_caches(caches, current_id, key):
    global coherence_messages
    for i, cache in enumerate(caches):
        if i != current_id:
            cache.invalidate(key)
            coherence_messages += 1

def worker_with_coherence(tid, caches):
    cache = caches[tid]
    for _ in range(ITERATIONS):
        action = random.choice(["read", "write"])
        if action == "read":
            if not cache.is_valid("x"):
                with memory_lock:
                    cache.write("x", shared_memory["x"])
            val = cache.read("x")
        else:
            new_val = random.randint(1, 100)
            with memory_lock:
                shared_memory["x"] = new_val
                cache.write("x", new_val)
            invalidate_other_caches(caches, tid, "x")

def worker_no_coherence(tid, caches):
    cache = caches[tid]
    for _ in range(ITERATIONS):
        action = random.choice(["read", "write"])
        if action == "read":
            if "x" not in cache.data:
                cache.write("x", shared_memory["x"])
            val = cache.read("x")
        else:
            new_val = random.randint(1, 100)
            shared_memory["x"] = new_val
            cache.write("x", new_val)

def run_simulation(with_coherence=True):
    global shared_memory, coherence_messages
    shared_memory = {'x': 0}
    coherence_messages = 0
    caches = [Cache() for _ in range(NUM_THREADS)]
    threads = []

    start = time.time()
    for tid in range(NUM_THREADS):
        if with_coherence:
            t = threading.Thread(target=worker_with_coherence, args=(tid, caches))
        else:
            t = threading.Thread(target=worker_no_coherence, args=(tid, caches))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    end = time.time()

    return end - start, coherence_messages

def tampilkan_grafik(waktu_dengan, pesan_dengan, waktu_tanpa, pesan_tanpa):
    labels = ['Dengan Koherensi', 'Tanpa Koherensi']
    waktu = [waktu_dengan, waktu_tanpa]
    pesan = [pesan_dengan, pesan_tanpa]

    fig, ax1 = plt.subplots()

    ax2 = ax1.twinx()
    ax1.bar(labels, waktu, color='skyblue', label='Waktu (detik)')
    ax2.plot(labels, pesan, color='orange', marker='o', label='Pesan Koherensi')

    ax1.set_ylabel('Waktu (detik)')
    ax2.set_ylabel('Jumlah Pesan Koherensi')
    plt.title('Perbandingan Performa dengan dan tanpa Koherensi')

    fig.tight_layout()
    plt.show()
