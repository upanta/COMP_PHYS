from random import uniform as uni
from vpython import *


w=graph()
c=gdots()
x=[]
for j in range(3):
	for i in range(10000):
		rnd = uni(0,1)
	#	print(random.uniform(0,1))
		x.append(rnd)
	
x.sort()

for i in range(len(x)):
	c.plot(i,x[i])


