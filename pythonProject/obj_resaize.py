my_list = [1, 2, 3]
print(my_list)
print(id(my_list))
# my_list2 = [1, 2, 3]
# print(my_list2)
# print(id(my_list2))
# my_list2.append(4)
# print(my_list2)
# print(id(my_list2))
my_list2 = my_list
print(my_list2.append(4))
print(my_list2)
print(my_list)

