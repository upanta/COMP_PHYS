from numpy import arange, array, empty
import random
import matplotlib.pyplot as plt
mu = 0.1
sigma = 0.5

dt = 0.001

x0 = 0
tmax = 1


def generatePOS(t):
	x_list = []
	x = x0
	
	for i in t:
		x = x + mu * dt + sigma * random.gauss(0,1) * dt**0.5
		x_list.append(x)
	return x_list	





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
