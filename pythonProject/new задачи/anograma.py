
# def are_anagrams(str1, str2):
#     """Функция для проверки, являются ли две строки анаграммами."""
#     # Убираем пробелы и переводим строки к нижнему регистру, затем сортируем символы
#     return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())
#
# # Пример использования
# string1 = "мука"
# string2 = "кума"
# print("Анаграммы:", are_anagrams(string1, string2))  # Вывод: Анаграммы: True

def spiral_fill(n):
	"""Функция для заполнения 2D массива по спирали."""
	matrix = [[0] * n for _ in range(n)]
	left, right = 0, n - 1
	top, bottom = 0, n - 1
	num = 1
spiral_fill(3)