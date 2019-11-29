from vpython import *
import matplotlib.pyplot as plt
import random

r = 5
dx = 0.1

X = arange(-1*r,1*r,dx)

mean = 0
sigma = 1

k = 1 / (2*pi*sigma**2)**0.5

p = [ k * exp((-0.5 * i**2) / (sigma**2)) * 100000 * dx for i in X]

numData = 100000
data = [random.gauss(mean,sigma) for i in range(numData)]



#plt.hist(data, X, density = numData, stacked = numData)
n, bins, patches = plt.hist(data,X)#, density=True)

#maxm = max(n)
#minm = min(n)
#n = [(i - minm)/(maxm - minm) for i in n]
#n, bins, patches = 
plt.plot(X,p)
#plt.hist(p, X)
plt.xlim(-1*r,r)
#plt.ylim(0,1)
plt.show()
