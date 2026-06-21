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

print("--------------")
# Accessing the First Element of Series
data = np.array(['g', 'e', 'e', 'k', 's', 'f',
                 'o', 'r', 'g', 'e', 'e', 'k', 's'])
s = pd.Series(data)
print(s[0])

# first 5 elements
print(s.head())

# last 10 elments
print(s.tail(10))
print(s[-10:])

# Access element using Label
#Accessing a Single Element Using index Label

data = np.array(['a','b','c','d','e'])
s = pd.Series(data, index=[1,2,3,4,5])
print(s[2])

# multiple element
print(s[[2,4,5]])

# Access Multiple Elements by Providing Label of Index

s = pd.Series(range(0,5), index=['a','b','c','d','e'])
print(s['e'])
print(s[['c','a','e']])


# Arithmetic Operations on Series
s1 = pd.Series([1,2,3,4], index = ['a','b','c','d'])
s2 = pd.Series([10,11,12,13], index=['a','b','c','d'])
print(s1, "\n", s2)
print(s1 + s2)

#comparision
s1 = pd.Series([10, 20, 30])
s2 = pd.Series([10, 25, 30])

print(s1==s2)

# missing data in DataFrame

df = pd.DataFrame({'A':[1,2,None], 'B':[4,None, 6]})
df1 = pd.DataFrame({'A':[1,None,3], 'B':[None,5,6]})
print(df,"\n",df1)
print(df+df1)
