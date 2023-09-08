## Things I would like to learn this semester and also a python function

# List of things I would Like to learn:

1) How Quantum computing is implemented
2) How to properly use version control
3) How to cleanly integrate C++ with python
4) How to effectively document/format my code so that it's more readable to collaborators
5) How to use the other tools like colab and jupyter to collaborate on projects

# My python function, which returns the factorial of a given integer

#This function takes an integer num and returns num facotrial (num!). I.e. num*(num-1)*(num-2)...
#Warning: may take a while to run if you throw in a huge number!

def factorial(num):
    
    fact = 1
    
    for i in range(1, num+1):
        fact = fact*i
    
    return fact
