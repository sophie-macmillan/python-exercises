from random import random

def shuffle(L):
	'''
	Uses the Dursten algorithm in order to shuffle the list L
	'''
	n = len(L)
	NL = L                     #creates a new list, identical to the original, so that the original list is preserved
	Nlist = range(1, n)        #creates a new list, with the indexes of the original list as elements
	BNlist = Nlist[::-1]       #reverses the list Nlist
	
	for i in BNlist:
		j = random()           #generates a random number between 0 and 1
		j = int(j*i)           #random number is converted to a random integer between 0 and i
		NL[j], NL[i] = NL[i], NL[j]    #swaps the items in the j-th position and the i-th position in the list
	return NL
	