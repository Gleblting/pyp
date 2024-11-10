class bankacount:

	def __init__(self, name, balans):
		print('new object')
		self.name = name
		self.balans = balans

	def __add__(self, other):
		print('--------', '\nmetod add')
		if isinstance(other, bankacount):
			return self.balans + other.balans
		if isinstance(other, (int, float)):
			return self.balans + other
			# return bankacount(self.name, self.balans + other)
		return NotImplemented
		# if isinstance(other, (int, float)):
		# 	return bankacount(self.balans + other)
	def __mul__(self, other):
		print('--------', '\nmetod mul')
		if isinstance(other, bankacount):
			return self.balans * other.balans
		if isinstance(other, (int, float)):
			return self.balans * other
		if isinstance(other, str):
			return self.name + other
		raise NotImplemented

	def __cli2add__(self, other):
		print('naoborot')
		return self+other

	def __repr__(self): #отвечают за текстовое изображение в системе для разр
		return f"client - {self.name} c balansom - {self.balans}"

	def __sub__(self, other):
		print('--------', '\nmetod sub')
		if isinstance(other, bankacount):
			return self.balans - other.balans
		if isinstance(other, (int, float)):
			return self.balans - other

cli = bankacount('gleb', 200)
print(cli.balans)#1
print(cli.balans + 100)#2
print(cli + 400)#3 noy
# print(cli + 'bbbj')#4 noy

cli2 = bankacount('maks', 800)
print(cli + cli2)
print(cli2 + cli)
# print(10 + cli2)# no
print(cli2.__add__(10))
# print((10).__add__(cli2))
# print((70) + cli2)

#___________________mul* sub- truediv /
# print(cli * 3)

print(cli*2)
print(cli*'jb')

cl3 = bankacount('hvv', 60)
print(cl3-20)

