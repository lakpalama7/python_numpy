import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Title': ['The Crown', 'Stranger Things', 'Breaking Bad', 'The Mandalorian', 'Avatar: The Last Airbender', 'The Office', 'Game of Thrones', 'Cosmos: A Spacetime Odyssey', 'The Good Place', 'Black Mirror', 'The Chosen', 'The Bible'],
    'Genre': ['Drama', 'Sci-Fi', 'Drama', 'Sci-Fi', 'Animation', 'Comedy', 'Fantasy', 'Documentary', 'Comedy', 'Sci-Fi', 'Drama', 'Drama'],
    'Release_Year': [2016, 2016, 2008, 2019, 2005, 2005, 2011, 2014, 2016, 2011, 2019, 2013],
    'Director': ['Peter Morgan', 'The Duffer Brothers', 'Vince Gilligan', 'Jon Favreau', 'Michael Dante DiMartino, Bryan Konietzko', 'Greg Daniels', 'David Benioff, D. B. Weiss', 'Brannon Braga', 'Michael Schur', 'Charlie Brooker', 'Dallas Jenkins', 'Various'],
    'Seasons': [4, 4, 5, 2, 3, 9, 8, 1, 4, 5, 2, 1],
    'Duration_Minutes': [60, 50, 47, 40, 23, 22, 57, 60, 22, 60, 45, 43]
}
df = pd.DataFrame(data)
print(df)

# bar plot
g = df.groupby('Genre')['Seasons'].mean()
g.plot.bar(figsize=(10,6), color='coral', title='Bar plot of Average Seasons by Genre')
plt.show()

g_bar = df.groupby('Genre')['Duration_Minutes'].mean()
g_bar.plot.bar(figsize=(10,6), color='blue', title='Average duration of genre')
plt.show()

#histrogram
df['Duration_Minutes'].plot.hist(bins=10, figsize=(10,6), color='skyblue', edgecolor='black', title='Histogram of duration')
plt.show()

df['Seasons'].plot.hist(bins=10, figsize=(10,6), color='skyblue', edgecolor='red', title='Histogram of Seasons')
plt.show()

print(df['Seasons'].value_counts())

# Scatter plot
df.plot.scatter(x='Release_Year',y='Seasons', figsize=(10,6), title='Release vs Seasons')
plt.show()

print(df[['Release_Year','Seasons']])

# Box plot

df.plot.box(column='Duration_Minutes', figsize=(10,6), showfliers=True)
plt.show()

#Pie chart
g = df['Genre'].value_counts()
print(g)
g.plot.pie(figsize=(10,6), autopct='%1.1f%%', title='Pie chart of genre distribution')
plt.show()
# Area plot
ap = df.groupby('Release_Year')['Seasons'].sum()
print(ap)

ap.plot.area(figsize=(10,6), title='Area plot of total seasons by Release year', color='lightgreen')
plt.show()
# line plot
df.plot.line(x='Genre',y='Release_Year', figsize=(10,6), title='Genre vs Release year', marker='D', linestyle='-')
plt.show()