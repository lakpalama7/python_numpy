import pandas as pd
import numpy as np

data = { 'Name': ['Lukas', 'Sofia', 'Hiroshi', 'Marta', 'Yannis', np.nan, 'Elena'],
         'City': ['Berlin', 'Madrid', 'Tokyo', 'Warsaw', 'Athens', 'Oslo', 'Lisbon'] }

df = pd.DataFrame(data)
print(df)

# string operations
print(df['Name'].str.lower())
print(df['Name'].str.upper())
print(df['Name'].str.strip())
print(df['Name'].str.split('a'))
print(df['Name'].str.len())
print(df['Name'].str.cat(sep=','))

print(df['City'].str.get_dummies())
print(df['Name'].str.startswith('E'))
print(df[df['Name'].str.startswith('E')])
print(df['Name'].str.endswith('a'))
print(df['Name'].str.replace('Elena','Chor'))
#repeat
print(df['Name'].str.repeat(2))
#count 
print(df['Name'].str.count('a'))
print(df['Name'].str.find('a'))
print(df['Name'].str.findall('a'))

#islower(), isupper()
print(df['Name'].str.islower())
print(df['Name'].str.isupper())
print(df['Name'].str.isnumeric())
print(df['Name'].str.isalpha())
print(df['Name'].str.isalnum())
print(df['Name'].str.swapcase())