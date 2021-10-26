import math
from everything.rand import rand
from everything.customexceptions import numberNotOperableException




pi = 3.141592653589

class mathfuncs():
	global pi
		
	class rect():
		'''This is to "create" a rectangle'''
		length = 0
		width = 0
		area = length*width
		perimeter = length*2 + width*2
		def __init__(self,length , width):
			try:
				self.length = length
				self.width = width
				self.area = length*width
				self.perimeter = length*2+width*2
			except:
				raise numberNotOperableException
		def map(self):
			'''Create tkinter window and display rect'''




		'''These are static methods'''
		def getarea(length, width):
			try:
				return length*width
			except:
				raise numberNotOperableException
		def getperimeter(area = None, length = None, width = None):
			try:
				if area == None and length and width != None:
					return length*2 + width*2
				elif area != None and length != None:
					return length*2 + area/length*2
				elif area != None and width != None:
					return width*2 + area/width*2
				else:
					print('Not enough data.')
			except:
				raise numberNotOperableException
		
	class square():
		'''This is to "create" a square'''
		length = 0
		area = length*length
		perimeter = length*4
		def __init__(self, length):
			try:
				self.length = length
				self.area = mathfuncs.power(length, 2)
				self.perimeter = length*4
			except:
				raise numberNotOperableException
			
		def map(self):
			'''Create tkinter window and display square'''


		'''These are static methods'''
		def getarea(length):
			try:
				return length*length
			except:
				raise numberNotOperableException
		def getperimeter(length = None, area = None):
			try:
				if length == None and area != None:
					return math.sqrt(area)*4
				elif area == None and length != None:
					return length*4
				else:
					print('Not enough data.')
			except:
				raise numberNotOperableException
			
	
	class circle():
		'''This is to "create" a circle'''
		diameter = 0
		radius = diameter/2
		area = radius*radius*pi
		circumference = diameter*pi
		def __init__(self, diameter):
			try:
				self.diameter = diameter
				self.radius = diameter/2
				self.area = self.radius*self.radius*pi
				self.circumference = self.diameter*pi
			except:
				raise numberNotOperableException
		
		def map(self):
			'''Create tkinter window and display circle'''


		'''These are static methods'''
		def getarea(radius):
			try:
				return radius*radius*pi
			except:
				raise numberNotOperableException
		def getcircumference(diameter):
			try:
				return diameter*pi
			except:
				raise numberNotOperableException

	class cube():
		def getvolume(length):
			try:
				return length*length*length
			except:
				raise numberNotOperableException

	class random():
		def int(x,y):
			try:
				return rand.int(x,y)
			except:
				raise numberNotOperableException
	
		def float(x,y):
			try:
				return rand.uniform(x,y)
			except:
				raise numberNotOperableException

	def add(*nums):
		answer = 0
		try:
			for i in range(0, len(nums[0])):
				answer += nums[0][i]
		except:
				raise numberNotOperableException
			 
		return answer

	def multiply(*nums):
		answer = 1
		try:
			for i in range(0, len(nums[0])):
				answer *= nums[0][i]
		except:
				raise numberNotOperableException
			 
		return answer

	def divide(*nums):
		answer = nums[0][0]	
		try:
			for i in range(1, len(nums[0])):
				answer /= nums[0][i]
		except:
				raise numberNotOperableException
			 
		return answer

	def subtract(*nums):
		answer = nums[0][0]
		try:
			for i in range(1, len(nums[0])):
				answer -= nums[0][i]
			return answer
		except:
				raise numberNotOperableException
	
	def pwr(x,y):
		try:
			answer = 1
			for i in range(0,y):
				answer*=x
			return answer
		except:
				raise numberNotOperableException
	
	def sqrt(x):
		try:
			return math.sqrt(x)
		except:
				raise numberNotOperableException 
	
	def abs(x):
		try:
			if x < 0:
				x*=-1
			return x
		except:
				raise numberNotOperableException
			 
	def lcm(x,y):
		try:
			return mathfuncs.abs(x*y) // mathfuncs.gcd(x,y)
		except:
				raise numberNotOperableException
			 
	def gcf(x,y):
		try:
			i = 2
			factors = []
			factors2 = []
			possible = []
			while i * i <= x:
				if x % i:
					i += 1
				else:
					x //= i
					factors.append(i)
			if x > 1:
				factors.append(x)
				
			i = 2
			while i * i <= y:
				if y % i:
					i += 1
				else:
					y //= i
					factors2.append(i)
			if y > 1:
				factors2.append(y)

			for i in range(0, len(factors)):
				for j in range(0, len(factors2)):
					if factors[i] == factors2[j]:
						possible.append(factors[i])
			gcf = 1
			for i in range(0, len(possible)):
				gcf*=possible[i]
			
			return gcf
		except:
				raise numberNotOperableException
			 

	def gcd(x,y):
		try:
			return math.gcd(x,y)
		except:
				raise numberNotOperableException