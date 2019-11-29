import numpy as np

def makepairs(S):
	list1 = S[:len(S)//2]
	list2 = S[len(S)//2:]	
	pairs = [[list1[i],list2[i]] for i in range(len(list1))]
	return pairs













print(makepairs(range(16)))
