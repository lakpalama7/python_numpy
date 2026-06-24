import pandas as pd
import numpy as np

data = {
'School ID': [101, 102, 103, np.nan, 105, 106, 107, 108],
'Name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
'Address': ['123 Main St', '456 Oak Ave', '789 Pine Ln', '101 Elm St', np.nan, '222 Maple Rd', '444 Cedar Blvd', '555 Birch Dr'],
'City': ['Mumbai', 'Delhi', 'Bengaluru', 'Chennai', 'Kolkata', np.nan, 'Pune', 'Jaipur'],
'Subject': ['Math', 'English', 'Science', 'Math', 'History', 'Math', 'Science', 'English'],
'Marks': [85, 92, 78, 89, np.nan, 95, 80, 88],
'Rank': [2, 1, 4, 3, 8, 1, 5, 3],
'Grade': ['B', 'A', 'C', 'B', 'D', 'A', 'C', 'B']
}

df = pd.DataFrame(data)
print(df)

print(df.isnull().sum())

# remove rows with missing values
clean_df=df.dropna()
print(clean_df)
print("---------------")

# Imputation methods: replace missing values with estimated values
# mean, median and mode interpretation
print(df)
mean_imputation=df['Marks'].fillna(df['Marks'].mean())
median_imputation=df['Marks'].fillna(df['Marks'].median())
mode_imputation=df['Marks'].fillna(df['Marks'].mode().iloc[0])
print("Imputation using mean")
print(mean_imputation)
print("impuatation using median")
print(median_imputation)
print("imputation using mode")
print(mode_imputation)

# Interpolation technique
# using the trend or pattern of surrounding data

linear_inter = df['Marks'].interpolate(method='linear')
quadratic_inter = df['Marks'].interpolate(method='quadratic')

print("Linear Interpolation")
print(linear_inter)
print("Quadratic Interpolation")
print(quadratic_inter)