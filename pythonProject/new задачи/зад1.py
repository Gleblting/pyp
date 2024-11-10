
num1 = float(input("Введи первое число: "))
num2 = float(input("Введи второе число: "))
num3 = float(input("Введи третье число: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("Наибольшее число из трех чисел", largest)
