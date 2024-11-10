class point:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __len__(self):
		print('len')
		return abs(self.x - self.y)

	def __bool__(self):
		print('bool')
		return self.x != 0 or self.y != 0


p1 = point(1, 5)
print(bool(p1))
p2 = point(5, 5)
print(bool(p2))

p3 = point(0, 0)
print(bool(p3))
p4 = point(2, 3)
if p4:
	print('hello')
