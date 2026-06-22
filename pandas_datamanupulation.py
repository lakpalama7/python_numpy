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