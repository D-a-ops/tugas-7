# simulator.py

import threading
import time
import random
import matplotlib.pyplot as plt

NUM_THREADS = 4
ITERATIONS = 100
shared_memory = {'x': 0}
coherence_messages = 0

class Cache:
    def __init__(self): 
        self.data = {} 

    def read(self, key): 
        return self.data.get(key, None)

    def write(self, key, value): 
        self.data[key] = value

    def invalidate(self, key): 
        self.data[key] = None

def worker(tid, caches, with_coherence=True):
    global coherence_messages
    cache = caches[tid]
    for _ in range(ITERATIONS):
        action = random.choice(["read", "write"])
        if action == "read":
            if not cache.read("x"):
                cache.write("x", shared_memory["x"])
        else:
            new_val = random.randint(1, 100)
            shared_memory["x"] = new_val
            cache.write("x", new_val)
            if with_coherence:
                for i, c in enumerate(caches):
                    if i != tid: 
                        c.invalidate("x")
                        coherence_messages += 1

def run_simulation(with_coherence=True):
    global coherence_messages
    caches = [Cache() for _ in range(NUM_THREADS)]
    threads = []
    
    start = time.time()
    for tid in range(NUM_THREADS):
        t = threading.Thread(target=worker, args=(tid, caches, with_coherence))
        threads.append(t)
        t.start()

    for t in threads: t.join()
    return time.time() - start, coherence_messages

def tampilkan_grafik(waktu_dengan, pesan_dengan, waktu_tanpa, pesan_tanpa):
    labels = ['Dengan Koherensi', 'Tanpa Koherensi']
    fig, ax1 = plt.subplots()
    
    ax2 = ax1.twinx()
    ax1.bar(labels, [waktu_dengan, waktu_tanpa], color='skyblue', label='Waktu (detik)')
    ax2.plot(labels, [pesan_dengan, pesan_tanpa], color='orange', marker='o', label='Pesan Koherensi')

    ax1.set_ylabel('Waktu (detik)')
    ax2.set_ylabel('Jumlah Pesan Koherensi')
    plt.title('Perbandingan Performa dengan dan tanpa Koherensi')
    plt.tight_layout()
    plt.show()
