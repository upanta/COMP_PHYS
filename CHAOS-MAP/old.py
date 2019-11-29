from vpython import *
#from visual.graph import *

x = 0.40
r = 2.50

win = graph(xmin=2.85, xmax=4.0, xtitle='t', ytitle='x(t)')
curve = gdots(color=color.red, size=0.5)


#for r in arange(2.85, 4, 0.001):
for t in arange(0,50):
	x = r*x*(1-x)
	print(x)
	curve.plot(pos=(t,x))
