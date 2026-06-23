import pandas as pd
import numpy as np
from datetime import datetime

rd = pd.date_range(start='1/1/2019', end='1/08/2019', freq='Min')
print(rd)
print(type(rd))

df = pd.DataFrame(rd, columns=['date'])
df['data'] = np.random.randint(0,100, size=(len(rd)))
print(df.head())

# convert to string format
s = [str(x) for x in rd]
print(s[1:11])

# accessing specific datetime
df.set_index('date', inplace=True)
print(df.head(2))
filter_date = df.loc['2019-01-05']
print(filter_date.iloc[1:11])


# create DateTime values

date_time=pd.date_range(start='01/01/2026', end='01/07/2026',freq='Min')
print(date_time)

# create dataframe
df = pd.DataFrame(date_time, columns=['datetime'])
df['data'] = np.random.randint(0,100, size=(len(date_time)))
print(df.head())

# set index
df.set_index('datetime', inplace=True)
print(df.head())

# access specific date based on 'datetime' index label
filter_date = df.loc['2026-01-06']
print(filter_date)

print(filter_date.iloc[20:30])
print(filter_date.head())