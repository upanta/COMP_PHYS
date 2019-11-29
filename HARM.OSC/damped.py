from vpython import *


##init
x0 = 0 
v0 = 1
tmax = 100
dt = 0.09
wind = graph(xmin=0, fast=False, xmax=tmax, xtitle='t', ytitle='x')
curve = gdots(color=color.blue, radius=1, label='exact position')
curve2 = gcurve(color = color.red, radius = 1, label='damped position')

curve3 = gdots(color = color.green, radius = 1, label='damped velocity')
v = v0
x = x0
omg = 0.5

A = x0
B = v0 / omg

c = 1.0

for t in arange(0,tmax,dt):
#	v = v - ( omg ** 2 ) * dt * x
	rate(100)	
	v = v - c * dt * v - dt * omg ** 2 * x

	x = x + v * dt

	xExt = B*sin(omg*t) + A*cos(omg*t)
	curve.plot(pos=(t,x))
	curve2.plot(pos=(t,xExt))
	
	curve3.plot((t,v))
	
