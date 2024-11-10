
def factorial(n):
    """Функция для вычисления факториала числа n."""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i  # Умножаем результат на число i
    return result

def calculate_factorials(numbers):
    """Функция, которая принимает список чисел и возвращает список их факториалов."""
    factorials = []  # Создаем пустой список для хранения факториалов
    for num in numbers:
        fact = factorial(num)  # Вычисляем факториал
        factorials.append(fact)  # Добавляем его в список
    return factorials

# Пример использования
numbers = [0, 1, 2, 3, 4, 5]
print("Факториалы:", calculate_factorials(numbers))  # Вывод: Факториалы: [1, 1, 2, 6, 24, 120]