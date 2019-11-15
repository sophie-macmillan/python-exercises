from random import random

Integers = range(1, 21)
GreekLetters = [" alpha ", " beta ", " gamma ", " delta ", " epsilon ", " zeta ", "eta",
" theta ", " iota ", " kappa ", " lambda ", "mu"]

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

print shuffle(Integers)
print shuffle(GreekLetters)

def check_shuffle(L):
	'''
	Checks that the shuffled list and the original list contain the same elements, and are the
	same length
	'''
	NL = shuffle(L)
	for e in L:
		if e not in NL:   #checks to see if any elements in the shuffled list are different to the original
			return "Error! Lists are not the same!"
			
	if len(L) != len(NL): #checks to see if the original and shuffled lists are the same length
		return "Error! the shuffled list is not the same length as the original list!"
			
	else:
		return "The lists are the same"

	
def quality(L):
	'''
	Returns the quality of the shuffle function, by shuffling a list L, and checking the ratio of 
	element pairs with the second element greater than the first
	'''
	QL = shuffle(L)
	prev0 = QL[0]         #sets the first element in the list as prev0
	prev1 = QL[1]         #sets the second element in the list as prev1
	bigger = 0.0
	pairs = 0
	
	for item in range(len(QL)+2):
		if prev0 < prev1:
			bigger += 1    #adds 1 to the 'second element is bigger' count
		
		pairs = pairs + 1  #counts the number of pairs
		prev0 = prev1      #sets the first element of the pair to the next element in the list

		if item+2 >= len(QL):
			break          #if the second element in the pair is out of the list range, then breaks the for loop
		else:
			prev1 = QL[item+2]     #sets the second element in the pair
	q = bigger/pairs       #works out the ratio
	return q
