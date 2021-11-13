from everything.customexceptions import randomCalculationFailedException, invalidSeedException
import datetime


class rand():
	seed = 0
	
	def check(start, stop, randomnum):
		randomnumint = int(randomnum)
		try:
			if float(randomnumint) == randomnum:
				return rand.uniform(start, stop)
			if start < randomnum < stop:
				return randomnum
			elif randomnum < start:
				randomnum+=rand.uniform(1,start-5)
				return rand.check(start, stop, randomnum)
			elif randomnum > stop:
				randomnum-=rand.uniform(1,stop+5)
				return rand.check(start, stop, randomnum)
		except RecursionError:
			return float(start)
			
	def clear_seed():
		rand.seed = 0

	def getseed():
		seed = str(datetime.datetime.now())
		seed = seed.replace('-', '')
		seed = seed.replace(':', '')
		seed = seed.replace('.', '')
		seed = seed.replace(' ', '')
		seed = seed.replace('0', '1')
		seed = list(seed)
		for i in range(0, len(seed)):
			seed[i] = int(seed[i])
		
		rand.seed = seed
		return seed

	def uniform(start, stop):
		try:
			if start == stop:
				return start
			if stop < start:
				raise randomCalculationFailedException('Stopping point is less than starting point')
			if rand.seed != 0:
				if type(rand.seed) == list:
					seed = rand.seed
				else:
					seed = list(str(seed))
					for i in range(0, len(seed)):
						seed[i] = int(seed[i])
			else:
				seed = rand.getseed()

			randomnum = seed[0]
			counter = 1
			while True:
				if counter > 50:
					return rand.uniform(start, stop)
				elif counter > 10 and start < randomnum < stop:
					break
				for i in range(1,19):
					if randomnum > stop:
						randomnum/=seed[i]
					else:
						randomnum*=seed[i]
						
				counter+=1				
			
			return rand.check(start, stop, randomnum)
		except RecursionError:
			return float(start)
		except UnboundLocalError:
			return rand.uniform(start, stop)


			
	def int(start, stop):
		return int(rand.uniform(start, stop))