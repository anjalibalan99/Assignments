"""  
  Assignment 1 & 2 - Prime Number 
  jan 10, 2023
  Anjali Krishna
"""
import math
n=10000
c=0
k=0
s=0
for i in range (2, n):
    k=k+1  
    if i > 1:  
        for j in range (2, i):  
            if (i % j) == 0:  
                break  
        else: 
            c=c+1 # count
            s=s+math.log(i)
            if c==450:
                print("450th prime number is",i)
                break
            
    if k%50==0 and c<455:
        print ("{} prime numbers are found so far".format(c))
        print("sum of log values of {} prime numbers is".format(c),s)
        print("the ratio of number and sum is", c/s)

