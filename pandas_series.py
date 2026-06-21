import pandas as pd
import numpy as np

# creating series from numpy array
data = np.array(['a','b','c','d','e'])
print(data)

s = pd.Series(data)
print(s)

# series from List
data = [1,2,3,4,5]
s = pd.Series(data)
print(s)

# series from dict
data = {
    'one':1,
    'two':2,
    'three':3,
    'four':4,
}
s = pd.Series(data)
print(s)

# series from numpy function

data = np.linspace(0,10,5)
print(data)
s1 = pd.Series(data)
print("s1: ", s1)
data = np.arange(0,10,2)
print(data)
s2 = pd.Series(data)
print("s2:", s2)

# using range
s = pd.Series(range(0,10))
print(s)

# using list comprehension
index = [x for x in 'abcdefg']
data = range(1,20,3)
s = pd.Series(data,index=index)
print(s)

s = pd.Series(np.linspace(10,15,5), index=[x for x in 'abcde'])
print(s)

s = pd.Series(np.arange(20,30,2), index=[x for x in range(1,6)])
print(s)

s = pd.Series(range(10,20), index=[x for x in range(0,10)])
print(s)