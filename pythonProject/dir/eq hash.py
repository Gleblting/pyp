class point:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __eq__(self, other):
		print('eq')
		return isinstance(other, point) and self.x == other.x and self.y == other.y
	def __hash__(self):
		return hash((self.x, self.y))

p1 = point(1, 5)
print(id(p1))
p2 = point(1,5)
p3 = point(2,3)
print(id(p2))
print(p1==p2)
print(hash(p1))
print(hash(p2))
print(hash(p3))
# print(hash[1, 3, 4])



