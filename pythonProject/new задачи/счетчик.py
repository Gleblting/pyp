
import time  # Импортируем библиотеку time для использования задержки

def countdown(n):
    """Функция обратного счётчика от n до 0."""
    while n >= 0:  # Пока n больше или равно 0
        print(n)  # Печатаем текущее значение n
        time.sleep(1)  # Ждем 1 секунду
        n -= 1  # Уменьшаем n на 1

# Пример использования
countdown(5)  # Запускаем обратный счётчик от 5