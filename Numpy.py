#Write a NumPy program to create a random 10x4 array and extract the first five rows of the array and store them into a variable.
import numpy as np
n=np.random.rand(10,4)
print("Show the original Array")
print(n)
a=n[:5,:]
print("Now,Show first 5 rows of the given array : ")
print(a)
