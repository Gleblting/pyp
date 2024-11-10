try:
	print(10 / 0 )
except ZeroDivisionError as e:
	print(e)
# except TypeError as e:
# 	print(e)
# else:
# 	print('cod is god')
# finally:
# 	print('all')
except Exception as e:
	print(e)
print('Continue...')
