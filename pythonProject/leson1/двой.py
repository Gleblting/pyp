N = int(input("Введите число N: "))
power = 0
while True:
	result = 2 ** power
	if result > N:
		break
	print(result)
	power += 1