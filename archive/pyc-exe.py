from py_compile import compile
from sys import argv
from time import sleep as delay
from everything.console import Colors
from os import chdir, getcwd

rootdir = getcwd()

if len(argv) == 1:
	print(f'{Colors.RED}File not specified.{Colors.ENDC}')
	delay(5)
else:
	with open(argv[1], 'r') as f:
		code = f.read()

	if '\\' in argv[1] or '/' in argv[1]:
		dr2 = argv[1].rsplit('/', 1)[0]
		dr = argv[1].rsplit('\\', 1)[0]
	else:
		dr = ""
		dr2 = ""
	print('Exec? (Y/n)')
	exc = input()
	cdr = False
	if exc == 'Y' or exc == 'y':
		try:
			try:
				chdir(dr)
				cdr = True
			except NotADirectoryError:
				chdir(dr2)
			except FileNotFoundError:
				chdir(dr2)
		except FileNotFoundError:
			pass
		except NotADirectoryError:
			pass
		exec(code)
		chdir(rootdir)
	delay(2)
	filename = argv[1].replace(".py", "").replace(dr, "").replace(dr2, "")
	try:
		compile(argv[1], f'{dr+"/" if cdr else dr2+"/"}__pyc-exe__/build/{filename}.pyc', argv[1], True)
	except OSError:
		print('Script not in any subdirectory, diverting to active executing script location')
		compile(argv[1], f'__pyc-exe__/build/{filename}.pyc', argv[1], True)
	'''with open('') as f:
		pass
		write some random stuff
	'''
	print(f'Successfully compiled {argv[1]} to pyc (python bytecode)')

	