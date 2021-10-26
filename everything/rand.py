from everything.customexceptions import randomCalculationFailedException, invalidSeedException
import datetime


class rand():
	set_seed = False
	seed = 0
	
	def check(start, stop, randomnum):
		randomnumint = int(randomnum)
		if float(randomnumint) == randomnum:
			return rand.uniform(start, stop)
		if start < randomnum < stop:
			return randomnum
		elif randomnum < start:
			randomnum+=rand.uniform(1,100)
			return rand.check(start, stop, randomnum)
		elif randomnum > stop:
			randomnum-=rand.uniform(1,100)
			return rand.check(start, stop, randomnum)
			
	def set_seed(seed):
		if int(seed) != seed:
			raise invalidSeedException('Seed must be of type int')
		if len(str(seed)) != 19:
			raise invalidSeedException('Seed must be of length 19.')
		seed = list(str(seed))
		for i in range(0, len(seed)):
			seed[i] = int(seed[i])
			if seed[i] == 0:
				seed[i] = 1
		
		rand.set_seed = True
		rand.seed = seed

	def clear_seed():
		rand.set_seed = False

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
			if rand.set_seed:
				seed = rand.seed
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
			raise randomCalculationFailedException('Number gap may have been too small')


			
	def int(start, stop):
		return int(rand.uniform(start, stop))