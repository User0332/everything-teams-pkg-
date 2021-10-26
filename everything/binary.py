from everything.rand import rand

class byte():
	def generate():
		try:
			key = ''
			for i in range(0, 8):
				key+=str(rand.int(0,1))
			
			return key

		except Exception as e:
			print(e)

class bit():
	def generate():
		try:
			return str(rand.int(0,1))

		except Exception as e:
			print(e)