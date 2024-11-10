def reverse_string(s):
    """Функция для реверса строки."""
    reversed_str = ""  # Пустая строка для хранения реверсированной строки
    for char in s:  # Проходим по каждому символу в строке
        reversed_str = char + reversed_str  # Добавляем текущий символ в начало новой строки
    return reversed_str  # Возвращаем реверсированную строку

print(reverse_string('stroka'))