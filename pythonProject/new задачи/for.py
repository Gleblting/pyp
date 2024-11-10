#Простые числа, это те числа, которые делятся без остатка только на 1 и
# на само себя. Самое маленькое простое число, это 2. И так, приступим к коду.

lower = 900
upper = 1000

print("Диапазон чисел между", lower, "и", upper)

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

