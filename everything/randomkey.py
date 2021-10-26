from everything.customexceptions import letterCaseNotFoundException, specialCharacterNotSpecifiedException
from everything.rand import rand
from everything.defaultarrays import upletters, lowletters, numbers, specialchars

class Randomkey():
	def mix(length, case, special):
		try:
			key = ''
			if special == True:
				if case == 'lower':
					for i in range(0, length):
						randomnum = rand.int(1,3)
						if randomnum == 1:
							key+=numbers[rand.int(0,len(numbers)-1)]
						elif randomnum == 2:
							if rand.int(1,2) == 1:
								key+=lowletters[rand.int(0, len(lowletters)-1)]
						else:
							key+=specialchars[rand.int(0, len(specialchars)-1)]
				elif case == 'upper':
					for i in range(0, length):
						randomnum = rand.int(1,3)
						if randomnum == 1:
							key+=numbers[rand.int(0,len(numbers))]
						elif randomnum == 2:
							if rand.int(1,2) == 1:
								key+=upletters[rand.int(0, len(upletters)-1)]
						else:
							key+=specialchars[rand.int(0, len(specialchars)-1)]
				elif case == 'all':
					for i in range(0, length):
						randomnum = rand.int(1,3)
						if randomnum == 1:
							key+=numbers[rand.int(0,len(numbers)-1)]
						elif randomnum == 2:
							if rand.int(1,2) == 1:
								key+=upletters[rand.int(0, len(upletters)-1)]
							else:
								key+=lowletters[rand.int(0, len(lowletters)-1)]
						else:
							key+=specialchars[rand.int(0, len(specialchars)-1)]

				else:
					raise letterCaseNotFoundException(case)
			elif special == False:
				if case == 'lower':
					for i in range(0, length):
						if rand.int(1,2) == 1:
							key+=numbers[rand.int(0,len(numbers)-1)]
						else:
							if rand.int(1,2) == 1:
								key+=upletters[rand.int(0, len(upletters)-1)]
							else:
								key+=lowletters[rand.int(0, len(lowletters)-1)]
				elif case == 'upper':
					for i in range(0, length):
						if rand.int(1,2) == 1:
							key+=numbers[rand.int(0,len(numbers)-1)]
						else:
							if rand.int(1,2) == 1:
								key+=upletters[rand.int(0, len(upletters)-1)]
							else:
								key+=lowletters[rand.int(0, len(lowletters))]
				elif case == 'all':
					for i in range(0, length):
						if rand.int(1,2) == 1:
							key+=numbers[rand.int(0,len(numbers)-1)]
						else:
							if rand.int(1,2) == 1:
								key+=upletters[rand.int(0, len(upletters)-1)]
							else:
								key+=lowletters[rand.int(0, len(lowletters)-1)]
				else:
					raise letterCaseNotFoundException(case)
			else:
				raise specialCharacterNotSpecifiedException(special)
			
			return key
		except letterCaseNotFoundException:
			raise
		except specialCharacterNotSpecifiedException:
			raise
		except Exception as e:
			print(e)

	def numbers(length):
		try:
			key = ''
			for i in range(0, length):
				key+=numbers[rand.int(0, len(numbers)-1)]

			return key
		except Exception as e:
			print(e)
	
	def lowercase(length):
		try:
			key = ''
			for i in range(0, length):
				key+=lowletters[rand.int(0, len(lowletters)-1)]

			return key
		except Exception as e:
			print(e)
	
	def uppercase(length):
		try:
			key = ''
			for i in range(0, length):
				key+=upletters[rand.int(0, len(upletters)-1)]

			return key
		except Exception as e:
			print(e)

	def chars(length):
		try:
			key = ''
			for i in range(0, length):
				key+=specialchars[rand.int(0, len(specialchars)-1)]

			return key
		except Exception as e:
			print(e)

	def letters(length):
		try:
			key = ''
			for i in range(0, length):
				if rand.int(1,2) == 1:
					key+=upletters[rand.int(0, len(upletters)-1)]
				else:
					key+=lowletters[rand.int(0, len(lowletters)-1)]
			
			return key
		except Exception as e:
			print(e)

	def numchars(length):
		try:
			key = ''
			for i in range(0, length):
				if rand.int(1,2) == 1:
					key+=numbers[rand.int(0, len(numbers)-1)]
				else:
					key+=specialchars[rand.int(0, len(specialchars)-1)]
			
			return key
		except Exception as e:
			print(e)

	def byte():
		try:
			key = ''
			for i in range(0, 8):
				key+=str(rand.int(0,1))
			
			return key

		except Exception as e:
			print(e)