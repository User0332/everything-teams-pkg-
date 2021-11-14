import time as t
import sys
import os
try:
	import getch
except ImportError:
	os.system('pip uninstall getch -y')
	os.system('pip install getch')
	import getch
from everything.console import Console
from everything.console import colors
from everything.rand import rand

#fakecoding
Console.clear()

files = ['fakecode.txt', 'fakecode2.txt', 'fakecode3.txt', 'fakecode4.txt']

def fakecode():
	with open(f'fakecode/{files[rand.int(0,3)]}', 'r') as f:
			code = f.read()

	sequence = ['|','/','―','\\']
	for i in range(5):
		for i in range(0, 4):
			print(f'Loading: {sequence[i]}')
			t.sleep(0.25)
			Console.clear()



	print('Do you want to type? (y/n): ')
	typeinput = getch.getch()
	if  typeinput == 'y':
		typing = True
	elif typeinput == 'Y':
		typing = True
	else:
		print('Okie dokie - watch and enjoy')
		t.sleep(2)
		typing = False
	
	print_index = 0

	if typing:
		print('Get ready to type furiously')
		t.sleep(2)

		count = 3
		

		while count > 0:
			if count == 3: print(f'In {count}') 
			else: print(count)
			t.sleep(1.25)
			count-=1

		print('GO!')
	
	while True:
		if typing:
			char = getch.getch()
		if print_index > len(code):
			break
		else:
			sys.stdout.write(colors.RED + code[print_index:print_index + 1] + colors.ENDC)
			sys.stdout.flush()
		print_index += 1
		if not typing:
			t.sleep(0.01)

	for i in range(15):
		Console.clear()
		t.sleep(0.2)
		print(f'{colors.OKGREEN}\n\nACCESS GRANTED\n\n{colors.ENDC}')	
		t.sleep(0.2)
	
	Console.clear()
	print('exiting...')
	t.sleep(2)
	print('lol what a joke')



fakecode()

