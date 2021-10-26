class Console():
	def WriteLine(values, sep = None, end = '\n', file = None, flush = False):
		print(values, sep = sep, end = end, file = file, flush = flush)

	def ReadLine(prompt):
		return input(prompt)