programming_dictionary = {
"переменная": "именованное хранилище данных",
"цикл": "конструкция, повторяющая выполнение определенного блока кода",
"функция": "блок кода, предназначенный для выполнения определенной задачи"
}

term = input("Введите термин для определения: ")

if term in programming_dictionary:
	print(programming_dictionary[term])
else:
	print("Термин не найден в словаре.")