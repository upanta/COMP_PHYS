import numpy as np
import random


cities = ['A','Y','S','C','X']
n = 8
Pc = 0.8
Pm = 0.08

NofGen = 1000

dist = {'AY':51,
	'AS':89,
	'AC':125,
	'AX':232,
	'YS':123,
	'YC':172,
	'YX':279,
	'SC':112,
	'SX':231,
	'CX':106}

def functionVal(path):
	total_dist = 0
	x = path[0]
	for city in path[1:]:
		if x+city in dist:
			total_dist += dist[x+city]
		else:
			total_dist += dist[city+x]
		x = city
	return 1/total_dist

def genPOP(L, num):
	sol=[]
	for i in range(num):
		sol1 = np.random.choice(L, size=len(L), replace=False) 
		x = ''.join(sol1)
		sol.append(x)
	return sol


def fitness(S):
#	decimalSol = [int(i,2)/(len(S) - 1) for i in S]
	fit = [abs(functionVal(i)) for i in S]
	return fit

def calcProb(S):#, Pop): ##Arguments sample solution and Population solutions
	f = fitness(S)
#	populationFIT = fitness(Pop)
	sumOffit = sum(f)#populationFIT)
#	print('\n\nfitness\tsumoffit\n',f, '\t', sumOffit)
	Prob = [(i/sumOffit) for i in f]
	return Prob

def flip(stringBIT):
	if stringBIT == '0':
		return '1'
	else:
		 return '0'

def makepairs(S):
	list1 = S[:len(S)//2]
	list2 = S[len(S)//2:]	
	pairs = [[list1[i],list2[i]] for i in range(len(list1))]
	return pairs

def exchangeGenes(mom, dad, n):
	child1 = mom[:(len(mom)-n)] + dad[(len(dad)-n):]
	
	child2 = dad[:(len(dad)-n)] + mom[(len(mom)-n):]

	return [child1, child2]

def crossover(parents, Pc):
	mom, dad = parents[0], parents[1]
	##number of genes to exchange from right
	numOfgenes2exch = random.randint(1,len(mom)-1)

	if random.uniform(0,1) < Pc:
		print(numOfgenes2exch)
		return exchangeGenes(mom, dad, numOfgenes2exch)
	else:
		return parents


def mutate(individual, Pm):
	child = ''
	for i in range(len(individual)):
		if random.uniform(0,1) <= Pm:
			child += flip(individual[i])
		else:
			child += individual[i]
	return child 
	

def makebabies(S, Pc, Pm):
	pairs = makepairs(S)
	print('\nPairs made\n', pairs)
	children = []
	for ACouple in pairs:
		newgen = crossover(ACouple, Pc)
		children.extend(newgen)
	print('After crossover  \n', children, '\n')
	
	return children
#	newChildren = []
#	for individual in children:
#		newChildren.append(mutate(individual, Pm))
#	print('After mutation \n', newChildren, '\n\n')
#	return newChildren

def main(L, Pc, Pm, n, NofGen):
	Pop = genPOP(L, len(L))
	print(Pop)
	
#	f = fitness(Pop)
#	print(f)
	
	Prob = calcProb(Pop)#, Pop)
	print(Prob)
	Sample = np.random.choice(Pop, size = n, p = Prob)
	print(Sample)

	for itern in range(NofGen):
		print('Gen ', itern)
		Sample = makebabies(Sample, Pc, Pm)
		print(Sample,'\n\n')
		Prob = calcProb(Sample)
#		print(Prob)
#		bestones = np.random.choice(Pop, size=len(Pop)-n, p=calcProb(Pop))
#		Pop=np.append(bestones, Sample)
#		Prob = calcProb(Pop)
		Sample = np.random.choice(Sample, size = n, p = Prob)
	
	return Sample

Final = main(cities, Pc, Pm, n, NofGen)

print([int(i,2) for i in Final])
