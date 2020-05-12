#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Ques.1.Given an array of integers, every element appears twice except for one. Find that single one.

def findSingle( ar, n):   #here n=number of element in array
    res = ar[0] 

# Do XOR of all elements and return 
    for i in range(1,n): 
        res = res ^ ar[i] 

    return res 

# Driver code 
ar = [2, 3, 5, 4, 5, 3, 4] 
print ("Element occuring once is", findSingle(ar, len(ar)) )
 


# In[ ]:


#approach used in question no 1
Let ^ be xor operator as in C and C++.

res = 7 ^ 3 ^ 5 ^ 4 ^ 5 ^ 3 ^ 4

Since XOR is associative and commutative, above 
expression can be written as:
res = 7 ^ (3 ^ 3) ^ (4 ^ 4) ^ (5 ^ 5)  
    = 7 ^ 0 ^ 0 ^ 0
    = 7 ^ 0
    = 7 

