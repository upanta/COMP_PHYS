from vpython import *


##init
x0 = 0 
v0 = 1
tmax = 100
dt = 0.09
wind = graph(fast=False, xtitle='x', ytitle='v')
curve = gcurve(color=color.blue, radius=1, label='exact position')
curve2 = gcurve(color = color.red, radius = 1, label='forced osscillation')

#curve3 = gdots(color = color.green, radius = 1, label='damped velocity')
v = v0
x = x0
omg = 0.5

A = x0
B = v0 / omg

c = 0.1

Amp = 0.5
omega = 0.5

for t in arange(0,tmax,dt):
#	v = v - ( omg ** 2 ) * dt * x
	rate(100)	
	v = v - c * dt * v - dt * omg ** 2 * x + dt * Amp * sin(omega*t)

	x = x + v * dt

	xExt = B*sin(omg*t) + A*cos(omg*t)
	curve.plot(pos=(x,v))
#	curve2.plot(pos=(x,v))
	
#	curve3.plot((t,v))
	
