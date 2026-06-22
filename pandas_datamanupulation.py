import pandas as pd
import numpy as np

df = pd.DataFrame()
df['name'] = ['John','Emma','Liam','Oliva']
df['age']=[20,30,40,50]
df['student']=[True,True,False,True]

print(df)

#Adding row
newrow=pd.DataFrame([['Sophia',22,False]],columns=df.columns)
df=pd.concat([df,newrow],ignore_index=True)
print(df)

#dropping colum
df.drop('age', axis=1, inplace=True)
print(df)

#dropping rows
df.drop(0, inplace=True)
print(df)

# selecting data from dataframe
print(df['name'])
print(df[['name','student']])
print(df.iloc[3]) # internal index value
print(df.loc[4]) # label value

# filtering data
print(df[df['student'] == True])

#sorting
print("-------")
print(df.sort_values(by='name'))
print(df.sort_index())


# grouping
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
print(df.head(2))
gf = df.groupby('Team')
print(gf.first())

# group by multiple columns
gf = df.groupby(['Team','Position'])
print(gf.first())

# aggrigate function

agg_data = df.groupby(['Team','Position']).agg(
    total_salary = ('Salary','sum'),
    avg_salary=('Salary','mean'),
    count = ('Name','count')
)
print(agg_data)

# transformation method
print(df.head(2))
df['rank in team'] = df.groupby('Team')['Salary'].transform(lambda x:x.rank(ascending=False))
print(df)

# filtering groups 
fdata = df.groupby('Team').filter(lambda x: x['Salary'].mean() >=1000000)
print(fdata)