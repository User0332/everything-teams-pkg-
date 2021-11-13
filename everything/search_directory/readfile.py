from os import walk, name
from os.path import join
from everything.console import Console
import time as t

cont = False

def read(limit, directory=None, print_failures=True):
	if name == 'nt':
		cont = not print_failures
		if directory == None:
			directory = 'C:/'
		print('Starting file read\n\n')
		t.sleep(3)
	else:
		cont = not print_failures
		if directory == None:
			directory = '/home'
		print('Starting file read\n\n')
		t.sleep(3)


	filedata = "Start of data:\n\n\n"

	filenames = []
	failed = []

	counter = 0

	for path, directories, files in walk(directory):
		if counter > limit:
			break
		for file in files:
			print('found', join(path, file))
			filenames.append(join(path, file))
			counter+=1
			

	for file in filenames:
			print(f'Writing {file}\'s data to string:')
			with open(file, 'r') as f:
				try:
					filedata+=f'File {file}:\n\n\n{f.read()}\n\n\n'
				
					Console.debug(f'Successfully written {file}\'s data to string', 'unknown', 'unknown',True)
				except UnicodeDecodeError:
					if not cont:
						Console.debug(f'Failed to write file to string: not a unicode character', 'unknown', 'unknown',True)

					failed.append(file)
					
	if cont:
		print('Failed to write: \n')
		for file in failed:
			print(file)



	with open('file_data.txt', 'w') as f:
		f.write(filedata)
	
	print('File data successfully copied to script location')
	t.sleep(1)

	with open('file_data.txt', 'a') as f:
		f.write('Falied:')
		for file in failed:
			f.write(file+'\n')
		
