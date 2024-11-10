### Задача 10: Упаковка последовательностей



def pack_sequence(seq):
	"""Функция для упаковки последовательных дубликатов в кортежи."""
	packed = []
	for item in seq:
		if not packed or packed[-1][0] != item:
			packed.append((item, 1))  # Добавляем новый элемент с количеством 1
		else:
			packed[-1] = (packed[-1][0], packed[-1][1] + 1)  # Увеличиваем количество для дублирующегося элемента
	return packed

pack_sequence([1, 2, 2])