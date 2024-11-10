class bankacount:

	def __init__(self, name, balans):
		self.name = name
		self.__balans = balans

	def get(self):
		return self.__balans

	def set(self, value):
		if not isinstance(value, (int, float)):
			raise ValueError(' <fkfyc ljk;ty ,snm xbckjv')
		self.__balans = value

	# def del(self):
	# 	print()

	balan = property(fget=get, fset=set)



ob_cl = bankacount('ivan', 100)
# print(ob_cl.balans)
# ob_cl.balans = 200
# print(ob_cl.balans)

maks = bankacount('mis', 300)
print(maks.balan)
maks.balan = 500
print(maks.balan)
