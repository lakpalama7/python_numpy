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

# Attributes of Numpy

a = np.array([[1,2,3],[4,5,6]])
print(a.shape) # returns the dimensions of array
print(a.dtype)
print(a.ndim) # return number of dimension


# Matrix multiplication
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.multiply(a,b))
print(np.dot(a,b))
print(a.ndim)

a="finland"
arr = np.fromiter(a, dtype='U2')
print(arr)

a = np.empty((4,3), dtype=np.int16)
print(a)

b = np.ones((4,3), dtype=np.int32)
print(b)

c = np.zeros((4,3), dtype=np.int32)
print(c)

# Attributes of ndarray

a = np.array([[1,2,3],[4,5,6]])
print(a.shape) # return dimension of array
print(a.ndim) # return number of dimension
print(a.dtype) #data types
print(a.size) # total elements in array
print(a.itemsize) # return size in bytes of each element.

print('-----------------')
# Multi dimensional indexing
# index and slice each dimension in multi dimensional arrays

a = np.array([[1,2,3],[4,5,6],[7,8,9]])

#indexing
print(a[2,2])
#slicing
print(a[::2,::2]) # firt row and last row, first col and third col of each row


# Reshaping : change the shape of array while keeping all datas

a = np.arange(0,10)
print(a)
r = a.reshape(2,5)
print(r)
r = a.reshape(5,2)
print(r)

# Flattening: convert multidimensional array into one dimension

a = np.array([[1,2,3],[4,5,6]])
f = a.flatten()
print(f)

a = np.array([[[1,2,3],[4,5,6]], [[10,20,30],[40,50,60]]])
f = a.flatten()
print(f)

print(type(a))
print(a.dtype)

# creating arrays 

# zeros array
a = np.zeros((3,4))
print(a)

# ones array
a= np.ones((2,3), dtype=int)
print(a)

# full array
a = np.full((2,2),7)
print(a)

# random values
# generate float values between 0 to 1
a=np.random.rand(2,3)
print(a)

# generate int values
a = np.random.randint(1,10, size=(3,3))
print(a)

# range value
a = np.arange(0,10,2)
print(a)

# generate array with specified number size each element are evenly spaced with in range
a = np.linspace(0,10,5)
print(a)


# Identity and diagonal matrics
a=np.eye(3) # generate 3*3 matrics, with 1's in diagonal 
print(a)

a=np.diag([1,2,3]) # generate matrix with diagonal [1,2,3]
print(a)

# empty
a = np.empty([3,], dtype=int)
print(a)
a = np.empty([2,2], dtype=int)
print(a)


# resize 
arr = np.array([1,2,3,4,5,6])
arr.resize((3,4), refcheck=False)
print(arr)

arr.resize((4,4), refcheck=False)
print(arr)

# stack
a = np.array([1,2,3])
b = np.array([4,5,6])
res = np.stack((a,b), axis=0)
print(res)
res = np.stack((a,b), axis=1)
print(res)

m = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])

n = np.array([[[10, 20], [30, 40]],
              [[50, 60], [70, 80]]])

print(np.stack((m,n), axis=0))
print("----------")
print(np.stack((m,n), axis=1))
print("---------")
print(np.stack((m,n), axis=2))
print("-------")
print(np.stack((m,n), axis=3))

#split array

arr = np.array([1, 2, 3, 4, 5, 6])
res = np.array_split(arr,3)
print(res)

#split -- divides into sub array of equal size...
a = np.arange(6)
print(np.split(a,2))

# it allows uneven split also
a = np.arange(13)
res = np.array_split(a, 5)
print(res)

#vsplit
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
res = np.vsplit(arr,2)
print(res)
#hspilt
arr = np.array([[1, 2, 3,0], [4, 5, 6,0], [7, 8, 9,0], [10, 11, 12,0]])
res = np.hsplit(arr,2)
print(res)

arr = np.arange(24).reshape((2, 3, 4))
print(arr)

#broadcasting in conditional

a = np.array([12, 24, 35, 45, 60, 72])
b = np.array(["Adult", "Minor"])
res = np.where(a > 18, b[0], b[1])
print(res)

# Normalizing data
img = np.array([ [100, 120, 130],
                 [90, 110, 140],
                 [80, 100, 120] ])

m = img.mean(axis=0)
s = img.std(axis=0)
res = (img-m)/s
print(res)
