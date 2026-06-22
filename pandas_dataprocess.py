import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('employee.csv')
print(data.head(2))
print(data.tail(2))
#columns

print(data.columns)
#info
print(data.info())
print(data.describe())

# find missing value
print(data.isnull().sum())

# removing missing values
data = data.dropna()
print(data.head(2))

# fill missing values
data = data.fillna(0) # fill all null value with '0'
print(data.head(2))

# fill missing value based on column
data['name'] = data['name'].fillna('xyz')

# row and col manipulations

# remove row at index 4
data.drop(4, inplace=True)
print(data)

# remove col  dept_id
data.drop('dept_id', axis=1, inplace=True)
print(data.head(2))

# rename column
data.rename({'emp_id':'id','name':'full name'}, axis=1, inplace=True)
print(data.head())

data['newcol']=[x for x in range(len(data))]
print(data.head())

data.rename({'full name':'name'}, axis=1, inplace=True)
# sorting

print(data.sort_values(by='salary'))
print(data.sort_values(by='salary', ascending=False))

#sorting by multi columns
print(data.sort_values(by=['name','salary']).head(5))


# Merge dataframe
df1 = pd.DataFrame({
        'Name':['Jeevan', 'Raavan', 'Geeta', 'Bheem'], 
        'Age':[25, 24, 52, 40], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']})
df2 = pd.DataFrame({'Name':['Jeevan', 'Raavan', 'Geeta', 'Bheem'],
                    'Salary':[100000, 50000, 20000, 40000]})

print(df1,"\n",df2)
#concat
print(pd.concat([df1,df2], axis=0))
print('--------')
print(df1.merge(df2))
print('---------')
df1.set_index('Name', inplace=True)
df2.set_index('Name', inplace=True)
print(df1.join(df2))

# function call

def fun(value):
    if value > 90000:
        return 'rich'
    
    elif value > 50000:
        return 'medium'
    
    else:
        return 'poor'
    
df2['status'] = df2['Salary'].apply(fun)
print(df2)

# lambda operator
const= df1['Age'].max()
print(const)

df1['Avgage'] = df1['Age'].apply(lambda x: x/const)
print(df1)

# dataframe visualization

df = pd.DataFrame([
    [180, 110, 18.9, 1400],  
    [360, 905, 23.4, 1800],  
    [230, 230, 14.0, 1300],  
    [600, 450, 13.5, 1500]
], columns=['Col A', 'Col B', 'Col C', 'Col D'])

# Normalization Techniques in Pandas
# 1. Maximum absolute scaling
df_scaled = df.copy()
print(df_scaled)

for column in df_scaled.columns:
    df_scaled[column] = df_scaled[column] / df_scaled[column].abs().max()

print(df_scaled)

df_scaled.plot(kind='bar')
plt.show()

#2. min-max scaling
scaled = df.copy()
for col in scaled.columns:
    scaled[col] = (scaled[col] - scaled[col].min()) / (scaled[col].max() - scaled[col].min())

print(scaled)

scaled.plot(kind='bar')
plt.show()

# z-score scaling

z_scaled = df.copy()

for col in z_scaled.columns:
    z_scaled[col] = (z_scaled[col] - z_scaled[col].mean()) / z_scaled[col].std()

print(z_scaled)
z_scaled.plot(kind='bar')
plt.show()

