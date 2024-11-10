# public, protected (ащищенные 1 черточки), privie(риватные 2 черточки) инкапсуляция (скрытие)
class cat:

	def __init__(self, name, age=10, color=None):
		self.__name = name
		self.__age = age
		self.__color = color
		# self.get_data()

	# def set_data(self,name, age, color = None): # metod
	# 	self.name = name
	# 	self.age = age
	# 	self.color = color

	def __get_data(self):
		print('name', self.__name, 'age', self.__age, 'color', self.__color ) # обращение к полям класа через self

	def print_data(self):
		self.__get_data()

cat1 = cat('Barsik','17','white')
# cat1.set_data('Barsik','18')
# cat1.__get_data()
# print(cat1._color)
cat1.print_data()
print(dir(cat1))
print(cat1._cat__color)