# Ввод строки и подстроки
s = input("Введите строку: ")
substring = input("Введите подстроку: ")

# Поиск всех вхождений подстроки
positions = []
pos = s.find(substring)


while pos != -1:
    positions.append(pos)
    pos = s.find(substring, pos + 1)

# Вывод результата
if positions:
    print("Подстрока найдена на позициях:", positions)
else:
    print("Подстрока не найдена")