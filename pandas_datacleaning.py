import pandas as pd
import numpy as np

d = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}
df = pd.DataFrame(d)
print(df)

# missing values
print(df.isnull().sum())

bool_v = pd.isnull(df['First Score'])

print(df[bool_v])
print(df.iloc[2,0])

print(df.isna().sum())

# check non-missing values using notnull()

print(df.notnull())
print(df.notnull().sum())

# filter non-missing values
n_null = pd.notnull(df['First Score'])
print(df[n_null]['First Score'])

print(df)

# fill missiing value 
df.fillna(0, inplace=True)
print(df)

d = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}
df = pd.DataFrame(d)
print(df)

# fill with custom value
df['First Score']=df['First Score'].fillna(0, inplace=True)
print(df)

df['Second Score']=df['Second Score'].fillna(df['Second Score'].agg('mean'),inplace=True)
print(df)

df['Third Score'] = df['Third Score'].fillna(df['Third Score'].agg('min'), inplace=True)
print(df['Third Score'])

d = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}
df = pd.DataFrame(d)
print(df)

# replace nan value
df = df.replace(to_replace=np.nan, value=99)
print(df)


dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score': [52, 40, 80, 98],
        'Fourth Score': [np.nan, np.nan, np.nan, 65]}
df = pd.DataFrame(dict)
print(df)

# drop rows with at least one NULL value
df.dropna(inplace=True)
print(df)

# dropping rows having all value null

dict = {'First Score': [100, np.nan, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score': [52, np.nan, 80, 98],
        'Fourth Score': [np.nan, np.nan, np.nan, 65]}
df = pd.DataFrame(dict)
print(df)
df.dropna(how='all', inplace=True)
print(df)

# dropping cols with at least one null value
dict = {'First Score': [100, np.nan, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score': [52, np.nan, 80, 98],
        'Fourth Score': [60, 67, 68, 65]}
df = pd.DataFrame(dict)
print(df)
print(df.dropna(axis=1))

# drop rows with missing values 
print(df.dropna(how='any'))

# drop duplicates
data = {
    "Name": ["Alice", "Bob", "Alice", "David"],
    "Age": [25, 30, 25, 40],
    "City": ["NY", "LA", "NY", "Chicago"]
}

df = pd.DataFrame(data)
print(df)

print(df.drop_duplicates())

# drop all duplicates
print(df.drop_duplicates(keep=False))

# change datatypes
data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'], 
        'Age': [25, 30, 22, 35, 28], 
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'], 
        'Salary': [50000, 55000, 40000, 70000, 48000]}

df = pd.DataFrame(data)
print(df.info())
# convert age to float
df['Age'] = df['Age'].astype(float)
print(df.dtypes)
df['Salary'] = df['Salary'].astype(float)
print(df.dtypes)

#Converting a Column to a DateTime Type
df['Join Date'] = ['2021-01-01', '2020-05-22', '2022-03-15', '2021-07-30', '2020-11-11']
print(df)
print(df.dtypes)

# convert 'join Date' to datetime
df['Join Date'] = pd.to_datetime(df['Join Date'])
print(df.dtypes)

# convert multiple cols datatypes
df = df.astype({'Age':int,'Salary':str})
print(df.dtypes)

# dropping null values

df = pd.DataFrame({'FirstName': ['Vipul', 'Ashish', 'Milan'],
                            "Gender": ["", "", ""],
                            "Age": [0, 0, 0]})
print(df)
df['department']=np.nan
print(df)
df.dropna(axis=1, inplace=True)
print(df)

# replace empty string with null value
df.replace(to_replace="", value=np.nan, inplace=True)
print(df)
df.dropna(axis=1,inplace=True)
print(df)

# replace zeros with null
df.replace(to_replace=0, value=np.nan, inplace=True)
print(df)

df.dropna(axis=1, inplace=True)
print(df)