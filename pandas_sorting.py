import pandas as pd
import numpy as np

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Score': [85, 90, 95, 80]}

#sorting
df = pd.DataFrame(data)
print(df)

s = df.sort_values(by='Age')
print(s)

s = df.sort_values(by='Age', ascending=False)
print(s)

# sort values by multiple colum

s = df.sort_values(by=['Age','Score'])
print(s)

# sorting data with missing values
data = {
    "Name": ["alice", "Bob", "Charlie", "david"],
    "Age": [28, 22, None, 22]
}
df = pd.DataFrame(data)
s = df.sort_values(by=['Age','Name'],na_position='first')
print(s)

#sort by index
s = df.sort_index()
print(s)

s = df.sort_index(ascending=False)
print(s)

#Applying Custom Sorting Logic

s = df.sort_values(by='Name', key=lambda c:c.str.lower())
print(s)