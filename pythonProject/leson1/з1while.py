s = input("Введите строку: ")
vowels = "aeiouAEIOU"
count = 0
index = 0
while index < len(s):
    if s[index] in vowels:
        count += 1
    index += 1
print("Количество гласных в строке:", count)