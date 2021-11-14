class importfuncs():
	def main(imported, code):
		if 'os' in imported:
			importfuncs.osfuncs()
		elif 'time' in imported:
			importfuncs.timefuncs()
		elif 'sys' in imported:
			importfuncs.sysfuncs()
		elif 'random' in imported:
			importfuncs.randomfuncs()
	
	def osfuncs(code):
		pass

	def timefuncs(code):
		pass

	def randomfuncs(code):
		pass

	def sysfuncs(code):
		pass