from everything import mathfuncs as m, pyinter, pyyt, Console, time as t, discordPkg, interfacePkg, Randomkey, sys, notEnoughInfoException, bit, byte
#Early version import ^ will throw error. Does not properly import.


def main():
	interfacePkg.install()
	discordPkg.install()


	num = m.add((23874923857928723,234928304,234982034,2348270487239,2349293847))
	num2 = m.multiply((2, 4, 5))
	num3 = m.divide((100, 10, 5))
	num4 = m.subtract((100, 50, 10))
	num5 = m.random.int(1, 100)
	num6 = m.random.float(1, 100)
	num7 = m.lcm(6,3)
	num8 = m.gcd(12, 36)
	num9 = m.gcf(328, 792)
	num10 = m.square.getarea(90)
	num11 = m.rect.getarea(10, 3289)
	num12 = m.square.getperimeter(area = 49)
	num13 = m.pwr(3, 3)
	num14 = m.pwr(12387194862398479812743982739148739281479, 2)
	num15 = m.sqrt(num14)

	myrect = m.rect(8, 4)

	Console.write(num)
	t.sleep(0.1)
	Console.write(num2)
	t.sleep(0.1)
	Console.write(num3)
	t.sleep(0.1)
	Console.write(num4)
	t.sleep(0.1)
	Console.write(num5)
	t.sleep(0.1)
	Console.write(num6)
	t.sleep(0.1)
	Console.write(num7)
	t.sleep(0.1)
	Console.write(num8)
	t.sleep(0.1)
	Console.write(num9)
	t.sleep(0.1)
	Console.write(num10)
	t.sleep(0.1)
	Console.write(num11)
	t.sleep(0.1)
	Console.write(f'Perimeter is: {num12}')
	t.sleep(0.1)
	Console.write(num13)
	t.sleep(0.1)
	Console.write(num14)
	t.sleep(0.1)
	Console.write(num15)
	t.sleep(0.1)
	Console.newlines(10)
	Console.write(f'Length: {myrect.length}\nWidth: {myrect.width}\nArea: {myrect.area}\nPerimeter: {myrect.perimeter}')


	one = pyinter.create_display((200,400))
	Console.write(pyinter.display.stats)

	#pyyt.download('https://www.youtube.com/watch?v=2kttVyakHN4')
	Console.write(pyyt.stats('https://lol.www.youtube.com/watch?v=2kttVyakHN4'))

	sys.path.append('js')

	from jspyinterpreter import run

	run()

	myvar = '123456'

	Console.filereadprint('testcode.txt')
	print('\n')
	Console.filereadprint('testcode.txt', True, 0)
	print('')
	Console.filereadprint('testcode.txt', True, 1)
	print('')
	Console.filereadprint('testcode.txt', True, 2)
	print('')
	Console.printlist(myvar)
	Console.indent('this is indented', 3)
	Console.debug('Console functions successful', 'main.py', 84, True)
	Console.exec('print("this is the code")')

	Console.write('Hello ')
	Console.write('World!')
	print()

	Console.clearlog()


	print('\nBit and Byte')
	t.sleep(1)
	print(bit.generate())
	t.sleep(1)
	print(byte.generate())
	t.sleep(1)
	print()

	print('\nGenerating random bytes (100)\n')
	t.sleep(2)

	for i in range(0, 100):
		t.sleep(0.1)
		print(Randomkey.byte())

	print('\nGenerating mixed random keys (100)\n')
	t.sleep(2)

	for i in range(0, 100):
		t.sleep(0.1)
		print(Randomkey.mix(10, 'all', True))

	print('\nGenerating number random keys (100)\n')
	t.sleep(2)

	for i in range(0, 100):
		t.sleep(0.1)
		print(Randomkey.numbers(10))

	print('\nGenerating lowercase random keys (100)\n')
	t.sleep(2)

	for i in range(0, 100):
		t.sleep(0.1)
		print(Randomkey.lowercase(10))

	print('\nGenerating uppercase random keys (100)\n')
	t.sleep(2)

	for i in range(0, 100):
		t.sleep(0.1)
		print(Randomkey.uppercase(10))

	print('\nGenerating special character random keys (100)\n')
	t.sleep(2)

	for i in range(0, 100):
		t.sleep(0.1)
		print(Randomkey.chars(10))

	print('\nGenerating letter-only random keys (100)\n')
	t.sleep(2)

	for i in range(0, 100):
		t.sleep(0.1)
		print(Randomkey.letters(10))

	print('\nGenerating number and special character random keys (100)\n')
	t.sleep(2)

	for i in range(0, 100):
		t.sleep(0.1)
		print(Randomkey.numchars(10))

	t.sleep(1)
	Console.debug('Random Key Generation Successful','main.py', 136, True)



	Console.clearlog()