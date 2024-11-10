# def wraper(): #внешняя функцияобласть видм=имости фуекция инер
# 	name = 'Maks'
# 	def inner(): # внутрення фцнуция у которой своя локальная зона видимости но она использует внешнюю функцию
# 		print('Меня зовут', name)
# 	return inner # чтобы вызвать замыкание нужно вернуть внутрению функцию не вызывая ее
# imy = wraper()
# print(imy) # ссылается на вложенную функию инер,которая находиться в врапер функ
# imy()
# imy2 = wraper()
# imy2()
# imy()


# def wraper(value):
# 	name = value # начение в переменной не исчезает
# 	def inner():
# 		print('Меня зовут', name)
# 	return inner
# imy = wraper('Gleb')
# imy()
# imy22 = wraper('Maks')

def add(value):
	def inner(a):
		return value + a
	return inner

per1 = add(5)
print(per1)
print(per1(2)) # per1 принимает значение функ иннер
# per2 = add(10)
# print(per2(4))
# print(per1(6))

# def counter():
# 	count = 0
# 	def inner():
# 		nonlocal count # указание что ссылаюсь на переменную находящую не в локальной зоне видимости
# 		count += 1
# 		return count
# 	return inner
#
# a = counter()
# print(a)
# print(a())
# print(a())
# print(a())

# def add(a, b):
# 	return a + b
#
# def counter(fun):
# 	count = 0
# 	def inner(*args, **kwargs):
# 		nonlocal count
# 		count += 1
# 		print(f"функция {fun.__name__} вызывавалась {count} раз ")
# 		return fun(*args, **kwargs)
# 	return inner
#
# per1 = counter(add) # в пер1 записываетя функция инер
# print(per1(10, 20))
# print(per1(15, 5))
#
# def umnoj(a, b, c):
# 	return a * b * c
# per2 = counter(umnoj)
# print(per2(15, 5, 1))





