import os

path = 'C:\\vscode'
# print(os.listdir(path))
# for papka in os.listdir(path):
# print(papka, type(papka), path + '\\' + papka, os.path.isdir(path + '\\' + papka))

def obxod(path, level=1):
	print('LEVEL=', level, 'CONTENT=', os.listdir(path))
	for papka in os.listdir(path):
		if os.path.isdir(path+'\\'+papka):
			print('Спускаемся', path+'\\'+papka )
			obxod(path+'\\'+papka, level+1)
			print('Возвращаемся в', path)
obxod(path)

