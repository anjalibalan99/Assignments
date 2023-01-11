# """
# Problem Two - prime number
# Anjalikrishna 
# Jan 10-1-23


# """


# # To find the sum of prime numbers in python from 2 to n.

# # Defining the function 
# def Sum_Of_Primes(n):
# # creating a list to store the prime numbers
# 	prime = [True] * (n + 1)
	
# # We have created a boolean array "prime[0..n]".
# # We initialize all the entries as true.
# # Logic: The value in prime[i] if is prime it will be True, else False. 
	
# 	s = 2
# # As the prime numbers start from 2.
# 	while s * s <= n:
# # If the prime[s] is not changing, then it is a prime hence TRUE.
# 		if prime[s] == True:
# # We update all the multiples of s if the prime is TRUE.
# 			i = s * 2
# 			while i <= n:
# 				prime[i] = False
# 				i += s
# 		s = s + 1
		
# # We return the sum of primes generated through the Sieve of Eratosthenes.
# 	sum = 0
# 	for i in range (2, n + 1):
# 		if(prime[i]):
# 			sum = sum + i
# 	return sum

# n = int(input("\nPlease enter the last number up to which the sum of prime number is to be found:"))
# print("\n The sum of prime numbers in python from 1 to " , n, "is : ",Sum_Of_Primes(n))


# Take input from user
# upto = int(input("Find sum of prime numbers upto : "))

# sum = 0

# for num in range(2, upto + 1):

#     i = 2
    
#     for i in range(2, num):
#         if (int(num % i) == 0):
#             i = num
#             break

#     #If the number is prime then add it.
#     if i is not num:
#         sum += num

# print("\nSum of all prime numbers upto", upto, ":", sum)



# from math import *

# def isprime(x):
#   for j in range(2,1 + int(sqrt(x - 1))):
#     if x % j == 0:
#       return False
#   return True

# def primes(n):
#     # return [j for j in range(2, n) if isprime(n)]
#     for j in range(2,n):
#         if isprime(n):
#             print(j)
#     return [1,2,3,4]

# n=10
# logsum = 0

# for p in primes(n):
#     logsum += log(p)
# print(logsum)
    


# from math import *
# logsum = 0
# n = input('This is a logarithm ratio tester. Which number do you want to test? ')
# for x in range(2,n):                            #picks numbers to test
#     isprime = True
#     for divisor in range(2, 1+int(sqrt(x+1))):
#         if x%divisor == 0:                      #checks if x is prime
#             isprime = False                                  #computes log of prime
#             break
#     if isprime:
#         logsum += log(x)


# from math import log
# num=int(input("enter value :"))
# a=[]
# for i in range(2,num+1):
#     for j in range(2,i):
#         if (i % j ==0):
#             break
#     else:
#         a.append(i)
# print(a)
# logsum=0
# for p in a:
#     logsum += log(p)
# print(logsum)
