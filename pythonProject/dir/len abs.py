# class cat:
#
# 	def __init__(self, name, fam):
# 		self.name = name
# 		self.fam = fam
#
# 	def __len__(self):
# 		return len(self.name+self.fam)
#
# c = cat('maks', 'hvh')
# # print((-76).__abs__())
# # print('hhhh'.__len__())
#
# print(len(c))

class otrezok:

	def __init__(self, t1, t2):
		self.t1 = t1
		self.t2 = t2

	def __abs__(self):
		return abs(self.t2 - self.t1)

o = otrezok(8, 6)
print(abs(o))