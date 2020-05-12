#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Ques.5. Find Square root of given number.
#Given an integar A. Compute and return the square root of A. If A is not a perfect square, return floor(sqrt(A)).
#DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY 

# Returns floor of square root of x 
A = int(input('enter number:'))
def floorSqrt(A): 

# Base cases 
    if (A == 0 or A == 1): 
        return A 

# Staring from 1, try all numbers until 
# i*i is greater than or equal to x. 
    i = 1; result = 1
    while (result <= A): 
        i += 1
        result = i * i 

    return i - 1

# print
print("square root of number is" , floorSqrt(A))


# In[ ]:




