a = {
	'dff': 12,
	'cm': 4,
}
n = {}
for key, val in a.items():
	n[key] = val * 2
print(n)


sp = [2, 5,4]
n = []
for x in sp:
	if x > 2:
		n.append(x * 2)
print(n)

# a2 = {key ,val: * 2 for key ,val a.items()}
s = [x * 2 for x in sp if x > 2]
print(s)

for element in range(1, 4):
	for element2 in range(5, 9):
		print(element, element2)

for i in "acd":
	for j in "helo":
		print(i, j)
