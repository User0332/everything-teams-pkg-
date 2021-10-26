import os
import time as t
import sys
import datetime
from everything.customexceptions import notEnoughInfoException

class Console():
	def write(message):
		sys.stdout.write(message)
		
	def read(prompt, type = None):
		if type == str:
			return str(input(prompt))
		elif type == int:
			return int(input(prompt))
		elif type == float:
			return float(input(prompt))
		elif type == complex:
			return complex(input(prompt))
		elif type == bool:
			return bool(input(prompt))
		else:
			return input(prompt)

	def clear():
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')

	def newlines(newlines):
		for i in range(0, newlines):
			print('')
	
	def fileread(file, splitlines = False):
		if splitlines == True:
			with open(file, 'r') as f:
				data = f.read().splitlines()
				return data
		elif splitlines == False:
			with open(file, 'r') as f:
				data = f.read()
				return data
	
	def filereadprint(file, splitlines = False, index=0):
		if splitlines == True:
			with open(file, 'r') as f:
				data = f.read().splitlines()
				print(data[index])
		elif splitlines == False:
			with open(file, 'r') as f:
				data = f.read()
				print(data)
	
	def printlist(var):
		print(list(var))

	def printtuple(var):
		print(tuple(var))
	
	def error(error):
			raise error

	def exception(exception):
			raise exception

	def debug(message, filename, line, log = False):
		if log == True:
			with open('debug.log', 'a') as f:
				f.write(f'\n\nAt {datetime.datetime.now()} in file {filename}, line {line} - Debug: {message}')
		print(f'{colors.WARNING}\nAt {datetime.datetime.now()}:\n	File {filename}, line {line} - Debug Log: {message}\n{colors.ENDC}')
	
	def deletelog():
		os.remove('debug.log')

	def clearlog():
		with open('debug.log', 'a') as f:
			pass
		os.remove('debug.log')
		with open('debug.log', 'a') as f:
			pass
		
	def indent(message, indents):
		indent = ''
		for i in range(0, indents):
			indent+='	'
		print(indent+message)

	def exec(code = None, file = None, prefix = '\nEXEC START{\n', suffix = '\n}EXIT\n'):
		if code != None:
			pass
		elif file != None:
			with open(file, 'r') as f:
				code = f.read()
		elif file == None and code == None:
			raise notEnoughInfoException
		
		print(prefix)
		exec(code)
		print(suffix)
	
	def log(message):
		with open('debug.log', 'a') as f:
			f.write(message)

	def animate(message, color='', delay=0.1):
		print_index = 0
		while True:
			if print_index > len(message):
				break
			else:
				sys.stdout.write(color + message[print_index:print_index + 1] + Colors.ENDC)
				sys.stdout.flush()
			print_index += 1
			t.sleep(delay)
		

class Colors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	GREEN = '\033[32m'
	WARNING = '\033[93m'
	RED = '\033[1;31m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'