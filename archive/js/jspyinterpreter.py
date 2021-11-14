from javascript import *

def code_format(jscode):
	jscode = jscode.replace(';', '')
	jscode = jscode.replace('[function]', '@<111>#')
	jscode = jscode.replace('[catch]', '@<112>#')
	jscode = jscode.replace('[throw]', '@<113>#')
	jscode = jscode.replace('dict{', '@<114>#')
	jscode = jscode.replace('}dict', '@<115>#')
	jscode = jscode.replace('array{', '@<116>#')
	jscode = jscode.replace('}array', '@<117>#')
	jscode = jscode.replace('[constructor]', '@<118>#')
	jscode = jscode.replace('{', ':')
	for i in range(0, jscode.count('}')):
		try:
			index = jscode.index('}')
			jscode = jscode.replace('}', '', 1)
			counter = index
			while True:
				if jscode[counter] == ' ':
					jscodelist = list(jscode)
					jscodelist[counter] = ''
					jscode = ''
					for i in range(0, len(jscodelist)):
						jscode += jscodelist[i]
				else:
					break
		except:
			pass
	jscode = jscode.replace('function', 'def')
	jscode = jscode.replace('catch', 'except')
	jscode = jscode.replace('throw', 'raise')
	jscode = jscode.replace('this.', 'self.')
	jscode = jscode.replace('constructor(', 'def __init__(self,')
	for i in range(0, jscode.count('var')):
		try:
			index = jscode.index('var')
			jscode = jscode.replace('var', '', 1)
			counter = index
			while True:
				if jscode[counter] == ' ':
					jscodelist = list(jscode)
					jscodelist[counter] = ''
					jscode = ''
					for i in range(0, len(jscodelist)):
						jscode += jscodelist[i]
				else:
					break
		except:
			pass
	jscode = jscode.replace('//', '#')
	jscode = jscode.replace('/*', "'''")
	jscode = jscode.replace('*/', "'''")
	jscode = jscode.replace('@<112>#', 'catch')
	jscode = jscode.replace('@<113>#', 'throw')
	jscode = jscode.replace('@<111>#', 'function')
	jscode = jscode.replace('@<114>#', '{')
	jscode = jscode.replace('@<115>#', '}')
	jscode = jscode.replace('@<116>#', '[')
	jscode = jscode.replace('@<117>#', ']')
	return jscode




def run():
	with open('js/js_test.py', 'r') as f:
		code = f.read()

	local_vars = {'console' : console}

	code = code_format(code)

	exec(code, local_vars)
