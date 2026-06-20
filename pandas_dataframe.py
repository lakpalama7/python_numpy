import pandas as pd
import numpy as np

# indexing and selecting colums

data = pd.read_csv('employee.csv')
print(data.head())

# display only name
print(data['name'])
# display name and age
print(data[['name','emp_id']])

# indexing with loc[]
# selec single row by label
data = pd.read_csv('employee.csv', index_col='name')
print(data.head())
row = data.loc['Bob']
print(row)

# select multiple rows by label
rows = data.loc[['Eva','David']]
print(rows)

# select specifi rows and columns
r = data.loc[['Eva','Bob'], ['emp_id','salary']]
print(r)
print("using index")
print(data.iloc[0])

# select specifi rows and columns with index
r = data.iloc[10:15, 0:3]
print(r)

r = data.iloc[2, 0:2]
print(r)

# select all rows and specific colum
r = data.loc[:,['emp_id','salary']]
print(r)

# select all cols and specific row
r = data.iloc[10:15,:]
print(r)

# selecting multiple rows
r = data.iloc[[2,4,6]]
print(r)

# select specific rows and specific cols
r = data.iloc[[5,10],[0,3]]
print(r)

r = data.loc[['Eva','Grace'],['emp_id','salary']]
print(r)

print(data.tail())

r = data.at['Eva','emp_id']
print(r)
print(data.loc[['Eva','Peter'],'emp_id'])

#query

r = data.query("salary > 60000 and emp_id > 15")
print(r)