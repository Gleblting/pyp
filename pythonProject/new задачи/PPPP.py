def spiral_fill(n):
	"""Функция для заполнения 2D массива по спирали."""
	matrix = [[0] * n for _ in range(n)]  # Создаем n x n матрицу
	left, right = 0, n - 1
	top, bottom = 0, n - 1
	num = 1

	while left <= right and top <= bottom:
		for i in range(left, right + 1):  # Заполняем верхнюю сторону
			matrix[top][i] = num
			num += 1
		top += 1

		for i in range(top, bottom + 1):  # Заполняем правую сторону
			matrix[i][right] = num
			num += 1
		right -= 1

		if top <= bottom:
			for i in range(right, left - 1, -1):  # Заполняем нижнюю сторону
				matrix[bottom][i] = num
				num += 1
			bottom -= 1

		if left <= right:
			for i in range(bottom, top - 1, -1):  # Заполняем левую сторону
				matrix[i][left] = num
				num += 1
			left += 1

	return matrix


# Пример использования
result = spiral_fill(3)
for row in result:
	print(row)
	# Вывод: [[1, 2, 3], [8, 9, 4], [7, 6, 5]]