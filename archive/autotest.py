import time as t
import sys
from everything.console.colors import colors

with open('fakeautocode/code.txt')as f:
	code = f.read()

print_index = 0

while True:
		if print_index > len(code):
			break
		else:
			sys.stdout.write(colors.RED + code[print_index:print_index + 1] + colors.ENDC)
			sys.stdout.flush()
		print_index += 1
		t.sleep(0.1)


print('\nExecuting...')
t.sleep(1)
print('.')
t.sleep(1)
print('..')
t.sleep(1)
print('...\n')
t.sleep(1)
exec(code)