class spisok:

	def __init__(self, *args):
		self.values = list(args)

	def __repr__(self):
		return str(self.values)

s1 = spisok(1,2,546,757)
print(s1)
