  
def printGP(a, r, n):  
    for i in range(0, n):  
        curr_term = a * pow(r, i) 
        print(curr_term) 
  
a = 1.5 # starting number 
r = 3 # Common ratio 
n = 10 # N th term to be find 
  
printGP(a, r, n) 
  
