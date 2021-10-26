class file():
	def __init__(self, filename):
		self.filename = filename


	def read(self, splitlines = False):
		with open(self.filename, 'r') as f:
			if splitlines == True:
				return f.read().splitlines()
			else:
				return f.read()

	def write(self, text):
		with open(self.filename, 'w') as f:
			f.write(text)
	
	def append(self, text):
		with open(self.filename, 'a') as f:
			f.write(text)