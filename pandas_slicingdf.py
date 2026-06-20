import pandas as pd
import numpy as np

player_list = [['M.S.', 36, 75, 54280],
               ['A.B.D ', 38, 74, 34280],
               ['V.', 31, 70, 84280],
               ['S.', 34, 80, 44280],
               ['C.', 40, 100, 48000],
               ['J.', 33, 72, 78000],
               ['K.', 42, 85, 28000]]

df = pd.DataFrame(player_list, columns=['name','age','weight','salary'])
print(df)

# slicing using iloc[]

d = df.iloc[0:4]
print(d)

# slicing cols 

d = df.iloc[:,0:2]
print(d)

# specific rows and cols

d = df.iloc[[3,6],[2,3]]
print(d)

# specific cells
d = df.iloc[6,0] # row index 6 and col index 0
print(d)

# using boolean condition

d = df[df['age'] > 35]
print(d)

# slicing with loc[]
# set_indx()

df.set_index('name', inplace=True)
print(df.head(2))

# single row
d = df.loc['K.']
print(d)

# single row, singel col
d = df.loc['C.','age']
print(d)

# multi row, multi col
d = df.loc[['C.','M.S.'],['salary','age']]
print(d)

print(df.head())

# slicing rows

d = df.loc['V.':'C.']
print(d)