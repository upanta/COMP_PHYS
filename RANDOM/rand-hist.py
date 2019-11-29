from vpython import *
from random import random as rnd

h = graph()
c = gdots()
l=[]
for i in range(1000):
	x = rnd()
	
	c.plot((i,x))
	l.append(x)


h.plot(data=l)
