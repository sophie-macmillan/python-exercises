from dice import roll

def generate_number(Len):
	'''
	Generates a random integer number with Len digits
	'''
	hidden = ''                      #creates an empty string
	for n in range(Len):
		x = roll(10)                 #generates a random 1 digit number
		x = str(x)                   #converts that number to a string, so that
		hidden += x                  #it can be added to the empty string
		
	return hidden                    #returns a string of random numbers
	
def test_digits(I):
	'''
	Tests that the number of digits inputted is valid
	'''
	try:
		Itest = int(I)               #tries to convert I to an integer
		assert Itest > 0             #checks the integer is greater than 0
	except:
		return False                 #if either is not possible, False is returned

def test_guess(guess, L):
	'''
	Tests that the input guess is the right length
	and is of the right format
	'''
	try:
		guesstest = int(guess)             #tries to convert the guess input to an integer
		assert len(guess) == len(range(L)) #checks the guess is the same length as the hidden number
		assert guesstest >= 0              #checks that the guess is positive
		return True
	except:
		return False
		

		
def right_number(guess, hidden):
	'''
	Calculates the number of guess' digits 
	that are	in the hidden number
	'''
	listg = list(guess)                    #converts the string guess, to a list
	listh = list(hidden)                   #converts the string hidden, to a list
	copylistg = listg                      #creates a copy of the list guess
	
	lenguess = len(listg)                  
	
	for i in listh:
		if i in copylistg:                 #if a digit in the hidden number is in the guessed
			copylistg.remove(i)            #number, remove that digit from the copy of guess
			
	lencopy = len(copylistg)               
	
	n = lenguess - lencopy                #works out the length of the original guess, minus the 
                                          #length of the copied guess, with correct digits removed
			                              #n, is therefore the number of correct digits
	return n

def right_place(guess, hidden):
	'''
	Calculates the number of guess' digits
	that are in the correct position
	'''
	p = 0                                 #a count of the number of correctly positioned digits
	for i in range(len(guess)):
		if guess[i] == hidden[i]:         #if the digit in guess is equal to the digit in hidden
			p+=1                          #add one to the count
	return p
		
		

def play():
	'''
	Plays a single game of mastermind
	'''
	L = raw_input('How many digits would you like to play with?  ')
	
	while test_digits(L) == False:       
		#if the input not suitible, player asked for a proper input
		
		print 'Please enter an integer length greater than 0 '
		L = raw_input('How many digits would you like to play with?  ')
	
	L = int(L)                                    #converts L to an integer
	hidden = generate_number(L)                   #generates a hidden number of length L
	print 'You have', (2*L)+2, 'guesses!'
	
	print ' '                                     #leaves an empty line, for aesthetic purposes
	x = 1
	while x <= (2*L)+2:                               #insures the player gets the right number of turns
		guess = raw_input('Enter your guess:  ')
		

		while test_guess(guess, L) == False:        #if the input is not a valid guess
			if guess == 'quit' or guess == 'Quit':  #(unless the input is 'Quit', in which case
				return "You've exited the game"     #  the player exits the game )
			
			print 'Please enter an integer guess of the right length'
			guess = raw_input('Enter your guess:  ')  # the player is asked to re-enter a guess
			
			
		n = right_number(guess, hidden)             #n is the number of correct digits
		p = right_place(guess, hidden)              #p is the number of correctly positioned digits
		
		if guess == hidden:                         #if all of the digits are in the right place
		                                            #the player wins
													
			return 'Congratulations, you guessed the hidden number in ', x, 'guesses'
			
		print 'Your guess contains ', n ,'correct digits and ', p , 'of these digits are in the correct place'
		
		print ''                                       #leaves an empty line
		x += 1                                         #adds one to the turn count
		
		
	#if the player has used all of their turns, the program tells them what the hidden number was
	return 'Sorry, you lost! the hidden number was', hidden

print play()
