def hailstone(xn):
	'''
	Prints the hailstone sequence starting with xn, and prints sequence terminates when the sequence terminates
	'''
	L = [xn] #create a list with only the starting element in it
	for n in L:
		if xn%2 == 0:   #check to see if xn is divisible by 2
			xn = xn/2  #if yes, this is the next term in sequence
		elif xn == 1:
			L.append('Sequence terminates')  #add 'sequence terminates' to the list
			break  #stops sequence continuing if x = 1
		else:
			xn = 3* xn + 1
			
		L.append(xn) #add the next term to the list
		
	return L
	
				
		
print 'when Xn = 1, ', hailstone(1)
print 'when Xn = 2, ', hailstone(2)
print 'when Xn = 3, ', hailstone(3)
print 'when Xn = 4, ', hailstone(4)
print 'when Xn = 5, ', hailstone(5)
print 'when Xn = 6, ', hailstone(6)
print 'when Xn = 7, ', hailstone(7)
print 'when Xn = 8, ', hailstone(8)
print 'when Xn = 9, ', hailstone(9)
print 'when Xn = 10, ', hailstone(10)