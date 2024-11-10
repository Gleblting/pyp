N = int(input())

# Создается список из значений от 0 до N включительно
primes = [i for i in range(N + 1)]

# Вторым элементом списка является единица, которую
# не считают простым числом. Забиваем ее нулем
primes[1] = 0

# Начинаем с 3-го элемента
i = 2
while i <= N:
    # Если значение текущей ячейки до этого не было обнулено,
    # значит в этой ячейке содержится простое число
    if primes[i] != 0:
        # Первое кратное ему будет в два раза больше
        j = i + i
        while j <= N:
            # и это число составное,
            # поэтому заменяем его нулем
            primes[j] = 0
            # переходим к следующему числу,
            # которое кратно i (оно на i больше)
            j = j + i
    i += 1

# Избавляемся от всех нулей в списке
primes = [i for i in primes if i != 0]
print(primes)
# Пример выполнения:
#
# 35
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]