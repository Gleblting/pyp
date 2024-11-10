# class cat:
# 	name = None # поля
# 	age = None
# 	color = None
#
# cat1 = cat() # объекты
# cat1.name = 'Barsik'
# cat1.age = '18'
# cat1.color = 'white'
#
# cat2 = cat()
# cat2.name = 'koxa'
# cat2.age = '16'
# cat2.color = 'ryzi'
#
# print(cat1.name)
# print(cat2.name)
#____________________________________________________________________________________________________
class cat:
	name = None
	age = None
	color = None

	def set_data(self,nam, age, color): # metod
		self.name = nam
		self.age = age
		self.color = color

	def get_data(self):
		print('name', self.name, 'age', self.age ) # обращение к полям класа через self


cat1 = cat()
cat1.set_data('Barsik','18','white')
cat1.get_data()

cat2 =cat()
cat2.set_data('koxa','16','ryzi')
cat2.get_data()

