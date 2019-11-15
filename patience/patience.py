from shuffle import shuffle
from histogram import histogram
deck = range(1,14)*4               #sets the standard deck



def add_to_11(visible):
	'''
	tests to see if any of the elements in the list visible add to 11
	'''
	a = ()                         #creates an empty tuple, a
	if len(visible) == 1:          #checks that the list, visible, has at least two elements
		return a
		
	L = range(len(visible))        #L is a list of the indexes present in visible
		
	for n in L:                                #loops through each element in L
		for i in L:                            #loops through the list once for each element in L
			if visible[n] + visible[i] == 11:  #works out if any of the elements add to 11
				a = (i, n)                     #if they do, set a as a tuple containing the indexes
				break                          #stops the loop
	return a
	
def jqk(visible):
	'''
	tests to see if 11, 12, and 13 are in the list visible
	'''
	n = 0
	L = len(visible)
	t= ()
	
	
	if 11 not in visible:                  #works out if the list, visible doesn't have 11, 12, or 14 in
		return t
	if 12 not in visible:
		return t
	if 13 not in visible:
		return t
		
	else:
		while n < L:                       #loops through the list L, and assigns x, y and z
			if visible[n] == 11:           #to the indices of the cards which are the jack
				x = n                      #queen and king
			if visible[n] == 12:
				y = n
			if visible [n]==13:
				z = n
			n = n+1
		t = x, y, z	                       #creates a tuple containing the correct indices
		return t

		
def play(deck, verbose):  
	'''
	plays the game patience with a deck, deck. If verbose is True, prints out all of
	stages of the game
	'''
	deck = shuffle(deck)                   #shuffles the deck
	game = []                              #creates an empty list
	
	if len(deck)>0:                        #adds two random cards to the list game
		for n in range(2):
			game.append(deck.pop(0))
		
	if verbose== True:                     #prints the first game if verbose is True
		print game
	
	while len(game) <= 9:                   #the game only runs while there are less than nine piles
		a = jqk(game)
		b = add_to_11(game)
		if len(a) == 3:	                   #if there is a jack, queen and king present
			for A in a:               
				if len(deck) == 0:         #checks there are enough cards left in the deck
					if verbose:    #if not, and verbose is True, print the final stage
						print game
					return len(deck)       #return the number of cards left in the game
					
				else:
					game[A]= deck.pop(0)   #if there are enough cards left in the deck

					
		else:                              #if a jack, queen and king isn't present
			if len(b) == 2:                #but two cards add to 11
				for B in b:
					if len(deck) == 0:     #check there are cards left in the deck
						if verbose:
							print game     #if not, end game, and if verbose is True print the final stage
						return len(deck)   #and return the number of cards left in the deck
						
					else:
						game[B] = deck.pop(0) #if there are enough cards left in deck, replace the cards

					
				
			else:                             #if there are no cards that add to 11
				if len(deck) == 0:            #check there are enough cards left in deck
					if verbose:
						print game  
					return len(deck)
					                    
				game.append(deck.pop(0))      #if there are, add a new pile of cards to the game

				
		if verbose:                           #if verbose is True, print the stage
			print game
		
	return len(deck)                    #at the end of the game, return the number of cards left in deck



def many_plays(N):
	'''
	plays a game of patience N times
	'''
	Remaining = [0]*53             #creates an empty list, with 53 0's in it
	i = 0
	while i <= N:                  #the loop will only occur N times
		deck = range(1,14)*4       
		x = play(deck, False)      #plays N games of patience, without printing out all the stages
		Remaining[x] += 1          #adds one, to the index of the number of remaining cards
		i = i+1                    #adds one to i, to repeat the process
						
	return Remaining
	
x = range(53)           
y = many_plays(1000)
print histogram(x, y, width=200)   #prints a histogram with the results of 1000 games of patience