class mashin:

	def __init__(self, name):
		self.name = name


	def __repr__(self): #отвечают за текстовое изображение в системе для разр
		return f"Hello ob - {self.name}"

	def __str__(self): #отвечают за текстовое изображение в системе для пользователя
		return f"car - {self.name}"

# mas = mashin('tayta')
# print(mas)

# m = mashin('bmv')
# print(m)

n = mashin('lexsus')
n
# print(n)