import pandas as pd
import numpy as np

data = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                   '  ROSS    ', 'CHANDLER', ' JOEY    '],
                          
                          'Age': [30, 35, 37, 33, 34, 30],
                          
                          'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
                          
                          'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                  'IT', 'ARTIST']})

print(data)

# filter DataFrame with multiple conditions Using loc

d = data[(data['Salary'] >= 100000) & (data['Age'] < 40) & (data['JOB'].str.startswith('D'))][['Name','JOB']]

print(d)

# using query
d = data.query("Salary >=100000 and Age < 40 and JOB.str.startswith('D')")[['Name','JOB']]
print(d)

# usign numpy

d= np.where((data['Salary']>=100000) & (data['Age']<40) & (data['JOB'].str.startswith('D')))
print(d)
print(data.loc[d])

# query
d = data.query("Salary < = 100000 and Age < 40 and JOB.str.startswith('C')")
print(d)

