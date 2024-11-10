
def is_prime(num):
    """Функция, которая проверяет, является ли число num простым."""
    if num <= 1:  # 0 и 1 не являются простыми числами
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Проверяем делители до корня из num
        if num % i == 0:  # Если число делится на i без остатка
            return False  # num не простое
    return True  # num простое

# Пример использования
number = 29
if is_prime(number):
    print(f"{number} является простым числом.")  # Вывод: 29 является простым числом.
else:
    print(f"{number} не является простым числом.")