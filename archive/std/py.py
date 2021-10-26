from everything.customexceptions import StdErr1


def using_namespace(namespace):
	if namespace == '<stdio>':
		return '''import sys

class stdio:
	def write(string):
		sys.stdout.write(string)
		return 0

	def scan():
		return input()[0]'''

	elif namespace == '<stdos>':
		return '''from os import system as systcmd, name as osname

class stdos():
	def system(command):
		systcmd(command)
		return 0
	
	def clear():
		if osname == 'nt':
			stdos.system("cls")
		else:
			stdos.system("clear")

	def readfile(file):
		with open(file, 'r') as f:
			return f.read()

	def writefile(file, string):
		with open(file, 'w') as f:
			f.write(string)
		return 0'''
	elif namespace == '<stddelay>':
		return '''import time as t

def stddelay(milliseconds):
	t.sleep(milliseconds/1000)
	return 0'''


	pathnamespace = namespace.replace(".", "/")
	try:
		with open(f"{pathnamespace}.py", 'r') as f:
			functions = f.read()
			return functions
	except OSError:
		raise StdErr1(namespace)