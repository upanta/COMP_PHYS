###Uday Panta		9th October 2019

from numpy import arange, array, empty
import random
import matplotlib.pyplot as plt
mu = 0.1
sigma = 0.5

dt = 0.001

x0 = 1
tmax = 1


def generatePOS(dt):
	x_list = []
	x = x0
	t = 0
	while x<10000:
		x = x + mu * dt + x**3 + sigma * x * random.gauss(0,1) * dt**0.5
		t += dt
	return t	





numofTrials = 10
sumLIST = empty([len(arange(0, tmax, dt)),])
for i in range(numofTrials):
	t_list = arange(0,tmax,dt)
	x_list = generatePOS(t_list)
	sumLIST += array(x_list)
	plt.plot(t_list,x_list)

averagePATH = sumLIST / numofTrials
plt.plot(t_list, averagePATH, 'ro', markersize=3)
plt.xlim([0,1])

plt.show()
