from vpython import *
#from visual.graph import *

x = 0.25
r = 3.29

win = graph(xmin=2.85, xmax=4.00, xtitle='t', ytitle='x(t)')
curve = gdots(color=color.red)#, size=1)


for r in arange(2.85, 4.00, 0.001):
	for t in arange(0,150):
		x = r*x*(1-x)
		print(x)
		curve.plot(pos=(r,x))
