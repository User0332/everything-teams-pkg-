def printf(chars, *values):
	if type(chars) == str:
		print(chars, *values)
	else:
		raise TypeError("Argument \"chars\" passed to printf is not type char")