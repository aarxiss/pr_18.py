import threading
import random

# Генеруємо список із 1000 випадкових чисел від 1 до 100
numbers = [random.randint(1, 100) for _ in range(1000)]

# Змінна для збереження результатів
partial_sums = [0, 0, 0, 0]

# Функція для обчислення суми підсписку
def compute_sum(part, index):
    partial_sums[index] = sum(part)

# Ділимо список на 4 частини
chunk_size = len(numbers) // 4
chunks = [numbers[i * chunk_size:(i + 1) * chunk_size] for i in range(4)]

# Створюємо та запускаємо потоки
threads = []
for i in range(4):
    thread = threading.Thread(target=compute_sum, args=(chunks[i], i))
    threads.append(thread)
    thread.start()

# Очікуємо завершення всіх потоків
for thread in threads:
    thread.join()

# Обчислюємо загальну суму
total_sum = sum(partial_sums)
print("Загальна сума:", total_sum)
