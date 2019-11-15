from math import pi

def madhavaApproximation(N=20):
  f = 0.0
  s = 0
  Nn = 0.0
  Dn = 0.0


  for n in range(0, N+1): #first sequence generator to work out terms in sequence
    
    Nn = (-1.0)**n   #numerator of fraction
    
    Dn = (2.0*n + 1) * 3.0**n  #denominator of fraction 
    
    f = Nn/Dn  #fraction
    
    s = s + f  #sum of terms in the brackets
    
    Pn = 12**0.5 * s  #root 12 multiplyed by the sum of the brackets
    print 'When N =',n, ', Pn =',Pn
    
  
def accuracyByNumOfTerms(N=20):
    f = 0
    s = 0
    Nm = 0
    Dm = 0
    for m in range(0, N+1): #second sequence generator to work out the differences
      
      Nm = (-1.0)**m   
      
      Dm = (2.0*m + 1) * 3.0**m  
      
      f = Nm/Dm  
      
      s = s + f  
      
      Pm = 12**0.5 * s  
        
      D = Pm - pi  # difference between the mth term and pi
      
      modD = abs(D)  #the absolute value, used so the difference is always positive
      
      print 'The difference between P(', m, ') and pi is', modD
      
madhavaApproximation()
accuracyByNumOfTerms()