from os import walk, name
from os.path import join

def find(*filenames):
	if name == 'nt':
		directory = 'C:\\'
	else:
		directory = '/home'

	found = []

	for path, directories, files in walk(directory):
		for file in files:
			for correct in filenames:
				if file == correct:
					print('found', join(path, file))
					found.append(join(path, file))

	return found
	
		


