import pandas as pd
import numpy as np

# concatenating dataframe
# eithe vertically or horizontally

data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

data2 = {'Name': ['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
         'Age': [17, 14, 12, 52],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}

df1 = pd.DataFrame(data1, index=[0,1,2,3])
df2 = pd.DataFrame(data2, index=[4,5,6,7])
print(df1, "\n\n", df2)

# concate()

res = pd.concat([df1,df2])
print(res)

#Concatenating DataFrames by Setting Logic on Axes
data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd'],
         'Mobile No': [97, 91, 58, 76]}

data2 = {'Name': ['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'],
         'Age': [22, 32, 12, 52],
         'Address': ['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
         'Qualification': ['MCA', 'Phd', 'Bcom', 'B.hons'],
         'Salary': [1000, 2000, 3000, 4000]}

df = pd.DataFrame(data1, index=[0,1,2,3])
df1 = pd.DataFrame(data2, index=[2,3,6,7])
print(df, "\n\n", df1)

# set axis=1, inner= join

res = pd.concat([df,df1], axis=1, join='inner')
print(res)

# ignore index

res = pd.concat([df,df1], ignore_index=True)
print(res)

# use group keys

res = pd.concat([df,df1], keys=['x','y'])
print(res)


#Concatenating Mixed DataFrames and Series

data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

df = pd.DataFrame(data1,index=[0, 1, 2, 3])

s1 = pd.Series([1000, 2000, 3000, 4000], name='Salary')

print(df, "\n\n", s1)

# concat dataframe and series

res = pd.concat([df,s1], axis=1)
print(res)

# Merging DataFrame

#Merging DataFrames Using One Key
# Merge based on common columns
data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],}

data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}

df = pd.DataFrame(data1)

df1 = pd.DataFrame(data2)


print(df, "\n\n", df1)

# merge with common column 'key'
res = pd.merge(df,df1, on='key')
print(res)

#Merging DataFrames Using Multiple Keys

data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K1', 'K0', 'K1'],
         'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],}

data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K0', 'K0', 'K0'],
         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}

df = pd.DataFrame(data1)

df1 = pd.DataFrame(data2)


print(df, "\n\n", df1)

#merge with multiple keys
#merge only matching with 'key','key1'
res = pd.merge(df,df1, on=['key','key1'])
print(res)

# Merging DataFrames Using the how Argument

data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K1', 'K0', 'K1'],
         'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],}

data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K0', 'K0', 'K0'],
         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}

df = pd.DataFrame(data1)

df1 = pd.DataFrame(data2)


print(df, "\n\n", df1)

# how='left'

res = pd.merge(df,df1, how='left', on=['key','key1'])
print(res)

# how='right'

res = pd.merge(df,df1, how='right', on=['key','key1'])
print(res)

# how='inner'
res = pd.merge(df,df1, how='inner',on=['key','key1'])
print(res)

# how='outer'
res = pd.merge(df,df1,how='outer',on=['key','key1'])
print(res)

#Joining DataFrame

#Joining DataFrames Using .join()
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32]}

data2 = {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']}

df = pd.DataFrame(data1,index=['K0', 'K1', 'K2', 'K3'])

df1 = pd.DataFrame(data2, index=['K0', 'K2', 'K3', 'K4'])


print(df, "\n\n", df1)

# join()
print("---------")
res = df.join(df1)
print(res)
print("---------")

res = df1.join(df)
print(res)
print("----------")
# how='outer'
res = df.join(df1,how='outer')
print(res)


#  Joining DataFrames Using the "on" Argument

data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Key':['K0', 'K1', 'K2', 'K3']}

data2 = {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']}

df = pd.DataFrame(data1)

df1 = pd.DataFrame(data2, index=['K0', 'K2', 'K3', 'K4'])


print(df, "\n\n", df1)

# join() with 'on' arg

res = df.join(df1, on='Key')
print(res)

#Joining DataFrames with Different Index Levels (Multi-Index)
data1 = {'Name':['Jai', 'Princi', 'Gaurav'],
        'Age':[27, 24, 22]}

data2 = {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kanpur'],
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']}

df = pd.DataFrame(data1, index=pd.Index(['K0', 'K1', 'K2'], name='key'))

index = pd.MultiIndex.from_tuples([('K0', 'Y0'), ('K1', 'Y1'),
                                   ('K2', 'Y2'), ('K2', 'Y3')],
                                   names=['key', 'Y'])

df1 = pd.DataFrame(data2, index= index)


print(df, "\n\n", df1)

res = df.join(df1, how='inner')
print(res)