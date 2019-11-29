from numpy import exp, arange
from random import gauss 

a = -0.025
b = 0.25

tmax = 1.0
timesteps = 4000
dt = tmax / timesteps
def calcPathInt(tmax, dt):
	s = 0
	for i in arange(0,tmax,dt):
		t = i * dt
		s += exp(a*t + b * t**0.5 * gauss(0,1)) * dt
	return s



numOfPaths = 5000

sumI = 0
for n in range(numOfPaths):
	calc= calcPathInt(tmax, dt)
	sumI += calc
	if n % 73 == 0:
		print(calc)

avg = sumI / numOfPaths
ext = (exp((a+0.5*b**2)*tmax) - 1 )/ (a+0.5*b**2)


print("Calculated = ", avg)
print("Exact = ", ext)
