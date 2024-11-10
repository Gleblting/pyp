def decorator(fun): # Функция которая принимает другую функцию и возвращает функцию используются
# используются  чтобы изменить поведение функции не меняя  кода самой функцииб добавить какой лтбо функц
	def inner(*args, **kwargs): # пробрасывать аргументы *args, **kwargs
		print('start')
		fun(*args, **kwargs) # *args, **kwargs
		print('end')
	return inner

def obver(fun): # Функция которая принимает другую функцию и возвращает функцию используются
# используются  чтобы изменить поведение функции не меняя  кода самой функцииб добавить какой лтбо функц
	def inner(*args, **kwargs): # пробрасывать аргументы *args, **kwargs
		print('s2')
		fun(*args, **kwargs) # *args, **kwargs
		print('e2')
	return inner

@obver
@decorator # # say = decorator(say)
def say(n, a):
	print('Hello', n, a)

say('maks', 18)

# say = obver(decorator(say))
# say('maks', 18)