import pandas as pd

df = pd.read_csv('employee.csv')
print(df.head(2))

print(df['name'])
print(df[['name','emp_id','salary']])
print(df.index.values)
print(df.info())
print(df.describe())

# set emp_id as index
df.set_index('emp_id', inplace=True)
print(df.head())

# check nan values
print(df.isna().sum())


# saving dataframe to csv

nme = ["Aparna", "Pankaj", "Sudhir", "Geeku"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]
data = {
    'name':nme,
    'degree':deg,
    'score':scr
}
df = pd.DataFrame(data)
print(df)

# export to csv file
df.to_csv('file1.csv')
data = pd.read_csv('file1.csv')
print(data)

# drop Unnamed: 0 colm
data.drop(columns='Unnamed: 0', inplace=True)
print(data)

data = {
    'Name':['a','b','c','d','e'],
    'Score':[11,12,13,111,111]
}
df = pd.DataFrame(data)
print(df)

df.to_csv('file.csv', index=False)

data = pd.read_csv('file.csv', index_col='Name')
print(data)

data.reset_index(inplace=True)
print(data)

# export only selected colms

data.to_csv('f.csv', columns=['Score'], index=False)
print(pd.read_csv('f.csv'))
