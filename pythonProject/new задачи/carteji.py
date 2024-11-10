
# def sort_dict_by_value(d):
    """Функция для сортировки словаря по значениям."""
    sorted_items = sorted(d.items(), key=lambda item: item[1])  # Сортируем по значениям
    return sorted_items  # Возвращаем отсортированный список кортежей

# Пример использования
sample_dict = {'apple': 3, 'banana': 2, 'orange': 5}
print("Отсортированный словарь:", sort_dict_by_value(sample_dict))
# Вывод: Отсортированный словарь: [('banana', 2), ('apple', 3), ('orange', 5)]