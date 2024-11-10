class Counter:

	def __init__(self):
		self.count = 0
		print('init object', self)

	def __call__(self, *args, **kwargs):
		self.count += 1
		print(f"наш экземпляр вызывался {self.count} раз")
		# print('call ob', self)


# print(Counter())

a = Counter()
print(a)
b = Counter()
b()

с = Counter()
с()
с()
с()

