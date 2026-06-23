import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# load data
df1 = pd.read_csv('df1', index_col=0)
df2 = pd.read_csv('df2')
print(df1.head(2))

# line plot
print(df2.head(2))
df2.plot(style=['-','--','-.',':'], title='Line plot', xlabel='index',ylabel='values', grid=True)
plt.show()

# plot area
df2.plot.area(alpha=0.4) #alpha set transparency to make overlaps clearer.
plt.show()

#Bar plots
df2.plot.bar()
plt.show()

# Histogram plot
df1['A'].plot.hist(bins=50)
plt.show()

# scatter plot
df1.plot.scatter(x='A',y='B')
plt.show()

#box plot - show distribution of data showing median, quartiles , outliers

df2.plot.box()
plt.show()

#KDE
df2['a'].plot.kde()
plt.show()