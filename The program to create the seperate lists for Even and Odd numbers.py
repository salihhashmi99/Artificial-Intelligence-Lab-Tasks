"""
Write a program that creates a list of 10 random integers. Then create two lists by name odd_list and even list 
that have all odd and even values of the list respectively.
"""

import random
random=[random.randrange(1,50,1) for i in range(10)]
print ("The list of Random numbers is : "+str(random))

Olist=[]
Elist=[]
for n in random:
    if n%2==0:
        Elist.append(n)
    else:
        Olist.append(n)
        
print("The list of Even Integers in numbers is : ",Elist)
print("The list of Odd Integers in numbers is : ",Olist)
