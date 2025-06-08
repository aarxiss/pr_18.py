import threading
import time

def countdown():
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)

# Створення та запуск потоку
thread = threading.Thread(target=countdown)
thread.start()

# Очікування завершення потоку (необов'язково)
thread.join()
