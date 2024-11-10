
# Создаем простой калькулятор

# Эта функция складывает два числа
def add(x, y):
    return x + y

# Функция вычитания
def subtract(x, y):
    return x - y

# Функция умножения
def multiply(x, y):
    return x * y

# Функция деления
def divide(x, y):
    return x / y


print("Выберите операцию:")
print("1.Сложить")
print("2.Вычесть")
print("3.Умножить")
print("4.Делить")

while True:
    # Принимаем входные данные пользователя
    choice = input("Выберите действие(1/2/3/4): ")

    # Проверка входных данных
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Неправильный ввод")
