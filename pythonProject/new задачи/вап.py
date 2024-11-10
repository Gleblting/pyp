s = input("Введите строку: ")
substring = input("Введите подстроку: ")

# Поиск всех вхождений подстроки
positions = []
pos = s.find(substring, 2, 5)
print(pos)