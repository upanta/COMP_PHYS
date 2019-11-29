from __future__ import frame
from vpython import *


w = canvas()
f = frame()
x = y = z = 1

sigma = 10

beta = 8/3

rho = 28

dt = 0.01

ball = sphere(frame=f,radius=0.1, make_trail=True, retain=200)
ball.mass  = 1
ball.p = vector(1,1,1)
our_pos = []

for t in arange(0,100,dt):
	rate(200)
	x = rho * ( y -x ) * dt + x

	y = ( x * ( rho -z ) - y ) * dt + y

	z = ( x*y - beta*z) * dt + z

	ball.p = vector(x,y,z)
