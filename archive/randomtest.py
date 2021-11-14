from everything.rand import rand
import time as t

#rand.setseed(1234567890123098461)

for i in range(0,100):
	print(rand.uniform(1, 100))
	print(rand.seed)
	print(rand.int(1, 100))
	t.sleep(0.1)

rand.clearseed()
print(rand.uniform(1, 100))