from numpy import arange 
import random
import matplotlib.pyplot as plt
mu = 0.1
sigma = 0.5

dt = 0.001

x0 = 0
tmax = 1
timesteps = arange(1000, 10000, 1000)

def generateFINALPOS(t):
	x = 0
	for i in t:
		x = x + mu * dt + sigma * random.gauss(0,1) * dt**0.5
	return x	

averageFinalPOS = []
#sdDEV = []
finallist = []
for j in timesteps:
	numofTrials = 2000
#	finalPOS = []
	for i in range(numofTrials):
		t_list = arange(0,j*dt, dt)
		end = generateFINALPOS(t_list)
#		finalPOS.append(end)
		finallist.append(end)
	
#	averageFinalPOS.append(sum(finalPOS) / len(finalPOS))
#	term1 = sum([i**2 for i in finalPOS]) / len(finalPOS)
#	term2 = (sum(finalPOS) / len(finalPOS) ) ** 2
#	
#	sdDEV.append(term1 - term2)
print(finallist)
n, bins, patches = plt.hist(finallist, bins = arange(min(finallist), max(finallist),0.05))

plt.show()
