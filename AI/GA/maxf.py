import numpy as np
import random



numBits = 4
n = 8
Pc = 0.8
Pm = 0.08

NofGen = 1000

def functionVal(x):
	return np.sin(np.pi*x)

def genPopSoln(L):
	numofSoln = 2 ** L
	
	Solutions = [i for i in range(numofSoln)]
	return [np.binary_repr(j, width=L) for j in Solutions]

def fitness(S):
	decimalSol = [int(i,2)/(len(S) - 1) for i in S]
	fit = [abs(functionVal(i)) for i in decimalSol]
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

	newChildren = []
	for individual in children:
		newChildren.append(mutate(individual, Pm))
	print('After mutation \n', newChildren, '\n\n')
	return newChildren

def main(L, Pc, Pm, n, NofGen):
	Pop = genPopSoln(L)
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

Final = main(numBits, Pc, Pm, n, NofGen)

print([int(i,2) for i in Final])
