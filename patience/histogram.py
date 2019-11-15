def histogram(x, y, width):
	maxy = max(y)     #assigns the maximum in the list y, to maxy
	v = width/maxy    #works out the width divided by the maximum
	i = 0
	s = 0
		
	for n in y:     
		vh = int(n*v)      #works out v multipled by the number in y, and makes sure it is an integer
		h = vh*'*'		   #sets the number of *'s in the histogram
		print x[i], h, n   #prints the value of x, the number of stars, and the value of y
		i += 1
		s += n
	
	none = y[0] + 0.0      #the number of games with all cards used up, converted to a float
	all = s                #the total number of games played
	prob = none/all        #the probability of winning a game
	return prob
