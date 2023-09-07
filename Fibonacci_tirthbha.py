#!/usr/bin/env python
# coding: utf-8

# In[28]:

# Mr. Bhatta's first experience to the python!
# The Fabonacci numbers are the numbers in the following integer sequence
# 0,1,1,2,3,5,8,13,21,34,55,89,144,...
# The sequence of these numbers is given by: Fn = Fn-1 + Fn-2 such that F0 = 0 and F1 = 1
def fib(n): 
    #Taking initial fabonacci numbers 
    f=[0,1]
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])  # Fn = Fn-1 + Fn-2 
    return f[n]
print(fib(9))



# In[ ]:




