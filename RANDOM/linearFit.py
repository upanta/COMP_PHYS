from random import random as rnd
from vpython import *
import numpy as np


w = graph(xtitle = 'n', ytitle = '<x<sup>2</sup>(n)>')
c = gdots()
num_of_trials = 5000

def fit(x,y):
	a11 = len(x)
	a12 = sum(x)
	a21 = sum(x)
	a22 = sum([i^2 for i in x])

	matA = np.array([[a11,a12], [a21,a22]])
	
	b11 = sum(y)
	b21 = 2 * np.dot(x,y)

	matB = np.array([[b11,b21]])

	solution = np.linalg.solve(matA,matB)
	return solution 

y=[]
#while(steps<1000):
for steps in arange(10,100,10):
	distinN = []
	s = 0
	for i in range(num_of_trials):
		dist = 0
		for t in range(steps):
			r = rnd()
			
			if r >= 0.5:
				dist += 1
			else:
				dist -= 1
		distinN.append(dist)
		s += dist**2
	y.append(s)
	print('<x(n)> = ', sum(distinN) / len(distinN))
#	print(dist)

	#	c.plot(t,dist)
	#	print("Final destination in trial", i, "is", dist, "units away")
		
#	print("Average distance =", s / num_of_trials)	
	c.plot((steps,s/num_of_trials))

x = arange(10,100,10)

ft = np.polyfit(x,y,1)
a,b = ft[0], ft[1]
print(ft)


#a,b = fit(x,y)
#print(a,' and ', b)  
c2=gcurve()
c2.plot(0,b)
c2.plot(100,100*a+b)
	
#	steps += 10




