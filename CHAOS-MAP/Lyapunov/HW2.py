###Submitted by: Uday Panta	Date:16th September 2019


from vpython import *
from numpy import log
#from visual.graph import *

xA = 0.50
xB = 0.50001
r = 4.00

win = graph(xtitle='t', ytitle='dx(t)')
c = gcurve(color=color.red, radius=1)

dx_list = []

dx0 = abs(xA-xB)
n = 50
for t in arange(0,n):
	dx = abs(xA-xB)
	dx_list.append(dx)
	
	c.plot((t,dx))
	
	xA = r*xA*(1-xA)
	xB = r*xB*(1-xB)


lmbda = (1/n) * sum([log(dx_list[i+1]/dx_list[i]) for i in range(n-1)]) 

print('lambda for n=', n, 'is', lmbda)
