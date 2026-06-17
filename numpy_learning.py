import numpy as np


# Creating Numpy Arrays
# np.array() -- convert list into array

a1 = np.array([1,2,3]) # 1D array
print("1D array: ", a1)

a2 = np.array([[1,2],[3,4]]) # 2D array
print("2D array: ", a2)

a3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]]) #3D array
print("3D array:", a3)

#Using Numpy Functions
# provides utility functions for creating arrays fill with zeros, ones or ranges

a0=np.zeros((3,3))
print(a0)

a1=np.ones((2,2))
print(a1)

ar = np.arange(0,10,2)
print(ar)


# Numpy array indexing
# access element using individual position

a1 = np.array([10,20,30,40,50])
print(a1[2])
print(a1[-1])

a2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(a2[1,0]) # row 1, column 0
print(a2[2,2]) # row 2, column 2

# Slicing
# similar to indexing but allow to select multiple elements, rows, columns
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[1:]) # row slice, row 1 and row 2
print(a[:]) # all rows slice

print(a[:,1]) # all rows, column 1

print(a[:,2]) # all rows, column 2

# Advanced Indexing
a = np.array([10,20,30,40,50,60])
idx = np.array([1,2,3])

print(a[idx]) # idx value use as indexing in 'a'
cond = a > 30 # [False False False  True  True  True]
print(a[cond]) # boolean indexing


#Basic Arithmetic operations

x = np.array([1,2,3])
y = np.array([4,5,6])

print(x+y)
print(x-y)
print(x*y)
print(x/y)

# Unary Operation
# single operand tranformation such as negation, absolute

a = np.array([-3,-1,0,1,3]) # positive and negative values
print(np.absolute(a)) 
print(np.negative(a))

# Binary Operators
x = np.array([1,2,3])
y = np.array([4,5,6])

res = np.add(x,y)
print(res)
print(np.multiply(x,y))
print(np.divide(x,y))
print(np.subtract(x,y))

# Mathematical functions: such as sin,cos, exp

a = np.array([0, np.pi/2, np.pi])
print(np.sin(a)) # sin values

b = np.arange(0,5)
print(np.exp(b)) # exponential values
print(np.sqrt(b)) # square root of array values


#Sorting arrays

dtype = [('name','S10'),('year',int),('cgpa',float)]
vals = [('Hrithik',2009,8.5),
        ('Ajay',2008,8.7),
        ('Pankaj',2008,7.9),
        ('Aakash',2009,9.0)]

a = np.array(vals,dtype=dtype)
print(np.sort(a, order='name'))
print(np.sort(a, order='cgpa'))