def	filter_list(spisok, val):
	sp_end = []
	for i in spisok:
		if type(i) is val:
			sp_end.append(i)
	return sp_end



res = filter_list([2, 4, 3.5, True, 'stroka'], float)
print(res)