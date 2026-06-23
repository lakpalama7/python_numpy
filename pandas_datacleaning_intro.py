import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# load data source
df = pd.read_csv('diabetes.csv')
print(df.head())

#check data structure and missing values
print(df.info())
print(df.isna().sum())

#statistical summary and visualizing outliers
print(df.describe())

""" fig, axes = plt.subplots(len(df.columns), 1, figsize=(7,18), dpi=95)
for i, col in enumerate(df.columns):
    axes[i].boxplot(df[col], vert=False)
    axes[i].set_ylabel(col)
plt.tight_layout()
plt.show() """

# Remove outliers using IQR (interquartile range) method
# Insuline column
q1, q3 = np.percentile(df['Insulin'], [25,75])
print(q1, q3)
iqr = q3-q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
clean_df = df[(df['Insulin'] >= lower) & (df['Insulin'] <= upper)]
print(clean_df.head())

# Correlation analysis

corr = df.corr()
""" plt.figure(dpi=130)
sns.heatmap(corr, annot=True)
plt.show() """

print(corr['Outcome'].sort_values(ascending=False))

# visualize target variable distribution
""" plt.pie(clean_df['Outcome'].value_counts(),
        labels=['Diabetes','Not Diabetes'],
        autopct='%.f%%', shadow=True
        )
plt.title('Outcome Proportionality')
plt.show() """

print(clean_df['Outcome'].value_counts())

# Separate Features and target variabel
# prepare independent variable(features) and dependent variable (target)
x = df.drop(columns=['Outcome'])
y = df['Outcome']

# Scaling: Normalization and Standardization
# Normalization : MINMax Scaling - features bet 0 and 1
scaler = MinMaxScaler()
x_normalized = scaler.fit_transform(x)
print(x_normalized[:5])

# Standardization: transform features to have mean = 0 and std=1
scaler = StandardScaler()
x_standardized = scaler.fit_transform(x)
print(x_standardized[:5])