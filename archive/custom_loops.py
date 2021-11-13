import time as t

def _while(condition, code, vars=None):
	if not eval(condition, vars):
		return
	else:
		exec(code, vars)
		_while(condition, code, vars)

def range(start, stop=None, step=None):
	if step == None:
		increment = 1
	else:
		increment = step

	if stop == None:
		stop = start
		start = 0

	nums = []
	

	_while('start <= stop', 'nums.append(start)\nstart+=increment', {'start' : start, 'stop' : stop, 'increment' : increment, 'nums' : nums})

	return nums


for i in range(10):
	print(f'Hi {i}')
	t.sleep(1)
