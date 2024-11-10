#Напишите функцию, которая принимает на вход два списка целых чисел и возвращает новый список, содержащий все числа, которые есть в обоих списках.

def intersection(list1, list2):
    result = []
    for num in list1:
        if num in list2:
            result.append(num)
    return result