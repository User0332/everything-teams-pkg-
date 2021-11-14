import random
import time as t
import sys
from everything.console.colors import colors
from everything.randomkey import Randomkey
import importfuncs


code = ''''''


def animateprint(string):
	print_index = 0
	while True:
		if print_index > len(code):
			break
		else:
			sys.stdout.write(colors.RED + code[print_index:print_index + 1] + colors.ENDC)
			sys.stdout.flush()
		print_index += 1
		t.sleep(0.1)


def forloop(start, stop, var):
	if start > stop:
		stop1 = start
		start = stop
		stop = stop1
	return f'for {var} in range({start}, {stop}):'
	
varnames = 'qwertyuiopasdfghjklzxcvbnm'
varnames = list(varnames)
varnames.append('myvar')
varnames.append('num')
varnames.append('letter')
varnames.append('var')
varnames.append('variable')
varnames.append('number')
varnames.append('mystring')
varnames.append('mylist')
varnames.append('mynum')
varnames.append('be')
varnames.append('bee')
varnames.append('fox')
varnames.append('dog')
varnames.append('cat')
varnames.append('animal')
varnames.append('lion')
varnames.append('tree')
varnames.append('shrubs')
varnames.append('jaguar')
varnames.append('frog')
varnames.append('mouse')
varnames.append('ee')
varnames.append('eeee')
varnames.append('eeeee')
varnames.append('eeeeee')
varnames.append('eeeeeee')
varnames.append('eeeeeeee')
varnames.append('lotofvar')
varnames.append('_variable_')
varnames.append('thisvar')
varnames.append('soda')
varnames.append('water')
varnames.append('food')
varnames.append('pizza')
varnames.append('car')
varnames.append('van')
varnames.append('truck')
varnames.append('tire')
varnames.append('wheel')
varnames.append('chair')
varnames.append('desk')
varnames.append('computer')
varnames.append('classroom')
varnames.append('obj')
varnames.append('myarray')
varnames.append('mydict')
varnames.append('window')
varnames.append('pencil')
varnames.append('pen')
varnames.append('auto')
varnames.append('mobile')
varnames.append('automobile')
varnames.append('test')
varnames.append('assesment')
varnames.append('quiz')
varnames.append('pop')
varnames.append('quizzes')
varnames.append('grade')
varnames.append('state')
varnames.append('condition')
varnames.append('status')
varnames.append('system')
varnames.append('door')
varnames.append('picture')
varnames.append('frame')
varnames.append('button')
varnames.append('main')
varnames.append('js')
varnames.append('code')
varnames.append('tab')
varnames.append('run')
varnames.append('book')
varnames.append('bookmark')
varnames.append('mark')
varnames.append('karma')
varnames.append('cool')
varnames.append('lol')
varnames.append('userinput')
varnames.append('project')
varnames.append('projector')
varnames.append('line')
varnames.append('easter')
varnames.append('egg')
varnames.append('easteregg')
varnames.append('secret')
varnames.append('pwd')
varnames.append('password')
varnames.append('wait')
varnames.append('_time_')
varnames.append('locked')
varnames.append('installthis')
varnames.append('create_var')
varnames.append('myvar22')
varnames.append('myvar1')
varnames.append('myvar2879')
varnames.append('okcool')
varnames.append('pythoniscool')
varnames.append('varname')
varnames.append('myvarname')
varnames.append('lockeddoor')
varnames.append('opendoor')
varnames.append('closeddoor')
varnames.append('scroll')
varnames.append('scrollwheel')
varnames.append('track')
varnames.append('trackpad')
varnames.append('click')
varnames.append('leftclick')
varnames.append('rightclick')
varnames.append('leftmousebutton')
varnames.append('rightmousebutton')
varnames.append('leftmouseclick')
varnames.append('rightmouseclick')
varnames.append('mymath')
varnames.append('thisvar123')
varnames.append('aspdotnet')
varnames.append('runningoutofvarnames')
varnames.append('lolthesevarnames')
varnames.append('sorandom')

importarray = ['os', 'random', 'sys', 'time']

possible = [importarray, 'forloop', 'whileloop', 'array', 'input', varnames, 'func', 'class', 'obj', 'file', 'print']

code_vars = []
imported = []





def printvar(num):
	global code
	global code_vars
	for i in range(0,num):
		code+=f'print({code_vars[random.randint(0, len(code_vars)-1)]})\n'


def imports():
	global code
	for i in range(0, random.randint(0,len(importarray))):
		code+=f'import {importarray[i]}\n'
		imported.append(importarray[i])

	code+='\n'

def createvar(num):
	global code
	for i in range(0, num):
		try:
			varname = varnames[random.randint(0, len(varnames)-1)]
			code+=f'{varname} = "{Randomkey.mix(10, "all", False)}"\n'
			varnames.remove(varname)
			code_vars.append(varname)
		except ValueError:
			print('Too many lines.')
			exit(0)
	
	code+='\n'


def main():
	global code
	global varnames

	loop = int(input('Lines: '))
	imports()
	for i in range(0, loop):
		codetype = random.randint(0, len(possible)-1)
		if possible[codetype] == 'forloop':
			pass

	createvar(loop)
		
	printvar(loop)

	
	animateprint(code)

main()

print('\n\n')
run = str(input('Execute? (y/n): '))
if run == 'y':
	print('\n\n')
	print('Executing: ')
	t.sleep(1)
	print('.')
	t.sleep(1)
	print('..')
	t.sleep(1)
	print('...')
	print('\n')
	t.sleep(1)
	exec(code)