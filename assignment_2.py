"""Assignment 2 Problem 1: use successive approximation to find the value of an investment given salary,savings,rate,and duration
January 10,2023
"""
# problem 1
def fixedInvestor(salary,p_rate,f_rate,years):
    price=0
    for i in range(1,years+1):

        if i==1:
            
            price=price+salary*(p_rate)
            
        else:
            
            price=(salary*p_rate)+(price*f_rate)
            
    return price
# problem 2
def variableInvestor(salary,p_rate,v_rate):
    price=0
    interest=[]
    for i,j in zip(range(1,len(v_rate)),v_rate):
        if i==1:
            price=price+salary*(p_rate)
            
        else:

            price=(salary*p_rate)+(price*j)
        interest.append(price)
    return interest

# problem 3
def finallyRetired(saved,v_rate,expenced):
    price=saved*v_rate-expenced
    return price
     
print(fixedInvestor(50000,.15,1.05,3))
print(variableInvestor(50000,.15,[1,2,3,4,5]))
