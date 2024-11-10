#eq == / ne != / lt < / le <= / gt > / ge >=
class pramoug:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	@property
	def area (self):
		return self.a * self.b

	def __eq__(self, other):
		print('EQ')
		if isinstance(other, pramoug):
			return self.a == other.a and self.b == other.b

	def __lt__(self, other):
		print('lt')
		if isinstance(other, pramoug):
			return self.area < other.area
		elif isinstance(other, (int, float)):
			return self.area < other

	def __le__(self, other):
		print('le')
		return self == other or self < other


p1 = pramoug(1, 6)
print(id(p1))

p2 = pramoug(1, 6)
print(id(p2))
print(p1 == p2)

p3 = pramoug(2, 8)
print(p1 == p3)


print(p1 < p3)
print(p3 < p1)
print(p1.area)
print(p1 < 12)
# print(12 < p1)
print(p3 > p1)
print(p1 <= p2)
print(p1 <= p3)

