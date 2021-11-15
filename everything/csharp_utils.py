def run(filename):
	try:
		file = importlib.import_module(filename[0:-3])
	except ModuleNotFoundError:
		raise FileNotFoundError(f"File {filename} was not found.")
	try:
		for name in dir(file):
			if name == "Main":
				getattr(file, name)()
	except AttributeError as e:
		if str(e) == f"partially initialized module '{filename[0:-3]}' has no attribute 'main' (most likely due to a circular import)":
			raise MainEntryNotFoundError(filename)
		else:
			raise e
      
      
  
