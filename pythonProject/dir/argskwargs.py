list1 = [1, 2, 3, 4, 5]
# # a, b, c = list1
# a, *b, c = list1
# print(a, b, c)
# def my_args(*args):
# my_args(3, 6, 7)
# def my_fun(p1, p2, p3, p4, p5):
#     print(p1, p2, p3, p4, p5)
#
#
# my_fun(*list1)
# my_dict = {
#     'name': 'gleb',
#     'age': 25
# }
#
# raspacovka = {
#     **my_dict,
#     'new_key': 'hello'
# }
# print(raspacovka)
# my_dict2 = {
#     'name': 'gleb',
#     'age': '26',
#     'man': True
# }
# sum_dict = my_dict | my_dict2
# print(sum_dict)
my_dict = {
    'name': 'gleb',
    'age': 25
}
def raspovka_slovar(key1, kry2):
    print(key1, kry2)

raspovka_slovar(**my_dict)

# def f(**kwargs):
#     print(kwargs)
#
# f(a=1, b=4, c=6)