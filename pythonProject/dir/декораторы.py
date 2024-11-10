def decorator(fun): # Функция которая принимает другую функцию и возвращает функцию используются
# используются  чтобы изменить поведение функции не меняя  кода самой функцииб добавить какой лтбо функц
	def inner(n): # пробрасывать аргументы *args, **kwargs
		print('start')
		fun(n) # *args, **kwargs
		print('end')
	return inner
#
# def say(name):
# 	print('Hello', name)

def bay():
	print('Hgs')
# d = decorator(say)
# print(say)
# d()
# say = decorator(say)
# say('maks')


bay = decorator(bay)
bay()