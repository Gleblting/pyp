s = input("Введите строку: ")
reversed_string = ""
index = len(s) - 1
while index >= 0:
    reversed_string += s[index]
    index -= 1
print("Перевернутая строка:", reversed_string)