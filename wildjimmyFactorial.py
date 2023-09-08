#This function takes an integer num and returns num facotrial (num!). I.e. num*(num-1)*(num-2)...
#Warning: may take a while to run if you throw in a huge number!

def factorial(num):
    
    fact = 1
    
    for i in range(1, num+1):
        fact = fact*i
    
    return fact
