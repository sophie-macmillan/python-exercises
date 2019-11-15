from random import random

def roll(sides=6):
   
    x = random()
    x = int(x*(sides)) 
    return x

def test_roll(N=6000):
  
    count = [0]*7                      
    for i in range(N):
        j = roll()
        assert j in range(1,sides)
        count[j] = count[j] + 1

def choose(L):
    
    if len(L) == 0:
        return None
    x = random()
    i = int(x*len(L))
    assert 0 <= i < len(L)
    return L[i]

def throw(dice=1):
    sum = 0
    for n in range(dice):
        sum = sum + roll()
    return sum
	

