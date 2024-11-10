# import datetime
# print(datetime.datetime.now().date())
# import sys, os
# print(sys.path, os.name)
# from math import sqrt
# print(sqrt(25))
# from time import sleep as s
# s(5)
# print('спит 5 секунд')
# import function
# print(function.filter_list([1, 2, 3, 6, 'stroka', True], int))

# import cowsay
# cowsay.cow('Добрый вечер Катка')



# Для работы с файлами в Python используется функция open(). Она принимает два аргумента: имя файла и режим открытия файла. Режимы открытия могут быть следующие:
#
# ‘r’ — чтение (по умолчанию)
# ‘w’ — запись (если файл не существует, он будет создан)
# ‘a’ — добавление (открывает файл для добавления новых данных)
# ‘x’ — создание (создает новый файл, если он уже существует, вызывается исключение)
# ‘b’ — двоичный режим (используется для работы с двоичными файлами, например, изображениями)

# file = open('задачи/файл для записи.py', 'a')
# # file.write('\nhello world2\n')
# file.write('\nhello pethon2')
# file.close()

# file = open('задачи/файл для записи.py', 'r')
# # print(file.read(-1))
# for line in file:
# 	print(line, end='')
# file.close()

f = open('задачи/dfv.py', 'w') #если файл не создан, то он будет создан
f.write('helo\n')
f.write('world\n')

f.close()

f = open('задачи/dfv.py', 'a') #добавление данных
f.write('children\n')
f.write('maks\n')
# добавлять данные от пользователей через пер
f.close()

# read(size) — считывает из файла указанное количество символов (или весь файл, если size не указан)
# readline() — считывает одну строку из файла
# readlines() — считывает все строки файла в список

#Пример чтения всего файла:


# file = open('задачи/dfv.py', 'r')
# content = file.read()
# print(content)
# file.close()

# file = open('задачи/dfv.py', 'r')
# content = file.readline(2)
# content2 = file.readline()
# print(content)
# file.close()
#Пример чтения файла построчно:


# file = open('задачи/dfv.py', 'r')
# for line in file:
#     print(line, end='')
# file.close()

#Использование контекстных менеджеров позволяет автоматически закрыть файл после выхода из блока with. Это удобно и позволяет избежать ошибок, связанных с незакрытыми файлами.

#Пример чтения файла с использованием контекстного менеджера:


# with open('задачи/dfv.py', 'r') as file:
#     content = file.read()
#     print(content)
# try:
# 	file = open('задачи/dfvcgc.py', 'r')
# 	print(file.read())
# 	file.close()
# except FileNotFoundError as fil:
# 	print(fil)
# finally:
# 	file.close()


try:
	with open('задачи/dfvcgc.py', 'r', encoding='utf-8') as file:
		print(file.read())
except FileNotFoundError as fil:
	print(fil)








