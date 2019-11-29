import numpy as np

cities = ['A','Y','S','C','X']


def genPOP(L, num):
	sol=[]
	for i in range(num):
		sol1 = np.random.choice(L, size=len(L), replace=False) 
		x = ''.join(sol1)
		sol.append(x)
	return sol






print(genPOP(cities, 5))
