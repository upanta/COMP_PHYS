from vpython import *


##init
x0 = 0 
v0 = 1
tmax = 100
dt = 0.09
wind = graph(xmin=0, xmax=tmax, xtitle='t', ytitle='x')
curve = gdots(color=color.blue, radius=1)
curve2 = gdots(color = color.red, radius = 1)
v = v0
x = x0
omg = 0.5

A = x0
B = v0 / omg

for t in arange(0,tmax,dt):
	v = v - ( omg ** 2 ) * dt * x
	x = x + v * dt

	xExt = B*sin(omg*t) + A*cos(omg*t)
	curve.plot(pos=(t,x))
	curve2.plot(pos=(t,xExt))
	
