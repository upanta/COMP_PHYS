from random import random as rnd
from vpython import *



w = graph(xtitle = 'n', ytitle = '<x<sup>2</sup>(n)>')
c = gdots()
num_of_trials = 5000




#while(steps<1000):
for steps in arange(10,100,10):
	distinN = []
	s = 0
	for i in range(num_of_trials):
		dist = 0
		for t in range(steps):
			r = rnd()
			
			if r >= 0.2:
				dist += 1
			else:
				dist -= 1
		distinN.append(dist)
		s += dist**2
	print('<x(n)> = ', sum(distinN) / len(distinN))
#	print(dist)

	#	c.plot(t,dist)
	#	print("Final destination in trial", i, "is", dist, "units away")
		
#	print("Average distance =", s / num_of_trials)	
	c.plot((steps,s/num_of_trials))	
#	steps += 10




