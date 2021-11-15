import importlib
from everything.customexceptions import MainEntryNotFoundError

def run(filename):
	try:
		file = importlib.import_module(filename[0:-3])
	except ModuleNotFoundError:
		raise FileNotFoundError(f"File {filename} was not found.")
	try:
		exit_code = file.main()
		if type(exit_code) != int:
			raise TypeError("Function int main does not return type int")
		else:
			exit(exit_code)
	except AttributeError as e:
		if str(e) == f"partially initialized module '{filename[0:-3]}' has no attribute 'main' (most likely due to a circular import)":
			raise MainEntryNotFoundError(filename)
		else:
			raise e
