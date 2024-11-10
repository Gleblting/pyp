# class bulding:
#
# 	year = None
# 	city = None
#
# 	def __init__(self, year, city):
# 		self.year = year
# 		self.city = city
# 		# print(self.year, self.city)
#
# 	def get_info(self):
# 		print(self.year, self.city)
#
#
# shcol = bulding(2000, 'moscow')
#
# hous = bulding(1980, 'brinsk')
#
# shop = bulding(1970, 'vladivostok')
#_______________________________________________________________________________________________
# class bulding:
# 	year = None
# 	city = None
#
# 	def __init__(self, year, city):
# 		self.year = year
# 		self.city = city
#
# 	# print(self.year, self.city)
#
# 	def get_info(self):
# 		print(self.year, self.city)
#
# class shcol(bulding): # наследование
# 	pass
#
# shcol = bulding(2000, 'moscow')
# shcol.get_info()
#
# hous = bulding(1980, 'brinsk')
#
# shop = bulding(1970, 'vladivostok')

#_______________________________________________________
class bulding:
	year = None
	city = None

	def __init__(self, year, city):
		self.year = year
		self.city = city

	# print(self.year, self.city)

	def get_info(self):
		print(self.year, self.city)

class shcol(bulding): # наследование

	pipuls = 10


	def __init__(self, pipuls, year, city):
		super(shcol, self).__init__(year, city)
		self.pipuls = pipuls
		print(self.pipuls ,self.year, self.city)
	# def __init__(self, pipuls, year, city):
	# 	self.pipuls = pipuls

class hous(shcol): # дин класс родитель
	pass # вложенное наследование

class shop(bulding):
	pass
shcol = shcol(34, 2000, 'moscow')


hous = bulding(1980, 'brinsk')

shop = bulding(1970, 'vladivostok')