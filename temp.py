import threading

def worker():
    pass

threads = []
for i in range(3):
    t = threading.Thread(target=worker, name=f"worker-{i}")
    threads.append(t)
    t.start()
    print(threading.enumerate())