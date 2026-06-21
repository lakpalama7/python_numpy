import pandas as pd
import json
import requests

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

# Json normalized  method
data = {"One": {"0": 60, "1": 60, "2": 60, "3": 45, "4": 45, "5": 60},
        "Two": {"0": 110, "1": 117, "2": 103, "3": 109, "4": 117, "5": 102}}

jdata=json.dumps(data)
print(jdata)

df_norm = pd.json_normalize(json.loads(jdata))
print(df_norm)

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)
data = pd.json_normalize(response.json())
print(data.head())
print(data.columns)
print(data['title'])

# Handling text files

data = pd.read_csv('test.txt', header=None)
print(data)
# set column
data.columns = ['Name','Degree','Score']
print(data)

# write to file
data.to_csv('test.txt', index=None)