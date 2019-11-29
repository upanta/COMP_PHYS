from vpython import *



w = graph()

c = gcurve()

x = y = z = 1

sigma = 10

beta = 8/3

rho = 28

dt = 0.01

for t in arange(0,100,dt):
	rate(100)
	c.plot((x,z))
	x = sigma * ( y -x ) * dt + x

	y = ( x * ( rho -z ) - y ) * dt + y

	z = ( x*y - beta*z) * dt + z



