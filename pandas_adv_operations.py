import pandas as pd
import numpy as np

d = {
    'A':[10,20,30,40],
    'B':[15,25,35,45]
}

df = pd.DataFrame(d)
print(df)

# co relation
r = df.corr()
print(r)

d = {"StudyHours": [2, 4, 6, 8], "StressLevel": [8, 7, 5, 6]}
df = pd.DataFrame(d)
print(df.corr(method='kendall'))

d = {"MathMarks": [95, 70, 85, 60, 80], "SportsScore": [60, 75, 65, 80, 70]}
df = pd.DataFrame(d)
print(df.corr(method='spearman'))