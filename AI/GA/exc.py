def exchangeGenes(mom,dad,n):
	print(mom,dad)
	child1 = mom[:(len(mom)-n)] + dad[(len(dad)-n):]
	
	child2 = dad[:(len(dad)-n)] + mom[(len(mom)-n):]

	return child1, child2


print(exchangeGenes('00001011', '11111100', 4))
