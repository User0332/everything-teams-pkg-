from everything.rand import rand
import time as t

rand.set_seed(9243288845121123459)
rand.clear_seed()

for i in range(0, 100):
	print(rand.uniform(1, 100))
	t.sleep(0.1)