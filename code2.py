import threading
import time
import random

def download_file(file_id):
    duration = random.randint(3, 5)
    print(f"Файл {file_id} завантажується ({duration} сек)...")
    time.sleep(duration)
    print(f"Файл {file_id} завантажено.")

# Створення списку потоків
threads = []

for i in range(1, 4):
    thread = threading.Thread(target=download_file, args=(i,))
    threads.append(thread)
    thread.start()

# Очікування завершення всіх потоків
for thread in threads:
    thread.join()
