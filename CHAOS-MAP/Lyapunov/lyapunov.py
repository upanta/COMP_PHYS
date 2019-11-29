from vpython import *
from numpy import log
#from visual.graph import *

x0_A = 0.25
x0_B = 0.10
r = 4.00

#win = graph(xmin=2.85, xmax=4.00, xtitle='t', ytitle='x(t)')
#curve = gdots(color=color.red)#, size=1)



def final_val(x,n):
	for t in arange(0,n):
		x = r*x*(1-x)
	return x


dx0 = abs(x0_A-x0_B)


num = 5000

xT_A = final_val(x0_A,num)
xT_B = final_val(x0_B,num)

dxT = abs(xT_A - xT_B)


lmbda = log(dxT/dx0) / num


print('lambda for n=', num, 'is', lmbda)

