import pandas as pd
import numpy as np
# Data Structures in pandas

# Series
s = pd.Series()
print(s)
data = np.array(['a','b','c','d','e'])
s = pd.Series(data)
print(s)

# DataFrame
df = pd.DataFrame()
print(df)
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']
df = pd.DataFrame(lst)
print(df)

# creating dataframe from dict of Numpy array

data = {
    'A': np.array([1,2,3]),
    'B':np.array([4,5,6]),
    'C':np.array([7,8,9])
}
df = pd.DataFrame(data)
print(df)

# Creating dataFrame from List of Dictionaries

data = [
    {'name':'Mike','degree':'MBA','score':90},
    {'name':'Hari','degree':'BBS','score':50},
    {'name':'ram','degree':'MIT','score':60},
]

df = pd.DataFrame(data)
print(df)

# load data
df = pd.read_csv("employee.csv")
print(df.head())

#view and exploring data
df.info()

# Handling missing data

print(df.isna().sum())
print(df.isnull().sum())

# if null exist then
df = df.fillna(0)

# Selecting and filtering Data
salary = df[df['salary'] > 60000]
print(salary)

# Adding colum
df['total'] = df['salary'] + df['basic_salary']
print(df.head())

#Grouping data
res = df.groupby(['dept_id'])['emp_id'].value_counts()
print(res)

# Accessing and modifying the index
data = {
    'Name':['Jake','Eve','Charlie'],
    'Age':[22,23,24],
    'Gender':['Male','Female','Male'],
    'Salary':[2000,3000,5000]
}
df = pd.DataFrame(data)
print(df.index)
print(df)

# set index
res = df.set_index('Name')
print(res)
print(res.index)

#reset index
res = res.reset_index()
print(res)

# indexing with loc
# access rows and colums using labels to retrieve data

data = {
    'name':['alice','bob'],
    'age':[23,33],
    'city':['ny','la']
}
df = pd.DataFrame(data)
print(df)
df = df.set_index('name')
print(df)

#access data using loc() with label
print('access data with label')
row = df.loc['alice']
print(row)

# reset the index
df = df.reset_index()
print(df)

# set other index
df = df.set_index('age')
print(df)
row = df.loc[23]
print(row)



data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'], 
        'Age': [25, 30, 22, 35, 28], 
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'], 
        'Salary': [50000, 55000, 40000, 70000, 48000]}

df = pd.DataFrame(data)
# Display the entire DataFrame
print(df)

# access age data
age_col = df['Age']
print(age_col)

# acces rows by index
# iloc[] - for positional index
# loc[] -- label based index
row = df.iloc[4]
print(row)

# accessing multiple rows or cols
subset = df.loc[0:2, ['Name','Age']]
print(subset)

row=df.loc[:, ['Name','Age']]
print(row)

print(df[['Name','Age']])

# accessing rows based on condition
filter_age = df[df['Age']>25]
print(filter_age)

# access specific cells with at and iat
# at -- label based indexing
# iat---integer position indexing

sal = df.at[2,'Salary'] # row index and label
print(sal)
sal = df.iat[4, 0] # row index, col index
print(sal)

