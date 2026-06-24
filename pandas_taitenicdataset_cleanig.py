import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.read_csv('titanicdataset.csv')
df.info()
print(df.head(2))

# check for duplicates
print(df.duplicated())
print(df.isna().sum())

# data types
print(df.dtypes)
# dtype separate categorical and numerical columns
# object type for text or categorical data
cat_col = [col for col in df.columns if df[col].dtype == 'str']
num_col = [col for col in df.columns if df[col].dtype !='str']
print("categorical columns: ", cat_col)
print("Numerical columns: ", num_col)

# count unique values in categorical columns
print(df[cat_col].nunique())
print(df.nunique())

# calculate missing values as percentage
print(df.shape)
print(round((df.isna().sum() / df.shape[0]) * 100,2))

# drop irrelevant or data missing values
# drop column based on specific columns
df1 = df.drop(columns=['Name','Ticket','Cabin'])
print(df1.columns)
print(df1.shape)

# drop rows based on specific columns having missing values
df1.dropna(subset=['Embarked'], inplace=True)
print(df1.columns)
print(df1.shape)

# fill missing values
print(df1.isna().sum())
df1['Age'] = df1['Age'].fillna(df1['Age'].mean())
print(df1.isna().sum())


# Detect outliers with BoxPlot
""" plt.boxplot(df1['Age'], vert=False)
plt.ylabel('Variable')
plt.xlabel('Age')
plt.title('Age Distribution Box plot')
plt.show() """

# Calculate outlier boundaries and remove them
#calculate mean and std
mean = df1['Age'].mean()
std = df1['Age'].std()

# define bound as mena +/- 2 *std
lowerbound= mean - 2 * std
upperbound = mean + 2 * std
print("lowerbound : ", lowerbound, "\n", "upperbound: ", upperbound)
df2 = df1[(df['Age'] >= lowerbound) & (df1['Age'] <= upperbound)]
print(df2.shape)
print(df['Age'].min(), df['Age'].max())
print(df2['Age'].min(), df2['Age'].max())

# again check in boxplot for outliers
""" plt.boxplot(df2['Age'], vert=False)
plt.ylabel('Variable')
plt.xlabel('Age')
plt.title('Age distribution boxplot after removing outliers')
plt.show() """

# impute missing data again if any
print(df2.isnull().sum())

# Data validation and verification
# independent/feature or dependent/target features
# X - independent , Y- dependent
X = df2[['Pclass','Sex','Age', 'SibSp','Parch','Fare','Embarked']]
Y = df2['Survived']


# data formatting - convert data into standard format or structure
# for easy processing by algorithms or model for analysis.
# Data scaling and Normalization: MinMax scaling & Standardization Scaling
# MinMax scaling - scale values between 0 and 1

scaler = MinMaxScaler()
num_col = [col for col in X.columns if X[col].dtype !='str']
print(num_col)
x1 = X
x1[num_col] = scaler.fit_transform(x1[num_col])
print(x1.head())

# Z-score or Standardization
std_scaler = StandardScaler()
num_col = [col for col in X.columns if X[col].dtype !='str']
y = X
y[num_col] = std_scaler.fit_transform(y[num_col])
print(y.head())

